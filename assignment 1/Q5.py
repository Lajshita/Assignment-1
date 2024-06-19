string = input("Enter a string : ")

File_Name = "string.txt"
with open (File_Name,'w') as file :
    file.write(string)

print(f"{string} has been written in {File_Name}")    