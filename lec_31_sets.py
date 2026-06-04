#Topic=Sets
#Author=Saheer Azmi
#years=2026

#1:set hota kia hai ?✅
#👉A set is a collection of limits which is unorderdered,unchangeble,and does not allow duplicate values.

#👉set ak collection hai jisme :
#👉order fix nhi hota hai ❌
#👉duplicate allowed  nhi ❌
#👉direct change nhi kar skte hai ❌

#📌Example:
myset={"apple","mango","banana"}
print(myset)

#set me index nhi hota  ❌
#position nhi hota ❌


#2:Set Items ✅
#Set items are unordered, unchangeable, and do not allow duplicate values.



#3:Unordered ✅
#Unordered means that the items in a set do not have a defined order.

#👉:Set items can appear in a different order every time you use them, and cannot be referred to by index or key.



#4:Unchangeable ✅
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.

#5:Duplicates Not Allowed   ✅
#👉:Sets cannot have two items with the same value.

#Duplicate values will be ignored:

thisset = {"arham", "azmi", "talha", "azmi"}

print(thisset)


#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)



#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
#False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)




#6:Get the Length of a Set ✅
#To determine how many items a set has, use the len() function.
#Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#7:Set Items - Data Types ✅
#Set items can be of any data type:

#String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#A set can contain different data types:
#A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
print(set1)

#type()
#From Python's perspective, sets are defined as objects with the data type 'set':

#<class 'set'>
#What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))


#8:The set() Constructor ✅
#👉:It is also possible to use the set() constructor to make a set.


#Using the set() constructor to make a set:

thisset = set(("delhi", "patna", "gaya")) # note the double round-brackets
print(thisset)




#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.






#Acess set items ✅
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
#print(myset[0])    #error ayega ❌

#sahi tareeka loop se ✅

myset={"apple","banana","mango"}
for item in myset:
    print(item)


#2:Change Items ✅
#Once a set is created, you cannot change its items, but you can add new items.
#Direct change possible nahi ❌
#but indirectly kar skte hai ✅


#3:Python - Add Set Items ✅
#👉Add Items
#👉:Once a set is created, you cannot change its items, but you can add new items.
#👉:To add one item to a set use the add() method.

#👉:Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#👉:multiple item adds :
thisset={"saheer","arham","khan"}
thisset.update(["mallick"])
print(thisset)


#👉:To add items from another set into the current set, use the update() method

set1={"saheer","arham","ali","taha"}
set2={"pineapple","mango","papaya"}
set1.update(set2)
print(set1)



#Add Any Iterable ✅
#👉:The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#👉:iterable wo hota hai jisme multiple values ho aur jise loop(for)se travers kar skte ho.

#Example of iterable :
#👉:list -[1,2,3]
#👉:tuple-(4,5,6)
#👉:string-"abc"
#👉:set-{7,8,9}

#set me "add any iterable" ka matlab 
#👉:python me do important function hote hai :

#1: Add ()
#👉:sirf ek single element add karte hai 
s={1,2,3}
s.add(4)
print(s)



#:update ()

#👉:iterable ke nadar ke sab element ko ek-ek karke add karta hai :

s={1,2,3}
s.update([4,5,6])     #list pass ki 
print(s)


#Add elements of a list to a set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#👉:impotrtant differnces :

# s={1,2}
# s.add([3,4])      #❌Error (list add nhi hoti)

#Error kyun 👉kyunki list mutable hota hai set me allowed nhi :


s={1,2}
s.update([3,4])   #✅works
print(s)

#👉:kyunki update () iterable ko tod ke ek-ek element add karta hai 


#👉:string example 

s={1,2}
s.update("ab")
print(s)


#👉:tuple ke sath 
num={1,2,3}
s.update((3,4))
print (num)


#Real life smjho :
#👉:add()-ek admi ko rooom me bhjna 
#👉:update()-puri group ko bhejna (aur sb alag-alag enter honge)



#1Python - Remove Set Items ✅//////////////////////////////////////////////////
#Remove Item
#👉:To remove an item in a set, use the remove(), or the discard() method.
#👉:Removes was a specific item from the set.if the item does NOT exist -it gives error.
#👉:agar jo item tu hata rha hai wo set me hai -delete ho jayega 
#👉:agar nhi hai-program crash (error)❌dega

