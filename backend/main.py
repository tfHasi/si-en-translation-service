from flask import Flask, jsonify
from flask_cors import CORS
from routes.translate import translate_bp
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(translate_bp)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "sinhala-english-translator",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    if not os.getenv('HUGGINGFACE_API_KEY'):
        print("Warning: HUGGINGFACE_API_KEY environment variable not set")

    app.run(debug=True, host='0.0.0.0', port=5000)