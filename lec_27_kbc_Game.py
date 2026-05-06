#Topic=Kbc_game
#Author=saheer_azmi
#Date=2026


questions = [
    ["Q1: Capital of Bihar?", "A. Delhi", "B. Mumbai", "C. Kolkata", "D. patna","D" ],
    ["Q2: 2+2=?", "A. 3", "B. 4", "C. 5", "D. 6", "B"],
    ["Q3: Python is a ?", "A. Snake", "B. Language", "C. Car", "D. Game", "B"]
]

money = [1000, 2000, 5000]
total_money = 0

for i in range(len(questions)):
    question = questions[i]

    print("\n" + question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == question[5]:
        print("Correct Answer ✅")
        total_money = money[i]
    else:
        print("Wrong Answer ❌")
        break

print("\nYou won ₹", total_money)


#interviews answer :


#📌-we store the correct answer inside the list but do not display it.it is used internally to validate user input .

