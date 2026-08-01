import streamlit as st


def show_welcome():

    left, right = st.columns([2, 1], gap="large")

    with left:

        st.title("👋 Welcome Back, Sahithi!")
        st.caption("Prepare Smarter. Get Hired Faster.")

        c1, c2 = st.columns(2)

        with c1:
            st.button(
                "📄 Upload Resume",
                use_container_width=True,
                key="upload_resume_btn"
            )

        with c2:
            st.button(
                "📑 Demo Resume",
                use_container_width=True,
                key="demo_resume_btn"
            )

    with right:

        st.container(border=True)

        col1, col2 = st.columns([5, 1])

        with col2:
            st.markdown(
                "<div style='font-size:24px;text-align:right;'>🔔&nbsp;&nbsp;👤</div>",
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style='text-align:center;font-size:70px;'>
            🎯
            </div>

            <div style='text-align:center;color:gray;font-size:16px;'>
            AI Interview Preparation Platform
            </div>
            """,
            unsafe_allow_html=True
        )