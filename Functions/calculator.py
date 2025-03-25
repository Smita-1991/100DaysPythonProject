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



calculate_result(int(input("What's the first number?:")),input(f"+\n-\n*\n/\nPick an operation:"),
                    int(input("what's the next number?:")))
