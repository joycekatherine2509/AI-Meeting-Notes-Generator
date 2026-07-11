import re

fillers = [
    "um",
    "uh",
    "like",
    "you know",
    "actually",
    "basically"
    "Literally",
    "I mean",
    "Kind of",
    "Sort of",
    "Well",
    "Right",
    "Okay",
    "So"
]
def clean_text(text):
    for word in fillers:
        text = re.sub(
            r'\b' + word + r'\b',
            '',
            text,
            flags=re.IGNORECASE
        )
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
def remove_duplicates(text):
    sentences = text.split(".")
    unique = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence not in unique:
            unique.append(sentence)

    return ". ".join(unique)