with open("cupcakes.txt", "r") as cupcakes_file:
    print("The file has been opened")
    content = cupcakes_file.read()
    print(content)