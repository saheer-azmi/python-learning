#1:Python Lists///////////////////////////////////////////////////////////////
mylist = ["apple", "banana", "cherry"]

#👉:Lists are used to store multiple items in a single variable.
#👉:list ek container hai jisme Hum multiple values ek sath store kar skte hai :

#👉:Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#👉:Lists are created using square brackets:

#example:

num=[10,20,30,40,50]
print(num)

fruits=["apple","mango","papaya"]
print(fruits)


thislist = ["apple", "banana", "cherry"]
print(thislist)


#2👉:list properties ://///////////////////////////////////////////////////////////

#1:ordered 

#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#items ka fixed order hota hai - output hamesa  same order me ayega 
#If you add new items to a list, the new items will be placed at the end of the list.
 

fruits=["apple","banana","mango"]
print(fruits)                         #output haesa same order me ayega :



#2:Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#list ko change kar skte hai :

city=["patna","delhi","punjab"]
city[2]="mumbai"
print(city)

name=["saheer","arham"]
name[0]="khan"
print(name)


num=[1,2,3]
num[1]=4
print(num)


#3:Allow duplicates:///////////////////////////////////////////////////

#lists can have items with the same value:
#same value multiple baar aa skta hai 

name=["saheer","azmi","saheer"]
print(name)


#4:List Length//////////////////////////////////////////////////////////////

#To determine how many items a list has, use the len() function:
#kitne item hai list me uske liye len ka use karte hai :

name=["saheer","azmi","arham"]
print(len(name))




#5:List Items - Data Types///////////////////////////////////////////////////////
#List items can be of any data type:
#list me different types store ho skte hai :

#Example
#String, int and boolean data types:

types=[20,"saheer",True,8.9]
print(types)


#6:type() function ///////////////////////////////////////////////////////////////
#ye batata hai variable ka type kya hai 
#From Python's perspective, lists are defined as objects with the data type 'list':

#<class 'list'>

fruits=["banana","apple"]
print(type(fruits))



#7:list () constructor ////////////////////////////////////////////////////////////////////
#It is also possible to use the list() constructor when creating a new list.
#list banane ka dusra tareeka 

name=list(("saheer","azmi","arham"))
print(name)


#double bracket use hota hai ((""))
#kyunki andar tuple ja rha hai 


#FINAL SUMMARY :✅

#LIST=COLLECTION
#ORDERED=ORDER FIX 
#CHANGEABLE =EDIR KAR SKTE HAI 
#DUBLICATE ALLOWED 
#LEN()=LENTH
#LIST ME MULTIPLES DATA TYPE
#TYPE()=TYPE CHECK
#LIST()=CONSTRUCTOR



#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.






#1:Access List Items /////////////////////////////////////////////////////////////

#👇:you can acess list items by referring to the index number.
#👇:list ke items ko acess karne ke liye hum index number use karte hai :
#👇:index hamesa 0 se start hota hai 

#Examples:👇

fruits = ["apple", "banana", "cherry"]
print(fruits[2])

names=["saheer","arham","talha"]
print(names[2])



#2:Negative Indexing ✅ //////////////////////////////////////////////////////////////
#Negative indexing means start from the end
#negative indexing ko hum piche se count karte hai :
#-1 refers to the last item, -2 refers to the second last item etc.

#Examples:👇
#Print the last item of the list:

names=["saheer","arham","talha"]
print(names[-2])
print(names[-0])

fruits=["apple","mango","orange"]
print(fruits[-2])


#3-range of indexes (slicing)✅: /////////////////////////////////////////////////////
#you can specify a range of indexes by using start:end
#hum range me items niakl skte hai using start:end

fruits=["apple","mango","papaya"]
print(fruits[0:2])

#rule:👇
#start include hota hai 
#end include mhi hota hai 

#👉:0:3-0,1,2
city=["patna","delhi","goa","mumbai","kolkata"]
print(city[0:3])

#shortcut:

name=["saheer","talha","arham","arshad"]
print(name[:3])   #start se 

#Remember that the item in index 4 is NOT included

name=["saheer","talha","arham","arshad"]
print(name[3:])    #end tak

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third



#4-Range of negative indexes ✅: ///////////////////////////////////////////////
#you can also use negative indexes in slicing :
#slicing me negative index bhi use kar skte hai :

