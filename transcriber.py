from faster_whisper import WhisperModel
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)
def transcribe_audio(file):
    segments, info = model.transcribe(file)
    transcript = ""
    for segment in segments:
        transcript += segment.text + " "
    return transcript