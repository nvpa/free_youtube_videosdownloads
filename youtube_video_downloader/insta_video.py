import yt_dlp
import os

def download_instagram_reel(url, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
 
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'format': 'best[ext=mp4]',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading from: {url}")
        ydl.download([url])

# Example usage
reel_url = 'https://www.instagram.com/thetoontimes_t3/reel/DLHzlQUsnLq/'
download_path = 'D:/videos/'  # ✅ corrected path
download_instagram_reel(reel_url, download_path)

