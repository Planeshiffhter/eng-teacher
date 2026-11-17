export const MAX_RECORDING_SECONDS = 15;

function stopTracks(stream: MediaStream) {
  for (const track of stream.getTracks()) track.stop();
}

export async function recordLearnerAudio(
  signal: AbortSignal,
  onRecording: (stop: () => void) => void,
): Promise<Blob> {
  if (!navigator.mediaDevices?.getUserMedia || typeof MediaRecorder === 'undefined') {
    throw new Error('This browser cannot record microphone audio here. Try reading the sentence aloud.');
  }
  signal.throwIfAborted();

  let stream: MediaStream;
  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  } catch {
    throw new Error('Microphone access is unavailable. Check permissions or read the sentence aloud.');
  }
  if (signal.aborted) {
    stopTracks(stream);
    signal.throwIfAborted();
  }

  let recorder: MediaRecorder;
  try {
    recorder = new MediaRecorder(stream);
  } catch {
    stopTracks(stream);
    throw new Error('This browser could not start the audio recorder.');
  }

  return new Promise<Blob>((resolve, reject) => {
    const parts: Blob[] = [];
    let timer: ReturnType<typeof setTimeout> | undefined;
    let tracksStopped = false;

    function releaseMicrophone() {
      if (tracksStopped) return;
      tracksStopped = true;
      stopTracks(stream);
    }

    function cleanup() {
      clearTimeout(timer);
      signal.removeEventListener('abort', abort);
      recorder.ondataavailable = null;
      recorder.onstop = null;
      recorder.onerror = null;
      releaseMicrophone();
    }

    function fail(error: unknown) {
      cleanup();
      if (recorder.state !== 'inactive') {
        try {
          recorder.stop();
        } catch {
          // Cleanup has already released the capture stream.
        }
      }
      reject(error);
    }

    function abort() {
      fail(signal.reason);
    }

    function stop() {
      if (recorder.state === 'inactive') return;
      clearTimeout(timer);
      try {
        timer = setTimeout(() => fail(new Error('The browser did not finish preparing the clip.')), 3000);
        recorder.stop();
        releaseMicrophone();
      } catch {
        fail(new Error('The browser could not finish the recording.'));
      }
    }

    recorder.ondataavailable = ({ data }) => {
      if (data.size > 0) parts.push(data);
    };
    recorder.onstop = () => {
      if (parts.length === 0) {
        fail(new Error('No audio was captured. Try recording again.'));
        return;
      }
      const clip = new Blob(parts, { type: recorder.mimeType || parts[0].type });
      cleanup();
      resolve(clip);
    };
    recorder.onerror = () => fail(new Error('The browser stopped recording. Try again.'));
    signal.addEventListener('abort', abort, { once: true });

    try {
      recorder.start();
      timer = setTimeout(stop, MAX_RECORDING_SECONDS * 1000);
      onRecording(stop);
    } catch {
      fail(new Error('The audio recorder could not start. Try again.'));
    }
  });
}
