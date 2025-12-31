import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()

    users = response.json()

    with open("user_data_2.csv", "w", newline="")as csvfile:
        fieldnames = ["Name", "Email", "City", "phone"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for user in users:
            writer.writerow({
                "Name": user["name"],
                "Email": user["email"],
                "City": user["address"]["city"],
                "phone": user["phone"]})
    print("All users data saved successfully!")     
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)           
