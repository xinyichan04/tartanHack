import json
import os

import requests


def generate_meditation_text(environment, goal):

  meditation_text = f"Take on the role of a meditation guide. Craft a short, descriptive script to help someone feel calm and relaxed. Use soothing imagery, focus on deep breathing, and incorporate elements like nature, warmth, or gentle light to evoke a sense of peace and tranquility. The script should be {goal} in nature, and should take place at {environment}. Do not output more than three sentences."
  res = requests.post(
    "http://localhost:11434/api/generate", json={
      "model": "deepseek-r1:7b",
      "prompt": meditation_text,
    }
  )

  text = ""
  for res_part in res.text.split("\n"):
    if res_part.strip() != "":
      data = json.loads(res_part)
      text += data["response"]

  text = text.split("</think>")[1].strip()
  json_data = json.dumps({
    "message": text
  })
  return json_data
