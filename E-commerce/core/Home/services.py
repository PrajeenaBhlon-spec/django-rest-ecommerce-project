import requests

class GeminiChatbotClient:
    def __init__(self, api_key: str, api_url: str = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"):
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
      print(response.status_code)
      print(response.text)

      if response.status_code != 200:
        return "Error from Gemini API"

      result = response.json()
      return result["candidates"][0]["content"]["parts"][0]["text"]

