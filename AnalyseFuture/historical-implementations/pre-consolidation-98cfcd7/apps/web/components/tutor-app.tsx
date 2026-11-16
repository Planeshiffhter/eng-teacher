'use client';

// Audio-room composition adapted from the MIT-licensed LiveKit React starter.
// The original notice is retained in apps/web/LICENSE.
import { LiveKitRoom, RoomAudioRenderer, StartAudio, useConnectionState, useLocalParticipant, useRoomContext, useTranscriptions, useVoiceAssistant } from '@livekit/components-react';
import { ConnectionState, RoomEvent, type RemoteParticipant } from 'livekit-client';
import { useCallback, useEffect, useRef, useState } from 'react';
import { LESSON_SECONDS, lessonDeadline, mergeFeedback, parseTutorEvent, secondsRemaining, type TutorFeedback } from '@/lib/tutor-events';

interface ConnectionDetails { serverUrl: string; participantToken: string; roomName: string }

function MicIcon({ muted = false }: { muted?: boolean }) {
  return <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true"><rect x="9" y="2" width="6" height="13" rx="3" /><path d="M5 10v2a7 7 0 0 0 14 0v-2M12 19v3M8 22h8" />{muted && <path d="M3 3l18 18" />}</svg>;
}
function ArrowIcon() {
  return <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" /></svg>;
}
function SoundMark({ active = false }: { active?: boolean }) {
  return <div className={`sound-mark ${active ? 'is-active' : ''}`} aria-hidden="true">{[18, 38, 58, 32, 48, 25, 16].map((height, i) => <span key={i} style={{ height, animationDelay: `${i * 110}ms` }} />)}</div>;
}

