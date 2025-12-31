import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200:
    print("Request sucessful")
    data = response.json()

    print("Name", data["name"])
    print("Email", data["email"])
    print("city", data["address"]["city"])
    print("street", data["address"]["street"])

    with open("user_data_2.txt", "w") as file:
        file.write("Name:" + data["name"]+"\n")
        file.write("Email:" + data["email"]+"\n")
        file.write("City: " + data["address"]["city"] + "\n")
        file.write("City: " + data["address"]["street"] + "\n")
    print("Data saved to user_data_2.txt")
else:
    print("Request unsuccessful", response.status_code)
