import os
print(os.getcwd())  # Get the current working directory

#  this block is creating a new file and writing to it
with open("sample.txt","w") as file:
    file.write("Hello, World!")
    file.write("Hello, Python!")


# Append to files to existing file
with open("sample.txt","a") as file:
    file.write("\nThis is an additional line.")
    file.write("\nThis is an additional line.")

#  Read files
with open("sample.txt","r") as file:
    content = file.read()
    print(content)




