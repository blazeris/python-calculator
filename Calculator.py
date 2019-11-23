def add(firstTerm, secondTerm):
    return str(int(firstTerm) + int(secondTerm))

def subtract(firstTerm, secondTerm):
    return str(int(firstTerm) - int(secondTerm))

def multiply(firstTerm, secondTerm):
    return str(int(firstTerm) * int(secondTerm))

def divide(firstTerm, secondTerm):
    return str(int(firstTerm) / int(secondTerm))

def calculate(inputLine):

    #parentheses handling
    open = inputLine.find('(')
    if open is not -1:
        reversed = inputLine[::-1]
        close = len(inputLine) - reversed.find(')')
        inputLine = inputLine.replace(inputLine[open: close], calculate(inputLine[open + 1: close - 1]))

    #line to individual terms
    input_terms = inputLine.split()

    done = False
    while done is False:
        done = True

        while '*' in input_terms or '/' in input_terms:
            if '*' in input_terms:
                operator_index = input_terms.index('*')
            if '/' in input_terms:
                if operator_index is not -1:
                    operator_index = min(input_terms.index('/'), operator_index)
                else:
                    operator_index = input_terms.index('/')
            done = False
            if input_terms[operator_index] is '*':
                input_terms[operator_index] = multiply(input_terms[operator_index - 1], input_terms[operator_index + 1])
                input_terms.pop(operator_index + 1)
                input_terms.pop(operator_index - 1)
            elif input_terms[operator_index] is '/':
                input_terms[operator_index] = divide(input_terms[operator_index - 1], input_terms[operator_index + 1])
                input_terms.pop(operator_index + 1)
                input_terms.pop(operator_index - 1)

        while '+' in input_terms or '-' in input_terms:
            if '+' in input_terms:
                operator_index = input_terms.index('+')
            if '-' in input_terms:
                if operator_index is not -1:
                    operator_index = min(input_terms.index('-'), operator_index)
                else:
                    operator_index = input_terms.index('-')
            done = False
            if input_terms[operator_index] is '+':
                input_terms[operator_index] = add(input_terms[operator_index - 1], input_terms[operator_index + 1])
                input_terms.pop(operator_index + 1)
                input_terms.pop(operator_index - 1)
            elif input_terms[operator_index] is '-':
                input_terms[operator_index] = subtract(input_terms[operator_index - 1], input_terms[operator_index + 1])
                input_terms.pop(operator_index + 1)
                input_terms.pop(operator_index - 1)
    return input_terms[0]
print(calculate(input()))