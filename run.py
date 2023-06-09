
questions = ("What is the biggest island in the world?: ", 
             "Which gas is the most in the Earth's atmosphere?: ", 
             "Arsonphobia is a fear of: ", 
             "What is the lifetime of a dragonfly?: ", 
             "Which planet is close to the sun?: ", 
             "What is the name of the god of the seas \
              and oceans in Greek mythology?: ", 
             "How many time zones does Australia have?: ", 
             "What is the name of the largest country in the world?: ", 
             "How many colors does the rainbow have?: : ", 
             " What is the chemical symbol of silver?: ") 

options = (("A Madagascar", "B. Java", "C. New Zealand" "D. Greenland"), 
           ("A. Oxygen",  "B. Nitrogen", "C. Carbon dioxide", "D. Ozone"), 
           ("A. Spiders", "B. Water ", "C. Fire", "D. Poison"), 
           ("A. 24 hours", "B. One week", "C. One month", "D. Six months"), 
           ("A. Mars", "B. Venus ", "C. Earth", "D. Mercury"), 
           ("A. Poseidon", "B. Apollo", "C. Zeus", "D. Dionysus"), 
           ("A. 2", "B. 3", "C. 4", "D. 1"), 
           ("A. Canada", "B. USA", "C. Russia", "D. India"), 
           ("A. Five", "B. Six", "C. Seven", "D. Eight"),
           ("A. Na", "B. Fa", "C. Cu", "D. Ag")) 

answers = ("D", "B", "C", "A", "D", "A", "B", "C", "C", "D")
guesses = []
points = 0
question_num = 0

for questions in questions:
    print("-----------------------")
    print(questions)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, or D): \n").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        points = points + 1
        print("Good answer")
    else:
        print("Wrong answer")

    question_num = question_num + 1

def show_score():


    print(".............................")
    print("        Your score           ")
    print(".............................")


    percentage = (correct_answer/10) * 100
    print("you got " + str(percentage) + "% of good answers!")
