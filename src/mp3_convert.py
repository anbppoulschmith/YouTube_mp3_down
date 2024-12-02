import streamlit as st
import os
from src.download_steamlit import download_songs_streamlit

def mp3_convert():
    st.title("Mp3 converter for Youtube")
    st.write("On this streamlit site you can convert a youtube link to an mp3 file")
    st.write("---")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        youtube_link = st.text_input("Youtube link")

        if st.button('Convert'):
            mp3_data, file_name = download_songs_streamlit(youtube_link)

            if mp3_data:
                st.success("Conversion successful! Click to donwload below")
                st.download_button(
                    label="Download mp3",
                    data=mp3_data,
                    file_name=os.path.basename(file_name),
                    mime="audio/mpeg"
                )
            else:
                st.error("Failed to download or convert the Youtube link")