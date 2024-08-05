def readfile(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
# Example usage:
filename = "C:\\Users\\sange\\PycharmProjects\\files\\input.txt"
readfile(filename)
