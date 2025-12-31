import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    user = users[0]

    name = user["name"]
    email = user["email"]
    city = user["address"]["city"]

    file = open("Demo_2.txt","w")
    file.write(f"Name : {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"City : {city} \n")
    file.close()

    print("Successfully done!")

else:
    print("Request Failed")    
    




