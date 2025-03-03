#youtubede herhangi bir video indirmek
import yt_dlp

video_url = input("Youtube video URL sini girin:")

ydl_opts ={}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])