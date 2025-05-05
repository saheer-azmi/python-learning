# Automatic Arithmetic Operations
a = 10
b = 5

# Displaying all operations
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")


#Basic calculator with operator choice

a = input("enter first number: ")
b = input("Enter second number: ")
op = input("Enter operator (+, -, *, /): ")

a = int(a)
b = int(b)

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

# Simple Arithmetic Operations - Step by Step

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Advanced Arithmetic Operations with Exponentiation and Floor Division

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Addition
print(f"Addition: {a + b}")

# Subtraction
print(f"Subtraction: {a - b}")

# Multiplication
print(f"Multiplication: {a * b}")

# Division
print(f"Division: {a / b}")

# Exponentiation (Power)
print(f"Exponentiation (a^b): {a ** b}")

# Floor Division (Quotient without remainder)
print(f"Floor Division: {a // b}")

# Modulus (Remainder)
print(f"Remainder: {a % b}")