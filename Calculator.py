def add(firstTerm, secondTerm):
    return str(float(firstTerm) + float(secondTerm))

def multiply(firstTerm, secondTerm):
    return str(float(firstTerm) * float(secondTerm))

def exponent(firstTerm, secondTerm):
    return str(float(firstTerm) ** float(secondTerm))

def one_operator_math(operator, math):
    global input_terms
    operator_index = input_terms.index(operator)
    input_terms[operator_index] = math(input_terms[operator_index - 1], input_terms[operator_index + 1])
    input_terms.pop(operator_index + 1)
    input_terms.pop(operator_index - 1)
    
def calculate(inputLine):
    global input_terms
    # parentheses handling
    open = inputLine.find('(')
    if open is not -1:
        reversed = inputLine[::-1]
        close = len(inputLine) - reversed.find(')')
        inputLine = inputLine.replace(inputLine[open: close], calculate(inputLine[open + 1: close - 1]))
    # line to individual terms
    input_terms = inputLine.split()
    while '^' in input_terms:
        one_operator_math('^', exponent)
    while '*' in input_terms or '/' in input_terms:
        if '/' in input_terms:
            operator_index = input_terms.index('/')
            input_terms[operator_index] = '*'
            input_terms[operator_index + 1] = str(1 / float(input_terms[operator_index + 1]))
        elif '*' in input_terms:
            one_operator_math('*', multiply)
    while '+' in input_terms or '-' in input_terms:
        if '-' in input_terms:
            operator_index = input_terms.index('-')
            input_terms[operator_index] = '+'
            input_terms[operator_index + 1] = str(-float(input_terms[operator_index + 1]))
        elif '+' in input_terms:
            one_operator_math('+', add)
    return input_terms[0]
print(calculate(input()))