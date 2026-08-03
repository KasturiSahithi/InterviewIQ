import streamlit as st

def show_activity():

    st.markdown("""
<div style="
background:#181A24;
border-radius:22px;
padding:25px;
border:1px solid #2B2D3A;
height:330px;
">

<h2 style="color:white;">
⚡ Recent Activity
</h2>

<br>

<div style="color:white;font-size:18px;">
🟢 Resume Uploaded
</div>

<p style="color:#A1A1AA;">
2 minutes ago
</p>

<div style="color:white;font-size:18px;">
🔵 Resume Analyzed
</div>

<p style="color:#A1A1AA;">
5 minutes ago
</p>

<div style="color:white;font-size:18px;">
🟣 ATS Score Generated
</div>

<p style="color:#A1A1AA;">
5 minutes ago
</p>

<div style="color:white;font-size:18px;">
🟠 Questions Generated
</div>

<p style="color:#A1A1AA;">
10 minutes ago
</p>

</div>
""", unsafe_allow_html=True)