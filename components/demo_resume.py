import streamlit as st
import base64


def show_demo_resume():

    st.title("📑 Demo ATS Resume")

    st.write(
        "This is a sample ATS-friendly resume template that users can refer to while creating their own resume."
    )

    with open("assets/demo_resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Download Button
    st.download_button(
        label="⬇ Download Demo Resume",
        data=pdf_bytes,
        file_name="Demo_ATS_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )

    st.markdown("---")

    # PDF Preview
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="800"
        type="application/pdf">
    </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)