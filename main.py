import streamlit as st
from src.mp4_convert import mp4_convert
from src.mp3_convert import mp3_convert

st.set_page_config(page_title="Youtube mp3 converter",
                page_icon="🎥", 
                layout="wide", 
                initial_sidebar_state="auto")

tabs = st.sidebar.radio("Conversions", ["Mp3 converter", "Mp4 converter"])

if tabs == "Mp3 converter":
    mp3_convert()

elif tabs == "Mp4 converter":
    mp4_convert()