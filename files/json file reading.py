def readjson(filename):
    try:
        with open (filename,'r') as file:
            content=file.read()
            print(f"{filename}\n content in the file is {content}")
    except FileNotFoundError:
        print("file is not found")
filename="C:\\Users\\sange\\PycharmProjects\\files\\example.json"
readjson(filename)