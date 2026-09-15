#topic=for loop with else :
#Author="saheer azmi"
#date=2026


#1:Basic concept (simple language) ✅

#👉:normal soch :
#hum sochte hain:

#else sirf if ke sath hota hain

#👉:Reality :
#else loop ke sath bhi hota hai ✅


#2:Rule samajhlo (important)
#👉:for loop ka else tab chalega jab loop Normal tareeka se khatam hoga ..
#👉:agar loop ke beech me break aa gaya -else nhi chlega 


#👉3:simple example;

for i in range (5):
    print(i)
else:

  print("loop khatam hogya")


#👉4:Break wala case (important) ✅

for i in range (5):
   print(i)
   if i ==3:
      break
else:
   print("loop khatam hogaya")


#👉:Real use case (very important):
#👉:ye mostly searching me use hota hai 

#Example :number find karna 



nums=[1,3,5,7]
for num in nums :
   if num ==4:
      print("mil gaya")
      break
else :
   print("nhi mila ")

   

nums=[1,3,5,7]
for num in nums :
   if num ==3:
      print("mil gaya")
      break
else :
   print("nhi mila ")



#short formula :
#👉Loop without break -else runs 
#👉loop without break -else skipped


