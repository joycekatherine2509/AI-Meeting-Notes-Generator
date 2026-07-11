import streamlit as st

st.set_page_config(
    page_title="AI Meeting Notes Generator",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Meeting Notes Generator")
st.write(
    "Upload a meeting recording and automatically generate structured meeting notes."
)

uploaded_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file:
    st.success("Audio uploaded successfully!")