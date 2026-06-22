import streamlit as st
import os

from backend.transcriber import transcribe_audio
from backend.summarizer import generate_notes


st.set_page_config(
    page_title="AI Meeting Notes Generator",
    page_icon="📝"
)

st.title("📝 AI Meeting Notes Generator")

uploaded_file = st.file_uploader(
    "Upload Meeting Recording",
    type=["mp3", "wav", "mp4"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully")

    if st.button("Generate Notes"):

        with st.spinner("Transcribing Audio..."):
            transcript = transcribe_audio(file_path)

        st.subheader("Transcript")
        st.text_area(
            "",
            transcript,
            height=200
        )

        with st.spinner("Generating Meeting Notes..."):
            notes = generate_notes(transcript)

        st.subheader("Meeting Notes")
        st.markdown(notes)