import streamlit as st
def load_css():
    st.markdown("""
<style>
#MainMenu{
visibility:hidden;
}
footer{
visibility:hidden;
}
header{
visibility:hidden;
}
.stApp{
background:#0F111A;
}
.block-container{
padding-top:20px;
padding-left:30px;
padding-right:30px;
padding-bottom:20px;
}
</style>
""",unsafe_allow_html=True)