with open("sample.txt","r+") as file: 
    data = file.read()
    file.write("\n Hi I am Ayush")
    print(data)
