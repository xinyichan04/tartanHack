import requests
import json
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# DEEPSEEK_URL = "https://api.deepseek.com/v1/generate"

def generate_meditation_text(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
    "model": "deepseek-r1:7b",
    "prompt": "Say hi.",
    })
    # "prompt": prompt

    text = ""

    for res_part in res.text.split("\n"):
        if res_part.strip() != "":
            data = json.loads(res_part)
            text += data["response"]

    text = text.split("</think>")[1].strip()
    json_data = json.dumps({"message": text})
    # response = requests.post(DEEPSEEK_URL, json={"prompt": prompt}, headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"})
    return json_data

# def text_to_speech(text):
#     response = requests.post(DEEPSEEK_URL + "/tts", json={"text": text}, headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"})
#     return response.json().get("audio_url", "Error generating TTS.")
