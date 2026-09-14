#:tpoic=dictionaries
#:Author=saheer azmi
#:date=2026

#Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


#1:Dictionary ✅
#👉:Dictionaries are used to store data values in key:value pairs.
#👉:dictionary ek data tructure hai jsime data key aur value ke pair me store hota hai.
#👉:A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#👉:Dictionaries are written with curly brackets, and have keys and values:


#Create and print a dictionary:


#: 📌 Example :

student={
    "name":"saheer",
    "age":20,
    "course:":"cse"
}
print(student)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#2:Dictionary Items ✅
#👉:Dictionary items are ordered, changeable, and do not allow duplicates.
#👉:Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#👉:each element inside a dictionary's called an item,and it consists of a key and a value.
#👉:dictionary ke har element ko item bolte hai ,jo ek key + value pair hota hai 



employe={
    "name":"saheer",
    "age":20,
    "city":"patna"
}
print(employe)


#:3.Ordered or unordered ?  ✅
#👉:As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#👉:pehle dictionary ka order fix nhi hota tha ab (python 3.7 ke baad )Order same rhta hai jaisee insert kiya
#👉:When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#👉:Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

# 📌 Example :

num={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
}
print(num)


#4:Changeable  (mutable):  ✅///////////////////////
#👉:dictionaries are mutable ,meaning you can change values after creation.
#👉:dictionary ko modify (badal) kar skte ho banane ke baad 


student={"name":"saheer","age":20}
student["age"]=21
print(student)


#5:Duplicates not Allowed (keys): ✅
#👉:ictionaries cannot have two items with the same key:
#👉:duplicate keys are NOT allowed .if repeated ,the last value will overwrite ...
#👉:same key baar -baar nhi ho skta .agar ho toh last wali value save hogi ..

d={
    "name":"saheer",
    "name":"Azmi"
}
print(d)


#6:Dictionary Length ✅
#👉:To determine how many items a dictionary has, use the len() function:
#👉:use len () to get the number of item in a dictionary.
#👉:len () se dictionary me kitna items hain wo coutn milta hai ...


d={"a":1,"b":2,"c":3}
print(len(d))


c={"a":1,"b":2,"c":3,"d":4}
print(len(c))


#7:Dictionary Items - Data Types ✅
#👉:The values in dictionary items can be of any data type:
#👉:type() tells the type of a variable 
#👉:type () se pata chalta hai variable kis type ka hai ..

#:Example 📌

d={"name":"saheer"}
print(type(d))

 
#8:The dict() constructor 
#👉:It is also possible to use the dict() constructor to make a dictionary.
#👉:you can create a discionary using the dict () constryuctor 
#👉:dict () function se bhi dictionary bana skte hain.

#📌Example :
d=dict(name="saheer",age=20),
course="cse"
print(d)


#👉2:Python - Access Dictionary Items ✅////////////////////////////////////////////////

#👉:You can access the items of a dictionary by referring to its key name, inside square brackets:
#👉:dictionary me value ko key ke through acess karte hai ...


#method 1:Using [] ✅
#You can access the items of a dictionary by referring to its key name, inside square brackets
#👉:dictionary me value ko key ke through acess karte hain.


#method 1:using []
student={
    "name":"saheer",
    "age":20,
    "marks":85
}
print(student["name"])


#agar city type karta to error deta Q ki key exist nhi karti :


#method 2:using get ()


student={
    "name":"saheer",
    "age":20,
    "marks":85
}
print(student.get("city"))


#👉difference important :

#:method          key nhi mila to 
#[]                Error
#get()             none



#2.Get keys ✅
#The keys() method will return a list of all the keys in the dictionary.
#keys () return all keys of dictionary.
#keys () dictionary ki sarri keys return karta hai....

student={
    "name":"saheer",
    "age":20,
    "marks":85,
    "city":"patna"
}
print(student.keys())

#👉:Add a new item to the original dictionary, and see that the keys list gets updated as well: ✅

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change



#👉:Get Values ✅
#👉:The values() method will return a list of all the values in the dictionary. ✅

#👉:The values() method will return a list of all the values in the dictionary.
#👉:values () returns all value:
#👉:values() dictionary sarri values deta hai ...


