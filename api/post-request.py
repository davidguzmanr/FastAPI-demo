import requests
import json

text = 'That movie was horrible, a complete waste of time'

url = f'http://127.0.0.1:8000/sentiments?text={text}'
url = url.replace(' ', '%20')

response = requests.post(url)
response = json.loads(response.content.decode('utf-8'))

print(response)