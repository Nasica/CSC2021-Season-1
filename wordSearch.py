def rotateList(listToRotate):
    x = 0
    appendString = ""
    rotated = []
    while x < len(listToRotate):
        for line in listToRotate:
            appendString += line[x]
        x = x + 1
        rotated.append(appendString)
        appendString = ""
    return(rotated)

def diagonalList(listToDiag):
    appendString = ""
    for x in range(len(listToDiag)):
        for y in range(len(listToDiag)):
            

fileInput = open('wsInput.txt', 'r')

wordList = []
wordArray = []
for line in fileInput:
    if 'Remaining words:' in line:
        continue
    if line[0] == ' ':
        break
    wordList.append(line.strip())
for line in fileInput:
    if len(line) < 2:
        break
    if (line[0].isdigit()) or (line[1].isdigit()):
        wordArray.append(line[3:].replace(" ", "").strip())
columns = rotateList(wordArray)

diagonalList(wordArray)

for word in wordList:
    for line in wordArray:
        if (word in line) or (word[::-1] in line):
            print(line)
            print(word)
            print()

print("columns")

for word in wordList:
    for line in columns:
        if (word in line) or (word[::-1] in line):
            print(line)
            print(word)
            print()
