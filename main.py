# ===============================
# Calculator Pro 1.01
# ===============================

# ----- Operations -----

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def nth_root(n1, n2):
    if n2 == 0:
        print("Error: Root cannot be zero.")
        return None
    return n1 ** (1 / n2)


# ----- Dictionary of Operations -----

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,
    "^": nth_root
}


# ----- Helper Functions -----

def get_number(prompt):
    """Safely get a float from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter numbers only.")


def get_operator():
    """Ensure operator is valid."""
    while True:
        operator = input("""
Choose an operator:
    '+'  for addition
    '-'  for subtraction
    '*'  for multiplication
    '/'  for division
    '**' for exponent
    '^'  for nth root
Enter operator: 
""")
        if operator in operations:
            return operator
        else:
            print("Invalid operator. Please choose from the list.")


def ask_to_continue(result):
    """Ask user if they want to continue with result."""
    while True:
        choice = input(
            f"Type 'go to continue calculating with {result} "
            "or 'end' to start a new calculation: "
        ).lower()

        if choice == "go":
            return True
        elif choice == "end":
            return False
        else:
            print("Please enter 'go' or 'end'.")


# ----- Main Program Loop -----

print("\nHI! WELCOME TO CALCULATOR PRO 1.01\n")

while True:
    num1 = get_number("Enter your first number: ")

    while True:
        operator = get_operator()
        num2 = get_number("Enter your next number: ")

        result = operations[operator](num1, num2)

        if result is None:
            continue  # handles division by zero case

        result = round(result, 5)
        print(f"\nResult: {num1} {operator} {num2} = {result}\n")

        if ask_to_continue(result):
            num1 = result
        else:
            break