name=["saheer","arham","talha","arshad"]
print(name[-3:-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

fruits=["apple","mango","papaya","melon","kiwi","cheery"]
print(fruits[-4:-2])




#5:check if item exists :  /////////////////////////////////////////////////////
#to check if an item exists in a list ,use the in keyword.
#list me koi item ha ya nhi hai check karne ke liye in keyword use karte hai :

#Basic example :👇
fruits=["apple","banana","papaya"]
if "apple" in fruits:
    print("yes apple in fruits")


students=["adil","arham","talha"]
if "saheer" in  students:
    print("saheer present in class")


fruits=["apple","mango","papaya"]
if "lemon" in fruits:
    print("yes lemon in this list")
else:
 print("no lemon is not persnt in this list")


#example:👇
#Not in (important):
#use not in to check if item does Not exist
#agar check karna ho ki item list me mhi hai, to not in ka use karo:


fruits=["apple","mango","orange"]
if "grapes" not in fruits:
   print("item not present")


#real life example (interviews):
marks=[90,40,50,33]
if 33 in marks :
   print("pass")

num=[10,20,30]
if 40 not in num:
   print("yes")
else:
   print("no")



#1:Python - Change List Items✅ //////////////////////////////////////////////////////
#Change Item Value
#To change the value of a specific item,by using its index number:
#list ke kisi ek item ko change karne ke liye uska index use kar skte hai :

#Example :👇
fruits=["apple","mango","orange"]
fruits[2]="mango"
print(fruits)

name=["saheer","arham","dilshad"]
name[1]="talha"
print(name)


#2:change a range of item values :✅
#you can multiple items usinhg slicing 
#ek sath multiple items chnage karne ke liye range (slice )ka use karte hai:

#Examples:👇
fruits=["apple","banana","mango","papaya"]
fruits[1:3]=["orange","kiwi"]
print(fruits)

#📌example (1 item se replace):
fruits=["apple","mango","banana"]
fruits[1:3]=["papaya"]
print(fruits)

name=["saheer","arham","afroz"]
name[1:2]=["arshad","tahseen"]
print(name)


#3:short insert :✅
#use inseert ()add item at a specific postion
#list me kisi specific jagah pe item add karne ka liye insert () use karte  hai 

#📌 syntax :
#list:insert (index,value)

#📌Example :
fruits=["apple","mango","orange"]
fruits.insert(1,"orange")
print(fruits)

#smjho:
#👉index 1 pe new item add hua 
#👉 baki items right shift hogya


#✅Difference (important):

#method                           work
#fruits[1]="x"             replace karta hai 
# fruits.insert(1,"x")     beech me add karta hai 



#final summary 🧠:
#index use -single value change 
# slicing -multiple change
# insert ()-beech me add
# slicing me item kam/zada hota hai 

#📌:mini test
a=[10,20,30,40]
a[1:3]=[100]
print(a) 

b=[10,20,30]
b[1:2]=[50]
print(b)


a=[10,20,30,40]
a[1:3]=[29,33]
print(a)





#1:Python - Add List Items ✅  /////////////////////////////////////////////////
#Append Items
#To add an item to the end of the list, use the append() method:
#append () list ke last me item add karta hai 


#Using the append() method to append an item:

fruits=["apple","banana","mango"]
fruits.append("kiwi")
print(fruits)         #kiwi last me add hogya

name=["saheer","arham","talha"]
name.append("arif")
print(name)           #arif last me add hogya

#👉:important

#👉:append () sirf 1 item add karta hai 


city=["patna","delhi","kolkata","mumbai"]
name.append(["gujrat","punjab"])                 #ye list ke andar list ban gaya(nested list):
print(name)                      



#2:insert items ✅:
#insert () adds item at a specific postion
#insert () kisi specific index pe item add karta hai 



#📌syntax:
#list.insert(index,value)

#📌Example :


fruits=["apple","mango","kiwi"]
fruits.insert(1,"papaya")
print(fruits)

name=["saheer","arshad","talha"]
name.insert(0,"arham")
print(name)



#3:Extend items ✅
#extend() adds elements of another list to current list
#extend () dusri list ke sab items ko add karta hai 

#📌:Example-

fruits=["apple","mango","kiwi"]
more=["banana","orange"]
fruits.extend(more)
print(fruits)  

#ak ak item add hua 

#difference (Append vs Extend )
#interviews Questions:
#append 
a=[1,2]
a.append([3,4])
#[1,2,[3,4]]

#Extend
a=[1,2]
a.extend([3,4])
#[1,2,3,4]       


#4:Add Any iterable 
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Extend()can add any iterable (lis,tuple,set,string)
#extend() sirf list nhi,balki koi bhi iterable (tuple,set,string)add kar skta hai 



#📌Example:

#1:tuple add karna 
a=[1,2]
b=(3,4)
a.extend(b)
print(a)


#2:string add karna 
a=["saheer","arham"]
a.extend(["nikhil","arjun"])
print(a)

#strig ke charcater alag alag add hote hai 

#3: set add karna 

a=[1,2]
b={3,4}
a.extend(b)
print(a)


#final summary 🧠:


#method                   #work

#append ()         last me 1 item add
#insert ()         specific index pe add
#extend ()         multiple items add
#extend(iterable)  list,tuple,string,sab add

#differnece :
#👉append()=ek item
#👉extend()=tod ke sab add


#Final Test 
a=[1,2]
a.append([3,4])
a.extend([5,6])
print(a)





#Python - Remove List Items
#Remove Specified Item
#The remove() method removes the specified item.



#1:Remove specified item (remove())✅//////////////////////////////////////////
#remove () deletes a specific value (item)from the list
#remove () list me se kisi value ko delte karta hai(value dekar)

#📌Example:
fruits=["apple","banana","mango"]
fruits.remove("banana")
print(fruits)

name=["saheer","sarikh","dilshad"]
name.remove("saheer")
print(name)


#👉:important
#👉:agar same item 2 baar ho toh

name=["saheer","arham","talha","arham"]
name.remove("arham")
print(name)


#2:Remove Specified Index
#The pop() method removes the specified index.
#remove item using index
#index dekar item delte karta hai 

#example :(A) pop()

a=[10,20,30,40]
a.pop(2)            #index 2=30 remove
print(a)

name=["saheer","arham","talha"]
name.pop(2)
print(name)

#📌important :
#👉:agar index na do :
a.pop()
#👉:last item remove hota hai 


#(B)del keyword
#Deletes item using index (or whole list):
#del se index ya porri list delete kar skte hai 


name=["saheer","arham","arshad"]
del name[1]
print(name)


#:👇 whole list delete
city=["patna","delhi","jaipur"]
del city

#👉:ab list exist hi nhi karegi


#3.clear the list(clear()) ✅
#remove all items ,but still exists
#list ke saree item hata deta hai,per list khali rah jata hai

name=["saheer","arham","talha"]
name.clear()
print(name)


#difference (Important):

#Method           work                   simple language

# remove       value se delete           ("banana")=naam se banda hatao
# pop()        index se delete            (1)=position se banda bhagaao 
# del          index ya list delete       
# clear ()    sab htao (list empty)      sabko bhagaa do 




#mini interview level Questions :

#Q1?:
a=[1,2,3,4,3]
a.remove(2)
print(a)

#Q2?:
a=[10,20,30,40]
a.pop(2)
print (a)

#Q3?:
a=[10,20,30]
del a[1]
print (a)

#Q.4?

a=[1,2]
a.clear()
print(a)







#👉:Python - Loop Lists ✅

#loop kiya hota hai ?

#👉A loop is used to repeat a task multiple times automatically :
#👉loop ka matlab hai ek hi kaam ko baar-baar automatically karna

#📌Example (real -life):
#👉 agar tujhe 100 baar "hello"print karna hai 
#❌bina loop -100 baar likhna padega 
#✅loop- 1 line me ho jayega 


#loop kyu use karte hai ?
#👉time bachne ko
#👉repetitive kaam automate karne ke liye
#👉data (list) ke har item pe kaam karne ke liye 

#loop kab use karte hai ?
#jab list ho 
#jab multiple data ho
#jab same kaam repeat ho


#interview me kaise puchte hain?
#👉"print all items of a list"
#👉"find even numbers in list"
#👉"sum of list"
#👉"search items in list "


#1:Loop Through a list (for loop)✅
#use for loop to iterate over each item
#for loop list ke haar item pe ek-ek karke chlta hai......



fruits=["apple","mango","banana"]
for fruit in fruits:
  print(fruit)


#2:Loop through index numbers  
#jab hume list ke index number(0,1,2,3.....)ke basis per loop chalana ho,tb hum range ()use karte hai :
#when you want to loop through a list using index postions ,you use:
#for i in range(len(list)):
#len(list)-gives total element
#range()-creates numbers from 0 to length -1
#i-index number


#📌Example 1:
fruits=["apple","banana","mango","chery"]
for fruit in range (len(fruits)):
   print(fruit)

#yha sirf index print ho rha hai

#📌Example 2:
fruits=["apple","mango","banana"]
for i in range (len(fruits)):
   print(i,fruits[i])

#i=index numder(0,1,2...)
#fruits[i]=us index ka value

fruits=["apple","mango","banana"]
for fruit in range(len(fruits)):
   print(fruits[fruit])


#📌Example 3:(real use case):
marks=[20,10,40]
for i in range(len(marks)):
   print("subject",i+1,"marks:",marks[i])


#important difference :
#method                    use
#for i in list         sirf value
#for i in              index+value
#range(len(list))


#shortcut (Best way):
#enumerate()

fruits=["apple","mango","banana"]
for i ,value in enumerate(fruits):
   print(i,value)



#👇📌interview Question:

#Q1:list ka index kaise acess karte hai?
#👉 for i in range (len(list))


#Q2:range (len(list)) kyu use hota hai ?
#👉 kyunki ye 0 se list ke last index tak numbers generate karta hai...



#1.Reverse loop (ulta loop)✅///////////////////////////
#loop from last index to first using negative step
#list ko piche se agea print krna 

#👉:method 1:range()se

fruits=["apple","banana","mango","kiwi"]
for i in range (len(fruits)-1,-1,-1,):
   print(fruits[i])


#easy method :(Best)
fruits=["apple","mango","banana"]
for item in reversed (fruits):
   print(item)

#ye zada clean aur professional hai :



#2:step loop (jump loop)
#har element skip karke print karna  (jaise 2-2 step)

#Example :✅
numbers=[10,20,30,40,50,60]
for i in range (0,len(numbers),2):
   print (numbers[i])


#Reverse +step Together 
numbers=[10,20,30,40,50,60]
for i in range (len(numbers)-1,-1,-2):
   print(numbers[i])


#📌:REAL LIFE USE EXAMPLE:
marks=[80,70,60,50,]
for i in range(0,len(marks),2):
   print("checking marks:",marks[i])


#📌:Using a While Loop
#You can loop through the list items by using a while loop.
#A while loop runs as long as the condition is True :
#while loop tab tak chlta hai jab tak condition shi hai,tab tak code repeat hota hai 
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.

#📌Basic syntax:
#while condition:
   #code


#Example 1 (Basic):

i=0
while i<5:
   print(i)
   i=i+1

#👉 important Rule:
#👉i=i+1 (increment)zaroor karo warna loop infinite ho jayega ❌


#infinite loop Example (galti)
#i=0
#while i <5:
  #print(i)

#👉ye kabhi rukega ni 


#while loop with list
#Example 2:list print using while

fruits=["apple","mango","banana"]
i=0
while i<len(fruits):
   print(fruits[i])
   i+=1



#Reverse while loop

numbers=[10,20,30,40]
i=len (numbers)-1
while i>=0:
   print(numbers[i])
   i-=1


#while loop + break 

i=0
while i <10:
   if i ==5:
      break
   print(i)
   i+=1


#while loop with continue 

i=0
while i<5:
   i +=1
   if i ==3:
      continue 
   print(i)


#Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists:

#list comprehension kya hota hai ?

#short aur smart tarika list banana ka (1 line me)
#A concise way to create list in one line


#BASIC syntax :
#new_list=[expression for item in iterable]

#example 1:
numbers =[1,2,3,4]
new_list=[x for x in numbers]
print(new_list)


#example 2(square):
numbers=[1,2,3,4]
squares=[x*x for x in numbers]
print(squares)



#example 3(conditions):
numbers=[1,2,3,4,5,6]
even =[x for x in numbers if x %2==0]
print(even)


#Example 4 (if-else)

numbers=[1,2,3,4]
result=["even" if x%2==0 else "odd" for x in numbers]
print(result)


#normal loop vs list comprehension 

#❌normal way 

numbers =[1,2,3]
result=[]

for x in numbers:
   result.append(x*x)


#List Comprehension ✅//////////////////////////////////
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example:

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement with a conditional test inside:


#list comprehension kya hota hai ?
#👉A concise way to create lists in a single line
#👉 list banane ke  sort aur smart tarika (1 line me )


# 📌:Basic syntax /////
#👉new_list=[expression for item in iterable]

#Example:


#normal example :

numbers=[1,2,3,4]
newlist=[]
for x in numbers:
   newlist.append(x)
print(newlist)


#Ab same ka short form (list comprehension):
numbers=[1,2,3,4]
new_list=[x for x in numbers]
print(new_list)


#Ab thora interseting :
numbers=[1,2,3,4]
new_list=[x*x for x in numbers]
print(new_list)

#even numbers :

numbers=[1,2,3,4,5]
new_list=[x for x in numbers if x%2==0]
print(new_list)

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement with a conditional test inside:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]   #ye origional list hai data 
newlist = []                                         #empty list banye jisme result store hoga 
for x in fruits:    
   if "a" in x:                       #check karo kia "a" hai fuit me ?
    newlist.append(x)                    

print(newlist)


#With list comprehension you can do all that with only one line of code:

#Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#differnecs samjho:
#Normal                      list comprehension

#4 lines                  1 line
#easy to understand       short &fast
#begineer friendly         interviews +pro level



#2:The Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.

#yaad kaise rakhe:
#[kya banana hai for kha se lena hai if kab lena hai]

#one real example :
numbers=[1,2,3,4]
new_list=[x for x in numbers if x%2==0]
print(new_list)



#3:condition kia hota hai ?
#condition filters item(selects only some elements)

#👉kaun sa item lena hai ,kaun sa nhi

#different condition Examples:

#Example 1:Even numbers
[x for x in numbers if x%2==0]         #only even 

#Example 2:greater than 2 
[x for x in numbers if x>2]                #only grater than 2

#example 3:string me check                  
fruits=["banana","apple","kiwi"]
[x for x in fruits if "a" in x]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)


