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

    #parentheses handling
    open = inputLine.find('(')
    if open is not -1:
        reversed = inputLine[::-1]
        close = len(inputLine) - reversed.find(')')
        inputLine = inputLine.replace(inputLine[open: close], calculate(inputLine[open + 1: close - 1]))

    #line to individual terms
    inputTerms = inputLine.split(" ")

    done = False
    while done is False:
        done = True

        while ("*" or "/") in inputTerms:
            operator_index = inputTerms.index("*" or "/")
            done = False
            if inputLine[operator_index] is '*':
                inputTerms[operator_index] = multiply(inputTerms[operator_index - 1], inputTerms[operator_index + 1])
                inputTerms.pop(operator_index + 1)
                inputTerms.pop(operator_index - 1)
            elif inputLine[operator_index] is '/':
                inputTerms[operator_index] = divide(inputLine[operator_index - 1], inputLine[operator_index + 1])
                inputTerms.pop(operator_index + 1)
                inputTerms.pop(operator_index - 1)

        while ('+' or '-') in inputTerms:
            operator_index = inputTerms.index('+' or '-')
            done = False
            if inputTerms[operator_index] is '+':
                inputTerms[operator_index] = add(inputTerms[operator_index - 1], inputTerms[operator_index + 1])
                inputTerms.pop(operator_index + 1)
                inputTerms.pop(operator_index - 1)
            elif inputLine[operator_index] is '-':
                inputTerms[operator_index] = subtract(inputLine[operator_index - 1], inputLine[operator_index + 1])
                inputTerms.pop(operator_index + 1)
                inputTerms.pop(operator_index - 1)

    return inputTerms[0]
print(calculate(input()))