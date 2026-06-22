# AI Meeting Notes Generator

An AI-powered meeting assistant that automatically converts meeting recordings into structured meeting notes. The application uses **Whisper** for speech-to-text transcription and **Gemini AI** for generating summaries, key discussion points, action items, and decisions, helping teams reduce manual documentation efforts.

---

## 🚀 Features

* Upload meeting recordings (MP3, WAV, MP4)
* Automatic speech-to-text transcription using Faster-Whisper
* AI-generated executive summaries
* Extraction of key discussion points
* Action item identification
* Decision tracking
* Interactive Streamlit web interface
* Fast and easy meeting documentation

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* Faster-Whisper
* Gemini AI

### Utilities

* Python Dotenv

---

## 📂 Project Structure

```text
AI-Meeting-Notes-Generator/

│
├── app.py
├── requirements.txt
├── .env
│
├── backend/
│   ├── transcriber.py
│   └── summarizer.py
│
├── uploads/
│
└── outputs/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Meeting-Notes-Generator.git

cd AI-Meeting-Notes-Generator
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your API key from:

[Google AI Studio](https://aistudio.google.com?utm_source=chatgpt.com)

---

## ▶️ Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

If not, visit:

```text
http://localhost:8501
```

---

## 📋 How to Use

1. Launch the application.
2. Upload a meeting recording (MP3, WAV, or MP4).
3. Click **Generate Notes**.
4. The system will:

   * Transcribe the recording
   * Generate an executive summary
   * Extract key discussion points
   * Identify action items
   * Highlight decisions made
5. Review the generated meeting notes.

---

## 📸 Sample Output

```text
Executive Summary
-----------------
The team discussed the upcoming dashboard launch and project timeline.

Key Discussion Points
---------------------
• Dashboard release schedule
• UI testing progress
• Resource allocation

Action Items
------------
• Sarah - Complete UI testing by Wednesday
• John - Schedule stakeholder review meeting

Decisions Made
--------------
• Dashboard launch date remains Friday.
```

---

## 🎯 Future Enhancements

* Speaker Identification
* Meeting Sentiment Analysis
* PDF Export
* DOCX Export
* Meeting History Dashboard
* Calendar Integration
* Email-Ready Meeting Minutes
* Multi-Language Support

---

## 💼 Resume Highlights

* Developed an AI-powered meeting assistant using Whisper and Gemini AI to automate meeting documentation.
* Built speech-to-text and summarization pipelines for converting audio recordings into actionable meeting notes.
* Implemented extraction of summaries, action items, and decisions using Large Language Models (LLMs).
* Designed a Streamlit-based user interface for seamless meeting note generation.

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a pull request

---

### Author

**Nishant Ruwali**

GitHub: github.com/nishuruwali18-glitch/