#:Example 📌

#👉:Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

num={1,2,3}
num.remove(2)
print(num)


#2:Discard () method 
#👉:removes the item if it exists.
#👉:if not-does Nothing (no error)
#👉safe method hai -item ho ya na ho ,program crash nhi karega:


#:📌Example
#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

num={1,2,3}
num.discard(2)
print(num)

#👉:No Error case 

s={1,2,3,4,5,}
s.discard(6)
print(s)


#👉:Differnces (important interviews point):
#Method          item nhi mila toh
#remove           error ❌
#discard         no error ✅





#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

#The return value of the pop() method is the removed item.

#:📌Example
#Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

s={1,2,3,4}
x=s.pop()
print("Removed:",x)
print(s)

s={1,2,3,4}
x=s.pop()
print(x)
print(s)



#4:clear method ✅
#👉:Remove all item from the set 
#👉:set ko pura empty kar deta hai 

s={1,2,3}
s.clear()
print(s)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


#5:Del keyword 
#👉:Deletes the entire set from memory...
#👉:set hi uda deta hain-variable exist hi nhi krega 

#he del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)




#final summary :✅

#method           kya karta hai 
#remove ()        specific item delete (error agar na mile )
#discard ()        safe delete (no errror)
#pop ()            random item delete  
#clear ()           sab delete
#del                    pura set 



#1.Loop through a set  ✅///////////////////////////////////////////////
#You can loop through the set items by using a for loop:
#set ke har element ko ek-ek karke acess karne ke liye for loop use hota hai ..


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

num={1,2,3,4}
for item in num:
  print(item)

#👉:orddr fix nhi hota hai (kabhi 20 phle aa skta  hai):



#👉2:loop with len () + index (important concept)

# num={10,20,30}
# for i in range (len(num)):
#    print(num[i])

#typeerror:'set' object is not subscriptable 
#set me index ni hota hai (jaise list me hota hai)
#👉list:1[0]  ✅
#👉set:num[0] ❌


#3:loop using enumerate () (Advanced)

#use enumerate () to get index -like numbers 
#set me real index nhi hota ,but numbering de sakte ho


num={"apple","banana","mango"}
for i ,item in enumerate(num):
   print(i,item)

#order still random ho skta hai :




#4:loop with condition (filter)
num={5,10,15,20}
for item in num :
   if item >10:
      print(item)

#5:modify set inside loop (important)

#❌Wrong :

# s={1,2,3}
# for item in s :
#    s.remove(item)     #Error

#loop chal rha hai aur hum set change kar rhe hai - sytem confuse ho jata hai :


#correct way ✅:
s={1,2,3}
for item in s.copy():
   s.remove (item)
print (s)


#6:loop +add item ✅
s={1,2,3}
new_set=set()
for item in s:
   new_set.add(item*2)
print(new_set)


#final concept clear important :

#set vs list loop  
#feature   list          set 
#index      yes         ❌no
#order     fixed ✅       ❌random
#loop       Easy ✅    ✅Easy



#real life tip 

#👉 jab unique  data ho -set use
#👉 jab order important ho - list use 

s={2,4,6,8,10}
for item in s:
   print(item)
for item in s:
   if item >5:
      print (item)



#1:join set ✅//////////////////////////////////////////////
#👉:There are several ways to join two or more sets in Python.
#👉:2 ya zayda sets ko milana =join 
#👉:The union() and update() methods joins all items from both sets.
#👉:The intersection() method keeps ONLY the duplicates.
#👉:The difference() method keeps the items from the first set that are not in the other set(s).
#👉:The symmetric_difference() method keeps all items EXCEPT the duplicates.

#2:Union ✅
#👉: union() method returns a new set with all items from both sets.
#👉:Join set1 and set2 into a new set:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


a={1,2,3}
b={3,4,5}
c=a.union(b)
print(c)

#dono sets ke sab elements ak sath (duplicate nhi ayeag ):



#🧠👉You can use the | operator instead of the union() method, and you will get the same result.
#📌:Example
#se | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


#3:Join Multiple Sets ✅
#All the joining methods and operators can be used to join multiple sets.
#When using a method, just add more sets in the parentheses, separated by commas:

a={1,2}
b={3,4}
c={5,6}
result=a.union (b,c)
print(result)


