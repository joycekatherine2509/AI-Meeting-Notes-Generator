import streamlit as st
from transcriber import transcribe_audio
from cleaner import clean_text, remove_duplicates
from summarizer import summarize

st.set_page_config(
    page_title="AI Meeting Notes Generator",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0B1120;
}

/* Hero Banner */
.hero {
    background: linear-gradient(
        135deg,
        #0F172A,
        #1E3A8A,
        #2563EB
    );
    padding: 50px;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 35px;
}

.hero-title {
    color: white;
    font-size: 50px;
    font-weight: bold;
}

.hero-subtitle {
    color: #D1D5DB;
    font-size: 22px;
    margin-top: 10px;
}

/* Section Titles */
.section-title {
    color: #38BDF8;
    font-size: 30px;
    font-weight: bold;
    margin-top: 25px;
}

/* Download Button */
.stDownloadButton button {
    width: 100%;
    background-color: #22C55E;
    color: white;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
    font-size: 18px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Upload Box */
[data-testid="stFileUploader"] {
    border: 2px dashed #38BDF8;
    border-radius: 20px;
    padding: 25px;
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🤖 About")

    st.write("""
This application converts meeting recordings into structured notes automatically using AI.
""")

    st.markdown("---")

    st.subheader("🚀 Features")

    st.markdown("""
- ☆ Audio Upload
- ☆ Speech-to-Text
- ☆ AI Summarization
- ☆ Meeting Notes
- ☆ Download Notes
""")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.markdown("""
- Python
- Streamlit
- Faster-Whisper
- Generative AI
- NLP
""")

st.markdown("""
<div class="hero">
    <div class="hero-title">
        🤖 AI Meeting Notes Generator
    </div>

    <div class="hero-subtitle">
        Upload → Transcribe → Summarize → Download
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎙 Step 1", "Upload")

with col2:
    st.metric("📝 Step 2", "Transcribe")

with col3:
    st.metric("🤖 Step 3", "Summarize")

st.write("")

st.markdown(
    '<div class="section-title">📂 Upload Meeting Recording</div>',
    unsafe_allow_html=True
)

st.write(
    "Upload your meeting audio and let AI generate structured meeting notes automatically."
)

uploaded_file = st.file_uploader(
    "Choose your audio file",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:

    with open("meeting.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Audio uploaded successfully!")

    progress_bar = st.progress(0)

    with st.spinner("🎙 Transcribing audio..."):
        transcript = transcribe_audio("meeting.wav")
        progress_bar.progress(35)

    with st.spinner("📝 Cleaning transcript..."):
        cleaned_text = clean_text(transcript)
        cleaned_text = remove_duplicates(cleaned_text)
        progress_bar.progress(70)

    with st.spinner("🤖 Generating meeting notes..."):
        notes = summarize(cleaned_text)
        progress_bar.progress(100)

    st.balloons()

    st.divider()

    st.markdown(
        '<div class="section-title">📋 Generated Meeting Notes</div>',
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(
        ["📝 Meeting Notes", "📄 Raw Transcript"]
    )

    with tab1:
        st.markdown(notes)

    with tab2:
        st.write(transcript)

    st.write("")

    st.download_button(
        label="⬇ Download Meeting Notes",
        data=notes,
        file_name="meeting_notes.md",
        mime="text/markdown"
    )