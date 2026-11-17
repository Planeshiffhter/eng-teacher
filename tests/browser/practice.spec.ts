import { expect, test } from '@playwright/test';

test('quick exercises give feedback and the speaking prompt without a voice session', async ({ page }) => {
  const errors: string[] = [];
  const admissionRequests: string[] = [];
  page.on('pageerror', (error) => errors.push(error.message));
  page.on('request', (request) => {
    if (new URL(request.url()).pathname === '/api/session') admissionRequests.push(request.method());
  });

  await page.goto('/');
  await page.getByRole('link', { name: 'Quick exercises' }).click();
  await expect(page.getByRole('heading', { name: 'Quick exercises' })).toBeVisible();
  await page.getByRole('button', { name: 'Give a work update' }).click();
  await expect(page.getByRole('heading', { name: 'Grammar · 1 of 3', exact: true })).toBeFocused();
  await expect(page.getByRole('button', { name: 'Check answer' })).toBeDisabled();

  await page.getByRole('radio', { name: 'I check the figures yesterday.' }).check();
  await page.getByRole('button', { name: 'Check answer' }).click();
  await expect(page.getByText(/The answer is “I checked the figures yesterday\.”/)).toBeVisible();
  await expect(page.getByText(/Use the simple past/)).toBeVisible();
  await expect(page.getByRole('radio', { name: 'I checked the figures yesterday.' })).toBeDisabled();
  await page.getByRole('button', { name: 'Next question' }).click();

  await expect(page.getByRole('heading', { name: 'Vocabulary · 2 of 3', exact: true })).toBeFocused();
  await page.getByRole('radio', { name: 'The draft is on hold.' }).check();
  await page.getByRole('button', { name: 'Check answer' }).click();
  await expect(page.getByText('Correct.', { exact: true })).toBeVisible();
  await page.getByRole('button', { name: 'Next question' }).click();

  await page.getByRole('radio', { name: 'I can send a draft today and the full report tomorrow.' }).check();
  await page.getByRole('button', { name: 'Check answer' }).click();
  await page.getByRole('button', { name: 'Finish exercises' }).click();
  await expect(page.getByRole('heading', { name: 'Try it aloud' })).toBeFocused();
  await expect(page.getByText('You got 2 of 3 correct on your first try.')).toBeVisible();
  await page.getByText('See an example', { exact: true }).click();
  await expect(page.getByText('I checked the figures this morning.', { exact: false })).toBeVisible();
  await page.getByRole('button', { name: 'Practice again' }).click();
  await expect(page.getByRole('button', { name: 'Check answer' })).toBeDisabled();
  await page.getByRole('button', { name: 'Choose another situation' }).click();
  await expect(page.getByRole('heading', { name: 'Choose a situation' })).toBeFocused();

  await page.getByRole('button', { name: 'Find the right train' }).click();
  await expect(page.getByText('You want to ask for the next train’s departure time.', { exact: false })).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  await page.getByRole('link', { name: 'Speaking lessons' }).click();
  await expect(page.getByRole('heading', { name: 'Find your voice.' })).toBeVisible();
  expect(admissionRequests).toEqual([]);
  expect(errors).toEqual([]);
});
