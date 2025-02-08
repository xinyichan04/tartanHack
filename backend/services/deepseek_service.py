import requests
import json
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# DEEPSEEK_URL = "https://api.deepseek.com/v1/generate"

def generate_meditation_text(meditation_type, sound, tone, description):
    

    meditation_text = f"Take on the role of a meditation guide. Craft a short, descriptive script to help someone feel calm and relaxed. Use soothing imagery, focus on deep breathing, and incorporate elements like nature, warmth, or gentle light to evoke a sense of peace and tranquility. The script should be {meditation_type} in nature, and should take on a {tone} tone and contain {sound} sounds. In addition, take note of the following requests made by the user:{description}The script should be a continuous prose, which can be read out to simulate a meditation session."
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "deepseek-r1:7b",
        "prompt": meditation_text,
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