#without condition :
[x for x in numbers]
#👉sab item lelo(no filter)


#if -else condition (advance)
numbers=[1,2,3,4]
result=["even"if x%2==0 else "odd" for x in numbers ]
print(result)


#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
#iterable wo cheez hoti hai jisme multiple items hote hain aur jinhe hum ek-ek karke acess kar skte hai (loop ke through )...

#simple line :
#"jis cheez ko for loop me use kar skte ho - wo iterable hai "

#xample of iterable :
mylist=[1,2,3,]     #list
my_tuple=(4,5,6)    #tuple
my_string="hello"   #string 
my_set={7,8,9}      #set


#iterable ka use (loop me ):
fruits=["apple","banana","mango"]
for item in fruits:
   print(item)

#string bhi iterable hota hai :
name="saheer"
for ch in name:
   print(ch)

#matlb string ke charcters bhi ek-ek karke milta hai 


#iterable vs iterator (thoda advance but important):

#📌iterable :
#jisme loop chal skta hai 
#example:list,string

#📌iterator:
#jo actually next value deta hai (behind the scenes):

#Easy method :
#iterable=container
#iterator=jo ek ek item deta hai 


#list comprehension me iterable 
numbers=[1,2,3,4,5]
new_list=[x for x in numbers]

#numbers=iterable
#x=ek-ek value uth rahi hai 

