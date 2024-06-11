

# Function to get an integer input from the user with error handling.
def calculator():

    def inputNUM(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")


    # Get the first input from the user.
    number1 = inputNUM("Enter an integer for Calculation:\n ")

    # Get the second inout from the user.
    number2 = inputNUM("Enter an integer for Calculation:\n ")

    print("You entered:\n", number1, number2)

    # Get the calculation type from the user.
    calculation = input(
        "Enter what type of calculation you want from the given numbers\n"
        
        "add = addition\n"
        "sub = subtraction\n"
        "mul = multiplication\n"
        "expo = exponential\n"
        "dvd = division\n"
        "fdiv = floor division\n"
        "mod = modulus\n"

    ).strip().lower()

    # Perform the calculation according to the user.
    if calculation == 'add':
        print("Addition of the two numbers is:", number1 + number2)

    elif calculation == 'sub':
        print("Subtraction of the two numbers is:", number1 - number2)

    elif calculation == 'mul':
        print("Multiplication of the two numbers is:", number1 * number2)

    elif calculation == 'dvd':
        # Handle zero in Division.
        if number2 == 0:
            print("Error occurred : Division by zero is not allowed.")
        else:
            print("Division of the two numbers is:", number1 / number2)

    elif calculation == 'expo':
        print("Exponential of the two numbers is:", number1 ** number2)

    elif calculation == 'mod':
        # Handle zero in Modulus.
        if number2 == 0:
            print("Error: Modulus by zero is not allowed.")
        else:
            print("Modulus of the two numbers is:", number1 % number2)

    elif calculation == 'fdiv':
        # Handle zero in Floor Division.
        if number2 == 0:
            print("Error: Floor division by zero is not allowed.")
        else:
            print("Floor division of the two numbers is:", number1 // number2)

    else:
        print("Unsupported operation. Please enter a valid calculation type (add, sub, mul, expo, dvd, fdiv, mod).")

calculator()