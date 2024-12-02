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
            output_dir = "output"
            os.makedirs(output_dir, exist_ok = True)

            filepath = download_songs_streamlit(youtube_link, output_dir)

            if filepath:
                with open(filepath, "rb") as file:
                    st.success("Conversion successful! Click to donwload below")
                    st.download_button(
                        label="Download mp3",
                        data=file,
                        file_name=os.path.basename(filepath),
                        mime="audio/mpeg"
                    )
            else:
                st.error("Failed to download or convert the Youtube link")