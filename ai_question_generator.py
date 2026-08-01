from groq import Groq
import streamlit as st
from config import MODEL_NAME

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def generate_questions(resume_text, difficulty):

    try:

        prompt = f"""
Analyze the following resume:

{resume_text}

Generate interview questions based ONLY on the candidate's resume.

Rules:
- Generate exactly 15 interview questions.
- Questions must be technical and project-based.
- Questions should match the candidate's skills and experience.
- Number the questions from 1 to 15.
- Do NOT include headings like EASY, MEDIUM, or HARD.
- Do NOT include explanations, answers, strengths, weaknesses, or resume analysis.
- Return ONLY the numbered list of questions.
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"