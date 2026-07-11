import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(duration=30,
                 filename="audio/meeting.wav",
                 fs=44100):
    print("Recording Started...")
    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1
    )
    sd.wait()
    write(filename, fs, recording)
    print("Recording Saved.")