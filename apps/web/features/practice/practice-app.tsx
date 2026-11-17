'use client';

import Link from 'next/link';
import { type FormEvent, useEffect, useRef, useState } from 'react';
import { SelfListeningPractice } from '@/features/pronunciation/self-listening-practice';
import { ACTIVITIES, type Activity } from './activities';
import styles from './practice.module.css';

export function PracticeApp() {
  const [activity, setActivity] = useState<Activity | null>(null);
  const activityList = useRef<HTMLHeadingElement>(null);
  const returning = useRef(false);

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
        <h2 id="activity-heading" ref={activityList} tabIndex={-1}>
          {activity ? activity.title : 'Choose a situation'}
        </h2>
        {activity ? (
          <ExerciseSession key={activity.id} activity={activity} onExit={changeActivity} />
        ) : (
          <ul className={styles.activities}>
            {ACTIVITIES.map((item) => (
              <li key={item.id}>
                <button className="button button-mic" type="button" onClick={() => setActivity(item)}>
                  {item.title}
                </button>
                <p>{item.description}</p>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  );
}

function ExerciseSession({ activity, onExit }: { activity: Activity; onExit: () => void }) {
  const [step, setStep] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [results, setResults] = useState<boolean[]>([]);
  const [listening, setListening] = useState(false);
  const heading = useRef<HTMLHeadingElement>(null);
  const current = activity.exercises[step];
  const checked = results.length > step;

  useEffect(() => { heading.current?.focus(); }, [step]);

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (checked) {
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
    return (
      <div className={styles.session}>
        <h3 ref={heading} tabIndex={-1}>Try it aloud</h3>
        <p>You got {correct} of {activity.exercises.length} correct on your first try.</p>
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
