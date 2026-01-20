import subprocess
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def pick_audio_file():
    root = Tk()
    root.withdraw()  # hide main window
    root.attributes("-topmost", True)  # bring dialog to front
    file_path = askopenfilename(
        title="Select an audio file",
        filetypes=[
            ("Audio files", "*.mp3 *.wav *.m4a *.aac *.flac *.ogg *.wma"),
            ("All files", "*.*"),
        ],
    )
    root.destroy()
    return file_path

def convert_to_wav_16k_mono(input_file: str) -> str:
    base, _ = os.path.splitext(input_file)
    output_file = base + "_16k_mono.wav"

    cmd = [
        "ffmpeg",
        "-y",                 # overwrite if exists
        "-i", input_file,
        "-ar", "16000",       # 16kHz
        "-ac", "1",           # mono
        output_file
    ]

    subprocess.run(cmd, check=True)
    return output_file

if __name__ == "__main__":
    input_path = pick_audio_file()

    if not input_path:
        print("No file selected. Exiting.")
        raise SystemExit(0)

    try:
        out = convert_to_wav_16k_mono(input_path)
        print("Converted successfully!")
        print("Output:", out)
    except FileNotFoundError:
        print("ERROR: ffmpeg not found. Install ffmpeg and add it to PATH.")
    except subprocess.CalledProcessError:
        print("ERROR: ffmpeg failed to convert the file. Check the input file format.")
