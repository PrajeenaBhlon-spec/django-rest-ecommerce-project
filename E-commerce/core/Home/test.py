import requests

api_key = "AIzaSyCSj8_nXISeqTrqgvj-VPdb0KwrD6V2q-I"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

response = requests.get(url)
print(response.json())