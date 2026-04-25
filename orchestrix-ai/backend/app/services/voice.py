import tempfile
from pathlib import Path

import whisper

from app.core.config import get_settings

settings = get_settings()

_whisper_model = None


def transcribe_audio(raw_bytes: bytes, suffix: str = ".wav") -> str:
    global _whisper_model
    if _whisper_model is None:
        _whisper_model = whisper.load_model(settings.whisper_model)

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(raw_bytes)
        tmp_path = Path(tmp.name)

    result = _whisper_model.transcribe(str(tmp_path))
    tmp_path.unlink(missing_ok=True)
    return result.get("text", "").strip()


def synthesize_text_to_speech(text: str) -> str:
    import pyttsx3

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        output_path = tmp.name

    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path
