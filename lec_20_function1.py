#In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def my_function():
  print("Hello from a function")
my_function()


def my_function():
  print("hello from ")

def my_function(name):
  print("hello",name)
my_function("saheer")

#You can call the same function multiple times:
def my_function(name):
  print("hello",name)
my_function("arham")
my_function("arham")
my_function("arham")

def add(a,b):
  return a+b
result=add(2,3)
print(result)

#Function Names
#Function names follow the same rules as variable names in Python:

#A function name must start with a letter or underscore
#A function name can only contain letters, numbers, and underscores
#Function names are case-sensitive (myFunction and myfunction are different)
#Example
#Valid function names:

#calculate_sum()
#_private_function()
#myFunction2()

#Why Use Functions?
#Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

temp4=38
celsius4=(temp4-32)*5/9
print(celsius4)

#With functions, you write the code once and reuse it:

#Example

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#Return Values

def get_greeting():
  return "hello from a function"
message = get_greeting()
print(message)


def add():
  print(10+15)
x=add()
print(x)


def add():
  return 10+15
x=add()
print (x)


def add():
  print(5)

def add():
  return 5 
print(add())


#The pass Statement
#Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

def my_function():
  pass


#Arguments
#arguments are the value that are passed to a function when it is called.
#Arguments function ko call karte time diya jane wala values hote hai ,jin per fuction kaaam karta hai :

#A function with one argument:

def my_function(fname):
  print(fname + " Refsnes")    #argumenst wo value hai jo function ko batati hai ki kaam kaise aur kis chiz ke sath karni hai:
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def make_report(type,month):
  print(type,"report for",month)
make_report("sales","january")
make_report("attendance","february")

def biryani(type):
  print(type,"biryani ready")
biryani("chicken")
biryani("muttonn")

def withdraw (amount):
  print("collect",amount,"rupees")
withdraw(2000)
withdraw(500)


#parameters vs Arguments :   #function kay andar likha hua hai nam (dabba) (parameters hota hai )
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Email") # "Email" is an argument (Arguments = actual value jo function ko dete hain: function call karte waqt hota hai)


#Number of Arguments
#By default, a function must be called with the correct number of arguments.
#If your function expects 2 arguments, you must call it with exactly 2 arguments
#jitne parameters,utne arguments dene hi padte hain (agar match nhi hua ❌error)


def my_function(firstname, secondname):
  print(firstname + " " + secondname)
my_function("Ali", "khan")

def salery_slip(name,month):
  print("salery slip of",name,"for",month)
salery_slip("ali","january")
salery_slip("talha","february")
salery_slip("arham","march")

def apply_leave(name,days,reasons):
  print("Employee:",name)
  print("Leave Days:",days)
  print("Reason:",reasons)
apply_leave("saheer","2","fever")
apply_leave("arham","6","weddings")
apply_leave("talha","6","gym")


#Default Parameter Values/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#You can assign default values to parameters. If the function is called without an argument, it uses the default value:
#function ka parameter jisme pehle se value fixed hoti hai:
#agar user value na de toh default value use hoti hai :
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def send_email(name="client"):
  print("email sent to",name)
send_email("saheer")
send_email()

def send_email(name="client"):
  print("email sent to",name)
send_email("saheer")
send_email()

#Example 1:salery slip ("interview favorite")
def generate_salery(name,bonus=2000):
  print("salery slip generated for",name)
  print("Bonus:",bonus) 
generate_salery("saheer",5000)
generate_salery("saheer")

#Example 2:leave application system (real office use):
def apply_leave(employee,days=1):
  print(employee,"applied for",days,"day leave")
apply_leave("ali",5)
apply_leave("saheer")

#Keyword Arguments /////////////////////////////////
#You can send arguments with the key = value syntax.
#keywords wo hote hai jaha function call karte time parameter ka nam likh kar value dete hai:
#order matter nhi karta keyword arguments me :
#code readable hota hai smjh ata hai kaunsi value kis chiz ki hai :
#Example
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Example 1:Emplyoye registration : (interviw Question):
def employee(name,department):
  print(name,department)
employee(department="HR",name="Ali")

def register_employee(name,department,salery):
  print(name,department,salery)
register_employee(salery=10000,name="saheer",department="IT")

#Example 2 :leave application system :
def apply_leave(employee,days,reason):
  print(employee,days,reason)
  apply_leave(reason="medical",days=8,employee="saheer")

#Example 3: generate report:
def generate_report(type,format,year):
  print(type,format,year)

generate_report(year=2025,format="pdf",type="sales")


#Positional Arguments:
#When you call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order:
#posstional arguments me value ka order parameter ke order se match hona chaye :

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")


#office example :
def employee(emp_name,emp_id):
  print(emp_name,emp_id)
employee("saheer",101)


def emplyooe(emp_name, emp_id):
  print(emp_name,emp_id)
employee(101,"saheer")


#Mixing Positional and Keyword Arguments
#You can mix positional and keyword arguments in a function call.
#However, positional arguments must come before keyword arguments:
#mixing Allowed hai ,but positional arguments must come before keyword arguments.
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


#office code Exmple 1:
def emplyooe_details(name,emp_id,department="it",salery=20000):
  print("name",name)
  print("id",emp_id)
  print("department",department)
  print("salery",salery)

emplyooe_details("saheer",101)
emplyooe_details("Ali",102,salery=30000)
emplyooe_details("Rahul",103,department="HR",salery=25000)


#Example 2 leave application system:
def apply_leave(emp_name,days,leave_type="casual"):
  print(emp_name,"applied for",days,"day",leave_type,"leave")
apply_leave("saheer",2)
apply_leave("Ali",5,leave_type="sick")

#salery bonus type:
def give_bonus(emp_name,bonus=2000):
  print(emp_name,"got bonus of",bonus)
give_bonus("saheer")
give_bonus("Ali",bonus=5000)


#Passing Different Data Types
#You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
#The data type will be preserved inside the function:

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


#OFFICE REAL EXAMPLE :
def employee(emp):
  print("name:",emp["name"])
  print("salary:",emp["salary"])
employee_data={"name":"saheer","salary":30000}
employee(employee_data)


#Return Values?????????????????????????????????????????????????????????????????????????
#Functions can return values using the return statement:


def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)



def my_function(x,y):
  print (x*y)
result=my_function(5,3)
print(result)


#Question salary calculation system :
#create a function that calculates total salary after adding bonus and substracting tax.
#function ke result ko bahar bhj deta hai:
#is value ko hm kisi variable me store kar skte hai :

def calculate_salery(basic_salary,bonus=0,tax=0):
  total=basic_salary+bonus-tax 
  return total
result=calculate_salery(30000,bonus=5000,tax=2000)
print("total salary:",result)



#mployee salary +overtime(HR SYSTEM):
def calculate_salary(basic_salary,overtime_hours=0,tax=0):
  overtime_pay=overtime_hours * 500 
  total_salary=basic_salary+overtime_pay-tax
  return total_salary

salary=calculate_salary(30000,overtime_hours=10,tax=2000)
print("final salary:",salary)


#office Attendance :
def caluculate_attendance(total_days,persent_days):
  percentage=(persent_days/total_days)*100
  return percentage

attendance=caluculate_attendance(30,26)
print("Attendance percentage:",attendance)


#order bill 
def generate_bill(price,quantity,discount=0):
  total=price*quantity
  final_amount=total-discount
  return final_amount
bill=generate_bill(1000,3,discount=500)
print("Total bill:",bill)


def generate_bill(price,Quantity,discount=0):
  total=price*Quantity
  final_amount=total-discount
  return final_amount
bill=generate_bill(5000,3,discount=500)
print("total bill:",bill)


#Returning Different Data Types
#Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def class_students():
  return ["saheer","arham","talha"]
students=class_students()
print(students[0])
print(students[1])
print(students[2])

#Return number
def add(a,b):
  return a+b
result=add(5,3)
print(result)


#salery calculation:  (hr payroll software me emplyoee salary calculate karne ke liye):
def calculate_salary(basic,bonus,tax):
  return basic+bonus-tax

salary=calculate_salary(30000,2000,2000)
print("final salary:",salary)

#Return string 
def students(name):
  return "hello " + name
print(students("saheer"))

def player(name):
  return "ishan " + name
print(player("kishan"))

#new emplyooe ko automated email bhjne ke liye:
def generate_welcome_message(name):
  return f"welcome to the company,{name}"
message=generate_welcome_message("saheer")
print(message) 

#Return boolen 
def is_adult(age):
  return age >=18
print(is_adult(17))

#login authemation system me :
def check_login(username,password):
  if username=="saheer" and password=="1234":
    return True
  else:
    return False
print(check_login("saheer","1234"))


#return list (Attendance system):
def get_persent_employees():
  return["Ali","saheer","Arham"]
print(get_persent_employees)  #Aj kon persent hai uski list hr ko dene kay liye)



#return tuple (Bank transaction system):
def transaction(amount):
  return amount,"success"
result=transaction(5000)
print(result)  #amount +transaction status return karne kay liye .


#return dictionary (emplyooe data backend Api)

def emplyoee_details():
  return{
  "name":"saheer",
  "salary":40000,
  "deppartment":"IT"
  }
print(emplyoee_details())


#Return multiple values
def calculate(a,b):
  return a+b,a-b
result=calculate(10,5)
print(result)
  
#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments.
#parameters before / must be paseed positionally.
#parameters after / can be passed postionaly or as keyword.
def calculate_salary(basic_salary,/,bonus=0,tax=0,*,overtime_hours=0):
  overtime_pay=overtime_hours*400
  total_salary=basic_salary+bonus+overtime_pay-tax
  return total_salary

#function call
salary=calculate_salary(700,bonus=200,tax=100,overtime_hours=7)
print("salary slip:",salary)



