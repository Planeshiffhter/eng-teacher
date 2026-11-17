'use client';

import { useCallback, useEffect, useRef, useState, type ReactNode } from 'react';
import { createTeacherAudioAnimation, type TeacherAudioAnimation } from './teacher-audio';
import styles from './teacher-avatar.module.css';

type Appearance = 'audio' | 'woman' | 'man';

export function TeacherAvatar({ track, fallback }: { track: MediaStreamTrack | null; fallback: ReactNode }) {
  const [appearance, setAppearance] = useState<Appearance>('audio');
  const [failed, setFailed] = useState(false);
  const animation = useRef<TeacherAudioAnimation | null>(null);
  const mouth = useRef<HTMLSpanElement>(null);
  const visual = appearance !== 'audio';

  const closeAnimation = useCallback(() => {
    animation.current?.close();
    animation.current = null;
  }, []);

  const fallBackToAudio = useCallback(() => {
    closeAnimation();
    setAppearance('audio');
    setFailed(true);
  }, [closeAnimation]);

  useEffect(() => closeAnimation, [closeAnimation]);

  useEffect(() => {
    const current = animation.current;
    const marker = mouth.current;
    if (!visual || !current || !marker || !track) return;
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let frame = 0;
    let lastSample = 0;
    let opening = 0;

    const advance = (now: number) => {
      if (now - lastSample >= 33) {
        lastSample = now;
        try {
          const level = current.mouthOpening();
          opening += (level - opening) * (level > opening ? 0.72 : 0.52);
          marker.style.transform = `scaleY(${0.15 + opening * 0.85})`;
        } catch {
          fallBackToAudio();
          return;
        }
      }
      frame = window.requestAnimationFrame(advance);
    };

    const applyMotionPreference = () => {
      window.cancelAnimationFrame(frame);
      marker.style.removeProperty('transform');
      try {
        current.setTrack(motion.matches ? null : track);
        if (!motion.matches) frame = window.requestAnimationFrame(advance);
      } catch {
        fallBackToAudio();
      }
    };

    applyMotionPreference();
    motion.addEventListener('change', applyMotionPreference);
    return () => {
      window.cancelAnimationFrame(frame);
      motion.removeEventListener('change', applyMotionPreference);
      marker.style.removeProperty('transform');
      current.setTrack(null);
    };
  }, [fallBackToAudio, track, visual]);

  function selectAppearance(next: Appearance) {
    setFailed(false);
    if (next === 'audio') {
      closeAnimation();
    } else if (!animation.current) {
      try {
        // Resume in the learner's selection event so browser autoplay rules apply normally.
        const current = createTeacherAudioAnimation();
        animation.current = current;
        void current.resume().catch(() => {
          if (animation.current === current) fallBackToAudio();
        });
      } catch {
        fallBackToAudio();
        return;
      }
    }
    setAppearance(next);
  }

  return <div className={styles.view}>
    {visual ? <div className={styles.portrait} data-appearance={appearance} aria-hidden="true">
      <span className={styles.hair} />
      <span className={styles.shoulders} />
      <span className={styles.neck} />
      <span className={styles.face} />
      <span className={styles.fringe} />
      <span className={styles.brow} />
      <span className={styles.eyes} />
      <span className={styles.nose} />
      <span ref={mouth} className={styles.mouth} />
    </div> : fallback}
    <label className={styles.control}>Teacher view
      <select value={appearance} onChange={(event) => selectAppearance(event.target.value as Appearance)}>
        <option value="audio">Audio only</option>
        <option value="woman">Woman avatar</option>
        <option value="man">Man avatar</option>
      </select>
    </label>
    {failed && <p className={styles.failure} role="status">Avatar unavailable. You can continue the lesson with audio.</p>}
  </div>;
}
