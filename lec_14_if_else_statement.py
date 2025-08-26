#EXAMPLE 1; (BASIC IF SATEMENT:)
X=6
if X > 5:
   print("x is greater than 5")

#EXAMPLE 2:(BASIC IF-ELSE SATEMENT:)
X=5
if X>8:
   print("x is greater then 8")
else:
   print("X is not greater the 8")

#EXAMPLE 3; (BASIC IF-ELSE-STATEMENT:)
marks=80
if marks >=90:
   print("A+")
elif marks>=85:
   print("A")
elif marks >=82:
   print("B+")
elif marks >=89:
   print("B")
else:
   print("grade c")

#EXAMPLE 5;(BASIC SHORT HAND IF:)
#Ek hi line me if likhne ka shortcut:
#if condition: print("something")

a=10
if a>5:print("greater then 5")

#EXAMPLE 5;(BASIC HAND IF...ELSE)
#print("true condition ")if condition else:
#print("false condition")
a=12
b=20
print("a is greater") #if a > b  else
print("b is greater")


#example 6 ; (logical operators:and,or,not:)
#(i) and - both true hone chaye
a=5
if a>4 and a<10:
   print("a is between 1 and 10")

a=6
if a >4 and a<10:
 print("a is between 1 to 10")

#(2)or- koi ak true hona chaye:
 a =15
if a<5 or a>10:
   print("a is outside the range of 5 to 10")

a=12
if a>7 or a<10:
   print("a is outside the range of 7 to 10")

#(3) not-ulta karega condition ka:
a= False
if not a:
 print("a is false")

a=True
if not a:
   print("a is false")
else:
   print("a is true")
is_logged_in=False
if not is_logged_in:
 print("please login first!")


#EXAMPLE 7:NESTED IF (IF KE ANDAR IF)
  #if condition1:
   # if condition2:
a=10
if a>5:
  if a<15:
     print("a is between 5 and 15")
    
#EXAMPLE 8: THE PASS SATEMENT

a=13
if a<9:
 pass


# -----------------------------------------------
# Advanced If-Elif-Else with Real-Life Scenarios
# -----------------------------------------------

# 🎯 1. Check if person is eligible to vote
age = 18
if age > 17:
    print("1. ✅ Eligible to vote")
else:
    print("1. ❌ Not eligible to vote (Below 18)")

# 🏫 2. Grade calculation from marks (Nested if + elif)
marks = 85

if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("2.  Grade: A+")
    elif marks >= 80:
        print("2.  Grade: A")
    elif marks >= 70:
        print("2.  Grade: B")
    elif marks >= 60:
        print("2.  Grade: C")
    else:
        print("2. ❌ Fail")
else:
    print("2. ❗ Invalid marks entered")

# 💸 3. Check if user can withdraw from ATM
balance = 5000
withdraw_amount = 3000

if withdraw_amount >= balance:
    print(f"3. ✅ Withdrawn ₹{withdraw_amount}")
else:
    print("3. ❌ Insufficient Balance")

# 🔐 4. Simple login system using username and password
username = "admin"
password = "1234"

input_username = "admin"
input_password = "1234"

if input_username == username and input_password == password:
    print("4. 🔓 Login Successful")
else:
    print("4. 🔒 Login Failed")

# 🚦 5. Traffic Light System using if-elif
signal = "Red"

if signal == "Red":
    print("5. ⛔ STOP! Light is Red.")
elif signal == "Yellow":
    print("5. ⚠ WAIT! Light is Yellow.")
elif signal == "Green":
    print("5. ✅ GO! Light is Green.")
else:
    print("5. ❓ Invalid signal")

# ⚙ 6. Short hand if-else (Ternary) - Check number is even or odd
num = 7
print("6. ✅ Even") if num % 2 == 0 else print("6. 🔢 Odd")

# 🛑 7. Using 'not' operator - Check if user is not blocked
is_blocked = False

if not is_blocked:
    print("7. ✅ User is allowed to access")
else:
    print("7. 🚫 User is blocked")

# 📦 8. 'pass' statement when feature is under development
feature_enabled = True

if feature_enabled:
    pass  # 👨‍💻 Feature will be added later

print("8. 🧪 Feature is under construction (using pass)")

# 🔄 9. Compare 3 numbers to find the greatest
a, b, c = 15, 20, 10

if a > b and a > c:
    print("9. 🔢 A is the greatest")
elif b > c:
    print("9. 🔢 B is the greatest")
else:
    print("9. 🔢 C is the greatest")

# 🎫 10. Check discount eligibility based on age (Nested + and)
user_age = 65
is_member = True

if user_age >= 60:
    if is_member:
        print("10. 🎉 Eligible for senior citizen member discount")
    else:
        print("10. ✅ Eligible for senior citizen discount (non-member)")
else:
    print("10. ❌ No discount available")































































































































































































































