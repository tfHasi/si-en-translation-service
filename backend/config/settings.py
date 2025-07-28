import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
BASE_MODEL_URL = "https://api-inference.huggingface.co/models/"
MODEL_NAME = "facebook/mbart-large-50-many-to-many-mmt"