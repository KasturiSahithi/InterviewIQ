import streamlit as st

def show_cards():

    analysis = st.session_state.get("analysis", None)

    if analysis is None:
        ats = 0
        resume = 0
        skills = 0
        questions = 0

        ats_status = "Upload Resume"
        resume_status = "Waiting"
        skill_status = "Waiting"
        question_status = "Waiting"

    else:
        ats = analysis["ats_score"]
        resume = analysis["resume_score"]
        skills = len(analysis["skills"])
        questions = 15

        ats_status = "Excellent" if ats >= 85 else "Needs Improvement"
        resume_status = "Very Good" if resume >= 80 else "Average"
        skill_status = "Detected"
        question_status = "Ready"

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    cards = [
        ("🎯", "ATS Score", str(ats), ats_status, "#22C55E", ats),
        ("📄", "Resume Score", str(resume), resume_status, "#3B82F6", resume),
        ("🧠", "Skills", str(skills), skill_status, "#A855F7", min(skills * 10, 100)),
        ("🎤", "Questions", str(questions), question_status, "#F97316", 100 if questions else 0),
    ]

    for col, card in zip([col1, col2, col3, col4], cards):

        icon, title, value, subtitle, color, progress = card

        with col:

            st.markdown(f"""
<div style="
background:#181A24;
padding:25px;
border-radius:22px;
border:1px solid #2B2D3A;
">

<div style="font-size:38px;">
{icon}
</div>

<h3 style="color:white;">
{title}
</h3>

<h1 style="
color:white;
font-size:48px;
margin-bottom:0;
">
{value}
</h1>

<p style="
color:{color};
font-size:18px;
margin-top:5px;
">
{subtitle}
</p>

<div style="
height:10px;
background:#2B2D3A;
border-radius:20px;
margin-top:18px;
">

<div style="
height:10px;
width:{progress}%;
background:{color};
border-radius:20px;
">

</div>

</div>

</div>
""", unsafe_allow_html=True)