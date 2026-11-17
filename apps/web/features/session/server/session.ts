import { createHash, randomUUID, timingSafeEqual } from 'node:crypto';
import { AccessToken, RoomAgentDispatch, RoomConfiguration, TrackSource } from 'livekit-server-sdk';
import { DEFAULT_LESSON_ID, findLesson } from '../../lesson/catalog';

export type SessionConfig = {
  serverUrl: string;
  apiKey: string;
  apiSecret: string;
  accessCode: string;
  appOrigin?: string;
};

export class SessionError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

export function readConfig(env: Record<string, string | undefined> = process.env): SessionConfig {
  const required = ['LIVEKIT_URL', 'LIVEKIT_API_KEY', 'LIVEKIT_API_SECRET', 'PILOT_ACCESS_CODE'] as const;
  if (required.some((key) => !env[key]?.trim())) {
    throw new SessionError(503, 'Voice sessions are not configured. Ask the operator to configure LiveKit and the pilot access code.');
  }
  const server = new URL(env.LIVEKIT_URL!);
  if (!['ws:', 'wss:'].includes(server.protocol) || server.username || server.password) {
    throw new SessionError(503, 'The voice service URL is not configured correctly.');
  }
  if (env.PILOT_ACCESS_CODE!.length < 16 || env.LIVEKIT_API_SECRET!.length < 32) {
    throw new SessionError(503, 'The operator must configure a strong pilot access code and LiveKit API secret.');
  }
  return {
    serverUrl: env.LIVEKIT_URL!,
    apiKey: env.LIVEKIT_API_KEY!,
    apiSecret: env.LIVEKIT_API_SECRET!,
    accessCode: env.PILOT_ACCESS_CODE!,
    appOrigin: env.APP_ORIGIN,
  };
}

function secureEqual(a: string, b: string): boolean {
  return timingSafeEqual(createHash('sha256').update(a).digest(), createHash('sha256').update(b).digest());
}

/** Pilot-only process-local abuse protection; a distributed gateway is required before public rollout. */
export class RequestBudget {
  private starts: number[] = [];
  constructor(private readonly limit = 30, private readonly windowMs = 60_000) {}
  consume(now = Date.now()): boolean {
    this.starts = this.starts.filter((time) => time > now - this.windowMs);
    if (this.starts.length >= this.limit) return false;
    this.starts.push(now);
    return true;
  }
}

async function boundedJson(request: Request): Promise<unknown> {
  const reader = request.body?.getReader();
  if (!reader) throw new SessionError(400, 'Enter your pilot access code.');
  const chunks: Uint8Array[] = [];
  let length = 0;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      length += value.byteLength;
      if (length > 1024) {
        await reader.cancel();
        throw new SessionError(413, 'The session request is too large.');
      }
      chunks.push(value);
    }
    return JSON.parse(Buffer.concat(chunks).toString('utf8'));
  } catch (error) {
    if (error instanceof SessionError) throw error;
    throw new SessionError(400, 'The session request is invalid.');
  } finally {
    reader.releaseLock();
  }
}

export async function issueSession(request: Request, config: SessionConfig) {
  const origin = request.headers.get('origin');
  const expectedOrigin = config.appOrigin || new URL(request.url).origin;
  if (!origin || origin !== expectedOrigin) throw new SessionError(403, 'Start the lesson from this application.');
  const mediaType = request.headers.get('content-type')?.split(';', 1)[0].trim().toLowerCase();
  if (mediaType !== 'application/json') {
    throw new SessionError(415, 'Send a JSON session request.');
  }
  const body = await boundedJson(request);
  if (!body || typeof body !== 'object' || !('accessCode' in body) || typeof body.accessCode !== 'string' || body.accessCode.length > 256) {
    throw new SessionError(400, 'Enter your pilot access code.');
  }
  if (!secureEqual(body.accessCode, config.accessCode)) throw new SessionError(401, 'The pilot access code is incorrect.');
  const lesson = findLesson('lessonId' in body ? body.lessonId : DEFAULT_LESSON_ID);
  if (!lesson) throw new SessionError(400, 'Choose an available practice lesson.');

  // Neither room names, identities nor dispatch can be chosen by a caller.
  const roomName = `interview-${randomUUID()}`;
  const token = new AccessToken(config.apiKey, config.apiSecret, {
    identity: `learner-${randomUUID()}`,
    name: 'Learner',
    ttl: '10m',
  });
  token.addGrant({
    roomJoin: true,
    room: roomName,
    canSubscribe: true,
    canPublish: true,
    canPublishSources: [TrackSource.MICROPHONE],
    canPublishData: false,
  });
  // The server admits only this learner and the named agent. No room recording is started.
  token.roomConfig = new RoomConfiguration({
    name: roomName,
    metadata: JSON.stringify({ lesson_deadline_ms: Date.now() + 600_000, lesson_id: lesson.id }),
    maxParticipants: 2,
    emptyTimeout: 60,
    departureTimeout: 20,
    agents: [new RoomAgentDispatch({ agentName: 'eng-teacher' })],
  });
  return { serverUrl: config.serverUrl, roomName, participantToken: await token.toJwt(), lessonId: lesson.id };
}
