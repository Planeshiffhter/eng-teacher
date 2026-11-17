import { expect, test } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { ModuleKind, ScriptTarget, transpileModule } from 'typescript';
import type { createTeacherAudioAnimation } from '../../apps/web/features/avatar/teacher-audio';

test('a synthetic teacher track drives the mouth while its existing playback and track remain intact', async ({ page }) => {
  const source = readFileSync('apps/web/features/avatar/teacher-audio.ts', 'utf8');
  // Exercise the production adapter with a synthetic substitute for the room's remote teacher track.
  const { outputText } = transpileModule(source, { compilerOptions: { target: ScriptTarget.ES2022, module: ModuleKind.ES2022 } });
  await page.route('**/avatar-fixture', (route) => route.fulfill({
    contentType: 'text/html',
    body: '<!doctype html><button>Run audio test</button><audio autoplay></audio>',
  }));
  await page.route('**/teacher-audio-fixture.js', (route) => route.fulfill({
    contentType: 'text/javascript',
    body: outputText,
  }));
  await page.goto('/avatar-fixture');
  const result = page.evaluate(async () => {
    const moduleUrl = '/teacher-audio-fixture.js';
    const adapter = await import(moduleUrl) as { createTeacherAudioAnimation: typeof createTeacherAudioAnimation };
    return new Promise<{ playbackIntact: boolean; frameDifference: boolean; stoppedSampling: boolean }>((resolve, reject) => {
      async function run() {
        const tone = new AudioContext();
        const oscillator = tone.createOscillator();
        const volume = tone.createGain();
        const output = tone.createMediaStreamDestination();
        const replacement = tone.createMediaStreamDestination();
        const playback = document.querySelector('audio')!;
        const animation = adapter.createTeacherAudioAnimation();
        async function waitFor(label: string, check: () => boolean) {
          const until = performance.now() + 6000;
          while (!check()) {
            if (performance.now() > until) throw new Error(`Timed out waiting for ${label}`);
            await new Promise((done) => setTimeout(done, 30));
          }
        }
        try {
          await Promise.all([tone.resume(), animation.resume()]);
          volume.gain.value = 0.25;
          oscillator.connect(volume).connect(output);
          oscillator.start();
          const teacherTrack = output.stream.getAudioTracks()[0];
          playback.srcObject = output.stream;
          await playback.play();
          animation.setTrack(teacherTrack);
          await waitFor('initial mouth movement', () => animation.mouthOpening() > 0.5);
          const speaking = animation.mouthOpening();
          volume.gain.value = 0;
          await waitFor('mouth movement to stop during silence', () => animation.mouthOpening() < 0.05);
          const silent = animation.mouthOpening();
          volume.gain.value = 0.25;
          await waitFor('mouth movement to resume', () => animation.mouthOpening() > 0.5);
          animation.setTrack(replacement.stream.getAudioTracks()[0]);
          await waitFor('silence after track replacement', () => animation.mouthOpening() < 0.05);
          animation.setTrack(null);
          const stoppedSampling = animation.mouthOpening() === 0;
          animation.setTrack(teacherTrack);
          await waitFor('mouth movement after track attachment', () => animation.mouthOpening() > 0.5);
          animation.close();
          return {
            playbackIntact: !playback.paused && teacherTrack.readyState === 'live' &&
              !playback.muted && document.querySelectorAll('audio').length === 1,
            frameDifference: speaking - silent > 0.45,
            stoppedSampling,
          };
        } finally {
          animation.close();
          playback.srcObject = null;
          for (const track of [...output.stream.getTracks(), ...replacement.stream.getTracks()]) track.stop();
          await tone.close();
        }
      }

      document.querySelector('button')!.addEventListener('click', () => {
        void run().then(resolve, reject);
      }, { once: true });
      document.querySelector('button')!.setAttribute('data-ready', 'true');
    });
  });
  const button = page.getByRole('button', { name: 'Run audio test' });
  await expect(button).toHaveAttribute('data-ready', 'true');
  await button.click();
  expect(await result).toEqual({ playbackIntact: true, frameDifference: true, stoppedSampling: true });
});

test('either avatar can be selected and the lesson controls survive an unavailable audio analyzer', async ({ page, baseURL }) => {
  // Keep the room connecting without presenting a successful LiveKit or provider connection.
  const server = new URL(baseURL!);
  server.protocol = 'ws:';
  await page.routeWebSocket(`${server.origin}/**`, () => {});
  await page.route('**/api/session', (route) => route.fulfill({
    json: { serverUrl: server.origin, participantToken: 'fixture-token', roomName: 'test-room', lessonId: 'mock-interview' },
  }));
  await page.goto('/');
  await page.getByLabel('Pilot access code').fill('test-only-pilot-code');
  await page.getByRole('button', { name: 'Start my lesson' }).click();
  const picker = page.getByLabel('Teacher view');
  await expect(picker).toHaveValue('audio');
  await picker.selectOption('woman');
  await expect(page.locator('[data-appearance="woman"]')).toBeVisible();
  await picker.selectOption('man');
  await expect(page.locator('[data-appearance="man"]')).toBeVisible();
  await picker.selectOption('audio');
  await expect(page.locator('[data-appearance]')).toHaveCount(0);
  await page.evaluate(() => {
    Object.defineProperty(window, 'AudioContext', {
      configurable: true,
      value: class {
        constructor() { throw new Error('Simulated Web Audio failure'); }
      },
    });
  });
  await picker.selectOption('woman');
  await expect(picker).toHaveValue('audio');
  await expect(page.getByRole('status').filter({ hasText: 'Avatar unavailable' })).toBeVisible();
  await page.getByRole('button', { name: 'End lesson' }).click();
  await expect(page.getByRole('button', { name: 'Practice again' })).toBeVisible();
});
