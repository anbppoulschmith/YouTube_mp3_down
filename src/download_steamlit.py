from pytubefix import YouTube
from io import BytesIO

def download_songs_streamlit(url):
    if not url or not isinstance(url, str):
        print("Invalid YouTube URL provided")
        return None, None
    
    try:
        # Initialize the Youtube opject
        vid = YouTube(url)
        title = vid.title

        # Get the first available audiostream
        audio_stream = vid.streams.get_audio_only()

        # Create safe title
        safe_title = "".join([c if c.isalnum() or c in " ._-()" else "_" for c in title]) + ".mp3"

        # Creta a byte buffer
        buffer = BytesIO()

        # Temp file
        temp_file_path = audio_stream.download()
        with open(temp_file_path, 'rb') as temp_file:
            buffer.write(temp_file.read())
        buffer.seek(0)
        print(f"Downloaded and converted to mp3: {title}")

        return buffer, safe_title

    except Exception as e:
        print(f"Download failed for {url}: {e}")
        return None, None


def download_video(url, output_path):
    try:
        yt = YouTube(url)
        title = yt.title

        ys = yt.streams.get_highest_resolution()

        safe_title = "".join([c if c.isalnum() or c in " ._-()" else "_" for c in title]) + ".mp4"
        filepath = ys.download(output_path=output_path, filename=safe_title)
        print(f"Downloaded and converted to mp4: {title}")
        
        return filepath

    except Exception as e:
        print(f"Downloaded failed for {url}: {e}")