import os
import json
from colored import fg, attr
from google.oauth2.service_account import Credentials
import gspread
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Colour variables
GR = fg("dark_olive_green_2")
RD = fg("light_red")
GD = fg("gold_3a")
YL = fg("light_yellow")
BL = fg("turquoise_2")
R = attr("reset")

if os.environ.get('CREDS'):
    CREDS = Credentials.from_service_account_info(json.loads(os.environ.get('CREDS')))
else:
    CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('knowledge_quiz')

# Welcoming text
print(GR + "Welcome to General Knowledge Quiz" + R)
print(". . . . . . . . . . . . . . . . . . . . . . ")
print("The quiz has 10 questions about general knowledge. ")
print(". . . . . . . . . . . . . . . . . . . . . . ")
print("The game has two levels of difficulty.")
print("You can choose easy or difficult levels.")
print("There are 4 possible answers to each question. ")
print("You can choose A, B, C, or D. ")
print("At the end of the game, you can see the correct answers and compare them with the answers you gave.")
print(". . . . . . . . . . . . . . . . . . . . . . ")
print(BL + "I hope you will enjoy it:)" + R)
print(". . . . . . . . . . . . . . . . . . . . . . ")

# Ask if the player wants to start the game
players_name = ""
players_name = input(GR + "Please enter your name: \n" + R)
print(YL + "Hello " + str(players_name) + "", "I wish you the best of luck!\n" + R)


# User can choose the level of difficulty
def choose_difficulty_level():
    while True:
        print(GR + "Which difficulty level do you want to play?" + R)
        level = input("Write (e) for EASY or (d) for DIFFICULT: ").lower()
        if level in ('easy', 'difficult', 'e', 'd'):
            return 'easy' if level == 'e' else 'difficult'
        else:
            print("Invalid choice, please choose either 'easy' or 'difficult' (or 'e' or 'd').")
            
            
# Starting the game
def start_game():
    responses = []
    correct_responses = 0
    question_num = 1

    # Ask for the difficulty level
    while True:
        difficulty = choose_difficulty_level()
        if difficulty not in ('easy', 'difficult'):
            print(RD + "Invalid choice, the only options are easy or difficult" + R)
        else:
            break

    # Select questions based on the difficulty level
    if difficulty == 'easy':
        questions = easy_questions
        options = easy_options
    else:
        questions = difficult_questions
        options = difficult_options

    for key in questions:
        print(". . . . . . . . . . . . . . . . . . . . . . ")
        print(BL + key + R)
        for i in options[question_num - 1]:
            print(i)

        # Verify if the player is choosing a valid reply
        while True:
            reply = input("Choose (A, B, C, or D): \n")
            reply = reply.upper()
            if reply not in ('A', 'B', 'C', 'D'):
                print(RD + "Wrong choice, the only options are A, B, C, or D" + R)
            else:
                break

        responses.append(reply)

        correct_responses += verify_score(questions.get(key), reply)
        question_num += 1

    # Assign correct_responses to score
    score = correct_responses

    show_score(correct_responses, responses, questions, difficulty)

    # Update the leaderboard
    update_leaderboard(players_name, score, responses, difficulty)

    # Printing the leaderboard
    print_leaderboard(difficulty)

    # Return the score
    return score  


# Verifying if reply is correct or incorrect 
def verify_score(score, reply):
    if reply == score:
        print(GD + " Good answer" + R)
        return 1
    else:
        print(RD + "This is the wrong answer" + R)
        return 0


# Showing the players' answers and the correct answers
def show_score(correct_responses, responses, questions, difficulty):
    print(". . . . . . . . . . . . . . . . . . . . . . ")
    print(BL + f"                 YOUR SCORE - {players_name}                 " + R)
    print(". . . . . . . . . . . . . . . . . . . . . . ")

    percentage = (correct_responses / len(questions)) * 100
    print(". . . . . . . . . . . . . . . . . . . . . . ")
    print(GR + f"{players_name}, you got {percentage}% of good answers!" + R)
    print(". . . . . . . . . . . . . . . . . . . . . . ")

    print("These are your replies: ", end="")
    for i in responses:
        print(GD + i + " " + R, end="")
    print()
    print(". . . . . . . . . . . . . . . . . . . . . . ")

    print("These are the correct ones: ", end="")
    for i in questions.values():
        print(YL + i + " " + R, end="")
    print()
    print(". . . . . . . . . . . . . . . . . . . . . . ")


