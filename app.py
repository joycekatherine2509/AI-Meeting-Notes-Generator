import streamlit as st
from transcriber import transcribe_audio
from cleaner import clean_text, remove_duplicates
from summarizer import summarize

st.set_page_config(
    page_title="AI Meeting Notes Generator",
    page_icon="📝",
    layout="wide"
)
with st.sidebar:
    st.title("📌 About")
    st.write(
        "This application converts meeting recordings "
        "into structured meeting notes automatically."
    )

    st.markdown("### Features")
    st.markdown("""
    - 🎙 Audio Upload
    - 📝 Speech-to-Text
    - 🤖 AI Summarization
    - 📋 Action Items
    - ⬇ Download Notes
    """)

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    color: #4CAF50;
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #B0B0B0;
    font-size: 20px;
    margin-bottom: 30px;
}

.card {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #333333;
}

.stDownloadButton button {
    width: 100%;
    border-radius: 10px;
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">📝 AI Meeting Notes Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload → Transcribe → Summarize → Download</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🎙 Upload Audio")

with col2:
    st.info("📝 Speech-to-Text")

with col3:
    st.info("🤖 AI Summary")

st.write("")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "📂 Upload Meeting Audio",
        type=["wav", "mp3", "m4a"]
    )

    st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:

    with open("meeting.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Audio uploaded successfully!")

    with st.spinner("🎙 Transcribing audio..."):
        transcript = transcribe_audio("meeting.wav")

    with st.spinner("🤖 Generating meeting notes..."):
        cleaned_text = clean_text(transcript)
        cleaned_text = remove_duplicates(cleaned_text)
        notes = summarize(cleaned_text)

    st.divider()

    st.subheader("📋 Meeting Notes")
    st.markdown(notes)

    st.download_button(
        label="⬇ Download Meeting Notes",
        data=notes,
        file_name="meeting_notes.md",
        mime="text/markdown"
    )