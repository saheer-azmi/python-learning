#TOPIC:EXPECTIONS HANDLING 
#AUTHOR:SAHEER AZMI 
#DATE :2026

#1👉:Expections handling kya hota ?✅
#👉:An exception is an error that occurs during program excution  and stops that program.
#👉:jab program chal rha hota hai aur beech me error aa jaye jissee program crash ho jaye - usko expections bolte hain....


#Example ❌(Error without handling ):
# a=10
# b=0
# print(a/b)

#problem crash hogya yhi problem hai :


#2👉:Expections handling kya hai ? ✅
#👉:Error ko control karna taaki program crash na ho.
#👉:Handling errors so the program continues running instead of crashing 


#3:try-expect ka basic use : ✅

#try:
    #risky code 
#expect :
#error handle code


#Examples:✅:


try:
    a=10
    b=0
    print(a/b)
except:
    print("Error aa gya but handle ho gaya")


#program crash nhi hua :



#4:step-by-step samajh : ✅

#👉Flow :

#1:try block me code chalega 
#2:agar error aya -jump to expect 
#3:Expect handle karega 



#5:specific error handle karna ✅
#Galat (general): ❌
#except:
#sahi ✅:
#except ZeroDivisionError

#Example :

try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
  print("zero se divide nhi kar sakte")


#6:multiple expections handle karna ✅

try:
    num=int(input("Enter number:"))
    print(10/num)
except ValueError:
    print("number galat dala")
except ZeroDivisionError:
    print("Zero se divide nhi hota")



#7:else block kya hota hai ? ✅

#Runs only if NO error 

try:
    a=10
    b=2
    print(a/b)
except:
    print("Error")
else:
    print("sab shi chala")




#8:Finally block kya hota hai?
#👉:Always run hota hai (error aaye ya na aaye )
try:
    print("Try block")
except:
    print("error")
finally:
    print("ye hamesa chalega")




#👉:Real-life-example (important):
try:
    age=int(input("Enter age:"))
    print("Age:",age)
    name=(input("Enter your name:" ))
    print("name:",name)
except ValueError:
   print("please valid number dalo")



#👉:sabka combined example :
try:
    num=int(input("Enter number:"))
    result=10/num
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("Result:",result)
finally:
    print("program khatam")




#👉:kab use karte hai?
#👉:use when :

#👉user input le rahe ho
#👉file open kar rhe ho 
#👉Api call kar rhe ho
#👉calculation risky ho 


#👉:kab use nhi krna ?

#👉:simple code jahan error ka chance nhi hai 
#👉:har jagah unnecessary try-except mat lagao 



#ab tera kaam practice :
#bana:
#👉 User se number le
#👉 Agar number galat ho → message
#👉 Agar 0 ho → error handle
#👉 warna 100/num print

