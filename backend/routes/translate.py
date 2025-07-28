from flask import Blueprint, request, jsonify
from models.translator import HuggingFaceTranslator

translate_bp = Blueprint("translate", __name__)
translator = HuggingFaceTranslator()

@translate_bp.route('/api/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        text = data.get('text', '').strip()
        source_lang = data.get('source_lang', '').lower()
        target_lang = data.get('target_lang', '').lower()

        if not text:
            return jsonify({"error": "Text field is required"}), 400
        if source_lang not in ['si', 'en'] or target_lang not in ['si', 'en']:
            return jsonify({"error": "source language and target language must be in Sinhala('si') or English('en')"}), 400
        if source_lang == target_lang:
            return jsonify({"error": "source language and target language cannot be the same"}), 400

        translated_text = translator.translate(text, source_lang, target_lang)

        return jsonify({
            "success": True,
            "original_text": text,
            "translated_text": translated_text,
            "source_lang": source_lang,
            "target_lang": target_lang
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500