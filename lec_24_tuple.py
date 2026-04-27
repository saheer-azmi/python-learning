#Python Tuples////////////////////////////////////////

mytuple = ("apple", "banana", "cherry")

#Tuple ✅

#Tuples are used to store multiple items in a single variable.

#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

#A tuple is a collection which is ordered and unchangeable.

#Tuples are written with round brackets.

#Tuple kya hota hai ?

#ans-A tuple is a collection of items which is ordered and unchangeable..
#ans-tuple ek list jaisa hota hai 
#ans-per isme data change nhi hota hai (fixed hota hai):

thistuple = ("apple", "banana", "cherry")
print(thistuple)


num=(1,2,3,4,5)
print(num)

#Tuple Items ✅
#👉Tuple items are ordered, unchangeable, and allow duplicate values.

#👉Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#👉tuple ke andar jo item hoti hai unko items kahte hai 

num=(1,2,3,)   #1,2,3,=item hai 


#Ordered...✅
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#items have a fixed order 
#order fix hota hai -index se acess hota hai ..

name=("saheer","arham","talha")
print(name[0])

num=(1,2,3,4)
print(num[2])


#4:Unchangeable...✅
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#tuple cannot change items after creation
#ek baar tuple ban gaya -usko change nhi kar skte hai 

#num=(1,2,3,)
#num[0]=100       #error
#print(num)


#5:Allow duplicates....✅
#Since tuples are indexed, they can have items with the same value:
#tuple are same value multiple times ho skti hai..

name=("saheer","arham","malik","saheer")
print(name)


#6.Tuple lenth... ✅
#👉to determine how many items a tuple has, use the len() function:
#👉kitne items hai -len () se niklta hain

name=("saheer","arham","mallick")
print(len(name))

num=(1,2,3,4,5)
print(len(num))


#Create Tuple With One Item  ✅

#👉To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple..
#👉A tuple with one item must have a comma ,otherwise it is not considered a tuple.
#👉Agar tuple me sirf ak item hai,toh uske bad comma(,)lagana zarrori hai,warna wo tuple nhi hoga..


#Galat Example:❌

num=(7)
print(type(num))

num=(3,)
print(type(num))



#single item tuple=, comma compulsary

#8:Tuple items - Data Types ✅

#Tuple items can be of any data type:
#A tuple can contain items of different data types.
#tuple ke andar alag -alag type ke data store ho sakta hai..

num=(1,"apple",True,4.5)
print(num)



#type() function....✅
#From Python's perspective, tuples are defined as objects with the data type 'tuple':
#the type () function is used to check the data type of a variable ..
#type () function ka use kisi variable ka type check karne ke liye hota hai...


num=(1,3,4,5,)
print(type(num))

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
#The tuple() constructor is used to create a tuple from an iterable..
#tuple ka use kisi iterable (list,string,etc.)ko tuple me convert karne ke liye hota hai...


name=tuple([1,2,3])
print(name)


#example 2: (string - tuple):

name=tuple("abc")
print(name)


#👉🧠interviews line :

#A tuple is an ordered ,immutble collection that allows dublicates values and can store multiple data types...



#Python - Access Tuple Items
#Access Tuple Items
#You can access tuple items by referring to the index number, inside square bracket..
#we can acess tuple items using their index.
#hum tuple ke items ko index number se acess karte hai..

#📌Example:

fruits=("banana","mango","apple")
print(fruits[0])


#2:Negative Indexing
#Negative indexing means start from the end.

#-1 refers to the last item, -2 refers to the second last item etc.

#📌Example :

fruits=("apple","mango","banana")
print(fruits[-1])

#3.Range of indexes (slicing):
#we can specify a range of indexes to get a part of the tuple...
#hum slicing ka use karke tuple ka ek part nikal sakte hai ...


#📌example :

fruits=["apple","mango","orange","kiwi"]
print(fruits[1:3])

#👉start include 
#👉end include

#4:Range of negative 
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
#we can also use negative indexes in slicing.
#hum slicing me negatives index use karke peeche se range le skte hai 


#📌Example:

fruits=["apple","mango","banana","orange","kiwi"]
print(fruits[-4:-1])


#5:check if item exists : ✅
#we can check if an item exists using in keyword..
#hum in keyword se check kar skte hain ki koi item tuple me hai ya nahi....


#📌Example :

fruits=("apple","mango","orange")
if "apple" in fruits:
    print("yes apple in fruits")

#🧠:interviews Questions :
#"tuple items can be accessed using indexing,slicing,and negative indexing,and existence can be checked using 'in' keword."
#tuple=fixed data
#index=adress 



#1:ython - Update Tuples ✅
#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#tuples are immutable,meaning their values cannot be changed directly after creation ..
#matlab tuple banane ke baad uske andar ke values directly change nhi kar skte hai..

#🧠Trick important :
#tuple ko change karne ke liye :👉tuple -list me convert kro
#👉:List update karo 
#👉:Dobara tuple bana lo