#❌non-iterable example:
#You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
#error ayega because:
#int iterable nhi hota 



#interviews me kaise bole ?

#simple:
#iterable is an object which can be looped over,like,list,tuples,string,it allows accessing elements one by one.""

#mini interviews Questions :

#Q.1 iterable kya hota hai ?

#ANS- LOOP KE THROUGH JISME ITEMS KO ACESS KAR SKTE HAI 

#Q.2 kya string terable hai ?

#ans-Haan (character by character)

#Q.3 kya integer iterable hai ?

#ans-nhi 

#Q.4 Example of iterable?
#ans-list ,tuple ,string ,set

#real life 

#iterable=plate me rakhe hue biscuit 
#loop =tum ek-ek biscuit uthake kha rhe ho


#Example (list -iterator )

my_list=[10,20,30]
x=iter(my_list)   #👉iter () kya karta hai? iterable ko iterator me convert karta hai 
print(next(x))
print(next(x))
print(next(x))    #next () ka use 


#loop ke andar kia hota hai ?

my_list=[1,2,3]
for i in my_list:
   print(i)

#internally python ye karta hai:
it=iter(my_list)
print(next(it))
print(next(it))
print(next(it))

#👉matlab : for loop =automatic next() calling


#3:range () bhi iterable hai 

x=range(5)
for i in x :
   print(i)

