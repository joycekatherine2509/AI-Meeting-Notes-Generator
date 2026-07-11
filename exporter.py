import os

def save_markdown(text):
    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/meeting_notes.md",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(text)

    print("Markdown file generated successfully!")