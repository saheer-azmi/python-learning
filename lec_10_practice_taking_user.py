# name=input("enter your name:")
# print("welcome",name)
# age=int(input("enter your age:"))
# print("after 5 years old you become ",age+5)
# a=int(input("enter your first number:"))
# b=int(input("enter your second number:"))
# print("sum is:",a+b)
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# op=input("kya karna hai ?+ ya -?")
# if op=="+":
#     print("result:",a+b)
# elif op=="-":
#     print("result:",a-b)
# else:
#     print("galat input dia apne")
# first =input("first name:")
# last=input("last name:")
# print("apka full name hai :",first+""+last)

# # Student Marksheet Generator with Validation and Grade

# name = input("Enter student name: ")
# roll_no = input("Enter roll number: ")

# # Subject marks input
# math = int(input("Enter marks in Math (out of 100): "))
# science = int(input("Enter marks in Science (out of 100): "))
# english = int(input("Enter marks in English (out of 100): "))
# hindi = int(input("Enter marks in Hindi (out of 100): "))
# sst = int(input("Enter marks in SST (out of 100): "))

# # Validation
# if (math > 100 or science > 100 or english > 100 or hindi > 100 or sst > 100):
#     print("❌ Error: Marks cannot be more than 100.")
#     exit()

# # Total and Percentage
# total_marks = math + science + english + hindi + sst
# percentage = total_marks / 5

# # Grade and Pass/Fail
# if math < 33 or science < 33 or english < 33 or hindi < 33 or sst < 33:
#     result = "Fail"
#     grade = "F"
# else:
#     result = "Pass"
#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B+"
#     elif percentage >= 60:
#         grade = "B"
#     elif percentage >= 50:
#         grade = "C"
#     else:
#         grade = "D"

# # Output
# print("\n------ STUDENT MARKSHEET ------")
# print("Name:", name)
# print("Roll No:", roll_no)
# print("Math:", math)
# print("Science:", science)
# print("English:", english)
# print("Hindi:", hindi)
# print("SST:", sst)
# print("------------------------------")
# print("Total Marks:", total_marks, "/ 500")
# print("Percentage:", percentage, "%")
# print("Result:", result)
# print("Grade:", grade)
# print("------------------------------")

# # Check failed subjects
# failed_subjects = []

# if math < 33:
#     failed_subjects.append("Math")
# if science < 33:
#     failed_subjects.append("Science")
# if english < 33:
#     failed_subjects.append("English")
# if hindi < 33:
#     failed_subjects.append("Hindi")
# if sst < 33:
#     failed_subjects.append("SST")

# # Result and Grade
# if len(failed_subjects) > 0:
#     result = "Fail"
#     grade = "F"
# else:
#     result = "Pass"
#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B+"
#     elif percentage >= 60:
#         grade = "B"
#     elif percentage >= 50:
#         grade = "C"
#     else:
#         grade = "D"

# # Output
# print("\n------ STUDENT MARKSHEET ------")
# print("Name:", name)
# print("Roll No:", roll_no)
# print("Math:", math)
# print("Science:", science)
# print("English:", english)
# print("Hindi:", hindi)
# print("SST:", sst)
# print("------------------------------")
# print("Total Marks:", total_marks, "/ 500")
# print("Percentage:", percentage, "%")
# print("Result:", result)
# print("Grade:", grade)

# # Yeh line sirf fail hone par print hogi
# if result == "Fail":
#     print("❌ Failed in subjects:", ", ".join(failed_subjects))

# print("------------------------------")

name=input("enter your name:")
print("hello:",name)
age=int(input("enter your age:"))
print("madarchod:",age,"ka hai tum")
for i in range (3):
    name=input("nam likho :")
    print("welcome",name)
