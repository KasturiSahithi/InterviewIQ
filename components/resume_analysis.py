import streamlit as st

def show_resume_analysis():

    analysis = st.session_state.get("analysis", None)

    st.markdown("## 📄 Resume Analysis")

    if analysis is None:
        st.info("📄 Upload your resume to get AI-powered analysis.")
        return

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("### ✅ Strengths")
        for item in analysis["strengths"]:
            st.write("•", item)

    with col2:
        st.warning("### ⚠️ Weaknesses")
        for item in analysis["weaknesses"]:
            st.write("•", item)

    with col3:
        st.info("### 💡 Suggestions")
        for item in analysis["suggestions"]:
            st.write("•", item)