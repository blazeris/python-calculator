input = input()


def calculate(inputLine)
    inputLine = inputLine.replace(" ","")
    open = -1
    close = -1

    for i in range(inputLine.len() - 1):
        if inputLine[i] == '(':
            open = i
        if inputLine[i] == ')':
            close = i
            inputLine = inputLine[0,open] + calculate(inputLine[open + 1,close]) + inputLine(close + 1, inputLine.len())
print(calculate(input))