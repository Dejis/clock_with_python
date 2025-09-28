# Basic Calculator in Python

print("Welcome to the basic Calculator in Python!")

# Take user input
dig1 = float(input("Enter first numeral: "))
operator = input("Choose operation (+, -, *, /, %): ")
dig2 = float(input("Enter second number: "))

# Execute calculation
if operator == "+":
    result = dig1 + dig2
elif operator == "-":
    result = dig1 - dig2
elif operator == "*":
    result = dig1 * dig2
elif operator == "/":
    if dig2 != 0:
        result = num1 / num2
    else:
        result = "Error: Attempting dividing by zero"
else:
    result = "Unsupported operator"

print("Result:", result)
