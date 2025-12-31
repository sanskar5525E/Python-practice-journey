# password generator
import random
import string
while True:

    # asking
    length = int(input("Enter length of the password :"))

    characters = string.ascii_letters+string.digits+"!@#$%^&*"

    password = "".join(random.choice(characters) for i in range(length))

    print(password)

    msg = input("want another password {yes/no} :").lower()
    if msg == "no":
        break
    elif msg == "yes":
        continue
    else:
        print("invaild")
        break
