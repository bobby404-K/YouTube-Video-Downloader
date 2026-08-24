# YouTube Video Downloader

A simple Python script that downloads YouTube videos in the best available quality using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), merging separate video and audio streams with FFmpeg.

--- 

jijijij

## Features

- Downloads the best available video and audio streams
- Automatically merges them into a single playable file
- Works with any valid YouTube URL
- Minimal, beginner-friendly script

---

## Requirements

- Python 3.8 or later
- [`yt-dlp`](https://pypi.org/project/yt-dlp/)
- [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) (required for merging video and audio)

---

## Installation

### 1. Install yt-dlp

```bash
pip install yt-dlp
```

### 2. Install FFmpeg (Windows)

yt-dlp requires FFmpeg to merge separately downloaded video and audio streams. Without it, you'll see an error like:

```
ERROR: You have requested merging of multiple formats but ffmpeg is not installed. Aborting due to --abort-on-error
```

Follow the steps below to install it.

#### Step 1 — Download FFmpeg

Go to [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/) and download the **release essentials** build. Choose the `.zip` version — it extracts natively on Windows without needing extra tools like 7-Zip.

#### Step 2 — Extract and place the folder

1. Right-click the downloaded `.zip` file and select **Extract All**.
2. Move the extracted folder to `C:\` and rename it to `ffmpeg`.
3. Confirm that `ffmpeg.exe` exists at:
   ```
   C:\ffmpeg\bin\ffmpeg.exe
   ```

#### Step 3 — Add FFmpeg to your PATH

1. Press **Windows key**, search for **Environment Variables**, and open **Edit the system environment variables**.
2. Click **Environment Variables**.
3. Under **User variables**, select **Path**, then click **Edit**.
4. Click **New** and add:
   ```
   C:\ffmpeg\bin
   ```
5. Click **OK** on all open windows to save.

#### Step 4 — Verify the installation

Close **all** open terminal windows, then open a new **Command Prompt** and run:

```bash
ffmpeg -version
```

If installed correctly, you'll see version details printed along with an exit code of `0`.

---

## Usage

Run the script and paste a YouTube URL when prompted:

```bash
python main.py
```

```
enter the url of the video you want to download: https://youtu.be/EXAMPLE
```

The script will download the best video and audio streams and merge them automatically. The final file is saved in the same folder as the script.

---

## Script

```python
import yt_dlp

url = input("enter the url of the video you want to download: ")

yt_dlp.YoutubeDL(
    {"format": "bestvideo+bestaudio/best"}
).download([url])
```

---

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| `ffmpeg is not installed` | FFmpeg missing or not on PATH | Follow the Installation steps above |
| `No supported JavaScript runtime could be found` | yt-dlp warning about YouTube's newer extraction requirements | Install [Deno](https://deno.com/) and add `--js-runtimes deno` to your yt-dlp config if formats go missing |
| Command not recognized after installing FFmpeg | PATH not refreshed | Close **all** terminal windows and open a new one |

---

## Notes

- Downloaded files are saved in the directory the script is run from.
- This script is for personal use with content you have the right to download. Respect YouTube's Terms of Service and copyright laws.

---

## License

This project is provided as-is for educational purposes.
