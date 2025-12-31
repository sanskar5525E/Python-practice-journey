import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Sanskar test",
    "body": "Learning API",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Data:", response.json())
