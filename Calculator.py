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
    operationOrder = {'*', '/', '+', '-'}
    operations = {'*': multiply,
                  '/': divide,
                  '+': add,
                  '-': subtract
    }
    open = inputLine.find('(')
    if open is not -1:
        reversed = inputLine[::-1] #string slicing to reverse
        close = len(inputLine) - reversed.find(')')
        inputLine = inputLine.replace(inputLine[open: close], calculate(inputLine[open + 1: close - 1]))

    done = False
    while done is False:
        done = True
        operatorIndex = inputLine.find('*' or '/')
        while operatorIndex is not -1:
            operatorIndex = inputLine.find('*' or '/')
            operationSubstring = str(inputLine[operatorIndex - 1: operatorIndex + 2])
            done = False
            if inputLine[operatorIndex] is '*':
                inputLine = inputLine.replace(operationSubstring, multiply(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
            elif inputLine[operatorIndex] is '/':
                inputLine = inputLine.replace(operationSubstring, divide(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
            operatorIndex = inputLine.find('*' or '/')

        operatorIndex = inputLine.find('+' or '-')
        while operatorIndex is not -1:
            operationSubstring = str(inputLine[operatorIndex - 1: operatorIndex + 2])
            done = False
            if inputLine[operatorIndex] is '+':
                inputLine = inputLine.replace(operationSubstring, add(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
            elif inputLine[operatorIndex] is '-':
                inputLine = inputLine.replace(operationSubstring, subtract(inputLine[operatorIndex - 1], inputLine[operatorIndex + 1]))
            operatorIndex = inputLine.find('*' or '/')
    return inputLine
print(calculate(input()))