student={
    "name":"saheer",
    "age":20,
    "marks":85,
    "city":"patna"
}

print(student.values())



#👉:Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


#👉:Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change





#👉4:Get items :  ✅
#👉:The items() method will return each item in a dictionary, as tuples in a list.
#👉:items () returns key-value pairs as tuple.
#👉:items () key - value pairs ko tuple ke form me deta hai .


student={
    "name":"saheer",
    "age":20,
    "marks":85,
    "city":"patna"
}

print(student.items())


#👉:Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#👉:Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


#👉:check if key exists : ✅
#👉:To determine if a specified key is present in a dictionary use the in keyword:
#👉:use in keyword to check if key exists.
#👉:in keyword se check karte hai key present hai ya nahi


student={
    "name":"saheer",
    "age":20,
    "marks":85,
    "city":"patna"
}

if  "city" in student:
    print("yes","key is exists")



student={
    "name":"saheer",
    "age":20,
    "marks":85,
    "city":"patna"
}

if  "home" in student:
    print("yes","key is exists")
else:
    print("No","home is not persent")




#👉:full combined code (practice)
student={
    "name":"saheer",
    "age":21,
    "marks":85

}

#Acess 
print(student["name"])
print(student.get("age"))

#keys
print(student.keys())

#values
print(student.values())

#items
print(student.items())

#check key 

if "marks" in student :
    print("marks exists")



#final summary : ✅

#Topic           meaning 

#Acess           student["key"]
#safe Acess      get() safe acess
#keys            keys()
#values           values ()
#items            items ()
#check         "key" in dict 




student={
    "name":"saheer",
    "age":20,
    "city":"patna",
    "marks":90
}

print(student["name"])
print(student.get("marks"))
print(student.keys())
print(student.items())





#👉:Python - Change Dictionary Items  ✅

#👉1:Change value (single item) ✅
#👉:You can change the value of a specific item by referring to its key name:
#👉:key ke through hum kisi bhi value ko change /update kar skte hai..

#📌:syntax 
#👉:dictionary["key"]=new_value

#👉:Example :

student={
    "name":"saheer",
    "age":22,
    "city":"patna",
    "marks":86
}

#change age 
student["age"]=21
print(student)


student={
    "name":"saheer",
    "age":"23",
    "city":"patna",
    "marks":"87"
}


student["home"]="jehanabad"
print(student)



#👉:Update Dictionary  ✅
#👉:update () method is used to update multiple key-value pairs at once.
#👉:update () ka use karke hum ek sath multiple values change ya add kar skte hai.
#👉:The update() method will update the dictionary with the items from the given argument.
#👉:The argument must be a dictionary, or an iterable object with key:value pairs.


#📌:syntax 

#👉:dictionary.update({key:value})

#example :🧠

student={
    "name":"saheer",
    "age":20,
    "marks":85
}
student.update({
    "age":22,
    "marks":90
})
print(student)




#👉:update + add together

#👉:Example :

student.update({
    "age":23,         #existing 
#update
"city":"punjab"       #new-add
})

print(student)


#differnce (important for interviews):
#method                  #use
#student ["key"]=        single item change/item
#update                   multiple items change /add




#👉:Real - life logic : ✅

#👉:[] jab ek hi value change krni hai ho 
#👉:update()-jab ek sath bahut changes krna ho 

#👉:full practice code :

student={
    "name":"saheer",
    "age":20,
    "marks":86
}

#change single value 
student["age"]=21

#update multiple values 
student.update({
    "marks":95,
    "city":"pubjab"
})

print(student)



#👉:Python - Add Dictionary Items ✅
#👉:Adding Items
#👉:Adding an item to the dictionary is done by using a new index key and assigning a value to it:


#👉:Adding items (Basic Method)
#👉:you can add a new item by assigning a value to a new key .
#👉:naya key bana ke usme value assign karte hi wo dictionary me add ho jata hai...
#👉: Adding an item to the dictionary is done by using a new index key and assigning a value to it:


#syntax 📌:
#👉:dictionary["new_key"]=value

#Example 🧠:

student={
    "name":"saheer",
    "age":21
}

#add new item 
student["marks"]=85
print(student)

#👉:samjho :

#👉:agar key nayi hai- Add hoga 
#👉:agar key phle se hai -update hoga 




