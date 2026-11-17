'use client';

import Link from 'next/link';
import { type FormEvent, useEffect, useRef, useState } from 'react';
import { SelfListeningPractice } from '@/features/pronunciation/self-listening-practice';
import { ACTIVITIES, type Activity } from './activities';
import { clearProgress, enableProgress, PROGRESS_KEY, readProgress, saveProgress, type PracticeProgress } from './progress';
import styles from './practice.module.css';

export function PracticeApp() {
  const [activity, setActivity] = useState<Activity | null>(null);
  const [progress, setProgress] = useState<PracticeProgress | null>(null);
  const [storageError, setStorageError] = useState('');
  const activityList = useRef<HTMLHeadingElement>(null);
  const returning = useRef(false);

  useEffect(() => {
    function syncProgress() {
      try {
        setProgress(readProgress(window.localStorage));
        setStorageError('');
      } catch {
        setStorageError('This browser is blocking saved progress.');
      }
    }

    function onStorage(event: StorageEvent) {
      if (event.key === PROGRESS_KEY || event.key === null) syncProgress();
    }

    syncProgress();
    window.addEventListener('storage', onStorage);
    return () => window.removeEventListener('storage', onStorage);
  }, []);

  useEffect(() => {
    if (!activity && returning.current) {
      activityList.current?.focus();
      returning.current = false;
    }
  }, [activity]);

  function changeActivity() {
    returning.current = true;
    setActivity(null);
  }

  function toggleProgress(enabled: boolean) {
    try {
      if (enabled) {
        setProgress(enableProgress(window.localStorage));
      } else {
        clearProgress(window.localStorage);
        setProgress(null);
      }
      setStorageError('');
    } catch {
      setStorageError(enabled ? 'Progress could not be enabled in this browser.' : 'Progress could not be cleared. Try again or clear this site’s data.');
    }
  }

  function checkpoint(activityId: string, results: boolean[], completed: boolean) {
    if (!progress) return;
    try {
      setProgress(saveProgress(window.localStorage, activityId, results, completed));
      setStorageError('');
    } catch {
      setStorageError('This update could not be saved. You can still finish the exercises.');
    }
  }

  return (
    <main className={`app-shell ${styles.shell}`}>
      <header className="site-header">
        <Link className="wordmark" href="/">eng teacher</Link>
        <Link className="button button-mic" href="/">Speaking lessons</Link>
      </header>
      <div className="page-heading">
        <div>
          <h1>Quick exercises</h1>
          <p className="intro">Practice grammar and useful phrases for real situations.</p>
        </div>
      </div>
      <section className="practice-card" aria-labelledby="activity-heading">
        <div className={styles.progressControls}>
          <label>
            <input type="checkbox" checked={progress !== null} onChange={(event) => toggleProgress(event.target.checked)} aria-describedby="progress-note" />
            Save progress on this browser
          </label>
          <p id="progress-note">Save your place when you go to the next question, and keep your latest scores. Turning this off clears saved progress.</p>
          {storageError && <p role="status">{storageError}</p>}
        </div>
        <h2 id="activity-heading" ref={activityList} tabIndex={-1}>
          {activity ? activity.title : 'Choose a situation'}
        </h2>
        {activity ? (
          <ExerciseSession
            key={activity.id}
            activity={activity}
            draft={progress?.activities[activity.id]?.draft}
            onCheckpoint={(results, completed) => checkpoint(activity.id, results, completed)}
            onExit={changeActivity}
          />
        ) : (
          <ul className={styles.activities}>
            {ACTIVITIES.map((item) => {
              const saved = progress?.activities[item.id];
              return (
                <li key={item.id}>
                  <button className="button button-mic" type="button" onClick={() => setActivity(item)}>
                    {item.title}
                  </button>
                  <p>{item.description}</p>
                  {saved?.draft && <p className={styles.progressNote}>In progress · {saved.draft.length} of {item.exercises.length} answered</p>}
                  {saved?.latestScore != null && (
                    <p className={styles.progressNote}>
                      Latest result: {saved.latestScore} of {item.exercises.length} correct
                      {' · '}{saved.attempts} {saved.attempts === 1 ? 'completion' : 'completions'}
                    </p>
                  )}
                </li>
              );
            })}
          </ul>
        )}
      </section>
    </main>
  );
}

