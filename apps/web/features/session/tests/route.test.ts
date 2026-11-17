import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { TokenVerifier } from 'livekit-server-sdk';

const config = {
  LIVEKIT_URL: 'wss://test.livekit.cloud',
  LIVEKIT_API_KEY: 'test-key',
  LIVEKIT_API_SECRET: 'test-only-secret-with-at-least-32-characters',
  PILOT_ACCESS_CODE: 'test-only-pilot-access-code',
};

function request(body: unknown = { accessCode: config.PILOT_ACCESS_CODE, lessonId: 'everyday-conversation' }, contentType = 'application/json', origin = 'http://localhost:3000') {
  return new Request('http://localhost:3000/api/session', {
    method: 'POST', headers: { origin, 'content-type': contentType }, body: JSON.stringify(body),
  });
}

beforeEach(() => {
  vi.resetModules();
  for (const [key, value] of Object.entries(config)) vi.stubEnv(key, value);
  vi.stubEnv('APP_ORIGIN', '');
});
afterEach(() => vi.unstubAllEnvs());

describe('session API route with installed SDK and local signing', () => {
  it('returns a no-store token for the selected lesson with restricted grants', async () => {
    const { POST } = await import('../../../app/api/session/route');
    const response = await POST(request());
    expect(response.status).toBe(200);
    expect(response.headers.get('cache-control')).toContain('no-store');
    const body = await response.json();
    const claims = await new TokenVerifier(config.LIVEKIT_API_KEY, config.LIVEKIT_API_SECRET).verify(body.participantToken);
    expect(body.lessonId).toBe('everyday-conversation');
    expect(JSON.parse(claims.roomConfig!.metadata!).lesson_id).toBe('everyday-conversation');
    expect(claims.video).toMatchObject({ canPublishSources: ['microphone'], canPublishData: false });
    expect(JSON.stringify(body)).not.toContain(config.LIVEKIT_API_SECRET);
  });

  it('preserves typed admission failures and never returns a token for them', async () => {
    const { POST } = await import('../../../app/api/session/route');
    const cases = [
      [request(undefined, 'application/json', 'https://untrusted.example'), 403],
      [request(undefined, 'application/json-invalid'), 415],
      [request({ accessCode: 'wrong' }), 401],
      [request({ accessCode: config.PILOT_ACCESS_CODE, lessonId: 'unknown' }), 400],
    ] as const;
    for (const [input, status] of cases) {
      const response = await POST(input);
      expect(response.status).toBe(status);
      expect(response.headers.get('cache-control')).toContain('no-store');
      const body = await response.json();
      expect(body.error).toEqual(expect.any(String));
      expect(body.participantToken).toBeUndefined();
    }
  });

  it('enforces the route request budget with a retry hint', async () => {
    const { POST } = await import('../../../app/api/session/route');
    for (let index = 0; index < 30; index++) {
      expect((await POST(request({ accessCode: 'wrong' }))).status).toBe(401);
    }
    const response = await POST(request());
    expect(response.status).toBe(429);
    expect(response.headers.get('retry-after')).toBe('60');
    expect(response.headers.get('cache-control')).toContain('no-store');
    expect((await response.json()).participantToken).toBeUndefined();
  });

  it('hides missing and malformed configuration behind a no-token response', async () => {
    const { POST } = await import('../../../app/api/session/route');
    for (const url of ['', 'invalid-provider-url']) {
      vi.stubEnv('LIVEKIT_URL', url);
      const response = await POST(request());
      expect(response.status).toBe(503);
      const body = await response.json();
      expect(body.participantToken).toBeUndefined();
      expect(JSON.stringify(body)).not.toContain(config.LIVEKIT_API_SECRET);
      expect(JSON.stringify(body)).not.toContain('invalid-provider-url');
    }
  });
});
