#topic=finally keyword 
#Author="saheer Azmi"
#date=2026


#👉finally keyword in python : ✅

#👉:finally block always runs,wheather error comes or not 
#👉:finally ka code har condition me chalega -chahe error aye na aye .



#👉try:
    #risky code 

#except:
   #error handle 

#finally:
    #always run



#👉:flow kaise chlta hai 
#👉:python ka order :

#👉1:try chalega 
#👉2:agar error aya -except
#👉3:uske baad -finally
#👉4:agar error nhi aya-direct finally


#👉:Matlab 

#👉:situation                 finally chalega ?
#Error aya                     ✅yes
#error nhi aya                 ✅yes
#program return ho gya         ✅yes
#function khatam               ✅yes



#Example 1:

try:
    print("program start")
except:
    print("Error aya")
finally:
    print("finally block chala")

#👉:no error occurred  in try block ,so except did not run ,but finally still executed.
#👉:try me koi error nhi tha isliye except nhi chala lekin finally fir bhi chala



#Example 2: error ke sath 

try:
    print(10/0)
except ZeroDivisionError:
    print("zero se divide nhi hota ")
finally:
    print("program khatam")


#👉:Example 3 (finally without except):

try:
    print("hello")
finally:
    print("finally always chalega")

#finally use karne ke liye except zarori nhi hai :



#Example 4:Error but no except 

# try:
#     print(10/0)
# finally:
#     print("finally block")


#example 5-function finally 

def test():
  try:
    return "hello"
  finally:
      print("finally chala")
print(test())

#👉:function me return pehle likha hua hai.
#👉:fir bhi:finally phle execute hua 

#👉:why ?

#python bolta hai :
#👉:"Return karne se pehle finally chalao"

#Example 6-file handling 

try:
    file=open ("demo.text","r")
    print(file.read())

except FileNotFoundError:
    print("file  nhi mila")
finally:
    print("file close kar do")

#Real use 

#👉:Actually real projects me :
# finally:
#   file.close()

#likha jata hai...

#taki:

#eroor aye tab bhi file close ho 
#memory waste na ho 


#try except else finally:

#ye pura structure hota hai:
# try :
#     print("Try block ")
# except:
#     print("Error block")
# else:
#     print("no error")
# finally:
#     print("Always run")


#👉:try+except +finally +return inside function 

#👉:code kia kar rha hai?

