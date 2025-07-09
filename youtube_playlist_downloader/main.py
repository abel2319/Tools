from YouTubePlaylistDownloader import *
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="YouTube Playlist Downloader"
    )

    # Paramètres de qualité
    parser.add_argument('--format', type=str, default="mp3",
                        help='Format (default: mp3)')
    parser.add_argument('--resolution', type=int, default=720,
                        help='Resolution of files if mp4 (défaut: 720)')
    parser.add_argument('--link', type=str,
                        help='Playlist link (example: https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID)')
    parser.add_argument('--output_path', type=str, default="./output",
                        help='Output directory (default: ./)')

    args = parser.parse_args()

    # Exemple MP4 (720p)
    downloader = YouTubePlaylistDownloader(
        playlist_url=args.link, #"https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID",
        output_path=args.output_path,
        format=args.format,
        resolution=args.resolution
    )

    downloader.download()

if __name__ == "__main__":
    main()
