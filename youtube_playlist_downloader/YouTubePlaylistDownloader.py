import os
import yt_dlp

class YouTubePlaylistDownloader:
    def __init__(self, playlist_url, output_path="./downloads", format="mp3", resolution="720"):
        self.playlist_url = playlist_url
        self.output_path = output_path
        self.format = format.lower()
        self.resolution = resolution

        os.makedirs(self.output_path, exist_ok=True)

    def download(self):
        if self.format == "mp3":
            self._download_mp3()
        elif self.format == "mp4":
            self._download_mp4()
        else:
            raise ValueError("Format non supporté. Utilisez 'mp3' ou 'mp4'.")

    def _download_mp3(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(self.output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': False,
            'quiet': False
        }

        print(f"🔊 Téléchargement de la playlist en MP3...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.playlist_url])
        print(f"✅ Téléchargement MP3 terminé.")

    def _download_mp4(self):
        ydl_opts = {
            'format': f'bestvideo[height<={self.resolution}]+bestaudio/best[height<={self.resolution}]',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(self.output_path, '%(title)s.%(ext)s'),
            'noplaylist': False,
            'quiet': False
        }

        print(f"🎬 Téléchargement de la playlist en MP4 ({self.resolution}p)...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.playlist_url])
        print(f"✅ Téléchargement MP4 terminé.")
