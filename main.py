import streamlit as st

st.set_page_config(page_title="🎥 Movie Analyzer", layout="centered")

st.title("🎥 Movie Analyzer")


home = st.Page("pages/home.py",title="About Project")

ai_talk = st.Page("pages/ui.py",title="Ai Talk")

visualize = st.Page("pages/visual.py",title="Visualize Data")

mainpage = st.navigation([home,ai_talk,visualize])

mainpage.run()