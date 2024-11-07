from pytubefix import YouTube
from pytubefix.cli import on_progress
import pandas as pd
import os

# Output directory
output_dirc = "output"
if not os.path.exists(output_dirc):
    os.makedirs(output_dirc)

# Filename of excel file with URL-links
df = pd.read_excel('Book1.xlsx')
# What colume the list is to be made from. 
list_of_urls = [url for url in df['Youtubelink til sang'] if pd.notnull(url)]

# Defining a function that will take the url give them a output path and a filename
def download_songs(url, output_path):
    try:
        # Initialize the Youtube opject
        vid = YouTube(url, on_progress_callback=on_progress)
        title = vid.title

        # Get the first available audiostream
        audio_stream = vid.streams.get_audio_only()

        # Create safe title
        safe_title = "".join([c if c.isalnum() or c in " ._-()" else "_" for c in title])

        # Download the audio stream 
        audio_stream.download(output_path=output_path, filename=safe_title, mp3 = True)
        print(f"Downloaded and converted to mp3: {title}")

    except Exception as e:
        print(f"Download failed for {url}: {e}")

# Download each song
for url in list_of_urls:
    download_songs(url, output_path=output_dirc)

print("All songs have been converted")