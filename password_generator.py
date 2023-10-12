def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Can't divided by zero."
    
# Get user input

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose operation (+, -, *, /):")

# Perform calculation based on user's choice

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operation."

# Display the result
print("Result:", result)