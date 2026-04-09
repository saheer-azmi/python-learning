#EXAMPLE 1:
weather = "rainy"

match weather:
    case "sunny":
        print("Bahut dhoop hai. Chashma lelo 😎")
    case "rainy":
        print("Barish ho rahi hai. Chhata lelo ☔")
    case "cloudy":
        print("Badal chhaye hain. Mausam suhana hai 🌥")
    case _:
        print("Mausam ka pata nahi ❓")

#EXAMPLE 2:

choice=int(input("1.start\n2.setting\n3.Exit\n your choice:"))
match choice:
    case 1:
        print("game starting ")
    case 2:
        print("operating setting...")
    case 3:
        print("exiting gane...")
    case _:
        print("invalid option selected!")


#EXAMPLE 3:
fruit ="mango"
match fruit:
    case"apple"|"mango"|"banana":
        print("this fruit available now:")
    case _:
        print("this fruit not availbale:")

#EXAMPLE 4:
day=input("enter day :")
match day:
    case "monday"|"tuesday"|"wednesday"|"thrusday"|"friday":
        print("college jana padega ")
    case "saturday"|"sunday":
        print("chill day and learn python:")
    case _:
        print("invalid day enterned.")

# Default value:
#(jab koi bhi case match nhi hota ,tab case _: wala block chlta hai; yeh bilqul else jaisa kaam karta hai)
day="friday"
match day:
    case "monday":
     print("start of the week")
    case "sunday":
     print("holiday!")
    case _:
        print("normal Day")

#Combine multiple values-operator(yeh or ke jaisa work krta hai:)
fruit="mango"

match fruit:
    case "apple"|"banana"|"mango":
        print("this fruit is availbale:")
    case _:
        print("this fruit is not available:")

#if statement as  guards - case_if_condition;

age = int(input("Enter your age: "))

match age:
    case _ if age < 18:
        print("Minor  Access Denied")
    case _ if 18 <= age <= 60:
        print("Adult   Access Granted")
    case _:
        print("Senior Citizen  Special Access")


score = int(input("Enter your marks: "))

match score:
    case _ if score >= 90:
        print("Grade: A+")
    case _ if 75 <= score < 90:
        print("Grade: A")
    case _ if 60 <= score < 75:
        print("Grade: B")
    case _ if 40 <= score < 60:
        print("Grade: C")
    case _ if score < 40:
        print("Fail")
    case _:
        print("Invalid Score")