#👉:Update Dictionary (Adding multiple items )
#👉:The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#👉:The argument must be a dictionary, or an iterable object with key:value pairs.

teacher={
    "name":"harman",
    "age":21,
}

teacher.update({
    "marks":90,
    "city":"punjab"
})

print(teacher)





#3👉:Mix:Add +update Together
#👉:update () can both add new keys and update existing ones.
#👉:update () ek hi time pe new add +old update dono karta hai.



student={
    "name":"saheer",
    "age":21
}

student.update({
    "age":23,    #update
    "marks":95   #add
})

print(student)


#practice:

student={
    "name":"saheer"
}

student["age"]=21
student["marks"]=88

student.update({
    "city":"patna",
    "course":"cse"
})

print(student)





#👉:Python - Remove Dictionary Items ✅////////////
#👉:There are several methods to remove items from a dictionary:


#👉:pop () Method :
#👉:pop () removes an item using its key and returns its value.
#👉:pop () kisi specific key ko remove karta hai aur uski value return karta hai..

#🧠syntax :

#👉:dictionary.pop("key")



student={
    "name":"saheer",
    "age":21,
    "marks":87
}

removed=student.pop("age")
print(removed)
print(student)




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)





#2.popitem() method :
#👉:popitem () removes the last inserted item
#👉:pop item () dictionary ka last wala item delete krta hai.

#📌:Example :

student={
    "name":"saheer",
    "age":21,
    "marks":98
}
student.popitem()
print(student)




#del keyword : ✅
#👉:del is used to delete a specific key or entire dectionary 
#👉:del se hum spcific key ya poori dictionary delete kar skte hai.


#👉Example 1 (single key delete):

student={
    "name":"saheer",
    "age":21,
    "city":"patna"
}
del student["age"]
print(student)



#4:clear method ✅
#clear () removes all items but keeps the dictionary empty..
#clear () dictionary ke saree items hata deta hai ,par dictionary exist krti rhti hai.

student={
    "name":"saheer",
    "age":21,
}

student.clear()
print(student)




#👉:Loop Through a Dictionary ✅
#👉:You can loop through a dictionary by using a for loop. ✅

#👉:When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.


#1:loop through a dictionary (Basic ):
#👉:you can loop through  a dictionary using a for loop.
#👉:for loop ka use karke dictionary ke andar ke items per iterate karte hai.


student={
    "name":"saheer",
    "age":21,
    "marks":87
}
for x in student:
    print(x)


#👉default loop key ko print karte hai..


#2:loop through keys (one by one ):
#👉: use for x in dict or keys () to get all keys.
#👉:keys ko ek-ek karke acess kar ke liye for loop use hota hai.

#🧠:Example :


student={
    "name":"saheer",
    "age":21,
    "marks":87
}
for key in student.keys():
    print(key)




#3👉:Loop Through values (one by one)
#👉:use values () to get all values.
#👉:values ko ek-ek karke acess karne ke liye values () use hota hai..


#example :🧠
student={
    "name":"saheer",
    "age":21,
    "city":"patna"
}

for value in student.values():
    print(value)






#4👉:loop through keys-Acess values 
#👉:use keys to acess values inside loop.
#👉:loop me key use karke value nikalte hai.


student={
    "name":"saheer",
    "age":21,
    "city":"patna"
}
for key in student.keys():
    print(key)


student={
    "name":"saheer",
    "age":21,
    "city":"patna"
}

for key in student:
    print(key,"=",student[key])





#5👉:Loop Through items (key+value Together):
#👉:use items () to get both key and value.
#👉:items () se key aur value dono ek sath milte hain.


#Example 🧠:
student={
    "name":"saheer",
    "city":"patna",
     "age":21
}
for key,value in student.items():
    print(key,value)


#Real life understanding :
#👉Dictionary = data ka group 
#👉loop=sbko ek-ek karke dekhanna
#keys-subject ka nam 
#values-marks



#👉:practice task :

student={
    "name":"saheer",
    "age":21,
    "marks":23,
     "city":"patna"
}


for key in student:
    print(key)      #only key

for values in student.values():
    print(values)    #only values



for key,value in student.items():
    print(key,value)     #kay and values both



