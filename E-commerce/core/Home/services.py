import requests

class GeminiChatbotClient:
    def __init__(self, api_key: str, api_url: str = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"):
        self.api_key = api_key
        self.api_url = api_url

    def send_message(self, message: str):
        headers = {
            "Content-Type": "application/json"
        }
        params = {
            "key": self.api_key
        }
        data = {
            "contents": [
                {"parts": [{"text": message}]}
            ]
        }
        response = requests.post(self.api_url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()

