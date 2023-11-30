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
        data = leaderboard
