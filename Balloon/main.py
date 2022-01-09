# Description: Given a string text, you want to use the characters of text
# to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once.
# Return the maximum number of instances that can be formed.

def maxNumberOfBalloons(text: str) -> int:
    textLength = len(text)
    balloon = [['b',0],['a',0],['l',0],['o',0],['n',0]]
    for x in range(0, textLength, 1):
        for list in balloon:
            if text[x] in list:
                index = balloon.index(list)
                balloon[index][1] += 1
    balloon[2][1] //= 2
    balloon[3][1] //= 2
    minimum = min(balloon, key=lambda x: x[1])
    return minimum[1]


if __name__ == '__main__':
    answer = maxNumberOfBalloons("nalaebbballlooonnnboolnko")
    print(answer)
