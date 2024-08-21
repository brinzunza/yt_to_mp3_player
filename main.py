import yt_dlp
from moviepy.editor import VideoFileClip
import os

def download_video(url, output_path="video.mp4"):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def convert_to_mp3(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    audio.close()
    video.close()

def download_and_convert(url, video_path="downloaded_video.mp4", audio_path="output_audio.mp3"):
    print("Downloading video...")
    download_video(url, video_path)
    
    print("Converting to MP3...")
    convert_to_mp3(video_path, audio_path)
    
    if os.path.exists(video_path):
        os.remove(video_path)
    
    print(f"MP3 file saved as {audio_path}")
