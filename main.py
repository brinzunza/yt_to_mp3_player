import yt_dlp
import os

def download_audio_without_ffmpeg(url, output_path="output_audio"):
    # yt-dlp options to download the raw audio stream
    ydl_opts = {
        'format': 'bestaudio/best',  # Get the best audio-only format available
        'outtmpl': f"{output_path}.%(ext)s",  # Keep the original audio extension
        'noplaylist': True,  # Ensure it doesn't download a playlist
        'postprocessors': [],  # No post-processing to avoid using ffmpeg
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
    
    print(f"Audio downloaded and saved as {output_path}")

def main():
    url = input("Enter the YouTube URL: ")
    output_filename = input("Enter output file name (without extension): ")
    
    download_audio_without_ffmpeg(url, output_filename)

if __name__ == "__main__":
    main()