from faster_whisper import WhisperModel
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import json

def pick_audio_file():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = askopenfilename(
        title="Select an audio file to transcribe",
        filetypes=[
            ("Audio files", "*.wav *.mp3 *.m4a *.aac *.flac *.ogg *.wma"),
            ("All files", "*.*"),
        ],
    )
    root.destroy()
    return file_path

audio_path = pick_audio_file()
if not audio_path:
    print("No file selected. Exiting.")
    raise SystemExit(0)

model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio_path, language="en")

segments_list = []
full_text_parts = []

for s in segments:
    segments_list.append({
        "start": float(s.start),
        "end": float(s.end),
        "text": s.text.strip()
    })
    full_text_parts.append(s.text)

text_out = "".join(full_text_parts).strip()

data = {
    "audio_file": audio_path,
    "language": info.language,
    "language_probability": float(getattr(info, "language_probability", 0.0)),
    "text": text_out,
    "segments": segments_list
}

folder = os.path.dirname(audio_path)
base_name = os.path.splitext(os.path.basename(audio_path))[0]
json_path = os.path.join(folder, f"{base_name}.json")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Detected:", info.language, getattr(info, "language_probability", None))
print("Saved transcript JSON to:", json_path)
