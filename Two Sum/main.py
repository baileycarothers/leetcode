import sys

numList = [1, 2, 3, 4, 5, 6, 7, 8]

print("Enter the number to be summed to: ")
inputNum = input()
targetNum = int(inputNum)
answer1 = 0
answer2 = 0
answerFound = False

for i in range(0, len(numList)):
    for k in range(1, len(numList)):
        if numList[i] + numList[k] == targetNum:
            answer1 = i
            answer2 = k
            answerFound = True
            break
        else:
            continue
    if answerFound:
        break
    else:
        continue

print("The answer indices are " + str(answer1) + " and " + str(answer2))