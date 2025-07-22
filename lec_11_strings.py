# A string is a sequence of characters,
name="saheer"
print(name)
#how to write srings:
a = 'hello'
b = "world"
c = '''this is a multiline string'''
print(a)
print(b)
print(c)
#string indexing (chracter ko access karna)
#har character me ak index number hota hai,string form 0.
name="saheer azmi"
print(name[0])
print(name[8])
#string slicing (paet nikalna ):
name="saheer"
print(name[0:3])
print(name[:5])
print(name[:4])
#usefull string function (methods)
name="saheer azmi"
print(name.upper())
#name.upper()#sbko capital me lkarega 
name="SAHEER AZMI"
print(name.lower())
#name.lower()#sbko lower me kardeta hai:
name="     saheer azmi     "
print(name.strip())
#strip() first and last extra space remove kardeta hai,
#bich wala ko kuch nhi krta hai:
name="saheer"
print(name.replace("h","g"))
#replace("old","new"):character ye word ko replace kardega 
#h ko i se replace kardega 
sentence="saheer azmi is coder"
print(sentence.split(" "))
#" " space ka basic pe string ko split karta hai:
#har word alag ho jata hai is list mai 
text = "  Hello World  "

print("Original:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Strip:", text.strip())
print("Replace:", text.replace("World", "Saheer"))
print("Split:", text.strip().split(" "))

