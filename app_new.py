import streamlit as st
from PyPDF2 import PdfReader

from components.styles import load_css
from components.sidebar import show_sidebar
from components.welcome import show_welcome
from components.cards import show_cards
from components.resume_analysis import show_resume_analysis
from components.activity import show_activity
from components.interview import show_interview
from components.interview_report import show_interview_report
from components.demo_resume import show_demo_resume
from ai_resume_analyzer import analyze_resume
from ai_question_generator import generate_questions


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text

st.set_page_config(
    page_title="InterviewIQ",
    page_icon="🎯",
    layout="wide"
)

if "resume_text" not in st.session_state:
    st.session_state["resume_text"] = None

if "analysis" not in st.session_state:
    st.session_state["analysis"] = None

load_css()

left, right = st.columns([1, 4], gap="large")

with left:
    page=show_sidebar()

with right:
    if page=="🏠 Dashboard":
       show_welcome()

    # ---------------- Upload Resume ---------------- #

    if "show_uploader" not in st.session_state:
        st.session_state.show_uploader = False

    if st.session_state.get("upload_resume_btn", False):
        st.session_state.show_uploader = True

    uploaded_file = None

    if st.session_state.show_uploader:

        uploaded_file = st.file_uploader(
            "",
            type=["pdf"],
            label_visibility="collapsed"
        )

    if uploaded_file is not None:

        resume_text = extract_text_from_pdf(uploaded_file)
        st.session_state["resume_text"] = resume_text

        analysis = analyze_resume(resume_text)
        st.session_state["analysis"] = analysis

        questions = generate_questions(
            resume_text,
            "Medium"
        )

        st.session_state["questions"] = questions.split("\n")

        st.success("✅ Resume uploaded and analyzed successfully!")

    # ---------------- Pages ---------------- #

    if page == "🏠 Dashboard":

        show_cards()

        left_panel, right_panel = st.columns([3,1])

        with left_panel:
            show_resume_analysis()

        with right_panel:
            show_activity()

    elif page == "🎤 Mock Interview":
        show_interview()
    elif page == "📑 Demo Resume":
        show_demo_resume()
    elif page == "📊 Interview Report":
        show_interview_report()