#samjho :
#range(5)=iterable 
#ye numbers store nhi karta 
#ye ek-ek karke genrate karta hai



#Expression kya hota hai 

#an expression is any piece of code that produces a value
#expression woh hota hai jo kuch calculate karke result deta hai ..


#📌simple examples:
#5+3 = 8
#10*2 = 20
#"x" +"y"= "xy"

#Expression vs statement 
x=5       #❌statement(assigment)
x+2       #✅expression (value=7)

#rule :
#expression= value deta hai 
#statement=kam karta hai (assign,print etc.)


#2.list comprehension  me expression :

#[expression for item in iterable]

#yaha expression =kya output banana hai 

#Example 1(normal)::
x=[i for i in range(5)]
print(x)

#👉 expression i 


#example 2 (expresssion change karo)
x=[i*2 for i in range (5)]
print(x)

#👉Expression =i*2


#example 3:(condition ke sath):

x=[i for i in range (10) if i %2==0]

#👉Expression =i
#👉condition=if i %2==0


#interviews me kaise bole ?

#ans="expression is the part of list comprehension that defines what value will be added to the new list:"


#✅:Python - Sort Lists...////////////////////////////////

#1:Sort List Alphanumerically...
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#sorts list in ascending order(A-z or 0-9)
#list ko chote se bada arrange karta hai 


