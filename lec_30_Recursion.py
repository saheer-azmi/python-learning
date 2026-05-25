#Topic=Recursion
#name=saheer azmi 
#date=2026


#Recursion kia hota hai ?
#👉recursion is techinque where a function calls itself to solve a program.
#👉recursion matlab function khud ko baar-baar call karta hai jab tak kaam complete na ho jaye..


#📌example sabse basic :

# def hello ():
#     print("hello")
#     hello()
# hello()     #👉ye infinite challega❌(kabhi rukega nahi )


#👉:islie 2 chiz sabse zaruri hoti hai....

#2.Base case(stopping condition ):✅

#👉 condition where recursion stops:
#👉jab function ruk jata hai


#🔁Recursive case :
#👉where function calls itself.
#👉jab function khud ko dobara call karta hai 



#perfect example (countdown):

def count(n):      #ek function banaya jiska nam count hai
    if n==0:        #Base case
        return 
    print(n)
    count(n-1)      #Recursive case
count(5)            #program start yhi se hota hai (n=5 hogya)



#example 2 (Reverese print):
def count(n): 
    if n ==0:       
        return 
    count(n-1)   #recursive call pehle
    print(n)     #print baad me 
count(4)


#Golden rule (yaad rakh):

#position        output
#print phle    reverse (5-1)
#print baad me  normal (1-5)

#jab print recursive call ke bad hota hai,
#to values wapas aate time print hoti hain,isliye output reverse ho jata hai ...


#har line ka role smjho :

#👉lines                 kaam 
#👉def count(n)        function banaya
#👉if n ==0            stop condition(base case)
#👉print (n)             value print
#👉count(n-1)            khud ko dubara call 




#Fibonacci Sequence
#👉The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:
#👉each number=sum of previous two numbers 
#👉har numbers =pichle 2 numbers ka sum 
#0, 1, 1, 2, 3, 5, 8, 13, ...
#👉The sequence continues indefinitely, with each number being the sum of the two preceding ones.
#👉We can use recursion to find a specific number in the sequence:
#formula=f(n)=f(n-1)+f(n-2)
#📌code example :

def fib (n):
    if n==0:    #base case 
        return 0 
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)  #recursive 
print (fib(6))
    

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))



#4:Recursion with lists :
#👉using recursion to process list elements .
#👉list ke elements ko recursion se process karna.

#example 📌:

def sum_list(lst):
   if len(lst)==0:
      return 0
   return lst[0]+sum_list(lst[1:])
print(sum_list([1,2,3,4]))


#Recursion Depth Limit
#Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

#Example
#Check the recursion limit:

import sys
print(sys.getrecursionlimit())


#If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:

#Example
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

#Recusion kya hai ?
#👉function calling itself 

#base case kyu zarori hai ?
#👉=infinte loop rokne ky liye '

#fibonacci ka logic
#f(n)=f(n-1)+f(n-2)


