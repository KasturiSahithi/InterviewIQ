import streamlit as st

def show_hero():
    st.markdown("""
    <div style="
    padding:20px 35px;
    background:linear-gradient(135deg,#2563EB,#4F46E5,#7C3AED);
    border-radius:22px;
    color:white;
    margin-bottom:35px;
    box-shadow:0px 12px 30px rgba(37,99,235,0.25);
    ">

    <h1 style="margin-bottom:8px;font-size:40px;font-weight:700;">
    🎯 InterviewIQ
    </h1>

    <h4 style="margin-top:0;font-weight:500;color:#E0E7FF;">
    AI Interview Preparation Platform
    </h4>

    <p style="font-size:18px;margin-top:20px;color:#F8FAFC;">
    Prepare Smarter. Get Hired Faster.
    </p>

    <div style="font-size:18px;line-height:2;">
    ✅ AI Resume Analysis &nbsp;&nbsp;&nbsp;
    ✅ ATS Score &nbsp;&nbsp;&nbsp;
    ✅ AI Interview Questions &nbsp;&nbsp;&nbsp;
    ✅ Mock Interview &nbsp;&nbsp;&nbsp;
    ✅ Career Recommendations
    </div>

    </div>
    """, unsafe_allow_html=True)