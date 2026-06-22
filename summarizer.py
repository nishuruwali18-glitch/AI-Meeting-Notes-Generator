import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_notes(transcript):

    prompt = f"""
    You are a professional meeting assistant.

    Analyze the transcript and provide:

    1. Executive Summary
    2. Key Discussion Points
    3. Action Items
    4. Decisions Made

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)

    return response.text