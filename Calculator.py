input = input()

def add(firstTerm, secondTerm):
    return str(int(firstTerm) + int(secondTerm))

def subtract(firstTerm, secondTerm):
    return str(int(firstTerm) - int(secondTerm))

def multiply(firstTerm, secondTerm):
    return str(int(firstTerm) * int(secondTerm))

def divide(firstTerm, secondTerm):
    return str(int(firstTerm) / int(secondTerm))

def calculate(inputLine):
    inputLine = inputLine.replace(" ","")

    open = inputLine.find('(')
    if open is not -1:
        reversed = inputLine[::-1] #string slicing to reverse
        close = reversed.find(')')
        inputLine = inputLine[0, open] + calculate(inputLine[open + 1, input.len() - close - 1]) + inputLine(input.len() - close - 1, inputLine.len())

    done = False
    while done is False:
        done = True
        operatorIndex = inputLine.find('*' or '/')
        if operatorIndex is not -1:
            operationSubstring = str(inputLine[operatorIndex - 1: operatorIndex + 2])
            done = False
            if inputLine[operatorIndex] is '*':
                inputLine = inputLine.replace(operationSubstring, multiply(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
                print(inputLine)
            elif inputLine[operatorIndex] is '/':
                inputLine = inputLine.replace(operationSubstring, divide(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
                print(inputLine)
        else:
            operatorIndex = inputLine.find('+' or '-')
            if operatorIndex is not -1:
                operationSubstring = str(inputLine[operatorIndex - 1: operatorIndex + 2])
                done = False
                if inputLine[operatorIndex] is '+':
                    inputLine = inputLine.replace(operationSubstring, add(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
                    print(inputLine)
                elif inputLine[operatorIndex] is '-':
                    inputLine = inputLine.replace(operationSubstring, subtract(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
                    print(inputLine)
    return inputLine
print(calculate(input))