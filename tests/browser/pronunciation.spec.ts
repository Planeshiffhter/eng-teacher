import { expect, test, type Page } from '@playwright/test';

type CaptureProbe = {
  requests: number;
  tracks: MediaStreamTrack[];
  revokedUrls: string[];
};

async function inspectCapture(page: Page) {
  return page.evaluate(() => {
    const probe = (window as Window & { practiceCapture: CaptureProbe }).practiceCapture;
    return {
      requests: probe.requests,
      tracks: probe.tracks.map(({ readyState }) => readyState),
      revokedUrls: probe.revokedUrls,
    };
  });
}

test('recording is opt-in and releases browser resources on stop, delete, and close', async ({ page }) => {
  const writes: string[] = [];
  page.on('request', (request) => {
    if (request.method() === 'POST') writes.push(request.url());
  });
  await page.addInitScript(() => {
    const probe: CaptureProbe = { requests: 0, tracks: [], revokedUrls: [] };
    Object.defineProperty(window, 'practiceCapture', { value: probe });
    const devices = navigator.mediaDevices;
    const getUserMedia = devices.getUserMedia.bind(devices);
    devices.getUserMedia = async (constraints) => {
      probe.requests++;
      const stream = await getUserMedia(constraints);
      probe.tracks.push(...stream.getAudioTracks());
      return stream;
    };
    const revokeObjectURL = URL.revokeObjectURL.bind(URL);
    URL.revokeObjectURL = (url) => {
      probe.revokedUrls.push(url);
      revokeObjectURL(url);
    };
  });

  await page.goto('/practice');
  await page.getByRole('button', { name: 'Give a work update' }).click();
  await expect(page.getByRole('button', { name: 'Record and listen back' })).toHaveCount(0);
  for (const answer of [
    'I checked the figures yesterday.',
    'The draft is on hold.',
    'I can send a draft today and the full report tomorrow.',
  ]) {
    await page.getByRole('radio', { name: answer, exact: true }).check();
    await page.getByRole('button', { name: 'Check answer' }).click();
    await page.getByRole('button', { name: /Next question|Finish exercises/ }).click();
  }

  await page.getByRole('button', { name: 'Record and listen back' }).click();
  await expect(page.getByRole('heading', { name: 'Listen to your speaking' })).toBeVisible();
  expect(await inspectCapture(page)).toMatchObject({ requests: 0, tracks: [] });

  await page.getByRole('button', { name: 'Start recording' }).click();
  await expect.poll(() => inspectCapture(page)).toMatchObject({ requests: 1, tracks: ['live'] });
  await page.getByRole('button', { name: 'Stop recording' }).click();
  const audio = page.locator('audio[aria-label="Your practice recording"]');
  await expect(audio).toHaveAttribute('src', /^blob:/);
  await expect.poll(() => audio.evaluate((element: HTMLAudioElement) => element.readyState)).toBeGreaterThan(0);
  const clip = await audio.getAttribute('src');
  expect(await inspectCapture(page)).toMatchObject({ tracks: ['ended'] });

  await page.getByRole('button', { name: 'Delete recording' }).click();
  await expect(audio).toHaveCount(0);
  expect((await inspectCapture(page)).revokedUrls).toContain(clip);

  await page.getByRole('button', { name: 'Start recording' }).click();
  await expect.poll(() => inspectCapture(page)).toMatchObject({ requests: 2, tracks: ['ended', 'live'] });
  await page.getByRole('button', { name: 'Close recorder' }).click();
  await expect(page.getByRole('heading', { name: 'Listen to your speaking' })).toHaveCount(0);
  await expect.poll(() => inspectCapture(page)).toMatchObject({ tracks: ['ended', 'ended'] });
  expect(writes).toEqual([]);
});
