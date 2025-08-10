#Return the total number of characters:
name="saheer"
print(len(name))

#coverts the whole string to uppercase:
name="saheer azmi"
print(name.upper())

#coverts the whole string to lowercase:
name="SAHEER AZMI"
print(name.lower())

#rstrip=remove right space from the string:
text="hello  "
print(text.rstrip())

#replace(old,new)
text="hello world"
print(text.replace("world","saheer"))

#split = string ko part me tod deta hai,default space ke basis per:
text="my name is saheer"
print(text.split())

#capitalize=capitalizes only the first character of the string.
text="hello world"
print(text.capitalize())

#center(width)=string ko center me lata hai specified with ke andar
text=" saheer "
print(text.center(50))

#count = returns number of times a character or substring occurs:
text="banana"
print(text.count("b"))

#endwith=returns true if the string ends with the specified value:
text="hello saheer"
print(text.endswith("saheer"))

#find=returns index of first occurrence or -1 if not find :
text="saheer is good boy"
print(text.find("is"))

#index= find () jaisa hota hai ,lekin agar word na mile to error dedeta hai.
text="python"
print(text.find("h"))
text="python"
# print(text.find("z"))

#isalnum = returns true if all characters are alphanumeric:

print("SAHEER123".isalnum())
print("saheer00".isalnum())

#isalpha=Returns True if all characters are alphabetic:
print("python".isalpha())
print("python3".isalpha())

#islower= Returns True if all letters are lowercase:
print("hello".islower())
print("hEllo".islower())

#isprintable =Returns True if all characters are printable:
print("hello\n".isprintable())
print("saheer".isprintable())

#isspace= Returns True if the string contains only whitespace
print("   ".isspace())
print(" saheer " .isspace())

#istitle = har word ke 1st letters capitals hain to TRUE:
print("My Name Is Saheer".istitle())
print("my name is saheer ".istitle())

#ISUPPER : RETURNS TRUE IF ALL CHARACTERS ARE IN UPPERCASE:
print("HELLO SAHEER".isupper())
print("hello saheer".isupper())

#startswith= Returns True if the string starts with the given substring :
print("python is awesome".startswith("python"))
print("00 gud boy".startswith("is"))

#swapcase= agar string me capital letters hain to unhe small bana deta hai,\n
# aur jo small letters hain unhe capital bana deta hai

text="my Name is SaHeer azMi "
print(text.swapcase())

#title=har word ke 1st letter ko capital banata hai :
print("my name is saheer azmi".title())



