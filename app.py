import tkinter as tk
from tkinter import scrolledtext
from recorder import record_audio
from transcriber import transcribe_audio
from cleaner import clean_text
from summarizer import summarize
from exporter import save_markdown


def generate_notes():

    status_label.config(text="Recording...")

    root.update()

    record_audio(duration=60)

    status_label.config(text="Transcribing...")
    root.update()

    transcript = transcribe_audio("audio/meeting.wav")

    transcript_box.delete(1.0, tk.END)
    transcript_box.insert(tk.END, transcript)

    cleaned = clean_text(transcript)

    status_label.config(text="Generating Notes...")
    root.update()

    notes = summarize(cleaned)

    notes_box.delete(1.0, tk.END)
    notes_box.insert(tk.END, notes)

    save_markdown(notes)

    status_label.config(
        text="Meeting Notes Generated ✓"
    )


root = tk.Tk()
root.title("AI Meeting Notes Generator")
root.geometry("900x700")

title = tk.Label(
    root,
    text="AI Meeting Notes Generator",
    font=("Arial", 20)
)

title.pack(pady=20)

button = tk.Button(
    root,
    text="Start Recording",
    command=generate_notes,
    font=("Arial", 14)
)

button.pack(pady=10)

status_label = tk.Label(
    root,
    text="Ready"
)

status_label.pack()

tk.Label(
    root,
    text="Transcript"
).pack()

transcript_box = scrolledtext.ScrolledText(
    root,
    width=100,
    height=10
)

transcript_box.pack(pady=10)

tk.Label(
    root,
    text="Meeting Notes"
).pack()

notes_box = scrolledtext.ScrolledText(
    root,
    width=100,
    height=15
)

notes_box.pack(pady=10)

root.mainloop()