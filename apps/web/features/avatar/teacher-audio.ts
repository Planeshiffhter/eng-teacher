export interface TeacherAudioAnimation {
  setTrack(track: MediaStreamTrack | null): void;
  mouthOpening(): number;
  resume(): Promise<void>;
  close(): void;
}

/** Observe an existing teacher track without owning or changing its playback. */
export function createTeacherAudioAnimation(): TeacherAudioAnimation {
  const context = new AudioContext({ latencyHint: 'interactive' });
  const analyser = context.createAnalyser();
  analyser.fftSize = 1024;
  const samples = new Float32Array(analyser.fftSize);
  let source: MediaStreamAudioSourceNode | null = null;
  let track: MediaStreamTrack | null = null;

  function setTrack(next: MediaStreamTrack | null) {
    source?.disconnect();
    source = null;
    track = null;
    if (!next || context.state === 'closed') return;
    source = context.createMediaStreamSource(new MediaStream([next]));
    // RoomAudioRenderer plays the remote track. This graph terminates here.
    source.connect(analyser);
    track = next;
  }

  return {
    setTrack,
    mouthOpening() {
      if (context.state !== 'running' || track?.readyState !== 'live' || !track.enabled || track.muted) return 0;
      analyser.getFloatTimeDomainData(samples);
      let energy = 0;
      for (const sample of samples) energy += sample * sample;
      const rms = Math.sqrt(energy / samples.length);
      return Math.min(1, Math.max(0, (rms - 0.012) * 9));
    },
    resume: () => context.resume(),
    close() {
      setTrack(null);
      if (context.state !== 'closed') void context.close().catch(() => {});
    },
  };
}