#keywords-Only Arguments
#keywords-only arguments wo hote hai jinhe function call karte time nam likh kar hi dena padta hai:
#function me * ke baad jo parameters ate hai wo keyword -only-arguments ban jata hai:
#why use keyword-only arguments?
#code clear hota hai 
#confusion kam hota hai
#large function me safety milti hai

#salary system
def calculate_salary(baisc_salary,*,bonus=0,tax=0):
  total=baisc_salary+bonus-tax
  print("total salary",total)
calculate_salary(30000,bonus=5000,tax=2000)

#mixed arguments :
def employee(emp_id,name,/,deppartment,*,salary,bonus=0):
  total_salary=salary+bonus
  print("emp_id:",emp_id)
  print("name:",name)
  print("deppartment:",deppartment)
  print("total salary:",total_salary)

employee(101,"saheer","it",salary=30000)

#Combining Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
 
 
#Real office Example (professional):
def salary(emp_id,name,/,deppartment,*,basic_salary,bonus=0,tax=200):
  total=basic_salary+bonus-tax
  print("ID:",emp_id)
  print("name:",name)
  print("deppartment:",deppartment)
  print("tax",tax)
  print("Total salary:",total)

salary(101,"saheer","It",basic_salary=50000,bonus=2000,)


def performance_salary(emp_id,name,/,basic_salary,*,rating,extra_bnonus=0):
  if rating==5:
    performance_bonus=basic_salary*0.20
  elif rating==4:
    performance_bonus=basic_salary*0.10
  elif rating==3:
    performance_bonus=basic_salary*0.05
  else :
     performance_bonus=0
  total_salary=basic_salary+performance_bonus+extra_bnonus
  print("emplyoee_id:",emp_id)
  print("name:",name)
  print("basic_salary:",basic_salary)
  print("rating:",rating)
  print("extra_bnonus:",extra_bnonus)
performance_salary(101,"saheer",30000,rating=5,extra_bnonus=2000)



#Python *args and **kwargs/////////////////////////////////////////////////////////////////////////////////////////////////
#*args kya hota hai ?
#*args use hota hai jab hume pata nhi hota hai kitne possitional arguments ayenge.
#matlab :function unlimited posstional value le skta hai.
#However, sometimes you may not know how many arguments that will be passed into your function.
#*args=unlimited possitional arguments:
#type =tuple:
#Basic example :
def add_numbers(*args):
  print(args)
add_numbers(10,20,30)   #(*args ak tuple hota hai)

def box(*items):
  print(items)
box("eggs","banana","apple")    #sab value ak tuple me pack hogyi():

#unpack karna :
nums=[1,2,3]
box(*nums)
box(1,2,3)

#Default +normal +*args together:
def demo (a,b=5,*c):
  print(a)
  print(b)
  print(c)
demo(1,2,3,4)

def multiple(a,*b):
  print(a+sum(b))
multiple(10,20,-5,-5)


def total_salary(*salaries):
  total_salary=sum(salaries)
  print("Total salary:",total_salary)
total_salary(2000,30000,40000)

#Dynamic sum with validation : 
def safe_sum(*args):
  total=0       #sum store karne kay liye variables banaya)
  for value in args :   #har arguments ko ek ek karke check karenge.
   if not isinstance(value ,int):   #ye check karta hai: kya value integer hai 
    print("invalid input")  #agar value integer nhi hai tab function wahi stop ho jayega:
    return 
  total +=value     #agar valid hai to sum me add kar karte jao :
  return total      #akhir me total return karo.
  
print(safe_sum(10,20,30))
print(safe_sum(10,20,30))

#find maximum without max()
def find_max(*args):        
  if len (args)==0:   #check karo koi number diya bhi hai ya nhi  
    print("no value provided")  #agar nhi dia hai  toh ye print karega :
    return                 #function yhi stop ho jayega.aage ka code run nhi higa.
  maximum=args[0]        #pehle number ko temporary max maan lete hai. #Example (10,20,30) me phle 10 ko max manlia 
  for value in args :     #loop chlega ak ak karkar compare karega
    if value >maximum:     #check karte hai: kya current number,current maximum se bada hai?
      maximum=value         #agar bada hai to usko naya mximum bana do. 
      return maximum       #loop khtm hone kay bad final sbse bada number return karo.
  print(find_max(10,20,5)) 

#salery slip:
def yearly_salary(name,*monthly_salaries):
  total=sum(monthly_salaries)
  print("Emplyoee:",name)
  print("yearly salary:",total)

yearly_salary("saheer",30000,30000,30000,30000,30000,25000,40000)







#Using *args with Regular Arguments//////////////////////////////////
#*kwargs name ki koi special chiz nhi hoti hai:
#*ka matlab possitional arguments (tuple):
#**ka matlab keyword arguments (dictionary):
#nam kuch bhi rakhdete hai = *data ,*value,,*anything name important nhi hota hai ,star *important hota hai 
#using a


def bag (a,*b):
  print(a)
  print(*b)                         #B=tuple ban gaya
bag("biscuit","bottle","books","copy")    #normal arguments phle fill hota hai :#*args baki sabko elk tuple me pack karta hai :

#interview level Question :
                                    
# Question 1 :
def fun(*a):
  print(type(a))
  print(len(a))
fun()
#Question 2:
def fun (a,*b):
  print(a*sum(b))
fun (2,3,4)

 #tuple =immutable hota hai jo change nhi kar skte hai:
 #list=change kar skte hai 

#Question 3:  
def fun (*a):
  a=list(a)
  a[0]=100
  print(a)
fun(10,20,30,40)
  
#Question 4: new tuple genrate :
def fun (*a):
  new_tuple=(100,)+a[1:]
  print(new_tuple)
fun(10,20,30)     



#office work real example :

#example 1 - salary calculation 
#office me HR ko emplyoee ka total bonus calculate karna hai :
def total_bonus (name,*bonuses):
  print("name",name)
  return sum (bonuses)
print(total_bonus("saheer",5000,10000,30000))

#Question 2 - multiple file 
def process_files(*files):
  for file in files:
    print(f"processing {files}")
process_files("data1.csv","data2.csv","report.pdf")



#Arbitray keyword Arguments = **kwargs ////////////////////////////////////////
#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#This way, the function will receive a dictionary of arguments and can access the items accordingly:
#jitne bhi keyword arguments ayenge sab ko ek dictionary me pack kardo":

def person(**details):
  print(details)
person(name="saheer",age=20,field="it",city="Bihar")


def person(**details):
  print(details["name"])
person(name="saheer",age=20)


def person(**details):
  for key,value in details.items():
   print(key,":",value)
person(name="saheer",age=20,city="Delhi")


#REAL OFFICE EXAMPLE :

#Employee data :
def create_emplyoee(**info):
  print("emplyoee created")
  print(info)
create_emplyoee(
name="Rahul",
age=25,
deppartments="IT",
salary=50000
)

#mixed example 
def fun (a,*args,**kwargs):
  print("a=",a)
  print("args=",args)
  print("kwargs=",kwargs)
fun(10,"saher","it",name="azmi",age=20)





#*kwargs kya hota hai ?
#ye function ko allow karta hai:
#unlimited keyword arguments lene ke liye:
#function me jitne bhi value bhjoge wo sb dictionary me pack ho jate hai :
def person(name,age):
  print(name,age)
person("saheer",20)     #yaha fixed arguments hai

def person(**kwargs):
  print(kwargs)
person(name="saheer",age=20,city="delhi")

#jab tumhe nhi pata kitne arguments ayege future me tab *kwargs use karte hai :
def profile (**info):
  for key,value in info.items():
    print(key,":",value)
profile(name="saheer",age=25)
profile(name="aman",city="delhi",job="it")


#dynamic user creator :
def create_user(**kwargs):           #function bana rhe hai jo bhi keyword ayenge wo sab dictionary me store ho jayenga.
  required_fields=["name","email"]   #ek list banye ye batata hai kaun kaun se fields mandatory hai :
  for field in required_fields:      #loop chlega list kay upar 
   if field not in kwargs:           #check karo jo required field hai woh kwargs dictionary me exist karta hai ?
    return f"{field}is required"    #agar koi requird field missing hai to function yahin ruk jayega aur error message return karega
  return f"user {kwargs['name']} created with email{kwargs['email']}"
print(create_user(name="saheer",email="abc@gmail.com"))



#using **kwargs with Regular arguments :

def student(name,**details):
  print("name:",name)
  print("other details:",details)
student("saheer",age=18,city="patna")
#name fixed hai baki value future me change ho skte hai:

#Example 2 real office style :
def create_emplyoee(emp_id,**info):
  print("emplyoee ID",emp_id)
  for key,value in info .items():
    print(key,":",value)
create_emplyoee(
202,
name="saheer",
age=20,
deppartment="it",
city="delhi",
salary=30000)


#Combining *args and **kwargs
#You can use both *args and **kwargs in the same function.
#The order must be:

#regular parameters
#*args
#**kwargs


def order(base,*toppings,**instruction):
  print("Base:",base)
  print("toppings:",toppings)
  print("instruction:",instruction)
order("chesse","Olives","corn",
spicy=True,extra_chesse=True)

def emplyoee(emp_id,*skills,**details):
  print("id:",emp_id)
  print("skills",skills)
  print("details",details)
emplyoee(
101,
"python",
"Django",
name="saheer",
salary=3000,
location="delhi"
)


#Unpacking Arguments
#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
#Unpacking Lists with *
#If you have values stored in a list, you can use * to unpack them into individual arguments:


def add (a,b,c):
 print(a+b+c)
nums=[20,10,40]
add(*nums)


def student(name,age):
  print(name,age)
data={"name":"ali","age":18}
student(**data)




#Python Scope
#Scope
#A variable is only available from inside the region it is created. This is called scope.
#scope is the region of a program where a variable is accessible (visible and usable)
#scope decides where you can use a variable and you cannot.


#QUESTION 1?
#scope 3 chiz decide karta hai ?
#variable kaha visible hai :
#variable kaha use ho skta hai :
#variable kab tak memory me rhega:


