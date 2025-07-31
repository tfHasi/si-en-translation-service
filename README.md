# Sinhala-English Translation Service

A single-page bilingual translator that supports both text translation and audio transcription between **Sinhala** and **English** using WhisperX and mBART.

---

## Features

* Audio file upload and transcription (MP3, WAV, M4A, FLAC, OGG)
* Text translation between Sinhala ↔ English
* Auto language detection and source–target switching
* Fully responsive, minimalistic user interface

---

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript (Vanilla)
* **Backend:** Flask (Python)
* **Speech-to-Text:** WhisperX
* **Translation Model:** mBART (via Hugging Face Transformers)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tfHasi/si-en-translation-service.git
cd si-en-translation-service
```

### 2. Create and Activate a Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Backend

```bash
python main.py
```

By default, the backend runs on `http://localhost:5000`.

### 5. Open the Frontend

Open `index.html` in your browser. Make sure it points to `http://localhost:5000/api` in the JavaScript section.

---

## Notes

* Make sure WhisperX and mBART models are properly downloaded or cached before first use.
* For production, consider setting up CORS, file size limits, and HTTPS.

---

### Made with Love❤️