function ExerciseSession({ activity, draft, onCheckpoint, onExit }: {
  activity: Activity;
  draft?: boolean[] | null;
  onCheckpoint: (results: boolean[], completed: boolean) => void;
  onExit: () => void;
}) {
  const [step, setStep] = useState(draft?.length ?? 0);
  const [selected, setSelected] = useState<number | null>(null);
  const [results, setResults] = useState<boolean[]>(draft ?? []);
  const [listening, setListening] = useState(false);
  const heading = useRef<HTMLHeadingElement>(null);
  const current = activity.exercises[step];
  const checked = results.length > step;

  useEffect(() => { heading.current?.focus(); }, [step]);

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (checked) {
      onCheckpoint(results, step + 1 === activity.exercises.length);
      setSelected(null);
      setStep(step + 1);
    } else if (selected !== null) {
      setResults([...results, selected === current.correct]);
    }
  }

  function restart() {
    setListening(false);
    setResults([]);
    setStep(0);
  }

  if (!current) {
    const correct = results.filter(Boolean).length;
    const missed = activity.exercises.filter((_, index) => !results[index]);
    return (
      <div className={styles.session}>
        <h3 ref={heading} tabIndex={-1}>Try it aloud</h3>
        <p>You got {correct} of {activity.exercises.length} correct on your first try.</p>
        {missed.length > 0 && (
          <details>
            <summary>Review missed answers</summary>
            <ul className={styles.review}>
              {missed.map((exercise) => (
                <li key={exercise.prompt}>
                  <strong>{exercise.prompt}</strong>
                  <p>{exercise.options[exercise.correct]} {exercise.explanation}</p>
                </li>
              ))}
            </ul>
          </details>
        )}
        <p>{activity.speakingPrompt}</p>
        <details>
          <summary>See an example</summary>
          <p>{activity.example}</p>
        </details>
        <div className={styles.actions}>
          <button
            type="button"
            className="button button-mic"
            aria-expanded={listening}
            onClick={() => setListening(!listening)}
          >
            {listening ? 'Close recorder' : 'Record and listen back'}
          </button>
          <button type="button" className="button button-primary" onClick={restart}>Practice again</button>
          <button type="button" className="button button-mic" onClick={onExit}>Choose another situation</button>
        </div>
        {listening && <SelfListeningPractice phrase={activity.example} />}
      </div>
    );
  }

  return (
    <form className={styles.session} onSubmit={submit}>
      <h3 ref={heading} tabIndex={-1}>{current.focus} · {step + 1} of {activity.exercises.length}</h3>
      <fieldset className={styles.options} disabled={checked}>
        <legend>{current.prompt}</legend>
        {current.options.map((option, index) => (
          <label key={option}>
            <input
              type="radio"
              name="answer"
              checked={selected === index}
              onChange={() => setSelected(index)}
            />
            {option}
          </label>
        ))}
      </fieldset>
      <div aria-live="polite">
        {checked && (
          <p className={styles.feedback}>
            <strong>{results[step] ? 'Correct.' : `The answer is “${current.options[current.correct]}”`}</strong>
            {' '}{current.explanation}
          </p>
        )}
      </div>
      <div className={styles.actions}>
        <button type="submit" className="button button-primary" disabled={selected === null}>
          {checked ? (step + 1 === activity.exercises.length ? 'Finish exercises' : 'Next question') : 'Check answer'}
        </button>
        <button type="button" className="button button-mic" onClick={onExit}>Choose another situation</button>
      </div>
    </form>
  );
}