#Example:

a=[5,6,8,9]
a.sort()
print(a)

name=["saheer","aman","arham","mallick"]
name.sort()
print (name)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#sort () origional list ko change karta hai ..
#return none karta hai 

#Sort Descending
#To sort descending, use the keyword argument reverse = True:
#reverse order(big-small)
#bade se chote arrange 

#Examples :

a=[5,2,9,1]
a.sort(reverse=True)
print(a)



#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first):
#jab hum apne hisab se sort karna chacho:


#Examples 1:(absolute value):
a=[-10,-2,5,3]
a.sort(key=abs)
print(a)


#example 2(string lenghth):
a=["apple","kiwi","banana"]
a.sort(key=len)
print(a)


#4:Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

#👉capital /small ignore karega :

#🧠example:
a=["banana","Apple","cherry"]
a.sort(key=str.lower)
print(a)


name=["saheer","Arham","khaN"]
name.sort(key=str.lower)
print(name)



#5:Reverse order (shortcut)
#list ko ulta karna (sort nahi,bas reverse):
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.


#eaxmple :

a=[1,2,3]
a.reverse()
print(a)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#different very important :

#method       work
#sort       arrange karta hai
#reverse    ulta karta hai 


#6:sorted () function (interviews)
#new list banata hai (origional change nhi karta)

#📌example:
a=[5,2,9]
b=sorted(a)
print(a)
print(b)


#interviews answer:

#="sort() modifies the origional list,while sorted () returns a new sorted list:"








#Python - Copy Lists ✅//////////////////////////
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#copy list means creating a new list with same elements :
#copy list matlab ek nayi list banana jisme same data ho:

#example:🧠
a=[1,2,3]
b=a
b[0]=100
print(a)


a=[2,6,7]
b=a
b[1]=22
print(a)


#Use the copy() method
#You can use the built-in List method copy() to copy a list.

#📌syntax:
b=a.copy()

#example :


a=[1,3,5]
a.copy()
print(a)

a=[1,3,4,5,7]
b=a.copy()
b[0]=100
print(a)
print(b)

#ab dono alag list hain..
#ek change -dusra safe




#Use the list() method /////////////
#Another way to make a copy is to use the built-in method list().


#📌syntax:
b=list(a)

#example:

a=[1,2,3]
b=list(a)
b[1]=200
print(a)
print(b)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)




#Use the slice Operator
#You can also make a copy of a list by using the : (slice) operator.


#📌syntax:

b=a[:]


#example:

a=[1,2,3]
b=a[:]

b[2]=999
print(a)
print(b)

#pura list copy 


#difference interviews:

#method             kaam
#a=b              ❌refernce 
#copy()            ✅real copy
#list()            ✅real copy
#[:]                ✅real copy


#Python - Join Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
#joining lists means combining two lists into one 
#do list ko milkar ak list banana:


#📌syntax :
c=a+b

#🧠Examples:
a=[1,2]
b=[3,4]
c=a+b
print(c)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#👉+=dono list ko jod deta hai 
#👉 new list banata hai

#methpd 2 :using extend ()

#📌syntax :
a.extend(b)


#example :🧠
a=[1,2]
b=[3,4]
a.extend(b)
print(a)

#extend() origional list ko change karta hai:


#method 3:loop use karke 

#example :

a=[1,2]
b=[3,4]
for i in b :
   a.append(i)
print(a)

#interviws:
#"we can two list using +operator,extend()method,or by looping"







#List Methods
#Python has a set of built-in methods that you can use on lists.

#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

