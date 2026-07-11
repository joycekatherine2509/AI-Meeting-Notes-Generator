import streamlit as st
from transcriber import transcribe_audio
from cleaner import clean_text, remove_duplicates
from summarizer import summarize

st.set_page_config(
    page_title="AI Meeting Notes Generator",
    page_icon="📝"
)

st.title("📝 AI Meeting Notes Generator")
st.write(
    "Upload a meeting recording and generate structured meeting notes automatically."
)

uploaded_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:

    with open("meeting.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Audio uploaded successfully!")

    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio("meeting.wav")

    with st.spinner("Generating meeting notes..."):
        cleaned_text = clean_text(transcript)
        cleaned_text = remove_duplicates(cleaned_text)
        notes = summarize(cleaned_text)

    st.subheader("Meeting Notes")
    st.markdown(notes)

    st.download_button(
        label="⬇ Download Meeting Notes",
        data=notes,
        file_name="meeting_notes.md",
        mime="text/markdown"
    )