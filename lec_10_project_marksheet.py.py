name=input("enter student name:")
roll_no=int(input("enter student roll_no:"))
# subject marks input
math=int(input("enter marks in math(out of 100):"))
science=int(input("enter marks in science(out of 100):"))
hindi=int(input("enter marks in hindi(out of 100):"))
sst=int(input("enter marks in sst9out of 100):"))
english=int(input("enter marks in english):"))

#total and percentage
total_marks=english + hindi+ science+ sst+ math
percentage=total_marks/5

#validation
if english<33 or math<33 or science<33 or hindi<33 or sst<33:
    result="fail"
    grade="f"
else:
    result="pass"
if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B+"
elif percentage>=60:
    grade="B"
elif percentage>=50:
    grade="C"
else:
    grade="D"
 
#output
print("name:",name)
print("roll_no:",roll_no)
print("math:",math)
print("english:",english)
print("science:",science)
print("sst:",sst)
print("hindi:",hindi)
print("total_number:",total_marks,"/500")
print("percentage:",percentage,"%")
print("grade:",grade)
print("result:",result)


# Check failed subjects
failed_subjects = []

if math < 33:
    failed_subjects.append("Math")
if science < 33:
    failed_subjects.append("Science")
if english < 33:
    failed_subjects.append("English")
if hindi < 33:
    failed_subjects.append("Hindi")
if sst < 33:
    failed_subjects.append("SST")

# Result and Grade
if len(failed_subjects) > 0:
    result = "Fail"
    grade = "F"
else:
    result = "Pass"
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

# Output
print("\n------ STUDENT MARKSHEET ------")
print("Name:", name)
print("Roll No:", roll_no)
print("Math:", math)
print("Science:", science)
print("English:", english)
print("Hindi:", hindi)
print("SST:", sst)
print("------------------------------")
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage, "%")
print("Result:", result)
print("Grade:", grade)

# Yeh line sirf fail hone par print hogi
if result == "Fail":
    print("❌ Failed in subjects:", ", ".join(failed_subjects))

print("------------------------------")

