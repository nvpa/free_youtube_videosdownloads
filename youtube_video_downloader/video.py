import os
from yt_dlp import YoutubeDL

def download_video(url, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'best[ext=mp4]',  # download best video+audio merged
        'merge_output_format': 'mp4'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example: Save to D:\videos\FindingNemo1
video_url = 'https://www.youtube.com/watch?v=-GydnFPTgus&list=RDGMEMPipJmhsMq3GHGrfqf4WIqA&index=1'
download_path = r'D:\videos\FindingNemo1'

download_video(video_url, download_path)
