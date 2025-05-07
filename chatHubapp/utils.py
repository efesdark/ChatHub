import requests
import json
from django.conf import settings

def query_huggingface_chatbot(prompt):
    API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-small"
    headers = {
        "Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": {
            "text": prompt,
            # İsteğe bağlı parametreler:
            "max_length": 100,  # Maksimum yanıt uzunluğu
            "temperature": 0.9,  # Yaratıcılık seviyesi (0-1)
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Hata kontrolü
        result = response.json()
        return result.get("generated_text", "Bir hata oluştu.")
    except requests.exceptions.HTTPError as err:
        # Model yüklenirken 503 hatası alınırsa:
        if response.status_code == 503:
            estimated_time = response.headers.get("estimated_time", 10)
            return f"Model yükleniyor... Lütfen {estimated_time} saniye sonra tekrar deneyin."
        return f"Hata: {err}"