from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse

from app.services.voice import synthesize_text_to_speech, transcribe_audio

router = APIRouter(tags=["voice"])


@router.post("/voice/stt")
async def speech_to_text(file: UploadFile = File(...)):
    audio = await file.read()
    text = transcribe_audio(audio, suffix=".wav")
    return {"text": text}


@router.post("/voice/tts")
def text_to_speech(text: str = Form(...)):
    output_path = synthesize_text_to_speech(text)
    return FileResponse(output_path, media_type="audio/wav", filename="orchestrix-voice.wav")