export function TutorApp() {
  const [connection, setConnection] = useState<ConnectionDetails | null>(null);
  const [joining, setJoining] = useState(false);
  const [accessCode, setAccessCode] = useState('');
  const [message, setMessage] = useState('');
  const [finished, setFinished] = useState(false);
  const [feedback, setFeedback] = useState<TutorFeedback[]>([]);
  const ended = useRef(false);
  const joinAbort = useRef<AbortController | null>(null);

  useEffect(() => () => joinAbort.current?.abort(), []);

  const finish = useCallback((reason: string) => {
    if (ended.current) return;
    ended.current = true;
    setMessage(reason);
    setConnection(null);
    setJoining(false);
    setFinished(true);
  }, []);
  const receiveFeedback = useCallback((event: TutorFeedback) => setFeedback((previous) => mergeFeedback(previous, event)), []);

  async function startLesson(event: React.FormEvent) {
    event.preventDefault();
    if (joining) return;
    if (!window.isSecureContext || !navigator.mediaDevices?.getUserMedia) {
      setMessage('Microphone access needs HTTPS or localhost and a supported browser.');
      return;
    }
    ended.current = false;
    setMessage('');
    setFinished(false);
    setFeedback([]);
    setJoining(true);
    const controller = new AbortController();
    joinAbort.current = controller;
    const timeout = window.setTimeout(() => controller.abort(), 20_000);
    try {
      const response = await fetch('/api/session', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ accessCode }), signal: controller.signal,
      });
      const data: unknown = await response.json();
      if (!response.ok) {
        const serverMessage = data && typeof data === 'object' && 'error' in data && typeof data.error === 'string' ? data.error : 'The lesson could not start. Please try again.';
        throw new Error(serverMessage);
      }
      if (!data || typeof data !== 'object' || !('serverUrl' in data) || !('participantToken' in data) || !('roomName' in data) ||
        typeof data.serverUrl !== 'string' || typeof data.participantToken !== 'string' || typeof data.roomName !== 'string') {
        throw new Error('The voice session returned an invalid connection. Please try again.');
      }
      setConnection(data as ConnectionDetails);
      setAccessCode('');
    } catch (error) {
      if (!ended.current) setMessage(error instanceof Error && error.name !== 'AbortError' ? error.message : 'The lesson server did not respond. Please try again.');
    } finally {
      window.clearTimeout(timeout);
      setJoining(false);
    }
  }

  const corrections = feedback.filter((item) => item.action === 'correct' && item.corrected);

  return <main className="app-shell">
    <header className="site-header">
      <a className="wordmark" href="/" aria-label="Eng Teacher home"><span className="brand-icon" aria-hidden="true">e<span>˙</span></span> eng teacher<span className="pilot-tag">PILOT</span></a>
      <span className="header-note"><span className="tiny-dot" /> A little practice. More confidence.</span>
    </header>
    <div className="page-heading"><div><p className="eyebrow">YOUR SPEAKING SPACE</p><h1>Find your voice.</h1><p className="intro">A real conversation. One helpful correction at a time.</p></div><div className="lesson-chip"><span aria-hidden="true">◷</span> 10-minute lesson</div></div>

    {connection ? <LiveKitRoom
      serverUrl={connection.serverUrl}
      token={connection.participantToken}
      connect audio={{ echoCancellation: true, noiseSuppression: true }} video={false}
      onDisconnected={() => finish('The voice session has ended. Your practice recap is below.')}
      onError={() => finish('Could not connect to the voice room. Check your connection and try again.')}
      onMediaDeviceFailure={() => finish('Microphone access is unavailable. Allow microphone permission, check your input device, and try again.')}
      className="live-room"
    >
      <LessonRoom feedback={feedback} onFeedback={receiveFeedback} onFinish={finish} />
      <RoomAudioRenderer />
    </LiveKitRoom> : <div className="lesson-grid">
      <section className="practice-card welcome-card" aria-labelledby="lesson-title">
        <div className="card-topline"><span className="soft-tag">MOCK INTERVIEW</span><span className="audio-label"><MicIcon /> Audio lesson</span></div>
        <div className="tutor-presence"><SoundMark /><span className="presence-caption">Your next step starts with a conversation</span></div>
        <div className="welcome-copy"><h2 id="lesson-title">A little more interview-ready.</h2><p>Meet your AI speaking tutor. Talk about your experience, practice your answers, and build confidence for your next interview.</p></div>
        <div className="language-note"><span aria-hidden="true">अ / A</span><div><strong>English or Hindi–English. Your choice.</strong><p>Mix languages when you need to. We’ll help you find the English.</p></div></div>
        <form onSubmit={startLesson} className="start-form">
          <label htmlFor="pilot-access">Pilot access code</label>
          <div className="start-controls"><input id="pilot-access" name="pilot-access" type="password" autoComplete="off" required value={accessCode} onChange={(event) => setAccessCode(event.target.value)} placeholder="Enter your access code" maxLength={256} disabled={joining} /><button className="button button-primary" disabled={joining} type="submit"><MicIcon />{joining ? 'Connecting…' : finished ? 'Practice again' : 'Start my lesson'}<ArrowIcon /></button></div>
          <p className="permission-note">Allow microphone access when your browser asks. Headphones work best.</p>
        </form>
        {message && <p className="notice" role={finished ? 'status' : 'alert'}>{message}</p>}
      </section>
      <aside className="side-stack"><section className="info-card"><p className="eyebrow">A SIMPLE WAY TO IMPROVE</p><h2>Speak. Refine. Try again.</h2><ol className="lesson-steps"><li><span>01</span><div><strong>Make it a conversation</strong><p>Answer one interview question at a time. Take your time.</p></div></li><li><span>02</span><div><strong>Find a clearer way to say it</strong><p>See your original words and one useful suggestion, side by side.</p></div></li><li><span>03</span><div><strong>Say it with confidence</strong><p>Try the phrase aloud, then keep the interview going.</p></div></li></ol></section><div className="small-note"><span aria-hidden="true">↳</span><p>You can interrupt your tutor. This is your conversation, too.</p></div></aside>
    </div>}

    {!connection && finished && <section className="recap-section" aria-labelledby="recap-title"><p className="eyebrow">TODAY’S PRACTICE</p><h2 id="recap-title">Your lesson recap</h2>{corrections.length ? <div className="recap-grid">{corrections.map((item) => <FeedbackCard key={item.turn_id} feedback={item} />)}</div> : <p>No correction cards were received in this session. Live voice quality still depends on the connected services.</p>}<p className="muted small">Your recap stays in this page’s memory. Refreshing the page clears it.</p></section>}
    <footer className="site-footer"><span className="privacy-mark" aria-hidden="true">◇</span><p>This app does not record or save your lesson. Connected providers process live audio.</p><span>Built for progress, one conversation at a time.</span></footer>
  </main>;
}

