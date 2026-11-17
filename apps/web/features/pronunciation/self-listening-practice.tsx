'use client';

import { useEffect, useId, useRef, useState } from 'react';
import { MAX_RECORDING_SECONDS, recordLearnerAudio } from './recording';
import styles from './self-listening-practice.module.css';

type RecordingState =
  | { phase: 'idle' }
  | { phase: 'requesting' }
  | { phase: 'recording'; stop: () => void }
  | { phase: 'finishing' }
  | { phase: 'ready'; url: string }
  | { phase: 'error'; message: string };

function attachPlayback(element: HTMLAudioElement | null) {
  if (!element) return;
  return () => {
    element.pause();
    element.removeAttribute('src');
    element.load();
  };
}

export function SelfListeningPractice({ phrase }: { phrase: string }) {
  const headingId = useId();
  const [state, setState] = useState<RecordingState>({ phase: 'idle' });
  const request = useRef<AbortController | null>(null);
  const clipUrl = useRef<string | null>(null);

  useEffect(() => {
    function cancelHiddenCapture() {
      if (!document.hidden || !request.current) return;
      request.current.abort();
      request.current = null;
      setState({ phase: 'idle' });
    }
    document.addEventListener('visibilitychange', cancelHiddenCapture);
    return () => {
      document.removeEventListener('visibilitychange', cancelHiddenCapture);
      request.current?.abort();
      if (clipUrl.current) URL.revokeObjectURL(clipUrl.current);
    };
  }, []);

  function clear() {
    request.current?.abort();
    request.current = null;
    if (clipUrl.current) URL.revokeObjectURL(clipUrl.current);
    clipUrl.current = null;
    setState({ phase: 'idle' });
  }

  async function start() {
    clear();
    const attempt = new AbortController();
    request.current = attempt;
    setState({ phase: 'requesting' });
    try {
      const clip = await recordLearnerAudio(attempt.signal, (stop) => {
        setState({
          phase: 'recording',
          stop: () => {
            setState({ phase: 'finishing' });
            stop();
          },
        });
      });
      if (attempt.signal.aborted) return;
      const url = URL.createObjectURL(clip);
      clipUrl.current = url;
      setState({ phase: 'ready', url });
    } catch (error) {
      if (attempt.signal.aborted) return;
      const message = error instanceof Error ? error.message : 'The recording could not be saved.';
      setState({ phase: 'error', message });
    } finally {
      if (request.current === attempt) request.current = null;
    }
  }

  function handlePlaybackError() {
    clear();
    setState({ phase: 'error', message: 'This browser could not play your clip. Try recording again.' });
  }

  return (
    <section className={styles.panel} aria-labelledby={headingId}>
      <h3 id={headingId}>Listen to your speaking</h3>
      <p className={styles.phrase}>{phrase}</p>
      <p>Read the sentence aloud, then listen for which words you stressed and where you paused.</p>
      <p>The clip stays in this tab. Leaving this activity clears it.</p>

      {state.phase === 'requesting' && <p role="status">Waiting for microphone permission.</p>}
      {state.phase === 'recording' && <p role="status">Recording for up to {MAX_RECORDING_SECONDS} seconds.</p>}
      {state.phase === 'finishing' && <p role="status">Preparing your clip.</p>}
      {state.phase === 'error' && <p role="status">{state.message}</p>}
      {state.phase === 'ready' && (
        <audio
          ref={attachPlayback}
          controls
          controlsList="nodownload"
          preload="metadata"
          src={state.url}
          aria-label="Your practice recording"
          onError={handlePlaybackError}
        />
      )}

      <div className={styles.actions}>
        {(state.phase === 'idle' || state.phase === 'error') && (
          <button type="button" className="button button-mic" onClick={start}>Start recording</button>
        )}
        {state.phase === 'recording' && (
          <button type="button" className="button button-primary" onClick={state.stop}>Stop recording</button>
        )}
        {(state.phase === 'requesting' || state.phase === 'recording' || state.phase === 'finishing') && (
          <button type="button" className="button button-mic" onClick={clear}>Cancel recording</button>
        )}
        {state.phase === 'ready' && (
          <>
            <button type="button" className="button button-mic" onClick={start}>Record again</button>
            <button type="button" className="button button-mic" onClick={clear}>Delete recording</button>
          </>
        )}
      </div>
    </section>
  );
}
