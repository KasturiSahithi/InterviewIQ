import json
from groq import Groq
import streamlit as st
from config import MODEL_NAME

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def analyze_resume(resume_text):

    prompt = f"""
Analyze this resume.

Return ONLY valid JSON.

The JSON MUST have exactly this structure:

{{
  "ats_score": 90,
  "resume_score": 88,
  "skills": [
    "Python",
    "SQL",
    "Power BI"
  ],
  "strengths": [
    "...",
    "...",
    "..."
  ],
  "weaknesses": [
    "...",
    "...",
    "..."
  ],
  "suggestions": [
    "...",
    "...",
    "..."
  ]
}}

Rules:
- ATS score: integer between 0 and 100.
- Resume score: integer between 0 and 100.
- skills: maximum 10.
- strengths: maximum 5.
- weaknesses: maximum 5.
- suggestions: maximum 5.
- Return ONLY JSON.

Resume:

{resume_text}
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        text = (
            response.choices[0].message.content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(text)

    except Exception as e:

        st.error(f"AI Error: {e}")

        return {
            "ats_score": 0,
            "resume_score": 0,
            "skills": [],
            "strengths": [],
            "weaknesses": [],
            "suggestions": []
        }