# Update the details of leaderboard
def update_leaderboard(player_name, score, responses, difficulty):
    sheet_name = f'leaderboard_{difficulty.lower()}'
    try:
        leaderboard = SHEET.worksheet(sheet_name)
    except gspread.WorksheetNotFound:
        # Create the sheet if it doesn't exist
        leaderboard = SHEET.add_worksheet(sheet_name, 1, 3)
        leaderboard.update_acell('A1', 'Player Name')
        leaderboard.update_acell('B1', 'Score')
        leaderboard.update_acell('C1', 'Responses')

    leaderboard.append_row([player_name, score, ', '.join(responses)])


# Print the leaderboard 
def print_leaderboard(difficulty):
    try:
        leaderboard = SHEET.worksheet(f'leaderboard_{difficulty.lower()}')
        # Skip the header row
        data = leaderboard.get_all_values()[1:] 
        # Sort by score in descending order
        data.sort(key=lambda x: int(x[1]), reverse=True) 

        # Shows the player's name and score from the data
        simplified_data = [[row[0], row[1]] for row in data]

        # Print the leaderboard in a tabular format
        print(GD + tabulate(simplified_data[:10], headers=['Player Name', 'Score']) + R)
    except gspread.WorksheetNotFound:
        print(RD + "Leaderboard not available for this difficulty." + R)

# This function is asking the user if he wants to try again or end the game
def restart_game():
    while True:
        response = input(str(players_name) + ", would you like to try play one more time? (yes or no): \n")
        response = response.upper()
        if response not in ('YES', 'NO'):
            print("Invalid choice, the only options are YES or NO")
        elif response == "YES":
            return True
        else:
            break


# Quiz questions and answers with two levels 
# Difficult questions
difficult_questions = {
    "1. Which ancient wonder was located in Alexandria, Egypt?": "C",
    "2. What is the currency of Japan?": "C",
    "3. In computer science, what does the acronym 'SQL' stand for?": "C",
    "4. Who discovered penicillin?": "A",
    "5. What is the boiling point of water in Fahrenheit?": "A",
    "6. What is the smallest prime number?": "C",
    "7. What is the capital city of Bhutan?": "A",
    "8. In physics, what is the fundamental force responsible for radioactivity?": "B",
    "9. Which artist painted 'Starry Night'?": "A",
    "10. What is the powerhouse of the cell?": "B"
}

# Difficult answets

difficult_options = [
    ["A. Great Wall of China", "B. Hanging Gardens of Babylon", "C. Lighthouse of Alexandria", "D. Colossus of Rhodes"],
    ["A. Yuan", "B. Won", "C. Yen", "D. Ringgit"],
    ["A) Structured Question Language", "B) System Query Language", "C) Standard Query Language", "D) Sequential Query Language"],
    ["A. Alexander Fleming", "B. Louis Pasteur", "C. Joseph Lister", "D. Robert Koch"],
    ["A. 212°F", "B. 100°F", "C. 180°F", "D. 32°F"],
    ["A. 0", "B. 1", "C. 2", "D. 3"],
    ["A. Thimphu", "B. Kathmandu", "C. Dhaka", "D. Colombo"],
    ["A) Electromagnetic force", "B) Weak nuclear force", "C) Strong nuclear force", "D) Gravitational force"],
    ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
    ["A) Nucleus", "B) Mitochondria", "C) Endoplasmic reticulum", "D) Golgi apparatus"]
]

# Easy questions

easy_questions = {
    "1. What is the biggest island in the world?": "D",
    "2. Which gas is the most in the Earth's atmosphere?": "B",
    "3. Arsonphobia is a fear of:": "C",
    "4. What is the lifetime of a dragonfly?": "A",
    "5. Which planet is close to the sun?": "D",
    "6. What is the name of the god of the seas and oceans in Greek mythology?": "A",
    "7. How many time zones does Australia have?": "B",
    "8. What is the name of the largest country in the world?": "C",
    "9. How many colors does the rainbow have?": "C",
    "10. What is the chemical symbol of silver?": "D"
}

# Easy answers

easy_options = [
    ["A Madagascar", "B. Java", "C. New Zealand", "D. Greenland"],
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

print(YL + "Thank you for playing " + str(players_name) + "! Hope to see you soon:)" + R)

