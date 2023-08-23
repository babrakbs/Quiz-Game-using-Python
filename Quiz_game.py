questions = ("USA’s second biggest city is ____________?",
             "World Jump Day celebrated on: _____________?",
             "Top _______ highest mountains in the world are collectively called as ‘The Eight-thousanders’?",
             "Bali is an Indonesian Island which is a _________ Island.",
             "Who is the longest serving ruler of Indonesia?")

options = (("A:Seattle", "B:Atlana", "C:Newyork City", "D:Los Angeles"),
           ("A:20 July", "B:21 July", "C:22 July", "D:23 July"),
           ("A:10", "B:12", "C:14", " D:16"),
           ("A:Muslim", "B:Jewish", "C:Buddhist", "D:Hindu"),
           ("A: General Suharto ", "B:Joko Widodo", "C:Sukamo", "D:None of These"))


answers = ["D", "A", "C", "D", "A"]

user_guesses = []

question_numbers = 0

score = 0


for question in questions:
    print("\n",question, "\n")
    for option in options[question_numbers]:
        print(option)
    user_answer = input("Please Enter Your Answer (A, B, C, D): ").upper()
    user_guesses.append(user_answer)
    if user_answer == answers[question_numbers]:
        print("CORRECT ANSWER !")
        score+=10

    else:
        print("INCORRECT ANSWER !")
        print(f"{answers[question_numbers]} is the Correct Answer!")
    question_numbers += 1
    print("<------------------------------------------------------->")

print(f"Your Total Score is =",score)