#QUESTION 2?
#PYTHON ME SCOPE KYUN HOTA HAI ?

#=data control karne ke liye 
#har chiz har jagah access nhi honi chachiye.
#2=memory control karne ky liye :
#function khatam =andar ka varible delete.
#3code safe aur clean rakhne kay liye 
#har function apna kaam kare ,dusre ko disturb na kare.

#1-local scope = varible jo function kay andar banata hai....//////////////////////
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
#jo variable function ke andar banta hai,wo sirf us function ke andar hi use ho skta hai.usko bolte hai local scope.


#how define local scope ?
#python me indentation(space)decide karta hai.

#Example 1 ?>

def test():
  a=5
  print("inside:",a)
test()

#a=5--4 space ke andar -- function ke andar(local scope)
#space laga function kay andar:


#Example 2 ?>
def test():
  a=10
  print(a)
test()

def add():
  x= 5
  y= 10
  return x + y
result=add()
print(result)



#interview level Questions?//////////
x=5
def test():
  global x
  print(x)
  x=10
test()

#office work type =counter problem ?
count=0
def increment():
  global count
  count=count+1
  return count
print(increment())


#global use mat karo value pass karo ?
def increment(count):       #function define hota hai 
  count=count+1             #globale scope me variable bana 
  return count              #
count=0
count=increment(count)
print(count)


#2 Global scope :

#variable jo function kay bahar banta hai .?
#a global variable is a variable that is created outside any function and can be accessed anywhere in the program.
#jo variable function kay bahar banata hai,usko global variable scope kehte hai .
#aur wo program  ke kisi bhi function me use hi skta hai.


#how define Global variable >?
#>jo variable left side se start ho (identation nhi ho)
#>aur function ke bahar likha ho 
#>wo global hai......



#Baic example >
x=10                  #x- Global hai 
def test(): 
  print(x)             #function ke andar x define nhi hua 
test()                 #python ne global x use karlia 


#Global variable kha kha use hota hai ?>
#>function ke andar (read karne ke liye)
#>multiple function me
#>pure program me 


#> Example 2 >
x=100                          #>python ak variable banata hai   >>name=x  ,  value=100  ,location: >Global scope
def a():                       #>>python function banata hai,run nhi karta...
  print(x)
def b():
  print(x)
a()
b()


#Ak important Twist >>>>>>

x=100
def a():
  x=50
  print(x)        #output=50,100 >>>>>>>kyunki function ne apna alag local x bana lia hai 
a()
print(x)


#Questions 1:(interview style global variable):
total_users=0
def add_user():
  global total_users
  total_users=total_users+1
  return total_users
print(add_user())

#Question 2 :>>>>

count=10
def test():
  print (count)
  #count=5    #>>error ---
test()



#>>Question 2 >>>  (office work type - configuration variable):
tax_rate=19
def calculate_tax(amount):
  return amount * tax_rate /100 
print(calculate_tax(1000))

app_mode="development"
def start_app():
  if app_mode=="development":
    print("debug mode on")
  else:
    print("production mode")
start_app()

#difference between local scope and Global scope :
#local scope = variable created inside a function and accessible only inside that function.

#global scope = variable created outside all functions and accessible throughout the program.



#Example :
#local Example :

def test():
  a=10
  print(a)       #a sirf function ke andar hai
test()          #bahar use nhi kar skte hai :


#global example :
x=50
def test():
  print(x)            #x function ke  andar bhi use ho rha hai :
test()                #kyuki x global hai 


#same name case :
x=100
def test ():
  x=20
  print(x)
test()
print(x)


#global modify case :
x=5
def test():
  global x
  x=10
test()
print(x)


#test :
x=30
def demo ():
  print(x)
demo()
print(x)

x=40
def demo():
  global x
  x=40

demo()
print(x)

#final solid difference:                  

#feature                  #local scope             #global scope

#kaha banta hai           #function ke andar       #function ke bahar
#kaha use hota hai        #sirf function me        #pure program me 
#lifetime                 #temporary               #program ke end tak 
#modify rule              #direct                   #global keyword chahiye
                      
#Naming Variables:
#variable ek container hota hai jo kisi value ko store karta hai :
age=20
#age=variable name
#20=value

#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):


#variables naming rules :


#Rule 1 == letter ya undercore se start hone chye 
name="saheer"
age=25

#galat
#1name="saheer"      #number se start nhi kar skte hai :


#Rule 2 === Number baad me aa skta hai :
name="saheer"
age=30

#Rule 3 special characters allowed nahi :
#user-name="saheer"      #- desh allow ni hai :
#price$=100             #$ allowed nhi hai 


#Rule 4 ==python keywords use nhi kar skte hai:
#def=5
#class=10            #ye python ka reversed words hai 


# Case sensitive hota hai :
age=25
Age=25    

#ye dono alag variables hai.
#python me capital aur small letter alag hota hai .


#Good naming practice (professional level)///////////////
#variable ka name meaningfull hone chye :
#galat ❌
x=100
y=15

#✅Better
total_price=100
tax_rate=5


#Real office work example :
#Bad code ❌
a=100
b=5
c=a*b

#Good code ✅
salary=100
tax_rate=5
tax_amount=salary*tax_rate





#naming variables :
#If you operate with the same variable name inside and outside of a function, 
#Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()   

print(x)   #The function will print the local x, and then the code will print the global x:

x=300
def myfun():
  global x
  x=200
myfunc()
print(x)


#method 1
x=10
def test():
  global x
  x=x+5
  print(x)
test()

#method 2 : parameter use karo (best practice)
x=10
def test(x):
  x=x+5
  return x
x=test(x)
print(x)



#✅interview level Questions:
"if same variable name is used inside and outside function,what happens?"
#ANSWER---THEY ARE TREATED AS TWO DIFFERENT VARIABLES (LOCAL AND GLOBAL)



#GLOBAL KEYWORD kya hota hai ?.///////////////////////////////////////////////////////////////
#Global ak keyword hai jo function ke andar use hota hai :
#taki hum function ke bahar wale variable ko modify kar sken.


#simple line me :
#Agar function ke andar se global variable change karna ho-global likhna padega:


#Problem 
x=10
def test():
  x=20
  print(x)
test()
print(x)

#AB global kewyword use karo :
x=10
def test():
  global x
  x=20
  print(x)
test()
print(x)

#professional example :
#Bad way (global use):
count=0
def increment():
  global count
  count+=1
#Better way:
def increment(count):
  return count+1
count=0
count=increment(count)

#Global = function ke andar se bhar wale variable ko control karne ka permisssion hai 


#non local keywords ://///////////////
#nonlocal keyword use hota hai nested function (function ke andar function me).
#👉ye na global hota hai 
#👉na local hota hai 
#👉ye outer function ka variable hota hai 

#simple line :
#👉 agarinner function ko outer function ke variable ko modify karna ho >> nonlocal use karte hai .

#lets understand structure :
def outer ():
  x=10 #outer variable 

  def inner():
    pass
#yaha:
#x=outer function ka variables 
#inner()uske andar hai


#❌ problem kia hoti hai ?
def outer ():
  x=10
  def inner():
    x=20
    print(x)
  inner()
  print(x)
outer()


#Ab nonlocal use karte hai :
def outer():
  x=10
  def inner():
    nonlocal x
    x=20
    print(x)

  inner()
  print(x)
outer()


#Difference samjho (Bahut important):///////
#keyword  == kis variable ko change karta hai 
#local(normal)==sirf function ke andar  
#global==sirf function ke bahar wale variable 
#nonlocal==outer function ka variable 



#Kab usee hota hai ://///
#closures me 
#nested functions me 
#state maintain karne ke liye 



#Rule :
#👉 nonlocal tabhi chlega jab variable outer function me ho..
#👉 agar sirf global me ho aur outer me nhi -- error


#🧠interview type :

def counter():
  count=0
  def increment():
    nonlocal count
    count+=1
    return count
  return increment
c=counter()
print(c())
print(c())  #👉yaha count yaad rakha gaya isko closure bolte hain.

#👉ek line me yad rakho 
#nonlocal="muhje global nhi chhaiye ,mujhe outer function ka variable modify karna hai";





#The LEGB Rule//////////////////////////////////////////////
#Python follows the LEGB rule when looking up variable names, and searches for them in this order:


#Local - Inside the current function
#Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace


#1👉 Local scope (L)
#local matlb functio kay andar
def test():
  x=10
  print(x)
test()

#x=10 function ke andar bana 
#python phle local scope me dekhta hai 
#mil gaya =10 print



#👉 Enclosing scope (E)/////////
#ye tab hota hai jab functions ke andar function ho.
def outer():
  x=20
  def inner():
    print(x)
  inner()
outer()

#yaha:
#inner ke andar x nhi hai 
#python outer function me dekhega 
#isko enclosing scope bolte hain.


#👉Global scope (G):
#jo variable function ke bahar hota hai :
x=50
def test():
  print(x)
test()

#👉function me x nhi 
#enclosing bhi nhi 
#python global me dekhega


#Built-in-scope(B)
#python ke built-in-functions:
print(len("hello"))

#yaha:
#len ()built-in-function hai
#python ke andar already defined hota hai


#search order (important)
#python variables ko is order me dhoondta hai :
#local_Enclosing_Global_Built-in
#islie nam legb hai 



#🧠 complete Example :
x=100
def outer():
  x=50
  def inner():
    x=20
    print(x)
  inner()
outer()

#yaha 
#inner me x=20 local hai 
#outer me x=50_encloing hai 
#global me x =100- global 


#output=20
#kyuki python local me hi x mil gaya 




#Python Decorators/////////////////////////////////////////////////////////////////////////////////////////////
#👉Decorators let you add extra behavior to a function, without changing the function's code.
#👉decorator is a function that takes another function as input and returns a new function.
#👉decorators are useed for adding reusable functionality like logging ,authematication,and performance measurment without modifying .




