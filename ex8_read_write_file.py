def writeToFile(file, content):
    with open(file, "w") as fileObj:
        fileObj.write(content)


def appendToFile(file, content):
    with open(file, "a") as fileObj:
        fileObj.write(content)


def readFromFile(file):
    with open(file) as fileObj:
        return fileObj.read()


writeToFile("greet.txt", "Hello!\n")
appendToFile("greet.txt", "Goodbye!\n")
assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"

print(readFromFile("greet.txt"))
