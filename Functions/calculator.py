from os import times_result

import art

print(art.calculator)

def calculate_result(value1,operation,value2):
    if operation=="+":
        output=value1+value2
        print(f"{value1}{operation}{value2}={output}")
    elif operation=="-":
        output = value1 - value2
        print(f"{value1}{operation}{value2}={output}")
    elif operation=="*":
        output = value1 * value2
        print(f"{value1}{operation}{value2}={output}")
    else:
        output = value1 / value2
        print(f"{value1}{operation}{value2}={output}")
    return output

should_continue=True
first_number=int(input("What's the first number?:"))
operation=input(f"+\n-\n*\n/\nPick an operation:")
second_number=int(input("what's the next number?:"))
output=calculate_result(first_number,operation,second_number)

while should_continue:
    withOutput=input(f"Type 'y' to continue calculating with {output} or type 'n' to start new calculation:")
    if withOutput == 'y':
        operation = input(f"+\n-\n*\n/\nPick an operation:")
        second_number = int(input("what's the next number?:"))
        should_continue=calculate_result(output,operation,second_number)
    else:
        first_number = int(input("What's the first number?:"))
        operation = input(f"+\n-\n*\n/\nPick an operation:")
        second_number = int(input("what's the next number?:"))
        output = calculate_result(first_number, operation, second_number)
        break
