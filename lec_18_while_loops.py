#The while Loop 1:
#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1
i=1

while i<3:
  print(i)
  i +=1
#roll call example:
student=1
while student<=5:
  print(f"Roll No.{student}-present✅")
  student=student+1

student=1
while student<=3:
  print(f"Roll NO.{student}-persent✅")
  student=student+1
student=1

#stairs climbing example :
step=1
while step<=5:
  print(f"step {step}-chadh gaya ")
  step=step+1
  
#fruit khana
mango=1
while mango<10:
  print (f"{mango}aam kha lia")
  if mango==5:
    print("ab nhi khauga")
    break
  mango+=1
#game level
level=1
while level<=10:
  print(f"Level{level}complete🎮")
  if level==5:
    print("Game over 😊")
    break
  level +=1
#The continue Statement////////
#With the continue statement we can stop the current iteration, and continue with the next:
i=0
while i <5:
  i=i+1
  if i==3:
    continue
  print(i)

#Real life Example of continue:
floor=0
while floor<5:
  floor +=1
  if floor==3: #third floor repair me hai:
    continue
  print("Lift reached floor:",floor)

#Attendance example (ak student absent hai to skip kardo):
roll=0
while roll<6:
  roll+=1
  if roll==4:  #roll number 4 absent hai:
    continue
  print("present student roll no:",roll)

#fruits khridna("gnda fruits skip kardena"):
fruits=["apple","banana","mango","orange"]
i=0
while i<len(fruits):
  if fruits[i]=="mango":#ganda hai chordo
    i+=1
    continue
  print("bought:",fruits[i])
  i+=1




#The else Statement//////////
#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#Real life example while-else:
student=1
while student<=5:
  print(f"student {student}present")
  student+=1
else:
  print("Attendance completed")


#exam Questions :
q=1
while q<=4:
  print(f"question {q}attempted")
  q+=1
else:
  print ("all question attempted")

#nested while loop :////////
i=1
while i<=3: #outer loop
  j=1
  while j<=2: #inner loop
    print(f"i={i},j={j}")
    j+=1
    i+=1
#real life example of nested while loop:
day=1
while day<=5:
 period=1
 while period <=3:
   print(f"day{day},period{period}")
   period+=1
   day+=1
#resturant menu:
#outer loop- tables
#inner loop -customers

table = 1
while table <= 2:  # 2 tables
    customer = 1
    while customer <= 3:  # har table pe 3 customer
        print(f"Table {table}, Customer {customer}")
        customer += 1
    table +=1

#multiplication table:
for i in range (1,4):
  for j in range (1,6):
    print(i,"x",j,"=",i*j)
    print("------")