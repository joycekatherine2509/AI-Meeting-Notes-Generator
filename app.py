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
    background-color: #0E1117;
}

/* Hero section */
.hero {
    background: linear-gradient(90deg, #0F172A, #1E3A8A);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    color: white;
    font-size: 48px;
    margin-bottom: 10px;
}

.hero p {
    color: #D1D5DB;
    font-size: 20px;
}

/* Upload card */
.upload-card {
    background-color: #1E293B;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #334155;
    margin-top: 20px;
}

/* Section headings */
.section-title {
    color: #38BDF8;
    font-size: 28px;
    font-weight: bold;
}

/* Download button */
.stDownloadButton button {
    width: 100%;
    background-color: #22C55E;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    height: 3em;
}

/* Success message */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🤖 About")

    st.write(
        """
        Convert meeting recordings into structured notes
        automatically using AI.
        """
    )

    st.markdown("### 🚀 Features")

    st.markdown("""
    - 🎙 Upload Audio
    - 📝 Speech-to-Text
    - 🤖 AI Summarization
    - 📋 Meeting Notes
    - ⬇ Download Notes
    """)

    st.markdown("---")

    st.markdown("### 🛠 Tech Stack")

    st.markdown("""
    - Python
    - Streamlit
    - Faster-Whisper
    - Generative AI
    """)

st.markdown("""
<div class="hero">
    <h1>🤖 AI Meeting Notes Generator</h1>
    <p>
        Upload → Transcribe → Summarize → Download
    </p>
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

with st.container():

    st.markdown(
        '<div class="upload-card">',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Choose your audio file",
        type=["wav", "mp3", "m4a"]
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
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