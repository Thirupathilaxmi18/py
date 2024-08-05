import csv

def readfile(filename):
    try:
        with open(filename,'r') as csv:
            content=csv.read()
            print(f"{filename} the content in this is\n {content}")
    except FileNotFoundError:
        print("file is not found")
filename="C:\\Users\\sange\\PycharmProjects\\files\\example.csv"
print(readfile(filename))