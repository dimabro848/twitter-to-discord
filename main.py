from flask import Flask, request
import requests
import re
import os

app = Flask(__name__)  # Исправлено: name → name

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1376236154617200784/V2nYSfPBhmCUW2LLkdhvQ7mZd_dIG22LaXRDVE5hxM0kxv95rG-H1wZGz6yGzbG90t76"

def clean_text(text):
    return re.sub(r'#\w+', '', text).strip()

@app.route('/', methods=['GET', 'POST'])
def receive_tweet():
    if request.method == 'GET':
        return "Server is running!", 200

    data = request.json
    tweet_text = clean_text(data.get("text", ""))
    tweet_url = data.get("tweet_url", "")

    message = f"{tweet_text}\n{tweet_url}\n\n@everyone"

    requests.post(DISCORD_WEBHOOK_URL, json={
        "username": "UPvestor Chain",
        "avatar_url": "https://chat.openai.com/share-images/file-7MdYwSShajUYWoeTM7Yvmd",
        "content": message
    })

    return "OK"

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
