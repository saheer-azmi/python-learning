import time #time module import karo

#Time ko specific format me convert karo:
timestamp=time.strftime('%H:%M:%S') #hour:minnute:second:

print(timestamp)

timestamp=time.strftime('%H') #sirf hour 
print(timestamp)

timestamp=time.strftime('%M') #sirf minute
print(timestamp)

timestamp=time.strftime('%S') #sirf second
print(timestamp)



hour = int(time.strftime('%H'))
if hour<12:
   print("good morning ")
elif hour<17:
   print("good afternoon ")
elif hour<21:
   print=("good evening")
else:
   print("good night")


#final code:
import time 
name=input("enter your name:")
hour=int(time.strftime('%H'))

if hour<12:
   print("Good morning",name)
elif hour<17:
   print("Good Afternoon",name)
elif hour<21:
   print("Good evening",name)
else:
   print("good night",name)
#optional:current time print kr rha hu:
current_time = time.strftime('%H:,%M:,%S:')
print("current time:",current_time)







#def ka matlab hota hai function define karna:
import datetime

def greet(name):
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute

    print(f"Current Time: {hour}:{minute:02d}")

    if hour < 12:
        print("Good Morning " + name)
    elif hour < 17:
        print("Good Afternoon " + name)
    elif hour < 21:
        print("Good Evening " + name)
    else:
        print("Good Night " + name)

name_input = input("Enter your name: ")
greet(name_input)




