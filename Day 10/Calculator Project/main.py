import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4,8))

print(art.logo)

n1 = float(input("Input first number: "))
test = True
while test == True:
    opp = input("+\n-\n*\n/\nInput operation: ")
    n2 = float(input("Input second number: "))
    awns = operations[opp](n1,n2)
    print(f"{n1} {opp} {n2} = {awns}")
    if input(f"Type 'y' to continue calculating with {awns}, or type 'n' to start a new calculation: ") != "y":
        print("\n" * 20)
        n1 = float(input("Input first number: "))
    else:
        n1 = awns
