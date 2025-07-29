import requests
from config.settings import HUGGINGFACE_API_KEY, BASE_MODEL_URL, MODEL_NAME

class HuggingFaceTranslator:
    def __init__(self):
        self.api_key = HUGGINGFACE_API_KEY
        self.base_url = BASE_MODEL_URL
        self.model_name = MODEL_NAME
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def translate(self, text, source_lang, target_lang):
        payload = {
            "inputs": text,
            "parameters": {
                "src_lang": "si_LK" if source_lang == "si" else "en_XX",
                "tgt_lang": "en_XX" if target_lang == "en" else "si_LK"
            }
        }

        response = requests.post(f"{self.base_url}{self.model_name}", headers=self.headers, json=payload, timeout=30)

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and result:
                return result[0].get("translation_text", "")
        raise Exception(f"Translation failed: {response.status_code} - {response.text}")