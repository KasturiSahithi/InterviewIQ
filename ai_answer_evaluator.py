from groq import Groq
import streamlit as st
from config import MODEL_NAME

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def evaluate_answer(question, answer):

    try:

        prompt = f"""
You are an experienced technical interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer in the following format.

Score: X/10

Strengths:
- Point 1
- Point 2

Improvements:
- Point 1
- Point 2

Ideal Answer:
Provide a short ideal answer in 3-5 sentences.
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