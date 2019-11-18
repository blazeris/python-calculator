input = input()

def add(firstTerm, secondTerm):
    return firstTerm + secondTerm

def subtract(firstTerm, secondTerm):
    return firstTerm - secondTerm

def multiply(firstTerm, secondTerm):
    return firstTerm * secondTerm

def divide(firstTerm, secondTerm):
    return firstTerm / secondTerm

def calculate(inputLine):
    inputLine = inputLine.replace(" ","")
    operations = {'+': add,
                  '-': subtract,
                  '*': multiply,
                  '/': divide
                  }
    open = inputLine.find('(')
    if open is not -1:
        reversed = inputLine[::-1] #string slicing to reverse
        close = reversed.find(')')
        inputLine = inputLine[0, open] + calculate(inputLine[open + 1, input.len() - close - 1]) + inputLine(input.len() - close - 1, inputLine.len())
print(calculate(input))