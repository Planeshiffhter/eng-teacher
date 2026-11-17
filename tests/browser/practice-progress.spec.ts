import { expect, test, type Page } from '@playwright/test';

const FIRST_ACTIVITY = /Give a work update/;
const SAVE_PROGRESS = 'Save progress on this browser';
const FIRST_STEP = 'Grammar · 1 of 3';
const SECOND_STEP = 'Vocabulary · 2 of 3';
const STARTED = 'In progress · 1 of 3 answered';
const COMPLETED = 'Latest result: 2 of 3 correct · 1 completion';

async function checkAnswer(page: Page, answer: string) {
  await page.getByRole('radio', { name: answer, exact: true }).check();
  await page.getByRole('button', { name: 'Check answer' }).click();
}

test('quick exercises keep results out of local storage until the learner opts in', async ({ page }) => {
  await page.goto('/practice');
  const activity = page.getByRole('button', { name: FIRST_ACTIVITY });
  const save = page.getByRole('checkbox', { name: SAVE_PROGRESS });

  await expect(save).not.toBeChecked();
  expect(await page.evaluate(() => localStorage.length)).toBe(0);
  await activity.click();
  await checkAnswer(page, 'I check the figures yesterday.');
  await page.getByRole('button', { name: 'Next question' }).click();
  await checkAnswer(page, 'The draft is on hold.');
  await page.getByRole('button', { name: 'Next question' }).click();
  await checkAnswer(page, 'I can send a draft today and the full report tomorrow.');
  await page.getByRole('button', { name: 'Finish exercises' }).click();
  await expect(page.getByText('You got 2 of 3 correct on your first try.')).toBeVisible();
  expect(await page.evaluate(() => localStorage.length)).toBe(0);

  await page.reload();
  await expect(save).not.toBeChecked();
  await expect(page.getByText(COMPLETED, { exact: true })).toHaveCount(0);
  await activity.click();
  await expect(page.getByRole('heading', { name: FIRST_STEP, exact: true })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Check answer' })).toBeDisabled();
});

test('opted-in quick exercises save confirmed steps and clear progress on opt-out', async ({ page }) => {
  await page.goto('/practice');
  const activity = page.getByRole('button', { name: FIRST_ACTIVITY });
  const save = page.getByRole('checkbox', { name: SAVE_PROGRESS });
  const inProgress = page.getByText(STARTED, { exact: true });
  const completed = page.getByText(COMPLETED, { exact: true });
  const check = page.getByRole('button', { name: 'Check answer' });
  const next = page.getByRole('button', { name: 'Next question' });
  const firstStep = page.getByRole('heading', { name: FIRST_STEP, exact: true });
  const secondStep = page.getByRole('heading', { name: SECOND_STEP, exact: true });

  await save.check();
  await activity.click();
  await checkAnswer(page, 'I check the figures yesterday.');
  await expect(next).toBeVisible();
  await page.reload();
  await expect(save).toBeChecked();
  await expect(inProgress).toHaveCount(0);
  await activity.click();
  await expect(firstStep).toBeVisible();
  await expect(check).toBeDisabled();

  await checkAnswer(page, 'I check the figures yesterday.');
  await next.click();
  await expect(secondStep).toBeVisible();
  await page.reload();
  await expect(save).toBeChecked();
  await expect(inProgress).toBeVisible();
  await activity.click();
  await expect(secondStep).toBeFocused();
  await expect(check).toBeDisabled();

  await checkAnswer(page, 'The draft is on hold.');
  await next.click();
  await checkAnswer(page, 'I can send a draft today and the full report tomorrow.');
  await page.getByRole('button', { name: 'Finish exercises' }).click();
  await expect(page.getByText('You got 2 of 3 correct on your first try.')).toBeVisible();
  await page.getByText('Review missed answers', { exact: true }).click();
  await expect(page.getByText(/I checked the figures yesterday\. Use the simple past/)).toBeVisible();
  await page.reload();
  await expect(save).toBeChecked();
  await expect(completed).toBeVisible();

  await save.uncheck();
  await expect(completed).toHaveCount(0);
  await page.reload();
  await expect(save).not.toBeChecked();
  await expect(completed).toHaveCount(0);
  await expect(inProgress).toHaveCount(0);
  expect(await page.evaluate(() => localStorage.length)).toBe(0);
  await activity.click();
  await expect(firstStep).toBeVisible();
  await expect(check).toBeDisabled();
});

test('clearing progress in another tab keeps it disabled when an exercise advances', async ({ page, context }) => {
  await page.goto('/practice');
  const save = page.getByRole('checkbox', { name: SAVE_PROGRESS });
  await save.check();
  await page.getByRole('button', { name: FIRST_ACTIVITY }).click();
  await checkAnswer(page, 'I check the figures yesterday.');
  await page.getByRole('button', { name: 'Next question' }).click();

  const other = await context.newPage();
  await other.goto('/practice');
  const otherSave = other.getByRole('checkbox', { name: SAVE_PROGRESS });
  await expect(otherSave).toBeChecked();
  await expect(other.getByText(STARTED, { exact: true })).toBeVisible();
  await otherSave.uncheck();
  await expect(save).not.toBeChecked();

  await checkAnswer(page, 'The draft is on hold.');
  await page.getByRole('button', { name: 'Next question' }).click();
  expect(await page.evaluate(() => localStorage.length)).toBe(0);
});
