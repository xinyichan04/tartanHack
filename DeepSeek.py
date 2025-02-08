import requests
import json

res = requests.post("http://localhost:11434/api/generate", json={
    "model": "deepseek-r1:7b",
    "prompt": "Say hi.",
})

text = ""

for res_part in res.text.split("\n"):
    if res_part.strip() != "":
        data = json.loads(res_part)
        text += data["response"]

text = text.split("</think>")[1].strip()

print(text)
