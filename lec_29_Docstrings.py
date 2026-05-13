#topic=Docstring 
#Author=saheer azmi
#Date=2026


#1.Docstrings kia hota hai ?
#👉A docstings is a string used to discribe what a function /module does .
#👉Docsting=code ka description (explanataion) 3
#👉ye batata hai function kia karta hai :

#👉:simple line me :
#👉docsting =function ka "about section"


#2:kaise likte hai ?
#👉triple quotes me use hota hain?
def add (a,b):
    """This function adds two numbers """
    return a + b


#Rule (important)
#👉docstrings hamesa function ke andar first line me hota hai 
#❌galat:
def add (a,b):
    return a+b
"""wrong place"""

#use kyu karte hai ?

#documentation 
#Easy understandings 
#helpful in large projects 

#👉code samjhna ke liye 
#👉dusre log bhi easily samjah sake 
#👉interviews me clean code deikhne ky liye


#4:kaise use karte hai (acess)?
#👉Docstring dekhne ky liye :
def add (a,b):
    """this function adds two numbers"""
print (add.__doc__)


#5:multi-line Docsting 
def greet(name):
    """This function greets the user.
    it takes name as input."""
    return f"Helllo{name}"

#6:function +Docstring example(Real)

def sqaure (n):
    """Returns sqaure of a number """
    return n*n
print (sqaure (5))
print(sqaure.__doc__)


#7:Docsting bvs comement 

#feature  docstring         comment 
#syntax    """ """            #
#use       explanataion      notes 
#Acess      yes (doc)         no 


#interviews line :

#docstring  is used to describe the purpose of a function and can be accessed using doc 


#👉Docstring =youtube video ka description
#👉function=video


