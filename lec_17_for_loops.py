#EXAMPLE 1:(for loop with range);////////////////////////
for i in range(5):
   print("hello,saheer,Bhai",i)

for i in range (4,7):
   print("hello",i)

for i in range (1,6):
   print("hello,saheer,bhai",i)

for roll_no in range(1,8):
    print("student with roll no",roll_no,"come here")

for serial_no in range (1,4):
   print("pasint_with serial no",serial_no,"come here")

#REAL LIFE EXAMPLE:
for x in range(1,53):
    if x % 2==0:
     print(x,"is even")

for x in range (1,28):
   if x %2==0:
    print(x,"is even")


for x in range(1,21):
   if x % 2 !=0:
      print(x,"is odd")



#TABLE GENERATOR (MULTIPLICATION TABLE) 

num=int(input("enter a num:"))
for i in range(1,11):
   print(f"{num} x {i}={num*i}")


#LIST OF NAMES - EMAIL SENDER:
employees=["saheer","Ali","AHMED"]
for name in employees:
   print(f"sending email to {name}")

weddingcard=["saheer","arham","talha"]
for name in weddingcard:
   print(f"sending weddingcard to {name}")



#EXAMPLE:Total marks calculator(job:school ERP software)
marks={98,75,81,89,90}
total=0
for m in marks:
   total+=m
print("Total Marks=",total)


marks={65,66,56,87,90}
total=0
for m in marks:
   total+=m
print("Total marks=",total)


# Student Marksheet Generator

# Step 1: Input Student Name
name = input("Enter student name:")

# Step 2: Empty list to store subject marks
marks = []

# Step 3: Loop to input marks of 5 subjects
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Step 4: Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Step 5: Check for failed subjects
failed_subjects = 0
for mark in marks:
    if mark < 33:
        failed_subjects += 1

# Step 6: Print Report
print("\n----- Student Marksheet -----")
print("Name:", name)
print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if failed_subjects > 0:
    print("Result: FAIL")
    print("Failed Subjects:", failed_subjects)
else:
    print("Result: PASS ✅")
#practice   ///////////////////////////////////////////////////////////////////////
name=input("Enter student name:")
marks=[]
for i in range(1,6):
   mark=int(input(f"Enter marks for subject {i}:"))
   marks.append(mark)
total=sum(marks)
percentage=total/5
failed_subjects=0
for mark in marks:
   if mark<33:
    failed_subjects+=1

#print("\n---student Marksheet---")
print("Name:",name)
print("Marks:",marks)
print("total marks:",total)
print("percentage:",percentage,"%")
if failed_subjects>0:
   print("Result:FAIL")
   print("Failed subjects:",failed_subjects)
else:
   print("Result:pass✅")


#EXAMPLE 2: For loop with list:///////////////////////////////
fruits=["apple","mango","banana"]
for fruit in fruits:
   print("i like ",fruit)

#Real life example:
#send email to list of students:
students=["arham","ali","talha"]
for student in students:
 print("Email sent to",student)


#print shopping list:
 items=["milk","eggs","bread"]
for item in items:
 print("you need to buy",item)

#student attendance:
names=["saheer","arham","ahmed"]
for name in names:
   print(name,"is persent today")

#print score of students:
scores=["80","78","87"]
for score in scores:
   print("stuudent score:",score)

#favorite color choice:
colors=["red","black","yellow"]
for color in colors:
   print("my favorite color is",color)

#EXAMPLE 3:(FOR LOOP WITH STRING):\\\\\\\
for ch in "saheer":
   print(ch)
for sk in "virat kohli":
   print(sk)

#real life example:
name=input("enter your name:")
print("\n--your attendance--")
for nm in name:
   print(f"|{nm}|")

#example 2: count vowels in a name:
name=input("enter your name:")
vowels="aeioueAEIOUE"
count=0
for ch in name:
   if ch in vowels:
      count+=1
print(f"\number of vowel in your name:{count}")


#example 3: Reverse a string
name=input("enter your name:")
reversed_name=""
for ch in name:
   reversed_name=ch+reversed_name
print("Reversed name:",reversed_name)


#EXAMPLE 4: DETECT IF NAME HAS DUPLICATE LETTERS:
name=input("enter your name:")
seen=[]
for ch in name:
   if ch in seen:
      print(f"duplicate letter found:{ch}")
      break
   seen.append(ch)
else:
   print("no duplicate letters in name:")


#EXAMPLE :MINI PROJECT CHARACTER FREQUENCY COUNTER:
name=input("enter your name:")
freq={}
for ch in name:
   if ch in freq :
      freq[ch]+=1
else:
   freq[ch]=1
print("\n character frequency: ")
for key ,value in freq.items():
   print(f"{key}:{value}")




#EXAMPLE 4: USING FOR LOOP WITH RANGE (START,STOP,STEP:)///////////////////////////////////////////
for i in range(1,11,2):
   print(i)

#example:1(odd-numbered Roll No.ko attendance)
for roll_no in range(1,51,2):
   print(f"roll_no{roll_no}please mark your attedance (odd roll no only)")

#example:2(Every 2nd item ko list se utahna:)
items=['apple','banana','orange','mango','date']
for i in range(0,len(items),3):
   print(items[i])


#examples:3 stairs counting : har 2nd step pe light lagana:
for step in range(1,21,2):
   print(f"light fix on step {step}")

for balloon in range(1,11,2):
   print(f"Ballon {balloon}is colored red")

#clean every 2nd stair:
for stair in range(1,22,2):
   print(f"stair {stair} is cleaned")
#check even numbered traffic signals only:
for signal in range(2,11,2):
   print(f"check traffic signal {signal}")
#bttery levels on every 10%
for persent in range(10,101,10):
   print(f"battery at {persent}%")


#Example:5 nested for loop (loop inside loop)/////////////////////////////////////////////
for rownumber in range(1,4):
   for seatnumber in range(1,4):
      print(1,"*","=",rownumber*seatnumber)
      print("---------")

#real-life example:
#outer loop ->Rows
for row in range (1,4): #ROW 1,2,3
   #inner loop ->seats
  for seat in range(1,5): # seat 1,2,3,4
     print(f"Row{row}seat {seat}")
     print("------End of row----")



       
#example 7:(loop control -break & continue):
for i in range (1,10):
   if i == 5:
      break 
   print (i)
#real life break example:
papers=["englis","math","science","computer"]
for paper in papers:
   if paper =="science":
      print(f"{paper} paper mil gaya ,search stop!")
      break
      print(f"checking {paper}paper...")
for num in range(1,15):
   if num ==5:
      print("number 5 mil gaya,loop stop")
      break
   print(num)
   
correct_pin="1234"
for attemtp in range(3):
   pin =input("Enter PIN :")
   if pin ==correct_pin:
      print("Access granted")
      break
   else:
      print("wrong pin")

#stock search in warehouse:
items={"shirt","jeans","shoes","watch"}
for item in items:
   print(f"checking{item}..")
   if item =="shoes":
      print("shoes mil gaya order ready!")
      break


for i in range(1,20):
   if i ==8:
      continue
   print(i)

#real - life - example :(attendance list skip)
student=["ali","talha","arham","ahmed","osama"]
for name in student:
   if name=="talha":#absent hai:
      continue
   print(f"marking attendance for {name}")

#skipping weekends in work schedule
days={"mon","tue","wed","thru","fri","sat"}
for day in days:
   if day in["sat","sun"]:#weekend skip
      continue
print(f"working on {day} ")
