#👉:Copy a Dictionary ✅✅✅
#👉:You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#👉:There are ways to make a copy, one way is to use the built-in Dictionary method copy().

#1:problem samajah (important 🙋):

#example 📌:
d1={"name":"saheer","age":21}
d2=d1   #copy kia (socha copy hai )'
d2["age"]=25
print(d1)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



#❌problem :

#d2=d1 does Not craete a real copy.it creates a refernce.
#d2=d1 me copy nhi banata banta,dono same memory ko point krte hain.
#d2 change -d1 bhi chlega ❌

#concept :refernce vs copy 
#👉:d1 aur d2 dono same box ko use kar rhe hain



#2:copy a dictionary (correct way):

# ✅method 1:copy()

#👉:ceates a shallow copy of the dictionary.
#👉:copy()ek nayi dictionary banata hai (alag memory me )


#example 🧠:
d1={"name":"saheer","age":22,}
d2=d1.copy()
d2["age"]=30
print("d1:",d1)
print("d2:",d2)



#samjho :

#👉:Ab change sirf d2 me hua
#👉:d1 safe hai ✅



#2:method dict() constructor
#👉 you can also use dict()to copy a dictionary.
#👉 dict() se bhi copy bana skte hain

#🧠Example :

d1={"name":"saheer","age":21}
d2=dict(d1)
d2["name"]="azmi"
print(d1)
print(d2)



#differnce :

#method    result 
#d2=d1      ❌ same Reference
#d1.copy()    ✅Real copy
#dict(d1)      ✅real copy




#1:Nested Dictionaries ✅
#👉:A dictionary can contain dictionaries, this is called nested dictionaries.
#👉:A nested dictionary is a dictionary  inside another dictionary .
#👉:jab ek dictionary ke andar dusri dictionary hoti hai ,use nested dictionary kahte hai.

students={
    "student1":{
        "name":"saheer",
        "age":21,

     },
     "student2":{
    "name":"ali",
    "age":22
 }
}
print(students)


#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


#outer dictionary - students
#inner dictionary-student1,student1,student2




#2.Acess nested dictionary :
#👉use multiple  keys ton acess inner values.
#👉nested dictionary me value nikalne ke liye 2 keys use hoti hain






students={
    "student1":{
        "name":"saheer",
        "age":21,

     },
     "student2":{
    "name":"ali",
    "age":22
 }
}

print(students["student2"]["name"])




#3:Add data in nested dictionary 
#👉:you can add new key-value pairs inside inner dictionaries..
#👉:inner dictionary ke andar bhi new data add kar sakte hain.



students={
    "student1":{
        "name":"saheer",
        "age":21,

     },
     "student2":{
    "name":"ali",
    "age":22
 }
}

students["student1"]["marks"]=90
print(students)


#ab student1 me marks add ho gaya 





#4:change data in in nested dictionary :
#👉update values using keys.
#👉:same tarike se value change karte hai..


students={
    "student1":{
        "name":"saheer",
        "age":21,

     },
     "student2":{
    "name":"ali",
    "age":22
 }
}
students["student2"]["age"]=23
print(students)




#5:for loop Through nested dictionary :
#👉use nested loop.
#nested dcitionary ke liye double loop use hota hai ..




students={
    "student1":{
        "name":"saheer",
        "age":21,

     },
     "student2":{
    "name":"ali",
    "age":22
 }
}


for student,details in students.items():
    print("student",student)
    for key,value in details .items():
     print(key,"=",value)






#6:Another way (seprate dictionaries)


students={
    "student1":{
        "name":"saheer",
        "age":21,

     },
     "student2":{
    "name":"ali",
    "age":22
 }
}

s1={"name":"saheer","age":21}
s2={"name":"arham","age":33}

students={
    "student1":s1,
    "student2":s2
}

print(students)



#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#👉:List is a collection which is ordered and changeable. Allows duplicate members.
#👉:Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#👉:Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#👉:Dictionary is a collection which is ordered** and changeable. No duplicate members.
#👉:*Set items are unchangeable, but you can remove and/or add items whenever you like.
#👉:**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.



#Dictionary Methods ✅
#Python has a set of built-in methods that you can use on dictionaries.

#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary

