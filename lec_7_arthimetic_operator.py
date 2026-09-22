# Automatic Arithmetic Operations

# 1. Arithmetic 

price=750
quantity=4
discount=200
print(price*quantity-discount)

price=750
quantity=4
discount=200
print("multiplication(price*quantity-dicount)=",price*quantity-discount)

print("\n1. Arithmetic Operators:")
a = 15
b = 4
print("Addition (a + b) =", a + b)
print("Subtraction (a - b) =", a - b)
print("Multiplication (a * b) =", a * b)
print("Division (a / b) =", a / b)
print("Modulus (a % b) =", a % b)                             #reminder bachi hue value batai hai 
print("Exponentiation (a ** b) =", a ** b)                    #powwer ke liye use hoti hai 
print("Floor Division (a // b) =", a // b)                    #decimal part hata deta hai 


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
