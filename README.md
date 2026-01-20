# Local Whisper Transcriber

A local, offline Python toolset for converting audio files and transcribing them into text (JSON format) using [Faster Whisper](https://github.com/SYSTRAN/faster-whisper).

## Features

* **Audio Preprocessing:** Converts various audio formats (MP3, M4A, AAC, etc.) to 16kHz Mono WAV (optimized for AI models).
* **Fast Transcription:** Uses `faster-whisper` with INT8 quantization for quick inference on CPU.
* **JSON Export:** Outputs a structured JSON file containing the full text, language metadata, and segment-level timestamps.
* **Privacy:** Runs entirely locally on your machine. No data is sent to the cloud.

## Prerequisites

1.  **Python 3.8+**
2.  **FFmpeg:** This is required for the audio conversion script.
    * *Windows:* Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), extract, and add the `bin` folder to your System PATH.
    * *Mac:* `brew install ffmpeg`
    * *Linux:* `sudo apt install ffmpeg`

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/local-whisper-transcriber.git](https://github.com/YOUR_USERNAME/local-whisper-transcriber.git)
    cd local-whisper-transcriber
    ```

2.  Install the required Python packages:
    ```bash
    pip install faster-whisper tk
    ```
    *(Note: `tk` is usually included with Python, but required for the file selection dialogs).*

## Usage

### Step 1: Preprocess Audio (Optional but Recommended)
Run the preprocessing script to convert your audio to the optimal format (16kHz WAV).

```bash
python preprocess_audio.py
