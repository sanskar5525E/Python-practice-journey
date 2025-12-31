import os

files = os.listdir()

count = 1

for file in files:
    new_name = f"file_{count}.py"
    os.rename(file, new_name)
    count += 1
