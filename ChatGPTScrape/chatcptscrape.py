import requests

response = requests.get("https://chat.openai.com/chat")
print(response.text)