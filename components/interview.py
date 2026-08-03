import streamlit as st
from ai_interview_evaluator import evaluate_complete_interview


def show_interview():
    st.title("🎤 AI Mock Interview")

    if "questions" not in st.session_state:
        st.warning("Please upload a resume first.")
        return

    questions = st.session_state["questions"]

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "answers" not in st.session_state:
        st.session_state.answers = [""] * len(questions)

    current = st.session_state.current_question

    st.subheader("AI Generated Interview Questions")

    st.progress((current + 1) / len(questions))

    question = questions[current]

    clean_question = question
    if ". " in question:
        clean_question = question.split(". ", 1)[1]

    st.markdown(f"## Question {current + 1} of {len(questions)}")
    st.write(clean_question)

    # Load previous answer
    answer = st.text_area(
        "Your Answer",
        value=st.session_state.answers[current],
        height=180,
        key=f"text_{current}"
    )

    # Save answer immediately
    st.session_state.answers[current] = answer

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if current > 0:
            if st.button("⬅ Previous"):
                st.session_state.current_question -= 1
                st.rerun()

    with col2:
        if current < len(questions) - 1:
            if st.button("Next ➡"):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("🎯 Finish Interview"):

                report = evaluate_complete_interview(
                    questions,
                    st.session_state.answers
                )

                st.session_state["interview_report"] = report
                st.success("Interview Completed Successfully!")
                st.session_state["page"] = "📊 Interview Report"
                st.rerun()