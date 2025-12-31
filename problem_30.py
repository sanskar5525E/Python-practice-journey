import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Data:", response.json())
