import os

files = os.listdir()

count = 1

for problem in files:
    new_name = f"problem_{count}.py"
    os.rename(problem, new_name)
    count += 1
