import streamlit as st


def show_interview_report():
    st.title("📊 Interview Report")

    if "interview_report" not in st.session_state:
        st.info("Complete your interview first.")
        return

    report = st.session_state["interview_report"]

    st.success("✅ Interview Completed Successfully!")

    with st.container(border=True):
        st.subheader("📝 AI Evaluation Report")
        st.markdown(report)

    st.divider()

    st.info(
        "💡 Tip: Review the feedback carefully and work on the suggested improvements "
        "before your next interview."
    )