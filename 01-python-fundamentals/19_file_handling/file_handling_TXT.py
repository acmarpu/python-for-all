#  Read/write files from sample.txt
with open("sample.txt","w") as file:
    file.write("Hello, World!")
 

# Append to files
with open("sample.txt","a") as file:
    file.write("\nThis is an additional line.")


#  Read files
with open("sample.txt","r") as file:
    content = file.read()
    print(content)




