#Topic :import time 
#author:saheer azmi
#Date=2026


#✅:import time kia hota hai ?
#👉time module is used to work with time (current,time,delay,etc.)
#👉time ak module hai jise hum:current time dekh sakte hai.
#👉delay (rukna) kara ske hai 


#2:current time kaise nikalte hai ?
import time 
t=time.localtime()
print(t)

#ye pure time ka data deta hai (complex format):


#important part (hour nikalna ):
import time 
hour=time.localtime().tm_hour
print(hour)

#samjho:
#👉time.localtime()-current time deta hai
#👉tm._hour-sirf hour (0-20)nikalta hai

#3:✅Good Morning /Afternoon /night Logic 
import time
hour=time.localtime().tm_hour
if hour <12:
    print("Good Morning")
elif hour <18:
    print("good afternoon")
else:
    print("Good Night")

#4:practice codes :

import time
hour=time.localtime().tm_hour
print("current hour:",hour)

#code 2 ✅
import time
hour=time.localtime().tm_hour
if hour<12:
    print("Morning ho rha hai bhai")
else:
    print("sham  ya rat hogya bhai ")

#codes 3: Good morning /Afternoon /night Logic :

import time 
hour =time.localtime().tm_hour
if hour<12:
    print("Good mroning saheer")
elif hour<18:
    print("good afteernoon saheer")
else:
    print("good night saheer")

#4.Practice codes (important):

#✅code 1:
import time 
hour =time.localtime().tm_hour
print("current hour:",hour)


#✅code 2:
import time 
hour=time.localtime().tm_hour
if hour<12:
    print("Morning ho rha hai bhai")
else:
    print("sham ya rat hogya")

#code 3 (custom message):
import time 
hour=time.localtime().tm_hour
if hour < 12:
   print("good morning saheer ")
if hour < 18:
    print("good afternoon saheer")
else:
    print("good night saheer")

#interviews Questions :
#Q1.time.localtime()kya hota hai ?
#👉current time deta hai 

#Q2.tm_hour kya hota hai?
#👉hour nikalta hai (0-23)

#Q3:import time kyu use karta hai ?
#👉time nikalne ky liye 
