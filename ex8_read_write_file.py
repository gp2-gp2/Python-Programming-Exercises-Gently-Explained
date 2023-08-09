def writeToFile(file, content):
    pass


def appendToFile(file, content):
    pass


def readFromFile(file):
    pass


writeToFile("greet.txt", "Hello!\n")
appendToFile("greet.txt", "Goodbye!\n")
assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"