#🧠:code example :

x=("apple","mango","banana")

#step 1:convert to list 
y=(list(x))

#step 2:change value 
y[1]="mango"

#step3: convert back to tuple 

x=tuple(y)

print(x)


name=["saheer","azmi","arham"]
y=(list(name))
y[1]="khan"
name=tuple(y)
print(name)


#2:Add items in tuple 

#since tuples are immutable ,items cannot be added directly...
#we can add items by creating a new tuple.
#tuple me direct new item add nhi kar skte hai ❌
#hume naya tuple banana padta hai ya list trick use karni padti hai..✅



#👉:Method 1:using list 

x=("apple","mango")
y=list(x)
y.append("cherry")
x=tuple(y)
print(x)

#👉:method 2 using tuple concatenation 

x=("apple","mango","banana")
x=x+("cheery",)
print(x)



#3:Remove items from tuple 
#👉items cannot be removed directly from a tuple .
#👉convert to list -remove item-convert back.
#👉tuple se direct delete nhi kar skte hai  ❌
#👉list me convert karke remove karna padta hai ..

#code Example :

x=["apple","banana","cheery"]
y=list(x)
y.remove ("banana")
x=tuple(y)
print(x)


#👉Or you can delete the tuple completely:

#The del keyword can delete the tuple completely:

#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists


#summary :

#operation      direct possible      trick

#change value     no               list conversio
#Add item         no                list conversio
#Remove item      no                list conversio



#👉:Unpacking a Tuple
#👉:When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#👉:unpacking means assigning tuple values to varibales directly...
#👉:unpacking means assigning tuple values to variables directly..
#👉:unpacking ka matlab hai:👉Tuple ke andar jo values hain
#👉:unko alag-alag variables me store karna 



#🧠Basic example:

fruits=("apple","banana","mango")
a,b,c,=fruits
print(a)
print(b)
print(c)

#important rule :

#👉Variables =tuple items (same count hona chaiye)
#wrong example :
#fruits=("apple","banana","mango")
#a,b=fruits #error

#👉Error ayega because 3 values hai but 2 variables 


#2:using asterick (*)in unpacking 
#the asterick (*) is used to collect multiple values into a single variable (as a list).
#Asterisk (*) ka use hota hai :👉Extra values ko ek hi variable me store karne ky liye 
#ye values hota hai :


fruits=("apple","mango","cheery","banana")
a,*b=fruits
print(a)
print(b)

#a=first value
#b=baki sab values (list me)

#example 2:

fruits=("apple","mango","cherry","mango")
a,b,*c=fruits
print(a)
print(b)
print(c)



#important Rules(exam+interviws):
#✅Rule 1:

#👉only one asterick (*) allowed
#❌Wrong 
#a,b,*c=(1,2,3,4)


#✅Rule 2:

#👉Asterick variables always return list.


#Rule 3:
#👉position of *can be:
#start
#middle
#End

#Final summary : 🧠

#concept                 meaning
#unpacking            tuple values -variables
#same count           variables =values
#*(asterisk)           extra values collect karta hai
#output of *              always list



#Loop Through a Tuple
#You can loop through the tuple items by using a for loop.
#A loop is ued to iterate (go through )each item of a tuple one by one.
#loop ka matlab:tuple ke har item ko ek-ek krke acess karna..


#📌Example : 1 loop through a tuple (for loop)
fruits=("apple","mango","cheery")
for x in fruits:
    print(x)

#matlab loop ne ak ak item print kia :

#📌Example : 2 loop through index numbers ✅
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#we loop using index numbers (0,1,2...)to acess tuple items.
#yha hum index (position ) use karke item nikalte hai

fruits=("apple","mango","orange","banana")
for i in range (len(fruits)):
    print(fruits[i])

#len fruits=3
#range(3)=0,1,2
#fruits[i]=index se item nikalna


#using while loop 
#A while loop until a condition becomes false .
#while loop tab tak chlega jab tak condition true hai.


name=("saheer","khan","mallick")
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1


#1:Join Two Tuples  ✅
#To join two or more tuples you can use the + operator:

#joining tuples means combining two or more tuples into one tuple:
#join ka matlab :2 ya zada tuple ko jod kar ek naya tuple banana:

#📌Example :
tuple1=(1,2,3)
tuple2=(4,5,6)
result=tuple1+tuple2
print (result)

#2:Multiply Tuples ✅
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
#multiplying a tuple means repeating its elments multiple times ..
#multiply ka matlb : tuple ke item ko repeat karna :


#📌Example:

tuple =(1,2,3)
reult=tuple*2
print(result)

#simple example :

x=("a","b")
print(x*3)

#combine +multiply together 
t1=(1,2)
t2=(3,4)
result=(t1+t2)*2
print(result)


#Tuple Methods
#Python has two built-in methods that you can use on tuples.
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found


