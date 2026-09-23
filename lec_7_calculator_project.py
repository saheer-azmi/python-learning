#Basic automatic Arthmetic operator (Example)

a=22
b=12
print(f"addition:{a+b}")
print(f"substraction:{a-b}")
print(f"multiplication:{a*b}")
print(f"divison:{a/b}")
print(f"floor divison:{a//b}")
print(f"modulus:{a%b}")


bottels=8
bear=45
cream=8
mobile=8
cup=7
brush=7
dairy=8
print(f"addition:{bottels+bear+cream+mobile+cup+brush+dairy}")
print(f"subtraction:{bottels-bear-cream-mobile-cup-brush-dairy}")
print(f"multiplication:{bottels*bear*cream*mobile*cup*brush*dairy}")
print(f"division:{bottels/bear/cream/mobile/cup/brush/dairy}")



# user-input-calculator - 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

a=float(input("enter your first number:"))
b=float(input("enter your second number:"))

print(f"addition:{a+b}")
print(f"substraction:{a-b}")
print(f"multiplication:{a*b}")
print(f"divison:{a/b}")
print(f"floor division:{a//b}")
print(f"modulus:{a%b}")
print(f"power:{a**b}")








3#Basic calculator with operator choice

a = input("enter first number: ")
b = input("Enter second number: ")
op = input("Enter operator (+, -, *, /): ")


a=int(a)
b=int(b)

if op == "+":
    print("Result:", a + b)
elif op == "-":
 print("Result:", a - b)
elif op== "*":
 print("Result:", a * b)
elif op == "/":
  ("Result:", a / b)
else:
  print("Invalid operator")


#-logic if divison 0 agar b==0,hai to division mat karo..

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)

elif op == "-":
    print("Result:", a - b)

elif op == "*":
    print("Result:", a * b)

elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)

else:
    print("Invalid operator")

a=int(input("enter first number"))
b=int(input("enter second number"))
op=(input("+,-,*,/"))


if op=="+":
  print(f"result:{a+b}")
elif op=="-":
  print(f"result:{a-b}")
elif op=="*":
  print(f"result:{a*b}")
elif op=="/":
  print("result:{a/b}")
else:
  print("invalid opertor")

number1=int(input("enter the value of first no.="))
number2=int(input("enter second value of second no.="))

add=number1+number2

print("the sub of ",number1,"and",number2,"is",add)
sub=number1-number2
print("the substraction of",number1,"and",number2,"is",sub)
div= number1/number2
print("the division of",number1,"and",number2,"is",div)
div=number1/number2
print("the division of",number1,"and",number2,"is",div)
flr=number1//number2
print("the floor division of",number1,"and",number2,"is",flr)
exp=number1**number2
