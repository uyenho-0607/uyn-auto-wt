import base64
import os.path
import subprocess
import time
from src.data.consts import VIDEO_DIR


def compress_video(input_path, output_path):
    # Compress with ffmpeg
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-vcodec", "libx264", "-crf", "28",
        output_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return output_path


def save_recorded_video(video_raw):
    raw_path = os.path.join(VIDEO_DIR, f"test_video_{round(time.time())}_raw.mp4")
    final_path = os.path.join(VIDEO_DIR, f"test_video_{round(time.time())}.mp4")

    with open(raw_path, "wb") as f:
        f.write(base64.b64decode(video_raw))

    compress_video(raw_path, final_path)

    if os.path.exists(final_path):
        os.remove(raw_path)
        return final_path

    return raw_path