function LessonRoom({ feedback, onFeedback, onFinish }: { feedback: TutorFeedback[]; onFeedback: (event: TutorFeedback) => void; onFinish: (reason: string) => void }) {
  const room = useRoomContext();
  const connectionState = useConnectionState();
  const { agent, state } = useVoiceAssistant();
  const { localParticipant, isMicrophoneEnabled } = useLocalParticipant();
  const transcriptions = useTranscriptions();
  const [remaining, setRemaining] = useState(LESSON_SECONDS);
  const [micError, setMicError] = useState('');
  const [isTogglingMic, setTogglingMic] = useState(false);
  const deadline = useRef<number | null>(null);
  const transcriptEnd = useRef<HTMLDivElement>(null);

  const endSession = useCallback((reason: string) => {
    // Unmounting LiveKitRoom disconnects and stops its microphone tracks as well.
    onFinish(reason);
    void room.disconnect();
  }, [room, onFinish]);

  useEffect(() => {
    if (connectionState !== ConnectionState.Connected) return;
    deadline.current ??= Date.now() + LESSON_SECONDS * 1_000;
  }, [connectionState]);

  useEffect(() => {
    const timer = window.setInterval(() => {
      if (deadline.current === null) return;
      const left = secondsRemaining(deadline.current, Date.now());
      setRemaining(left);
      if (left === 0) endSession('Ten minutes complete. Here are the phrases you practiced today.');
    }, 250);
    return () => window.clearInterval(timer);
  }, [endSession]);

  useEffect(() => {
    if (connectionState === ConnectionState.Connected) return;
    const timer = window.setTimeout(() => endSession(
      'The voice connection timed out. Check your connection and try again.'
    ), 20_000);
    return () => window.clearTimeout(timer);
  }, [connectionState, endSession]);

  useEffect(() => {
    if (connectionState !== ConnectionState.Connected || agent) return;
    const timer = window.setTimeout(() => endSession('Your tutor could not join. Check that the voice agent and speech services are running, then try again.'), 30_000);
    return () => window.clearTimeout(timer);
  }, [connectionState, agent, endSession]);

  useEffect(() => {
    const receiveData = (payload: Uint8Array, participant?: RemoteParticipant, _kind?: unknown, topic?: string) => {
      if (!participant?.isAgent) return;
      const event = parseTutorEvent(payload, topic);
      if (event?.topic === 'tutor.feedback') onFeedback(event.data);
      if (event?.topic === 'tutor.error') endSession(event.data.message);
      if (event?.topic === 'tutor.lesson') {
        deadline.current = lessonDeadline(deadline.current ?? Date.now() + LESSON_SECONDS * 1_000, event.data.deadline_ms);
        if (event.data.state === 'ended') endSession('Your lesson is complete. Keep practicing the phrases in your recap.');
      }
    };
    room.on(RoomEvent.DataReceived, receiveData);
    return () => { room.off(RoomEvent.DataReceived, receiveData); };
  }, [room, onFeedback, endSession]);

  useEffect(() => { transcriptEnd.current?.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, [transcriptions]);

  async function toggleMic() {
    setTogglingMic(true);
    setMicError('');
    try { await localParticipant.setMicrophoneEnabled(!isMicrophoneEnabled); }
    catch { setMicError('Could not change microphone access. Check your browser permission and input device.'); }
    finally { setTogglingMic(false); }
  }

  const stateLabel = connectionState !== ConnectionState.Connected ? 'Connecting to your lesson…' : !agent ? 'Waiting for your tutor…' : state === 'speaking' ? 'Your tutor is speaking' : state === 'thinking' ? 'Your tutor is thinking' : state === 'listening' ? 'Your turn. We’re listening.' : 'Your tutor is getting ready…';
  const latest = feedback[feedback.length - 1];
  const visibleTranscripts = transcriptions.filter((item) => item.text.trim()).slice(-80);

  return <div className="lesson-grid">
    <section className="practice-card active-card" aria-label="Live interview lesson">
      <div className="card-topline"><span className="soft-tag"><span className="tiny-dot" /> LIVE INTERVIEW</span><span className="time-remaining" aria-label={`${remaining} seconds remaining`}>{Math.floor(remaining / 60)}:{String(remaining % 60).padStart(2, '0')} <span>remaining</span></span></div>
      <div className="active-presence"><SoundMark active={state === 'speaking'} /><h2 role="status">{stateLabel}</h2><p>Speak naturally. English and Hindi–English are welcome.</p><span className="audio-only">Audio only · You can interrupt at any time</span></div>
      <StartAudio className="button button-primary enable-audio" label="Enable tutor audio" />
      <div className="transcript-panel" aria-label="Live subtitles"><div className="section-title"><h3>Live subtitles</h3><span>Speech recognition may make mistakes</span></div><div className="transcript-scroll" role="log" aria-live="polite" aria-relevant="additions text">{visibleTranscripts.length ? visibleTranscripts.map((item) => <p key={item.streamInfo.id} className={item.participantInfo.identity === localParticipant.identity ? 'transcript-student' : 'transcript-tutor'}><span>{item.participantInfo.identity === localParticipant.identity ? 'You' : 'Tutor'}</span>{item.text}</p>) : <p className="transcript-placeholder">Your conversation will appear here as you speak.</p>}<div ref={transcriptEnd} /></div></div>
      {micError && <p className="notice" role="alert">{micError}</p>}
      <div className="session-controls"><button className={`button button-mic ${!isMicrophoneEnabled ? 'is-muted' : ''}`} onClick={toggleMic} disabled={isTogglingMic} aria-pressed={!isMicrophoneEnabled}><MicIcon muted={!isMicrophoneEnabled} />{isMicrophoneEnabled ? 'Mute mic' : 'Unmute mic'}</button><button className="button button-end" onClick={() => endSession('Lesson ended. Your practice recap is below.')}><span aria-hidden="true">■</span> End lesson</button></div>
    </section>
    <aside className="side-stack"><section className="info-card feedback-panel"><p className="eyebrow">ONE SMALL STEP FORWARD</p><h2>Your speaking notes</h2>{latest ? <FeedbackCard feedback={latest} /> : <div className="feedback-empty"><span aria-hidden="true">“</span><p>Speak freely. A helpful suggestion will appear here when there’s something worth practicing.</p></div>}</section><div className="small-note"><span aria-hidden="true">↳</span><p>Your original words stay separate from suggestions. Ask your tutor to clarify if something feels wrong.</p></div></aside>
  </div>;
}

function FeedbackCard({ feedback }: { feedback: TutorFeedback }) {
  return <article className="feedback-card"><span className="feedback-type">{feedback.action === 'correct' ? 'A clearer way to say it' : feedback.action === 'clarify' ? 'Let’s make sure we understood' : feedback.action === 'retry' ? 'Your speaking retry' : feedback.action === 'assist' ? 'Your teacher explains' : 'Keep the conversation going'}</span><div className="original-phrase"><span>You said</span><p>{feedback.original || 'No clear speech recognized'}</p></div>{feedback.corrected && <div className="corrected-phrase"><span>Try saying</span><p>{feedback.corrected}</p></div>}{feedback.explanation && <p className="explanation">{feedback.explanation}</p>}<p className="speaking-prompt">{feedback.spoken_response}</p></article>;
}
