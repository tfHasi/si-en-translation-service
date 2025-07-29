from flask import Blueprint, request, jsonify
from models.speaker import get_speech_processor
from werkzeug.utils import secure_filename
import logging

voice_bp = Blueprint("voice", __name__)
ALLOWED_EXTENSIONS = {"wav", "mp3", "m4a", "flac", "ogg"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@voice_bp.route('/api/transcribe', methods=['POST'])
def transcribe():
    try:
        if 'audio' not in request.files:
            return jsonify({"success": False, "error": "No audio file part in request"}), 400
        file = request.files.get("audio")
        if not file or file.filename == '':
            return jsonify({"success": False, "error": "No audio file provided"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"success": False, "error": "Unsupported file type. Allowed: wav, mp3, m4a, flac, ogg"}), 400

        lang = request.form.get("language")
        if not lang:
            return jsonify({"success": False, "error": "Language parameter is required"}), 400

        supported_languages = ["en", "si", "auto"]
        if lang not in supported_languages:
            lang = None
        audio_data = file.read()
        if len(audio_data) == 0:
            return jsonify({"success": False, "error": "Empty audio file"}), 400
        result = get_speech_processor().transcribe(audio_data, file.filename, language=lang if lang != "auto" else None)

        if not result["success"]:
            return jsonify({"success": False, "error": result["error"]}), 500

        return jsonify({
            "success": True,
            "transcribed_text": result["text"] or "",
            "detected_language": result["language"],
            "segments": result["segments"],
            "filename": secure_filename(file.filename),
            "segment_count": len(result["segments"])
        })
        
    except Exception as e:
        logging.error(f"Transcription error: {str(e)}")
        return jsonify({"success": False, "error": f"Internal server error: {str(e)}"}), 500