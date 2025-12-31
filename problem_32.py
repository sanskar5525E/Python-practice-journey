import requests
url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Status",response.status_code)
print("Data :",response.json())
