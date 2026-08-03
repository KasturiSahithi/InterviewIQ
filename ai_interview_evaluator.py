from groq import Groq
import streamlit as st
from config import MODEL_NAME

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def evaluate_complete_interview(questions, answers):

    try:

        interview_data = ""

        for i, (q, a) in enumerate(zip(questions, answers), start=1):

            interview_data += f"""
Question {i}:
{q}

Answer:
{a}

"""

        prompt = f"""
You are an expert HR and Technical interviewer.

Evaluate the COMPLETE interview below.

{interview_data}

Give your response in EXACTLY this format.

Overall Score: X/10

Question-wise Scores:
Q1: X/10
Q2: X/10
Q3: X/10
...

Strengths:
- Point 1
- Point 2
- Point 3

Weaknesses:
- Point 1
- Point 2

Suggestions:
- Point 1
- Point 2

Hiring Recommendation:
(Hire / Maybe Hire / No Hire)

Overall Feedback:
Write 6-8 sentences summarizing the interview.
"""

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

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"