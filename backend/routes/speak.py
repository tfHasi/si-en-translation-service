from flask import Blueprint, request, jsonify
from models.speaker import get_speech_processor
from werkzeug.utils import secure_filename

voice_bp = Blueprint("voice", __name__)
ALLOWED_EXTENSIONS = {"wav", "mp3", "m4a", "flac", "ogg"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@voice_bp.route('/api/transcribe', methods=['POST'])
def transcribe():
    file = request.files.get("audio")
    if not file or file.filename == '':
        return jsonify({"success": False, "error": "No audio file provided"}), 400
    if not allowed_file(file.filename):
        return jsonify({"success": False, "error": "Unsupported file type"}), 400

    lang = request.form.get("language")
    if not lang:
        return jsonify({"success": False, "error": "Language parameter is required"}), 400

    result = get_speech_processor().transcribe(file.read(), file.filename, language=lang)

    if not result["success"]:
        return jsonify({"success": False, "error": result["error"]}), 500

    return jsonify({
        "success": True,
        "transcribed_text": result["text"],
        "detected_language": result["language"],
        "segments": result["segments"],
        "filename": secure_filename(file.filename)
    })