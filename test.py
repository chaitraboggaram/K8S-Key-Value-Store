import requests

url = "http://localhost:8000/set/my_key/my_value"
response = requests.post(url)

print(response.text)
