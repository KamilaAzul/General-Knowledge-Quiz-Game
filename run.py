
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


# intro text 
   
print("Welcome to Knowledge Quiz")
print("-------------------------")
print("The quiz has 10 questions about general knowledge ")
print("-------------------------")

# Ask if player wants to start game

players_name = ""
players_name = input("Please enter your name: \n")
print("Hello "+str(players_name)+"", "I wish you the best of luck!\n")


def start_game():

    responses = []
    correct_responses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        # Verify if the player is choosing a valid reply
        while True:
            reply = input("Choose(A, B, C, or D): \n")
            reply = reply.upper()
            if reply not in ('A', 'B', 'C', 'D'):
                print("Wrong choice, the only options are A, B, C, or D")
            else:
                break

        responses.append(reply)

        correct_responses += verify_score(questions.get(key), reply)
        question_num += 1

    show_score(correct_responses, responses) 
     
# Verifying if the player gave a corect or incorrect reply


def verify_score(score, reply):

    if reply == score:
        print(" Good answer")
        return 1
    else:
        print("This is wrong answer")
        return 0

# This fucntion will show the correct results and the choices


def show_score(correct_responses, responses):

    print(". . . . . . . . . . . . . . . . . . . . . . ")
    print("                 YOUR SCORE                 ")
    print(". . . . . . . . . . . . . . . . . . . . . . ")

    percentage = (correct_responses/len(questions)) * 100
    print(". . . . . . . . . . . . . . . . . . . . . . ")
    print(str(players_name)+", you got " + str(percentage) + "% of good answers!")
    print(". . . . . . . . . . . . . . . . . . . . . . ")

    print("Those are yours replies: ", end="")
    for i in responses:
        print(i, end=" ")
    print()
    print(". . . . . . . . . . . . . . . . . . . . . . ")

    print("Those are correct ones: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print(". . . . . . . . . . . . . . . . . . . . . . ")


    
# This fucntion is asking the user if he wants to try again or end the game


def restart_game():
    while True:
        response = input(str(players_name)+", would you like to try play one more time? (yes or no): \n")
        response = response.upper()
        if response not in ('YES', 'NO'):
            print("Invalid choice, the only options are YES or NO")
        elif response == "YES":
            return True
        else:
            break


# Quiz questions and answers

questions = {
    "1: What is the biggest island in the world?": "D",
    "2: Which gas is the most in the Earth's atmosphere?": "B",
    "3: Arsonphobia is a fear of:": "C",
    "4: What is the lifetime of a dragonfly?": "A",
    "5: Which planet is close to the sun?": "D",
    "6: What is the name of the god of the seas and oceans in Greek mythology?": "A",
    "7: How many time zones does Australia have?": "B",
    "8: What is the name of the largest country in the world?": "C",
    "9: How many colors does the rainbow have?": "C",
    "10: What is the chemical symbol of silver?": "D"
    }


options = [["A Madagascar", "B. Java", "C. New Zealand", "D. Greenland"],
           ["A. Oxygen",  "B. Nitrogen", "C. Carbon dioxide", "D. Ozone"],
           ["A. Spiders", "B. Water ", "C. Fire", "D. Poison"],
           ["A. 24 hours", "B. One week", "C. One month", "D. Six months"],
           ["A. Mars", "B. Venus ", "C. Earth", "D. Mercury"],
           ["A. Poseidon", "B. Apollo", "C. Zeus", "D. Dionysus"],
           ["A. 2", "B. 3", "C. 4", "D. 1"],
           ["A. Canada", "B. USA", "C. Russia", "D. India"],
           ["A. Five", "B. Six", "C. Seven", "D. Eight"],
           ["A. Na", "B. Fa", "C. Cu", "D. Ag"]]

start_game()

while restart_game():
   start_game()

print("Thank you for playing! Byeee:)")