#👉:Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#👉:join set +tuple 
#👉 set sirf set hi nhi ,tuple/list bhi le skta hai 

a={1,2,3}
b=(3,4,5)
a.update(b)
print(a)

#👉:Update () me any iterable chalega (list ,tuple ,string)'

#👉:The union() method allows you to join a set with other data types, like lists or tuple
#👉:Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


#4:Update ✅
#👉:The update() method inserts all items from one set into another.
#👉:The update() changes the original set, and does not return a new set.
#👉:union()-naya set banata hai 
#👉:update()-existing set me add karta hai 

a={1,2,3}
b={4,5}
a.update(b)
print(a)

#👉:update()=permanet change 


#5:Intersection ✅
#👉:Keep ONLY the duplicates
#👉:The intersection() method will return a new set, that only contains the items that are present in both sets.
#👉:Dono sets me jo same value :

a={1,2,3}
b={2,3,4}
c=a.intersection(b)
print(c)



#👉:Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)



#👉:Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


#👉:The values True and 1 are considered the same value. The same goes for False and 0.
#👉:Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)




#6:differnces :(uique elements) ✅
#👉:The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#👉:jo a me hai per b nhi 

#👉:Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

a={1,2,3}
b={4,3,2}
print(a.difference(b))


#👉:You can use the - operator instead of the difference() method, and you will get the same result.
#Use - to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)


#7:Symmetric differnce (non-commomn)
#👉:The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#👉dono me jo common nhi hai :

a={1,2,3}
b={3,2,4}
print(a.symmetric_difference(b))



#👉:You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
#👉:Use ^ to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#👉common hata do ,baki sb sb lelo 


#🧠Final summary 

#👉:concept        Meaning 
#union  ()            sab elements
#upadte ()             set me add (permanent)
#intersection()         common
#difference ()          unique 
#symetric_differnce ()     non-common


#👉:Real life example

#👉=Boys
#👉=Girls

#operation      result

#Union            sab log
#intersection       same log
#difference        sirf boys
#symmetric          jo alag hai 




#👉:Python frozenset ✅////////////////////////////////
#👉:frozenset is an immutable version of a set.
#👉:Like sets, it contains unique, unordered, unchangeable elements.
#👉ferozenset=immutable set(chnage nhi kar skte hai 
#👉:mormal set-change ho skta hai
#👉:frozenset-lock ho jata hai
#👉:Unlike sets, elements cannot be added or removed from a frozenset.



#2:creating frozenset :
#✅Method 1:Direct 

fs=frozenset([1,2,3,4])
print(fs)


#method 2 :from set ✅

s={5,6,7}
fs=frozenset(s)
print(fs)


#3:frozenset Q use karte hai ?
#👉:3 main reason ✅

#👉1:data ko secure karna 
#👉 kooi chnage nii kar skta

#👉2:dictionary key me use karna :
d={frozenset([1,2]):"value"}
print(d)

#normal set use nhi kar skte hai ❌ :


#👉3:fast operations (safe Data)

#4👉 frozenset methods 
#important :
#❌add(),remove() nhi hoga 
#sirf read operations ✅

#1👉:Union ()
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)

a=frozenset([1,2,3])
b=frozenset([3,4,5])
print(a.union(b))


#2👉:intersection ()
a=frozenset([1,2,3])
b=frozenset([4,5,6])
print (a.intersection(b))


b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)


#3👉:differnce()


a=frozenset([1,2,3])
b=frozenset([3,4,5])
print(a.difference(b))

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)


#4:👉:syemmetric_differnce ()


a=frozenset([1,2,3])
b=frozenset([3,4,5])
print(a.symmetric_difference(b))


a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)


#5:issubset ():

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.issubset(b))


a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)


#6:issuperset():

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(b.issubset(a))


a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)



#:isdisjoint()	 	Returns whether two frozensets have an intersection

a=frozenset([1,2])
b=frozenset([3,4])
print(a.isdisjoint(b))


a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))


#copy:

fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)




#👉:set vs frozenset 


#Feature           set        frozenset

#change             yes         ❌no
#Add/remove         yes          ❌no
#immutable          ❌          ✅
#dict key            ❌           ✅

#final smjho:

#👉frozenset =set jo freze hogya hai :