#Example :

#socho ak normal function hai :
#coffee+sugar
#coffee+milk

#👉coffee whi hai bas extra features add hua 

#Basic Decorator
#Define the decorator first, then apply it with @decorator_name above the function.


def changecase(func):      #👉changecase ak decorator function hai:#👉function jo decorator ke pass jayega 
  def myinner():           #👉ye wrapper function hai.decorator ka kaam hota hai :
    return func().upper()  #👉1.function()call ho rha hai 2.uska result mil rha hai 3.upper()usko capital letters me change kar rha hai 
  return myinner           #👉Decorator new function return karta hai.
@changecase                #👉ye line python ko bolti hai:yani decorator myfunction ko modify kr rha hai.
def myfunction():          #👉normal function hai jo string return karta hai:
  return "Hello sally"
print(myfunction())        #python ab run karega kynki decorator ne function replace kardia :


#🧠REAL LIFE EXAMPLE :
#👉SOCHO AK OFFICE HAI:
#👉NORMAL FUNCTION
#👉OFFICE KKE ANDAR KA KAAM 
#ENTER OFFICE 
#LEKIN OFFICE KE GATE PER SECURIY GUARD HAI:
#SECURITY GURAD KIA KARTA HAI ?
#👉CHECK ID 
#👉PHIR ANDAR JANE DETA HAI :




#PYTHON CODE EXAMPLE :
def security(func):
  def wrapper():
    print("checking ID card...")
    func()
  return wrapper
@security
def enter_office():
  print("you entered the office")
enter_office()


def face_id(func):
  def wrapper():
    print("checking face iD...")
    func()
  return wrapper
@face_id
def open_phone():
  print("phone unlocked")
open_phone()

#🧠 job level Questions:

#LOGIN AUTHENTICATION DECORDER(MOST IMPORTANT)
#REAL-LIFE:
#website pe login check hota hai pehle---phir dashboard open hota hai :

#🧠Example 1:
is_logged_in=True        #user login hai 
def login_required(func):
  def wrapper():
    if is_logged_in:
     func()
    else:
      print("please login first")
  return wrapper
@login_required
def dashboard():
  print("welcome to dashboard")
dashboard()

#🧠Example 2:
def login_required(func):
  def wrapper():
    print("checking login...")
    func()
  return wrapper
def dashboard():
  print("welcome")
dashboard=login_required(dashboard)
dashboard()

# #Example 3:
import time
def timer(func):
  def wrapper():
    start=time.time()
    func()
    end=time.time()
    print("Time taken:",end-start)
  return wrapper

@timer
def work ():
  for i in range(1000000):
    pass
work()
#👉 ye ak normal function hai :
def dashboard():  
  print("saheer")
dashboard()

#👉Direct tareeka (without decorator)
import time 
def work():
  start=time.time()
  for i in range (1000000):
    pass
  end=time.time()
  print("Time:",end-start)
work()
#👉 DIrect approach (no decorators):
is_logged_in=True
def dashboard():
  if is_logged_in:
    print("welcome")
  else:
    print("Login first")
dashboard()


#Wrapper kya hota hai ?
#👉wrapper=extra function jo dusre function ko control karta hai :
#👉simple line wrapper ek "guard" hai jo check karta hai phir function ko chlne deta hai :

#👉simple version (important ):

def wrapper():
  print("checking login....")
  dashboard()

#yha wrapper kya kar rha hai ?
#👉phle check 
#👉phir dashboard call

#AB ISKO DYNAMIC BANA DETE HAI :
def login_required(func):
  def wrapper ():
    print("checking login...")
  return wrapper


#4:👉 dashboard kya hai ?
def dashboard():
  print("welcome")

#👉:ye origional fumction hai :
#👉:jisko hum control karna chate hai :

#Decorator=wrapper+original function control


#Multiple Decorator Calls
#👉A decorator can be called multiple times. Just place the decorator above the function you want to decorate.1
#👉jab ak function pe ak se zada decorators lagte hain:

#👉level zero:
#👉Decorator=function ko wrap karna (cover karna)
#👉multiple decorator=ek function ke upar multiple layers lagana
#jaise:
#Gift 🎁
#-paper wrap 
#-ribbon wrap 
#-sticker wrap


#step 1 👉simple code 
def A(func):           #👉A=DECORATOR FUNCTION FUNC=WO FUNCTION JO DECORATE HOGA (YHA HELLO)
  def wrap():          #👉YE WRAPPER FUNCTION HAI 👉YE ACTUAL CONTROL KARTA HAI KYA HOGA :
    print("A start")   #👉FUNCTION CHALNE SE PHLE YE PRINT HOGA :
    func()             #👉YE IMPORTANT HAI 👉YE ORIGIONAL FUNCTION CALL KARTA HAI (HELLO)
    print("A end")     #👉FUNCTION KE BAAD YE PRINT HOGA   
  return wrap          #👉MAIN ORIGIONAL FUNCTION KO REPLACE KAR RHE HAI WRAPPER SE 
def B(func):
   def wrap():
    print("B start")
   func()
   print("B end")
   return wrap
@A                         
@B                     #YE LIKHNE KA MTLB HELLO=A(B(hello))
def hello():
  print("hello")
hello()

#🧠Example 1:

def deco1(func):
  def wrapper():
   print("Deco1 start")
   func()
   print("Deco1 End")
  return wrapper
def deco2(func):
  def wrapper():
    print("Deco2 start")
    func()
    print("deco2 End")
  return wrapper

@deco1
@deco2
def hello():
  print("Hello")
hello()


#👉Arguments in the Decorated Function:✅✅
#👉STEP:1 simple code (Decorator with arguments)

def changecase(func):           #👉ye decorator function hai 👉(func=wo function jo decorate ho rha hai:)
  def myinner(x):               #👉ye wrapper function hai 👉x=jo input user dega
    result=func(x)              #👉ye origional function call kar rha hai :
    final_result=result.upper() #👉ye string ko capital bana rha hai:
    return final_result         #👉final result return hogya 
  return myinner                #👉 yha decorator bol rha hai :
@changecase                     #👉ye short form hai
def myfunction (name):
  return "hello"+name
print(myfunction("saheer"))





#👉*args and **kwargs✅✅✅✅✅✅

#🧠:*ARGS KYA HOTA HAI ?
#👉:SIMPLE LANGUAGE:
#(*ARGS=JITNA BHI VALUES AYENGI -SBKO EK BOX (TUPLE) ME DALDO)


#✅EXAMPLE :
def add(*args):
  print(args)
add(10,20,30)


#👉REAL USE (SUM):
def add (*args):
  total=0
  for i in args:
    total=total+i
  return total
print(add(10,20,30,40))


#👉REAL WORKING :
def add(*args):
  total=0
  for num in args:
    total+=num
  return total
print(add(5,10,15))

#👉REAL LIFE EXAMPLE :
#✅pizza order:
def order(*items):
  print("customer ordered:")
  for item in items:
    print("-",item)
order("pizza","Burger","coke")

#✅cab fare:
def total_fare(*rides):
  total=0
  for price in rides:
    total+=price
  return total
print(total_fare(10,20,30,40))

#👉job level example :
#✅suppose logging system:
def log_messages(*messages):
  for msg in messages:
    print("LOG:",msg)
log_messages("start","processing","End")

#DECORATOR ME USE :
def mydecorator (func):
  def wrapper(*args):
    print("Before function")
    result=func(*args)
    print("After function")
    return result
  return wrapper
@mydecorator
def add(a,b):
  return a+b 
print(add(10,20))


#✅**Kwargs kya hota hai ?

#**kwargs=jitni marzi named values bhjo (sab dictionary me ajti hain):


#👉EXAMPLE 1:✅
def demo (**kwargs):
  print(kwargs)
demo(name="saheer",age=20)

#👉example2:✅
def info(**kwargs):
  for key,values in kwargs.items():
    print(key,"=",values)
info(name="saheer",city="patna",age=24)


#EXAMPLE 3:✅
def user_profile(**data):
  print("user info:")
  for key,value in data.items():
    print(key,":",value)
user_profile(name="saheer",email="mallicksaheer0@gmail.com",country="INDIA")



#🧠job level example :
#logging system :
def log(**info):
  print("log details:")
  for k,v in info.items():
    print(k,"=",v)
log(event="login",user="saheer",status="sucess")


#👉DECORATOR ME USE:"

def mydecorator(func):
  def wrapper(**kwargs):
    print("Before")
    result=func(**kwargs)
    print("After")
    return result
  return wrapper
@mydecorator
def greet(name,city):
  return f"Hello{name}from{city}"
print(greet(name=" saheer ",city=" delhi "))
  

#👉*Args +**Kwargs together(Most important)
def demo(*args,**kwargs):
  print("Args:",args)
  print("kwargs:",kwargs)
demo(10,20,name="saheer",age=20)



#important Rules:✅
1#.**Kwargs always dictionary hota hai 
2#.key=value format me dena padta hai 
3#.*args pehle,**kwargs baad me


#👉Decorator With Arguments//////////////////////////
#👉Decorators can accept their own arguments by adding another wrapper level....
def deco (func):
  def wrapper():
    print("Hello")
  return wrapper      #yha sirf function aa rha tha(no extra arguments)

#👉2=solution=Decorator with arguments:
#👉ab 3 layer banega :

#🧠structure smajho (very important):
def decorator(argument):
    def actual_decorator(func):
        def wrapper():
            # kaam
            func()
        return wrapper
    return actual_decorator
                    
#✅3=Real example(Step By step):
def mydecorator(msg):
    def decorator(func):
        def wrapper():
            print("Message:", msg)
            func()
        return wrapper
    return decorator


@mydecorator("Welcome Saheer")
def hello():
    print("Hello function")

hello()




#👉simple code :
def mydecorator(msg):
    def decorator(func):
      def wrapper():
         print(msg)
         func()
      return wrapper
    return decorator
