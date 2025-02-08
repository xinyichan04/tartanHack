import requests
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_URL = "https://api.deepseek.com/v1/generate"

def generate_meditation_text(prompt):
    response = requests.post(DEEPSEEK_URL, json={"prompt": prompt}, headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"})
    return response.json().get("text", "Error generating text.")

def text_to_speech(text):
    response = requests.post(DEEPSEEK_URL + "/tts", json={"text": text}, headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"})
    return response.json().get("audio_url", "Error generating TTS.")
