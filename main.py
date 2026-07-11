from recorder import record_audio
from transcriber import transcribe_audio
from cleaner import clean_text, remove_duplicates
from summarizer import summarize
from exporter import save_markdown
from summarizer import summarize
record_audio(duration=60)

transcript = transcribe_audio("audio/meeting.wav")
print("Transcript:")
print(transcript)

cleaned_text = clean_text(transcript)
print("Cleaned Text:")
print(cleaned_text)

notes = summarize(cleaned_text)
print(notes)

save_markdown(notes)
cleaned_text = clean_text(transcript)
cleaned_text = remove_duplicates(cleaned_text)