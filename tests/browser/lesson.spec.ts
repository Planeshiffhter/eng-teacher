import { expect, test } from '@playwright/test';

test('responsive entry page, synthetic browser microphone, and honest missing-configuration error', async ({ page }) => {
  const errors: string[] = [];
  page.on('pageerror', (error) => errors.push(error.message));
  await page.goto('/');
  await expect(page.getByRole('heading', { name: 'Find your voice.' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Start my lesson' })).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  // Chromium supplies synthetic audio; this verifies browser permissions/devices only.
  // It is NOT a human microphone, provider or LiveKit end-to-end speech test.
  const mic = await page.evaluate(async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const tracks = stream.getAudioTracks();
    const live = tracks.length === 1 && tracks[0].readyState === 'live';
    tracks.forEach((track) => track.stop());
    return { live, stopped: tracks.every((track) => track.readyState === 'ended') };
  });
  expect(mic).toEqual({ live: true, stopped: true });
  await page.getByLabel('Pilot access code').fill('test-only-pilot-code');
  await page.getByRole('button', { name: 'Start my lesson' }).click();
  await expect(page.getByRole('alert').filter({ hasText: 'not configured' })).toContainText('not configured');
  await expect(page.getByRole('button', { name: 'Start my lesson' })).toBeEnabled();
  await expect(page.getByRole('button', { name: 'End lesson' })).toHaveCount(0);
  expect(errors).toEqual([]);
});

test('server does not issue credentials while unconfigured', async ({ request }) => {
  const response = await request.post('/api/session', { data: { accessCode: 'test-only-code' }, headers: { Origin: 'http://localhost:3100' } });
  expect(response.status()).toBe(503);
  expect(response.headers()['cache-control']).toContain('no-store');
  const body = await response.json();
  expect(body).toEqual({ error: expect.stringContaining('not configured') });
  expect(body.participantToken).toBeUndefined();
});

test('a failed voice-room connection returns control to the learner', async ({ page }) => {
  // Mock only the token endpoint. No fake successful voice lesson is presented.
  await page.route('**/api/session', (route) => route.fulfill({
    json: { serverUrl: 'ws://localhost:1', participantToken: 'invalid-test-token', roomName: 'test-room', lessonId: 'mock-interview' },
  }));
  await page.goto('/');
  await page.getByLabel('Pilot access code').fill('test-only-pilot-code');
  await page.getByRole('button', { name: 'Start my lesson' }).click();
  await expect(page.getByRole('button', { name: 'Practice again' })).toBeVisible({ timeout: 25_000 });
  await expect(page.getByRole('button', { name: 'End lesson' })).toHaveCount(0);
});

for (const { lessonId, heading } of [
  { lessonId: 'everyday-conversation', heading: 'A friendly chat. A little more confidence.' },
  { lessonId: 'cafe-order', heading: 'Order at a café in English.' },
]) {
  test(`${lessonId} selection changes the lesson and survives connection failure`, async ({ page }) => {
    let submitted: unknown;
    let release: () => void = () => {};
    const pending = new Promise<void>((resolve) => { release = resolve; });
    await page.route('**/api/session', async (route) => {
      submitted = route.request().postDataJSON();
      await pending;
      await route.fulfill({ json: {
        serverUrl: 'ws://localhost:1', participantToken: 'invalid-test-token', roomName: 'test-room', lessonId,
      } });
    });
    await page.goto('/');
    const picker = page.getByLabel('Practice focus');
    await picker.selectOption(lessonId);
    await expect(page.getByRole('heading', { name: heading })).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
    await page.getByLabel('Pilot access code').fill('test-only-pilot-code');
    await page.getByRole('button', { name: 'Start my lesson' }).click();
    await expect(picker).toBeDisabled();
    await expect.poll(() => submitted).toEqual({ accessCode: 'test-only-pilot-code', lessonId });
    release();
    await expect(page.getByRole('button', { name: 'Practice again' })).toBeVisible({ timeout: 25_000 });
    await expect(picker).toHaveValue(lessonId);
    await expect(picker).toBeEnabled();
  });
}
