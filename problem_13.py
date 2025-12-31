import os

files = os.listdir()

count = 1

for program in files:
    new_name = f"program_{count}.py"
    os.rename(program, new_name)
    count += 1
