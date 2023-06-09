def choose_play_game():
    """
    Asks the user if they want to play the game or not
    """
    
user_answer = input("Ready to face up to the challenge? (y/n):  \n").upper()

while True:
        if user_answer not in ('YES', 'NO'):
            print("Invalid choice, the only options are YES or NO. Try again: ")
            continue
        elif user_answer == "YES":
            print('Great choice, let the quiz begin!')
            quit()
        else:
            break