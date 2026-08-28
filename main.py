import yt_dlp


def download_videos(urls, is_playlist, download_audio):
    if download_audio:
        ydl_opts = {
            "format": "bestaudio/best",
            "noplaylist": not is_playlist,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
    else:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "noplaylist": not is_playlist,
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


def main():
    choice = input("Is this a playlist? (y/n): ").strip().lower()
    is_playlist = choice == "y"

    media_choice = input("Download audio or video? (a/v): ").strip().lower()
    download_audio = media_choice == "a"

    if is_playlist:
        url = input("Enter the playlist URL: ").strip()
        urls = [url]
    else:
        raw_input_urls = input(
            "Enter video URL(s) (separate multiple URLs with a comma): "
        ).strip()
        urls = [u.strip() for u in raw_input_urls.split(",") if u.strip()]

    if not urls:
        print("No valid URL(s) provided. Exiting.")
        return

    download_videos(urls, is_playlist, download_audio)


if __name__ == "__main__":
    main()
