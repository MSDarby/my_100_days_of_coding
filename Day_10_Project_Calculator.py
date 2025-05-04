import calculator_art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(calculator_art.logo)

    inp1 = float(input("Please enter your first number: \n"))

    program_continue = True
    while program_continue:
        for symbol in calculator_operation:
            print(symbol)
        operator = input("Please enter your mathematical operator \n")
        inp2 = float(input("Please enter your second number: \n"))

        answer = calculator_operation[operator](inp1, inp2)
        print(f"{inp1} {operator} {inp2} = {answer}")

        cont = input("Do you want to continue working with the previous result? \n"
              "please enter y for yes or n for no: \n").lower()

        if cont == 'y':
            inp1 = answer
        else:
            program_continue = False
            print("\n" * 20)
            calculator()

calculator()
