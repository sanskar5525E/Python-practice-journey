import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    file = open("Demo.txt", "w")

    for user in users:
        name = user["name"]
        email = user["email"]
        city = user["address"]["city"]

        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"City: {city}\n")
        file.write("---------------\n")

    file.close()
    print("All users saved successfully!")

else:
    print("Request Failed")