@mydecorator("Hello Bhai")
def test():
  print("inside function")
test()


#👉2:simple code:
def repeat(n):
  def decorator(func):
    def wrapper():
      for i in range(n):
            func()
    return wrapper
  return decorator
@repeat(3)
def hello():
  print("hii")
hello()


#👉Multiple Decorators/////////////////////////////////////////////////////
#You can use multiple decorators on one function.

#This is done by placing the decorator calls on top of each other.

#Decorators are called in the reverse order, starting with the one closest to the function.....

#👉multiple decorators kia hota hai ?
#✅Ek FUNCTION KE UPAR EK SE ZADA DECORATORS LAGANA?
@A
@B
def hello ():
  print("hello")

#sabse important baat ?
#👉ye code actually hota hai?
hello=A(B(hello))
#pehle B lagega-phir A lagega

#2👉simple working example :
def A (func):
  def wrapper():
    print("A start")
    func()
    print("A end")
  return wrapper

def B (func):
  def wrapper():
    print("B start")
    func()
    print("B end")
  return wrapper
@A
@B
def hello():
  print("hello")
hello()


#👉:clear example ?
def deco1(func):
  def wrapper():
      print("start 1")
      func()
      print("End 1")
  return wrapper
  
def deco2(func):
  def wrapper():
    print("start 2")
    func()
    print("End 2")
  return wrapper

@deco1
@deco2
def test ():
  print ("hello")
test()


#🧠 gold rule :
#BOttom decorator pehle function ke pass hota hai:
#Top decorator sabse bahar hota hai :



#Preserving Function Metadata
#Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

#👉:metadata kya hota hai ?
#👉:simple language:
#function ke bare me information =metadata 

#✅Example:
def hello(): 
  """This is hello function"""
  print("hello")
print(hello.__name__)
print(hello.__doc__)
#is function ka metadata:



#👉:without  wrapps :
def deco(func):
  def wrapper():
    print("Before")
    func()
  return wrapper

@deco
def hello():
  """This is hello function"""
  print("hello")
print(hello.__name__)
print(hello.__doc__)


#👉:with wraps (solutions):
from functools import wraps
def deco(func):
  @wraps(func)
  def wrapper():
    print("Before")
    func()
  return wrapper

@deco
def hello():
  """This is hello function"""
  print("hello")
print(hello.__name__)
print(hello.__doc__)



#Python Lambda:
#Lambda Functions
#A lambda function is a small anonymous function.
#lambda=chota function (shortcut function)
#A lambda function can take any number of arguments, but can only have one expression.

#Syntax
#lambda arguments : expression
#The expression is executed and the result is returned:

#👉1:lamda kya hota hai ?
#lambda=chota function (shortcut function):
#normal function ka shortcut version :


#👉normal function jo hum jante hai :
def add (a,b):
  return a+b
print(add(2,3))


#same kaam lambda se:
add=lambda a,b:a+b
print(add(2,3))


#AB important bat samjhte hai :
#👉lambda kooi naya magic nahi hai :
#👉ye bas:
#✅plain text :(same function ko short me likhna)

#👉2:bacha level samjh :
#soach :
#plain text
#✅tumko sirf ek kaam karna hai--number+10

#2 tareeka :
#❌ Bada tareeka 
def add10(x):
  return x+10


#✅chota tareeka 
lambda x:x+10


#✅:real life (marks add karna)//////
#har student ke marks me +5 grace add karne hai

#❌ normal way :
def add5(math):
  return math+5
marks=[30,40,50]
result=list(map(add5, marks))
print(result)

#✅ LAMBDA WAY (SHORT):
marks={30,40,50}
result=list(map(lambda x:x+5,marks))
print (result)      #har number me +5 add

#2 REAL LIFE ME (EVEN  NUMBER NIKALNA ):
#👉Situation:
#list me se sirf even number chahiye :
#✅lambda use 
nums=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,nums))
print(result)

#3 ✅interviews level Questions (sorting):
#👉situation :
#students ko marks ke basis pe sort karo
students=[("Ali",50),("saheer",90),("rahul",70)]

students.sort(key=lambda x:x[1])
print(students)


#4✅office work (data clean karna):
#👉 situtaion :
#negative values hatao (sirf posstive rakho):

#✅code
data =[-10,20,-5,30,40]
result=list(filter(lambda x:x>0,data))
print(result)


#5✅Fast calculation (quick use):
#👉 situation:
#2 number ka square niklna hai

square=lambda x:x*x
print(square(6))



#🙄kyu use karte hai ?
#👉 jab:
#chota kaam ho 
#1 line ka kaam ho 
#turant use karna ho 
#function sirf ek baar use karna ho 


#🧠 REAL SAMAJH :
#👉normal function:
#full machine banana
#👉 lambda:
#temporary machine (quick kam ke liye):
#4.Real life (important):
#EXAMPLE :LIST ME CHANGES:

#1.sabse pehle-lambda hota kya hai ?
#👉simple line :
#lambda=ek chhota function(shortcut):
#👉matlab:
#normal function ko short me likhne ka tareeka:

#Normal function (jo tu already jaanta hai):
def add(a,b):
  return a+b
print(add(2,3))


#same kaam lambda se:
add=lambda a,b:a+b    
print(add(2,3))


#important baat :
#👉 lambda koi naya magic nhi hai 
#👉ye bas:

#same function ko short me likhta hai:

#2.Bachaa level samajh :
#👉:Tumko sirf ek kaam karna hai --number +10

#👉2 tareka :
#❌ BADA TAREEKA :
def add10(x):
  return x+10


#✅chhota tareeka 
lambda x:x+10
#👉dono same kaam 

#3 kyu use karte hai ?
#jab:
#chhota kaam ho 
#1 line ka kaam ho 
#function sirf ek baar use karna ho ;


#4.REAL LIFE (IMPORTANT):

#EXAMPLE:LIST ME CHANGES
nums=[1,2,3]
result=list(map(lambda x:x+10,nums))
print(result)



#👉 yha kyu hai?
#har number me +10 add kiya 
#agar lambda nhi hota hai :
def addd10(x):
  return x+10
result =list(map(add10,nums))

#👉same kaam -but lamba code:

#5.office me kha use hota hai ?
#👉:real project me :

#data process  
#list /array/modify karna 
#sorting /filtering
#Api data handle karna 

#🧠example :

students=[("Ali",50),("saheer",90),("rahul",70)]
students.sort(key=lambda x:x[1])
print(students)
          

#Lambda with Built-in Functions
#Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
#Using Lambda with map()
#The map() function applies a function to every item in an iterable:

#Example
1#MAP KYA HOTA HAI ✅✅
#👉SIMPLE LINE :
#MAP=HAR ITEM PER SAME KAAM APPLY KARO :
#🧠REAL LIFE :
#SAB NUMBERS ME +10 ADD KARNA 

#✅CODE 

nums=[1,2,3,4]
result=list(map(lambda x:x+10,nums))
print(result)


#filter kia hota hai ✅✅
#👉 simple line :
#filter=sirf wo items rakho jo condition pass kare

#real life 
#sirf even numbers chahiye :

#✅code 
nums=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,nums))
print(result)

#🧠step by step 
#👉condition :
#x%2==0(even check)


#sorted kya hota hai ?
#sorted=data ko order me lagana

#real life 
#marks ke hisab se sort karna 

#CODE ✅
students=[("Ali",50),("saheer",90),("Rahul",70)]
result=sorted(students,key=lambda x:x[1])
print(result)


#DIFFERENCE IMPORTANT 
#FUNCTION     #KAAM 
#MAP          SAB PER KAAM KARO    (CHANGE KARO)
#FILTER       KUCH KO SELECT KRO   (CHUNNO)
#SORTED       ORDER ME LAGAO       (ARRANGE KRO)



#REAL OFFICE USE :
#👉YE SAB USE HOTA HAI :

#DATA CLEANING
#API DATA PROCESS
#STUDENT MARKS SYSTEM 
#SORTING RECORDS 
#REMOVING UNWANTED DATA


#🗣️ interview me kaise puchte hai ?
#👉 QUESTIONS :
#what is lambda function in python ?
#ANSWER-- A lambda function is a small anonymous function written in one line using the lambda keyword:

#why use lambda ?

#ANSWER=TO write short functions quickly without using def.


#kab use na kare ?
#ANSWER= CODE BADA HO ,MULTIPLE LINES HO,COMPLEX LOGIC HO

#LAMBDA SHORTCUT FUNCTION......


#Python Recursion 🧠🧠🧠🧠🧠 ////////////////////////////////////////////////////////////
#Recursion
#Recursion is when a function calls itself.

#Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

#The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates,
#  or one that uses excess amounts of memory or processor power. However
# when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.



#🧠Recursion hota kia hai ?////////////////

#👉recursion is a technique where a function calls itself to solve problem.

#🧠recursion mtlb function apne aap ko hi call karta hai jab tak condition satisfy na ho jaye:

#EXAMPLE ✅:
def show(n):                     #ye ak function hai jo ek number n leta hai :
  if n ==0:                      #agar n==0 hogya--function turant ruk jayega:
    return
  print(n)                       #jo current value hai n ki --wo print hogi 
  show(n-1)                      #function khud ko dobara call kar rha hai 
show(5)                          #har baar n 1 se kam ho rha hai 




def test(n):
  if n==0:
    return
  print("Hi",n)
  test(n-1)
  print("bye",n)
test(2)




#REAL LIFE EXAMPLE : ✅

#1:BOX inside Box (concept Demo):
#👉 Real life samjhne kay liye simple recursion:
def open_box(n):                   #👉function banaya jiska naam open_box hai  #👉n=numbers of boxes
  if n==0:                          #👉agar ye ni likhge function kabhi nhi rukega❌
    print("last empty box mil gaya ✅")       #👉"agar koi box nhi bacha --ruk jao:
    return                              #👉return=function ko yhi khatam kardo:
  print("open box",n)         #takki har step pe pata chle kaunsa box open ho rhs hai :(ye kaam ho rha hai BEFORE RECURSION)
  open_box(n-1)               #"AB BAKI KE(N-1)BOXES BHI OPEN KARO"
