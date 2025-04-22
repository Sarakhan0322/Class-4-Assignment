# file_handling.py

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
