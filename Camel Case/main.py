import sys

finalOutput = ""
emptySpace = " "
firstWord = True


def CamelCase(s):
    return s.capitalize()


def toLower(s):
    return s.lower()


for line in sys.stdin:
    if line == " \n":
        finalOutput += emptySpace
        firstWord = True
    else:
        if firstWord:
            finalOutput += toLower(line).strip()
            firstWord = False
        else:
            finalOutput += CamelCase(line).strip()

print(finalOutput)