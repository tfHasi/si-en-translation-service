import whisperx
import torch
import tempfile
import os
from pathlib import Path
from config.settings import WHISPER_MODEL_SIZE, WHISPER_COMPUTE_TYPE, WHISPER_LANGUAGE_CODE

class WhisperProcessor:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = whisperx.load_model(WHISPER_MODEL_SIZE, self.device, compute_type=WHISPER_COMPUTE_TYPE if self.device == "cuda" else "int8")
        self.align_model, self.metadata = whisperx.load_align_model(language_code=WHISPER_LANGUAGE_CODE, device=self.device)

    def transcribe(self, audio_data, filename, language=None):
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(filename).suffix.lower()) as tmp:
            tmp.write(audio_data)
            audio_path = tmp.name

        try:
            audio = whisperx.load_audio(audio_path)
            result = self.model.transcribe(audio, language=language)
            result = whisperx.align(result["segments"], self.align_model, self.metadata, audio, self.device)
            return {
                "success": True,
                "text": result.get("text", "").strip(),
                "segments": result.get("segments", []),
                "language": result.get("language", language or "unknown")
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            os.unlink(audio_path)

processor_instance = None

def get_speech_processor():
    global processor_instance
    if not processor_instance:
        processor_instance = WhisperProcessor()
    return processor_instance
