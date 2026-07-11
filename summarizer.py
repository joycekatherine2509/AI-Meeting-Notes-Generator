import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize(text):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Generate meeting notes in the following format:

    Executive Summary
    Key Decisions
    Action Items

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text