open_box(3)



#🧠AB SAME LOGIC DUSRE CODE ME APPLY KARO :
def show_menu(menu):
  for item in menu:
    print(item["name"])
    if "children"in item:
      show_menu(item["children"])



#2:mobile contact/nested list:
contacts=[
  "Aman",
  ["Rahul","Rohit"],
  ["Ali",["sara","zoya"]]
]
def show_contacts(lst):
  for item in lst:
    if type(item)==list:
        show_contacts(item)    #recursion
    else:
      print(item)
show_contacts(contacts)


#🧠factorial interview king :
def fact(n):
  if n ==1:
    return 1
  return n *fact(n-1)
print(fact(5))


#menu (tree structure -office work)

#code✅:
menu=[
  {"name":"Home"},
  {"name":"products","children":[
     {"name":"mobile"},
     {"name":"laptop"}
  ]},
  {"name":"about"}
]
def show_menu(menu):
  for item in menu:
    print(item["name"])   #print
    if "children"in item:   #check
      show_menu(item["children"])   #recursion
show_menu(menu)

#🧠instagram comments: ///
comments=[
  {"text":"nice","replies":[
    {"text":"Thanks","replies":[]}
  ]},
  {"text":"good","replies":[]}
]

def show_comments(comments):
  for c in comments:
    print(c["text"])     #(1)print comment
    if c ["replies"]:    #(2) check replies
      show_contacts(c["replies"]) #(3)recursion
show_comments(comments)



#🗣️basic-interviews 
#1.factorial 

#👉Questions:

#factorial kia hota hai?
#👉n!=n*(n-1)*(n-2)*....*1
#👉example:
#>5!=5*4*3*2*1=120
#>3!=3*2*1=6

# 1:find factorial using recursion:
def fact(n):
  if n ==1:
    return 1
  return n*fact(n-1)
print(fact(5))

#2:print 1 to n 
#QUESTIONS:
#print numbers from 1 to n using recursion
def print_n(n):
  if n ==0:
    return
  print_n(n-1)
  print(n)
print_n(5)


#3.sum of N numbers
#👉QUESTIONS:
#find sum of first N numbers:
def sum_n(n):
  if n ==0:
    return 0
  return n +sum_n(n-1)
print(sum_n(5))

#4 print n to 1
def print_n_to_1(n):
  if n==0:
    return
  print(n)
  print_n_to_1(n-1)

#👉deiffernces:
#print upar=descending
#print niche=ascending

#5 power (x^n)
def power(x,n):
  if n==0:
    return 1
  return x*power(x,n-1)
  
#Base Case and Recursive Case ✅
#Every recursive function must have two parts:

#A base case - A condition that stops the recursion
#A recursive case - The function calling itself with a modified argument
#Without a base case, the function would call itself forever, causing a stack overflow error.


#BASE CASE KYA HAI ?
#👉BASE CASE=FUNCTION KO ROKNE KA RULE:
#SIMPLE LINE:
#👉"YAHA AATE HI FUNCTION BAND HO JAYEGA:"
#KYU CHAHIYE?
#👉AGAR BASE CASE NHI DIA 
def loop (n):
  return loop(n-1)
#👉ye kya karega?
#👉infinite chlta rhega❌



#correct code (with base case):✅
def loop(n):
  if n ==0:     #base case
    return
  print(n)
  loop(n-1 )




#recursive case :"
#👉Recursive case kya hai ?
#👉jab function khud ko dobara call kare:
#example ✅
#loop(n-1)
#matlab:👉"same kaam fir karo ,but chhota input ke sath"




#REAL UNDERSTANDING :"

#👉RECURSION =2 CHEEEZ KA COMBO 
#1.BASE CASE
#👉RUKNE KAY LIYE :
#RECURSIVE CASE
#👉REPEAT KARNE KE LIYE



#COMPLETE EXAMPLE :
#SUM OF N  NUMBERS :
def sum_n(n):
  if n==0:                  #BASE CASE
    return 0
  return n+sum_n(n-1)   #RECURSIVE CASE
print (sum_n(3))


#QUESTTIONs:
def test(n):
  if n ==0:
    return 0
  return n +test(n-1)
print(test(4))


#1:Fibonacci Sequence
#The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:

0, 1, 1, 2, 3, 5, 8, 13, ...

#The sequence continues indefinitely, with each number being the sum of the two preceding ones.

#We can use recursion to find a specific number in the sequence:

#🗣️fibonacci kya hota hai?
#👉Ek number series hoti hai jisme :
#0,1,1,2,3,5,8,13


#2:important definition (interviews line):
#"fibonacci number is defined as."
#fib(n)=fib(n-1)+fib(n-2)




#3:base case (bahut important):
#fib(0)=0
#fib(1)=1

#👉ye hi base case hai(yahin rukna hai):

#4 recursive code :
def fib(n):
  if n==0:    #base case
    return 0
  if n ==1:     #base case
    return 1
  return fib(n-1)+fib(n-2)    #recurcive casee:
print(fib(5))



#8:interviews point 
#👉recursive fibonacci slow hota hai 
#👉time complexity:
#0(2^n) ❌(bad)


#9:optimized :
#DP/itrative method :
def fib (n):
  a,b=0,1
  for i in range (n):
    a,b=b,a+b  
    return a


#♨️final summary:
#👉fibonacci=sum of last 2 numbers
#👉base case=0,1
#👉recurcive case=fib(n-1)+fib(n-2)
#👉problem=slow (repeated  calss)
#👉best=iterative


#interviews level questions:

def fibonacci(n):
  #base case
  if n==0:
    return 0
  elif n==1:
    return 1
  #recursive case
  else:
    return fibonacci(n-1)+fibonacci(n-2)
  #input
n=int(input("enter number:"))
print("fibonacci:",fibonacci(n))

  
  
#Recursion with Lists////🧠🧠🧠
#Recursion can be used to process lists by handling one element at a time:


#👉1.Recursion +list kya hota hai ?
#👉:recursion =fnction khud ko call kare 
#👉:list=multiple values ek jagah store

#👉:jab hum list ko recursion se process karte hain,matlab:
#👉list ke har element ko ek ek karke handle karna:
#👉loop ki jagah recursion use karna


#2.real life soach 😊:
#👉socho tere pass list hai :
[1,2,3,4]
#👉tu kya karega normally?
#loop laga ke sbko print karega :
#👉Recursion me kya karega?
#pehle element le
#bakki list ko function ko de de(AGAIN CALL)

#3:SABSE IMPORTANT CONCEPT:
#✅BASE CASE
#👉JAB LIST EMPTY HO JAYE-STOP

#RECURSIVE CASE:
#👉1 ELEMENT PROCESS KAR
#👉BAKKI PER RECURSION CHALA

#EXAMPLE 1:LIST PRINT USING RECURSION :
def print_list(lst):    #base case 
  if len(lst)==0:
    return 
  print(lst[0])  #kaam
  print_list(lst[1:])
print_list([10,20,30,40])     #call


#5:example 2:sum of list (important interviews):
def sum_list(lst):    
  if len (lst)==0:    #base case  
    return 0
  return lst[0]+ sum_list(lst[1:])    #Recursive case
print(sum_list([1,2,3,4]))

 

#6:example3:find max in list (interviews favorite):
def find_max(lst):   
  if len (lst)==1:     #base case
    return lst[0]
  max_rest=find_max (lst[1:])    #recursvive call
  return lst[0] if lst[0]>max_rest  else max_rest
print(find_max([3,7,2,9,5]))


#7:EXAMPLE 4:REVERSE LIST (IMPORTANT):
def reverse_list(lst):  
  if len (lst)==0:  #base case
    return []
  return reverse_list(lst[1:])+[lst[0]]
print(reverse_list([1,2,3,4]))



#intervews me kia puchta hai?
#👉ye sb pkaa ata hai:
#sum of list
#max/min in list
#reverse list
#count elements
#search elment


#interviews level (search):
def serach (lst,target):      #base case
  if len(lst)==0:
    return False
  if lst[0]==target:
    return True
  return serach(lst[1:],target)
print(serach([1,2,3,4],3))



#python generators ://///////
#👉 Generator = data dene ka slow machine 

#Real-life Example :👉
#👉tere pass ak machine hai jo roti banati hai :
#normal function-ek baar me 100 roti bana ke de deta hai:
#Generator - ek ek roti banata hai ,jab tu bole tab 
#yahi hai generator :


#2.problem kya thi ?
#❌ normal list :
nums=[1,2,3,4,5]
#👉problem :
#sab data ek sath memory me aa gaya -
#agar 1 crore number hogya = memory problem

#3 solution = generator 
#👉generator bolta hai :"Main ek ek value dunga,sab ak sath nhi"

#4.sabse chota example :

def my_gen():
  yield 1 
  yield 2
  yield 3
  
#5.yeild ka matlab 
#👉yeild =value do +ruk jao (pause)
#👉return kya karta hai ?
# value dekar function band ❌
#👉yeild kya karta hai ?
# value deke rukta hai (phir baad me continue hota hai ✅)


#use kaise kare ?
g=my_gen()
print(next(g))  #1
print(next(g))  #2
print(next(g))  #3


#🧠step by step 

#g=my_gen()
#function run nhi hua 
#ek generator object bana

#next(g):
#function start
#yield 1 -value diya -ruk gaya

#👉next again :
#whi se start
#yeild 2
#👉fir:
#yield 3 

#7:Easy tarika (loop):

for i in my_gen ():
  print(i)

#👉Loop automatically next () karta hai ?

#8.kab use karte hai? (very important)

#👉jab data bada ho 👉

#Example ✅
def numbers():
  for i in range(10000000):
    yield i


