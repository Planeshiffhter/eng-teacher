import { describe, expect, it } from 'vitest';
import { TokenVerifier } from 'livekit-server-sdk';
import contract from '../../../../../tests/contracts/lesson-catalog.json';
import { issueSession, readConfig, RequestBudget, SessionError, type SessionConfig } from '../server/session';

const config: SessionConfig = {
  serverUrl: 'wss://test.livekit.cloud',
  apiKey: 'test-key',
  apiSecret: 'test-only-secret-with-at-least-32-characters',
  accessCode: 'test-only-pilot-access-code',
};
function request(body: unknown = { accessCode: config.accessCode }, origin = 'http://localhost:3000') {
  return new Request('http://localhost:3000/api/session', {
    method: 'POST', headers: { origin, 'content-type': 'application/json' }, body: JSON.stringify(body),
  });
}

describe('session token boundary (real local signing; no LiveKit service)', () => {
  it('signs room-scoped microphone-only tokens and dispatches only our named worker', async () => {
    const response = await issueSession(request({ accessCode: config.accessCode, roomName: 'attack', agentName: 'other' }), config);
    const claims = await new TokenVerifier(config.apiKey, config.apiSecret).verify(response.participantToken);
    expect(response.serverUrl).toBe(config.serverUrl);
    expect(response.roomName).toMatch(/^interview-/);
    expect(claims.video).toMatchObject({ room: response.roomName, roomJoin: true, canPublish: true, canPublishData: false, canPublishSources: ['microphone'] });
    expect(claims.roomConfig).toMatchObject({ maxParticipants: 2, agents: [{ agentName: 'eng-teacher' }] });
    expect(claims.roomConfig?.egress).toBeUndefined();
    const deadline = JSON.parse(claims.roomConfig!.metadata!).lesson_deadline_ms;
    expect(JSON.parse(claims.roomConfig!.metadata!).lesson_id).toBe('mock-interview');
    expect(response.lessonId).toBe('mock-interview');
    expect(deadline).toBeGreaterThan(Date.now() + 590_000);
    expect(deadline).toBeLessThanOrEqual(Date.now() + 600_000);
    expect(claims.sub).toMatch(/^learner-/);
    expect(claims.exp! - claims.nbf!).toBeLessThanOrEqual(10 * 60);
    expect(JSON.stringify(response)).not.toContain(config.apiSecret);
  });
  it('uses unique rooms for separate sessions', async () => {
    const a = await issueSession(request(), config);
    const b = await issueSession(request(), config);
    expect(a.roomName).not.toBe(b.roomName);
  });
  it('signs only the selected catalog lesson while retaining grants and deadline', async () => {
    for (const lessonId of contract.lesson_ids) {
      const response = await issueSession(request({ accessCode: config.accessCode, lessonId, greeting: 'injected prompt' }), config);
      const claims = await new TokenVerifier(config.apiKey, config.apiSecret).verify(response.participantToken);
      const metadata = JSON.parse(claims.roomConfig!.metadata!);
      expect(response.lessonId).toBe(lessonId);
      expect(metadata).toEqual({ lesson_id: lessonId, lesson_deadline_ms: expect.any(Number) });
      expect(metadata.lesson_deadline_ms).toBeGreaterThan(Date.now() + 590_000);
      expect(claims.video).toMatchObject({ canPublishSources: ['microphone'], canPublishData: false });
      expect(claims.roomConfig!.agents[0].agentName).toBe('eng-teacher');
    }
  });
  it('rejects explicit invalid lesson selections rather than falling back', async () => {
    for (const lessonId of [null, false, 42, [], {}, '', 'unknown', 'constructor', '__proto__']) {
      await expect(issueSession(request({ accessCode: config.accessCode, lessonId }), config)).rejects.toMatchObject({ status: 400 });
    }
  });
  it('rejects incorrect access codes and cross-origin requests', async () => {
    await expect(issueSession(request({ accessCode: 'wrong' }), config)).rejects.toMatchObject({ status: 401 });
    await expect(issueSession(request(undefined, 'https://evil.example'), config)).rejects.toMatchObject({ status: 403 });
  });
  it('rejects lookalike JSON media types', async () => {
    for (const contentType of ['application/jsonp', 'application/json-invalid', 'text/plain']) {
      const input = new Request('http://localhost:3000/api/session', {
        method: 'POST', headers: { origin: 'http://localhost:3000', 'content-type': contentType },
        body: JSON.stringify({ accessCode: config.accessCode }),
      });
      await expect(issueSession(input, config)).rejects.toMatchObject({ status: 415 });
    }
  });
  it('accepts case-insensitive JSON media types with charset parameters', async () => {
    for (const contentType of ['application/json; charset=utf-8', 'Application/JSON']) {
      const input = new Request('http://localhost:3000/api/session', {
        method: 'POST', headers: { origin: 'http://localhost:3000', 'content-type': contentType },
        body: JSON.stringify({ accessCode: config.accessCode }),
      });
      await expect(issueSession(input, config)).resolves.toHaveProperty('participantToken');
    }
  });
  it('supports an explicitly configured deployed origin', async () => {
    await expect(issueSession(request(undefined, 'https://tutor.example'), { ...config, appOrigin: 'https://tutor.example' })).resolves.toHaveProperty('participantToken');
  });
  it('rejects malformed, oversized or missing access-code input', async () => {
    await expect(issueSession(request({ accessCode: 'x'.repeat(2048) }), config)).rejects.toMatchObject({ status: 413 });
    await expect(issueSession(request([]), config)).rejects.toMatchObject({ status: 400 });
    const broken = new Request('http://localhost:3000/api/session', { method: 'POST', headers: { origin: 'http://localhost:3000', 'content-type': 'application/json' }, body: '{broken' });
    await expect(issueSession(broken, config)).rejects.toMatchObject({ status: 400 });
  });
  it('refuses unconfigured sessions without returning any secret', () => {
    expect(() => readConfig({})).toThrow(SessionError);
    expect(() => readConfig({ LIVEKIT_URL: config.serverUrl, LIVEKIT_API_KEY: 'key', LIVEKIT_API_SECRET: 'weak', PILOT_ACCESS_CODE: 'weak' })).toThrow(/strong/);
  });
  it('expires the pilot request budget after the configured window', () => {
    const budget = new RequestBudget(2, 1000);
    expect(budget.consume(0)).toBe(true);
    expect(budget.consume(100)).toBe(true);
    expect(budget.consume(200)).toBe(false);
    expect(budget.consume(1000)).toBe(true);
  });
});
