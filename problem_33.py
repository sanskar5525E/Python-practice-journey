import requests

# 1. API URL (where we are asking data from)
url = "https://jsonplaceholder.typicode.com/users/1"

# 2. Send GET request (ask for data)
response = requests.get(url)

# 3. Check if request was successful
if response.status_code == 200:
    print("Request successful")

    # 4. Convert response to Python dictionary
    data = response.json()

    # 5. Use the data
    print("Name:", data["name"])
    print("Email:", data["email"])
    print("City:", data["address"]["city"])

    # 6. Save data to a file
    with open("user_data.txt", "w") as file:
        file.write("Name: " + data["name"] + "\n")
        file.write("Email: " + data["email"] + "\n")
        file.write("City: " + data["address"]["city"])

    print("Data saved to user_data.txt")

else:
    print("Request failed with status:", response.status_code)
