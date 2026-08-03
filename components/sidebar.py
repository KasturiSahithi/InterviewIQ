import streamlit as st

def show_sidebar():

    pages = [
        "🏠 Dashboard",
        "🎤 Mock Interview",
        "📑 Demo Resume",
        "📊 Interview Report"
    ]

    if "page" not in st.session_state:
        st.session_state.page = "🏠 Dashboard"

    page = st.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state.page)
    )

    st.session_state.page = page

    return page