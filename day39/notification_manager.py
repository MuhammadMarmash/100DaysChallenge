import requests


class NotificationManager:
    def __init__(self):
        self.bot_chat_id = "1105545417"
        self.bot_token = "6161640296:AAFtIxF46nMEr4eEBeWDXDX9UGX5vIprlI4"

    def send_telegram_message(self, message):
        end_point = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        response = requests.post(end_point, params={
            "chat_id": self.bot_chat_id,
            "text": message,
            "parse_mode": "HTML"
        })
        response.raise_for_status()

