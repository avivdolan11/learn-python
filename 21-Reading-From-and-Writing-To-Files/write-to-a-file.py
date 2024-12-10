file_name = "my_first_file.txt"

with open(file_name, "w") as file_object:
    file_object.write("Hello \n")
    file_object.write("Lets go")