#fayda:
#memory save
#fast loading

#9:real life use :
#1.large data 1(crore numbers)
#2:file reading (line by line )
#3:Api data (slow loading)
#4:streaming data

#10:🧠Q use karte hai?
#memory bachne kay liye :
#fast processing ke liye:
#EK-ek data cahiye ho tab 

#11:🧠 genertaor vs list :
#List                #generators:

#sab ak sath       ek-ek value
#memory heavy      memory light
#fast for small    best for large


#12: ek solid example :
#✅even numbers generators :
def even(n):
  for i in range (n):
    if i %2==0:
      yield i 

for i in even (10):
  print(i)

#odd numbers generators :
def odd(n):
  for i in range (n):
    if i % 2!=0:
      yield i
for i in odd (11):
  print(i)



#The yield Keyword /////////
#1:yeild =value do +function ko pause karo :

#👉Difference yaad rakho :

#keyword 👉              kya karta hai :
#return                 value deke function khatam ❌

#yield                  value deke pause karta hai ✅


#2:Real-life-example :
#👉soacho ap juice machine use kar rhe hai :
#return -ek baar me 5 glass juice de diya  :
#yield -ek glass dega -ruk jayega -fir bolega "next"?

#yahi hi generator behaviour hai :

#3:🧠basic code (sabse chota ):
def demo():
  yield 1
  yield 2
  yield 3

g=demo()
print(next(g))    #1
print(next(g))    #2
print(next(g))    #3


#loop me kaise use hota hai :
def demo():
  yield 1
  yield 2
  yield 3

for i in demo():
  print(i)



#7.Real use (important):
#example :large data
def big_data(n):
  for i in range (n):
    yield i 
for num in big_data(1000):
  print(num)

#fayda :
#memory save ✅
#ek-ek value ati hai ✅




#working samjho (deep):
def test():
  print("start")
  yield 1
  print("middle")
  yield 2
  print ("End")


g=test()
print(next(g))
print(next(g))



#9.interviews level example :
#👉fibonacci using yield  (har num =pichle 2 numbers kaa sum)

def fib (n):
  a,b=0,1
  for _ in range (n):
    yield a 
    a,b =b,a+b 
for i in fib (5):
  print(i)

#code (Generator wala):
def fib (n):
  a,b=0,1
  for i in range (n):
    yield a 
    a,b=b,a+b 
for i in range (10):
  print(i)


#👉fayda:
#porri file memory me load ni hoti :

#geneerators expression:
gen =(x*x for x in range (5))
for i in gen :
  print(i)

#👉()=genertors
#👉[]=list

#kab use karte hai ?
#👉jab:


#1:data bada ho 
#2:memory bachani ho 
#3:ek-ek value chahiye ho 
#4:streaming data ho 


#interviews level :
#👉 ye pka  ata hai ?

#yield kya hai ?🗣️
#👉"yield function ko pause karta hai aur value return karta hai :

#2:yield vs return ?
#👉return-end
#👉yield-pause+continue 

#3:generator ka fayda >?
#👉 memory efficent 

#14:common mistake :
g=demo()
print(g)



#Generators Saves Memory
#Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

#For large datasets, generators save memory:

#Example:
#1👉:problem samjho sabse pehle :✅
nums =[i for i in range (100000)]
#👉kya hua :
#🗣️1 lakh number ek sath memory me agya :
#Ram use hogi :
#system slow hogi:

#ye hai problem :

#2:👉generator bolta hai 
#main  sab ak sath nhi dunga 
#jab tu bolega tab ek-ek dunga "
 
 
#🧠👉:genertaors code :
def my_gen(n):
  for i in range (n):
    yield i 

#4use kaise kare :

g=my_gen(100000)
print(next(g))  #0
print(next(g))  #1

#👉bas utna hi memory use ho rha hai jitna ek value ka hai :


#🧠5:Difference (most important)
#❌LIST 

nums=[i for i in range(5)]
print(nums)


#memory me sab store :


#Generator ✅:
gen =(i for i in range (5))
print(gen)


#memory me kch store nhi ❌
#jab call karoge tb value ayegi ✅


#👉REAL LIFE EXAMPLE ♨️:
#👉:SOCHO 
#❌list:

#Restaurant me 100 plate khana ek sath table par rakh diya :
#jagah bhar gaya :'


#✅:Generator :
#👉waiter ek-ek plate la rha hai 
#👉jagah bhi bachi 
#👉waste bhi nhi 
#😊ye hai generator :



#👉:List ❌ (galat approach -sab ek sath load ):
def get_food_list():                 #yha ek function bana:
  food =[]                           # empty list banayi (table abhi khali hai:)
  for i in range (1,6):              #loop chalega 1 se 5 tak 
    food.append (f"plate {i}")       #har loop me:(ek plate ban rhi hai : list me add ho rhi hai)
  return food                        #function pura list return kardeta hai :
plates =get_food_list()              #function call hua (ab plate me pura data agaya:)
for plate in plates:                 #loop start (👉ek ek plate niklega list se)
  print(plate)


#👉:Generator(correct waiter style ♨️):
def get_food_generator ():           #👉:function bana 
  for i in range (1,6):              
    yield f"plate{i}"                #👉:yaha magic hai #👉yeild ka matlab :("ek plate de ,ruk fir next time ana")
plates=get_food_generator()          #👉:yha function run nhi hota 👉sirf generator object banta hai 
for plate in plates:                 #👉loop start -genertaor ko bolta hai :("bhai ak plate dee")
  print(plate)



#important difference (list vs generator ):
#list ❌                    Generator ✅

#sab ek sath memory me       ek ek karke 
#heavy memory                light memory
#fast access                 slow but efficent


#🗣️final samjh (interviews line )
#LIST :
#👉 sab khana ek baar me serve 

#GENERATOR:
#waiter ek ke plate la rha hai






#7:🧠 proof (memory difference:)
import sys                          #python ka built-in module hai :👉iska use : memory size check karne ke liye 
lst=[i for i in range (10000)]      #SAB AK SATH MEMORY ME STORE HO RHA HAIN 
gen=(i for i in range (10000))      #NUMBERS READY NHI HAI ABBHI (JAB DEMAND HOGI TAB EK-EK BANEGA )(WAITER BOLRHA HAI JAB BOLEGE TAB PLATE LAUNGA )

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))


#INTERVIEWS QUESTIONS:?

#"LIST STORES ALL ELEMENT IN MEMORY ,SO IT CONSUMES MORE SPACE.GENERATOR ONLY PRODUCES VALUES ON DEMAND USING 
# YIELD ,SO IT IS MEMORY EFFICENT."


#LIST :
#memory heavy 
#fast access

#GENERATOR:
#memory light 
#lazzy execution

#8🧠 Real office work :

#Example:file reading 
def read_file(file):
  with open(file) as f:
    for line in f :
      yield line 
#fayda file ak sath load nhi hoti
#line by line atti hai 



#🧠Example :API DATA 
#👉server se data ata hai:
#ek-ek item process hota hai
#sab ek sath load nhi hota 
#👉generator use hota hai :


#intervies level Explanation 🗣️

#👉"generator memory efficent hota hai kyunki ye data ko ek sath store nhi karta,balki demand par ek-ek
# value generate karte hai using yield keywords"



#10:basic example (Easy):

#even numbers generators:
def even(n):
  for i in range (n):
    if i %2==0:
      yield i
for num in even (10):
  print(num)



#generator kab usee kare ?

#👉:Data bahut bada ho 
#👉:memory kam ho 
#👉:streaming ho 
#👉:EK-EK value chaye 




#Using next() with Generators
#You can manually iterate through a generator using the next() function:

def num():
  yield 1
  yield 2
  yield 3    #👉ye function return nhi karta👉ye yield karta hai (ek-ek value)


#2:generator ko call karte hai :
g=num()

#👉AB:❌g me 1,2,3 nhi hai 
#✅g ek generator object hai 


#Ab main magic -next()
print(next(g)) #1
print(next(g)) #2
print(next(g)) #3


#CODE WITH TRY (SAFE WAY):
g=num()
try:
    while True:
       print(next(g))
except StopIteration:
  print("khatam ho gya")

  

#for loop vs next ()
#👉 for loop :

for i in num ():
  print(i)

#python internally next() use karta hai 
#tu tension free 

#👉 next ():
g=num()
print(next(g))

#tu manually control kar rha hai

#REAL- USE-(INTERVIEW + OFFICE )

#final summary :
#concept                #meaning 

#1.yield                value dekar pause 
#2.generator            lazy data provider 
#3.next()               next value lena ka tool  
#4.stoplteration        data khatam 



#Generator Expressions:✅
#Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:




#1:Generator Expression kya hota hai ?
#🗣️:simple language me :

#Generator expression = shortcut way to create generator 

#example :
(i for i in range(5))

#👉ye ak generator bana rha hai (list nhi ):


#2.list vs generator (sabse important ):

#list comprehension ❌

lst=[i for i in range (5)]
print(lst)

#sab ek sath memory me store :



#Generator expression✅
gen=(i for i in  range (5))
print(gen)

#👉output:<generator object....>
#EK EK value jab chaiye tab milegi :



#3:kaise kam karta hai ?

gen =(i for i in range (5))
print(next(gen))
print(next(gen))
print(next(gen))

#har baar next call :
#generator resume hota hai 
#next value deta hai 



#loop ke sath use :
gen =(i for i in range (5))
for num in gen :
  print (num)

#automatically next() call hota hai :

#5.condition ke sath (important):
gen=(i for i in range (10)if i %2==0)
for num in gen :
  print (num)

#even numbers only 


#REAL - LIFE -EXAMPLE :
#❌ List way (memory heavy):
squares=[i*i for i in range (100)]

#10 lakh values ek sath memory me :

#✅Generator way (memory saving ):
squares=(i*i for i in range (100))
for i in squares:
  print(i)

