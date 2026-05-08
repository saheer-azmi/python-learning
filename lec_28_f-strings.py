#Topic=f-strings
#Author="saheer azmi"
#Date=2026



#code 1:
letter="hey my name is {} and i am from {}"
country="india"
name="saheer"

print(letter.format(name,country))


#code 2:
letter="hey my name is {1} and i am from {0}"
country="india"
name="saheer"

print(f"Hey my name is {name} and i am from {country}")


#WS3SCHOOL:

#Python String Formatting ✅
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

#Before Python 3.6 we had to use the format() method.

#1:F-STRINGS: ✅

#f-strngs kya hota hai ?
#👉An f -strings is a way to format stings by directly putting variables inside {}.
#👉f-strings me hum variables ko directly string ke andar likh skte hai {}me 
#👉easy+fast+modern method

#Example : 📌

name="saheer"
age=20
print(f"my name is {name} and i am {age} years old")

#Rule :
#👉"f"lagana zaoori hai string ke aage 
#👉{}ke andar variable 

name="saheer"
age=20
print(f"my name is {name} and i am {age}years old ")


#2:placeholder&modifiers ✅

#👉placeholder{}
#👉modifiers=formating rules

#{}=jaha value ayegi 
#modifiers=value ka format change karna 


#Exaple :📌

price=99.4564
print(f"price is {price:.2f}")     #.2f=2 decimal tak show karega 

price=44.2082
print(f"Ac price is {price:.2f}")


#3:PERFORM OPERATINS IN F-STRING :✅
#YOU CAN PERFORM OPERTAINS INSIDE {}
#{} KE ANDAR CALCULATIONS BHI KAR SKTE HO 

#Example ❌:
a=10
b=5
print(f"sum is {a+b}")

a=3
b=3
print(a+b) 


#4:Execute function in f-string  ✅


#👉you can call functions inside {}
#👉function bhi run kar skte ho 

name="saheer"
print(f"uppercase:{name.upper()}")

name="azmi"
print(f"uppercase:{name.upper()}")


#5:more modifiers ✅

num=5
print(f"{num:03}")

#total 3 digit 
#0 se fill krega 


#6:string format () method ✅
#👉old method to format string uisng .fotrmat()
#👉f-string se phle ye use hota hai 

#Example 📌:

name="saheer"
age=20
print("my name is {} and age is {}".format(name,age))

#multiples value :


print ("i love {} and {}".format("python","java"))






#7:Index Numbers () ✅
#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
#Aceess values by position 
#index ke through value control


#Example ❌
print("i love {0} and {1}".format("python","Html"))

#Also, if you want to refer to the same value more than once, use the index number:

#Example ❌
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))



#without index numbers :

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item number {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#with index numbers :

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#Named Indexes  ✅
#You can also use named indexes by entering a name inside the curly brackets {carname}, 
#but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
#use names instead of index 
#variable name se access


#Example 📌:

print("my name is {name}".format(name="saheer"))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


#interviews level summarry :

#👉f-string=modern +fast
#👉{}=placeholder
#👉calculation possible 
#👉function call posible 
#👉modifers =formating 
#👉.format()=old method 