#ek-ek karke generate - memory safe ✅

#7.kab use karte hai ?
#👉 use generator Expression when :

#large data ho 
#memory bachani ho 
#file reading 
#real-time procssing ho 


#interviews level example :✅

nums=(i*i for i in range (10) if i %2 !=0)
for n in nums:
  print(n)

#odd numbers ka square 

#10.short Trick yaad rakh :

#feature


#10.short trick yaad rakho :
#feature   list              generator 
#syntax    []                 ()
#memory    high               low 
#speed     fast(small data)   better (large data)
#stoarge   full               one by one 


#EK line me yaad rakho :

#generator expression = lazy evaluation (jab chiaye tab value ):


#FINAL REAL WORKING EXAMPLE (OFFICE TYPE):
prices=[100,200,300,400]
discount=(p*0.9 for p in prices)
for d in discount:
  print(d)





#Fibonacci Sequence Generator
#👉:Generators can be used to create the Fibonacci sequence.
#👉:It can continue generating values indefinitely, without running out of memory:


#1:fibonacci sequence kia hota hai?

#simple rule :

0,1,1,2,3,5,8,13,21

#Rule:👇
#next number =piche 2 numbers ka sum :


#variable samjho (important):
a=0
b=1

#👉 meaning :
#a=current number
#b=next number 

#👇update logic :

a,b=b,a+b 
#ye line hi Magic hai ♨️

#3.Normal (without generator ):

def fib(n):
  a,b=0,1
  for i in range (n):
    print(a)
    a,b=b,a+b 
fib(5)


#generator version (main topic):

def fib_gen(n):
  a,b=0,1
  for i in range (n):
    yield a 
    a,b=b,a+b

g=fib_gen(5)      #generator bana abhi kuch excute nhi hua hai :
print(next(g))           #0

#👉yield - o return 

#functio rukta hai (pause):
#next () se resume hota hai 

#loop ke sath (easy way):
for num in fib_gen(7):
  print(num)

#internally next hi call hota hai 

#7:generator kyu use karte hai?
#❌without generator :

#pura list memory me 
#heavy data -problem 

#Generator 
#ek ek value generate
#memory save

#🧠8:REAL - LIFE EXAMPLE must (♨️)

#stock market data /live data 
#numbers continuosly aa rha hai 
#👉tumhe ek-ek value process karni hai 

def fib_infinate():
  a,b=0,1
  while True :
    yield a 
    a,b=b,a+b 
g=fib_infinate()
for i  in range (10):
  print(next(g))

#infinite fibonacci (jab tak chacho)


#office use case:

#👉Example :
#Data streaming 
#large logs
#API RESPONSE CHUNKS 

#👉fibonacci ka concept use hota hai :
#algorithm optimization
#dynamic programming 



#intrerviws level Questions :

#Q.1- FIBONACCI USING GENERATOR :
def fib_gen(n):
  a,b=0 ,1 
  for _ in range (n):
    yield a 
    a,b=b,a+b
  
#Q.2:infinite fibonacci
def fib ():
  a,b=0,1
  while True:
    yield a 
    a,b=b,a+b 


#Q3.nth fibonacci 

def nth_fib(n):
  a,b=0,1
  for _ in range(n):
    a,b =b,a+b
  return a 


#11.common mistke 
#❌ye galat :

print(fib_gen(5))

#✅sahi:
print(list(fib_gen(5)))




#🧠final samjho 
#👉fibnacci = pateern 
#👉generator =memory efficent way 

#generator fibonacci ko ek ek karke deta hai ,list sab ak sath deta hai :


#Generator Methods : ✅
#Generators have special methods for advanced control:

#1🧠:Generator method kya hota hai ?
#👉:generator method = aisa function jo return ki jagah yield use karta hai 


#❌Normal function :
def normal ():
  return 1
  return 2

#problem :
#.ek baar me return hua -function khatam ❌

#generator function ✅:
def gen():
  yield 1
  yield 2

#output ek -ek karke milega :

#✅2:
#generator ka basic example :

def my_gen():
  yield 1
  yield 2
  yield 3

#use kaise kare ?
g=my_gen()
print(next(g))   #1
print(next(g))   #2
print(next(g))   #3

#3.line by line samjho :

g=my_gen()
#👉function run nhi hua :
#👉sirf generator object bana 


next(g)
#function start hua 
#pahle yield mila = 1 return 
#👉function ✅

next(g) 
#👉whi se resume 
#👉next yield -2


#yhi hi magic hai:pause+resume 


#generator vs function :
#feature         normal function      generator  
#keyword         return                yield 
#output          ek baar              multiples times 
#memory          high                 low 
#excution        ek baar              pause-resume 



#5: real life example (important):
#👉:Restaurant 😊:

#❌normal list :
#100 plates ek sath table per 
#memory waste 


def food_list():
  return["plate1","plate2","plate3"]


#✅generator (waiter system):

def food_gen():
  yield "plate1"
  yield "plate2"
  yield "plate3"

g=food_gen()
print(next(g))   #1
print(next(g))   #2
print(next(g))   #3

#waiter ek-ek plate la rha hai 

#👉.loop ke sath use :
for item in food_gen():
  print(item)

#👉internally next() hi call hota hai 

#7:important example (numbers):
def count (n):
  for i in range (n):
    yield i 
#use
g=count(5)
print(next(g))    #0 
print(next(g))    #1

#easy way :
for i in range(5):
  print (i)


#8.generator ka biggest advantage :
#👉:memeory save 

lst=[i for i in range (100)]     #heavy 
gen=(i for i in range (100))      #light 

#list sab ek sath 
#generator =ek-ek karke 

#9.REAL INTERVIEWS /OFFICE USE :

#👉 GENERATOR USE HOTA HAI :


#LARGE FILE  READING
#API DATA STREAMING 
#LOGS PROCESSING
#BIG DATA HANDLING 


#EXAMPLE REAL ✅
def read_file():
  for i in range(5):
    yield f"line{i}"

g=read_file()
print(next(g))
print(next(g))

#10.common mistake 
#❌direct print:
print(my_gen())
#✅correct
print(list(my_gen()))


#interviews question 

#Q.1 even numbers generator :
def even(n):
  for i in range (n):
    if i %2==0:
      yield i 
for num in even (10):
  print(num)

#samjho :even(10)-generator bana
#for loop-automatically next() call karta hai 



def even(n):
  for i in range (n):
    if i %2==0:
      yield i 
g=even(10)
print(next(g)) #0
print(next(g)) #1
print(next(g)) #2


#mai khud contro kar rha hu mujhe kis time next value chaiye :



#odd numbers generator 
def odd(n):
  for i in range (n):
    if i % 2 !=0:
      yield i 

for num in odd(10):
  print (num)

g=odd(10)
print(next(g)) #0
print(next(g)) #1
print(next(g)) #2

#square generator :

def square(n):
  for i in range(n):
    yield i*i

for num in square(5):
  print(num)



#real life use :

#suppose mai large data process kar rha hu :
def big_data():
  for i in range (10000):
    yield i 

for num in big_data():
  if num>5:
    break 
  print(num)

#👉benefit :
#sirf 0-5 hi generate hua 
#bakki data bana hi nhi 
#memory save 

#send() Method
#👉:The send() method allows you to send a value to the generator:

#1:send method kya hota hai ?
#👉:simple line :
#send()=generator ke andar value bhjne ka tareka 

#next() vs send ()

#👇method       kaam 

#next(g)         next value leta hai
#g.send(x)       value bjhta bhi hai +next value leta bhi hai


#2:Basic example:
def gen ():
  x=yield 1
  print("recived:",x)
  yield 2

g=gen()
print(next(g))        #start generator  
print(g.send(10))     #send value 


#3.Real life example ♨️:
#👉soch:
#tu phone pe order de rha hai :

#next()=call start
#send()=order dena 


#EXAMPLE:FOOD ORDER SYSTEM :
def waiter ():
  order =yield "kiya loge?"
  print("order mila:",order)
  yield "serve ho gaya"


g=waiter()
print(next(g))
print(g.send("pizza"))


#real use (office level):
#👉:Data processing /pipline 
def process():
  while True:
    data=yield
    print("processing:",data)

g=process()
next(g)     #start
g.send(10)
g.send(20)
g.send(30)


#6.interviews line 
#-send()used to send a value into a generator and resume its executation:""

#7.deep concept 

#👉 yield 2 kaam krta hai :

#1.value return karta hai 
#2.value recive bhi karta hai (send()se)


#✅8.mini example (clear understanding):
def test():
  a=yield 5
  print (a)
  g=test()

print(next(g))     #5
g.send(100)        #a=100


#final summary 

#concept       meaning 
#yield            pause 
#next()         next value 
#send()         value bhjna +resume



#👉:close() Method
#The close() method stops the generator:

#Example:

#close ()  kya hota hai ?

#close =generator ko turant band (stop)kar deta hai


#2.basic example :

def gen():
  yield 1
  yield 2
  yield 3

g=gen()
print(next(g)) #1
g.close()           #generator band
#print(next(g))     #error 


#kaise kam karta hai ?
#jab hum:

g.close()

#python internally :
#Generator exit

#throw karta hai 
#aur generator immeditally stop ho jata hai :

#real samjho (very important):

#soch:

#generator=water pipe 
#next()=pani le rha hai 
#close () =tap band kardia ❌


#5.adavantage example 

def gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("generator closed")

g=gen()
print(next(g))
g.close()


#6.real life example :
#suppose :

#👉 mai file read kar rha hun
#ya api call kar rha hu 
#👉agar beech me stop karna ho:

g.close


#inter viwws line :

#"close() method raises generaor exit inside the generator and stops its execution"



#11:full example :

def demo ():
  try:
    while True:
     x=yield
     print("value",x)
  finally:
    print("generator closed")
g=demo()

next(g)
g.send(10)
g.send(10)
g.close()


#close()=generator ko forcefully band krna :
