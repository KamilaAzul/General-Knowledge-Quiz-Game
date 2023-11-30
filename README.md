# General Knowledge Quiz: 3rd Project

<br/>  

## Introduction <a name="introduction"></a>  

My third project is a General Knowledge Quiz. It's a small game for people who have the willingness to learn new things and like to test their knowledge.
The script interacts with a Google Sheet to store and display leaderboard data. The game includes questions of varying difficulty levels, and the player's responses are scored and displayed along with correct answers at the end of the game.

<br/>![Quiz](assets/quiz.png)

[Visit the General Knowledge Quiz](https://general-knowledge-quiz-game-eabd9d6363af.herokuapp.com/)  

[Visit the General Knowledge Quiz Repository](https://github.com/KamilaAzul/General-Knowledge-Quiz-Game/blob/main/README.md)

<br/>    

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [The Business Goals of the Website](<#business-goal>)
    * [User Stories](<#user-stories>)
* [**Features**](<#features>)
    * [Quiz Flow](<#quiz-flow>)
* [**Technologies Used**](<#technologies-used>)
    * [Functions](<#classes&functions>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
*  [**Acknowledgements**](<#acknowledgements>)

## User Experience UX

I decided to use a background related to the theme of the game, which makes the quiz visually more pleasant to use.


<br>

### The Business Goal of the Website:

- Websie has no commercial goals. The site's goal is to provide an interactive quiz game to the users.
  
<br/> 

## User Stories

* As a user I want to understand how to play the game.
* As a user I want to choose the game difficulty level.
* As a user I want to play the game.
* As a user I want to see if my answer was correct.
* As a user I want at the end of the game see my score and the other users.
* Someone wants to be able to see the correct answers.
* As a user I want to have the possibility to play one more time.

[Back to top](<#contents>)

## Features

* User is welcome with the short welcoming message and short quiz instructions.
* User is asked to put the name.
* User is greeting “Good Luck” message,
* The user is asked what difficulty level he wants to choose.
* The quiz starts and the user can choose the answer A, B, C or D.
* If the answer is anything else (A, B,C or D)will be given, the user will see this message: "Wrong choice, the only options are A, B, C, or D"
* After answering, the user can see whether the answer was correct or wrong.
* After providing all the answers, the user can see his/her result.
* The user can see his/her answers and compare them with the correct answers
* The user can see the leaderboard with the top ten results.
* Once the game is completed a user will have an option to play one more time or to quit.

**Use of Colours**

- Colours have been utilise to make the questions and answers more legible and the correct and incorrect answer announcements more interesting.

## Quiz Flow

The flowchart shows the entire cycle of the game and the planning process.


## Technologies Used

- [Python](https://www.python.org) is used as the back-end programming language.
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) is used as a cloud-based for game development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)

[Back to top](<#contents>)

## Functions

* The script includes some setup code at the beginning, such as importing necessary modules, setting up Google Sheets API credentials, and printing a welcome message. It uses the gspread library to interact with Google Sheets for leaderboard functionality. Additionally, it uses the colored and tabulate libraries for colorful console output and tabulating leaderboard data.

* The script defines two sets of questions and answers for easy and difficult levels. The questions are stored in dictionaries, and the corresponding answer choices are stored in lists.

### The primary functions used on this application are:

- `def start_game()`
This function initiates the quiz game. It begins by asking the user to choose a difficulty level using `choose_difficulty_level()`.  It presents questions depending on the chosen difficulty level, make validation of the user's responses, it calculates the score, and updates the leaderboard. Function displays the user's score, responses, correct answers, and the leaderboard.
![Alt text](<assets/askingNameLevel.png>)
- `verify_score(score, reply)` 
This function check a correct answer and the user's response, returns 1 if the response is correct and 0 otherwise. It also provides feedback to the user about the correctness of their response.
![Alt text](<assets/wrongAnswer.png>)
- `show_score(correct_responses, responses, questions, difficulty)` 
This function shows the user's score, percentage of correct answers, the user's responses, and the correct answers after completing the quiz.
- `def update_leaderboard(player_name, score, responses, difficulty)`  
This function updates the leaderboard with the player's name, score, and responses. 
- `def print_leaderboard(difficulty)` This function prints the leaderboard for the specified difficulty level. It prints the top 10 players with their scores.

![Alt text](<assets/Score.png>)

- `def restart_game()` 
This function asks the user if they want to play again. If the response is 'YES', it returns True, allowing the game to restart. Otherwise, it breaks out of the loop, ending the game.

[Back to top](<#contents>)

### Imports

I've used the following Python packages and/or external imported packages.


- `os`: it's used to access environment variables using os.environ.get
- `json`: it's used to load JSON data from the environment variable 'CREDS'
- `colored`: a third-party library for adding color to text in the console. It's used here to set color variables for text output.
- `google.oauth2.service_account`: part of the Google API Python client library. It's used for handling Google service account credentials.
- `gspread`: it's a Python wrapper for the Google Sheets API. It's used to interact with Google Sheets.
- `tabulate`: it's a third-party library for creating ASCII tables from data. It's used to format and display the leaderboard.
 
- `SCOPE` containing URLs for different Google API scopes, and it sets up color variables using the colored library.

* The script checks if the 'CREDS' environment variable is set. If it is, it loads the Google service account credentials from the environment variable. Otherwise, it loads them from a file named 'creds.json'.

* The script initializes a Google Sheets client (GSPREAD_CLIENT) and opens a Google Sheet named 'knowledge_quiz'.

* The script then prints a welcome message and asks the user for their name.


### Future Features possible to implement:

* Game Progression- adding more question, creating more levels of difficulty and different fields of knowledge.

[Back to top](<#contents>)

# Testing

I tested my project on [CI Python Linter](https://pep8ci.herokuapp.com) and as well with [Python Checker](https://www.pythonchecker.com/).

![CI Python Linter](assets/pep8ciTesting.png)

* 25: E501 line too long (86 > 79 characters)
43: E501 line too long (107 > 79 characters)
45: E225 missing whitespace around operator
51: E201 whitespace after '('
52: E501 line too long (83 > 79 characters)
55: E302 expected 2 blank lines, found 1
56: E111 indentation is not a multiple of 4
56: E117 over-indented
62: E501 line too long (96 > 79 characters)
65: E302 expected 2 blank lines, found 1
74: E222 multiple spaces after operator
74: E501 line too long (85 > 79 characters)
97: E501 line too long (82 > 79 characters)
118: W291 trailing whitespace
120: W291 trailing whitespace
121: E302 expected 2 blank lines, found 1
130: E302 expected 2 blank lines, found 1
132: E501 line too long (84 > 79 characters)
153: E302 expected 2 blank lines, found 1
166: W291 trailing whitespace
167: E302 expected 2 blank lines, found 1
171: W291 trailing whitespace
173: W291 trailing whitespace
179: E501 line too long (88 > 79 characters)
184: E302 expected 2 blank lines, found 1
186: E501 line too long (107 > 79 characters)
196: W291 trailing whitespace
206: E501 line too long (87 > 79 characters)
214: E501 line too long (120 > 79 characters)
216: E501 line too long (130 > 79 characters)
217: E501 line too long (87 > 79 characters)
221: E501 line too long (111 > 79 characters)
222: E501 line too long (91 > 79 characters)
223: E501 line too long (87 > 79 characters)
234: E501 line too long (85 > 79 characters)
258: E111 indentation is not a multiple of 4
260: E501 line too long (89 > 79 characters)
261: W391 blank line at end of file

I managed to fix some of those errors but ate the end there are still some "line too long" and "trailing whitespace".
They have no impact on the operation of the code.

Final result:

* 23: E501 line too long (86 > 79 characters)
40: E501 line too long (108 > 79 characters)
48: E501 line too long (83 > 79 characters)
59: E501 line too long (96 > 79 characters)
60: W293 blank line contains whitespace
61: W293 blank line contains whitespace
72: E501 line too long (84 > 79 characters)
95: E501 line too long (82 > 79 characters)
116: W291 trailing whitespace
119: W291 trailing whitespace
132: E501 line too long (84 > 79 characters)
168: W291 trailing whitespace
173: W292 no newline at end of file
<br>

![Python Checker](assets/testing.png)


[Back to top](<#contents>)

## User stories testing:

* As a user I want to understand how to play the game.
    * Quiz is very simple to understand. Instruction about the choices is given to the player.
* As a user I want to choose the game difficulty level.
   * User can choose easy or difficult game level.
* As a user I want to play the game.
    * Quiz works with no problems.
* As a user I want to see if my answer was correct.
    * After answering, the player can see whether his answer is correct or not.
* As a user I want at the end of the game see my score and the other users.
    * After the last answer is given, the player's final score will be displayed in a table, together with the scores of the other best users.
* Someone wants to be able to see the correct answers.
    * At the end of the game, the user can see his/her answers and compare them with the correct answers.
* As a user I want to have the possibility to play one more time.
    * After answering all the answers, the player has the option to start the game again.


## Lighthouse validation

Deployed project was tested by the Lighthouse Audit tool to check for any major issues.

![Alt text](assets/Lighthouse.png)

[Back to top](<#contents>)

 ## Deployment

 <br>

 ### How to make a local Clone
1. Navigate to the main page of the repository.
2. Click the green Code Button at top right of the repository.
3. Copy the url for the repository.
4. Open Git Bash and Change the current working directory to where you want the cloned directory.
5. Type git clone, and then paste the URL you previously copied using $ git clone. 
6. Pressing enter will then create your clone.  

[Back to top](<#contents>) 


### How to fork a GitHub Repository
1. Log into GitHub and go to the required Repository.
2. The Fork button is at the top right corner of the page.
3. After clicking on this button the copy of the repository is made in your own GitHub account.  

 [Back to top](<#contents>)

<br/>

### Deploying to Heroku
* Log in to Heroku,
* After login we can see the dashboard. To 'Create new app'
 Select 'New' and click 'Create new app'. 
* Pick a unique name for your app.
* Select your region and create your app.
* In the settings tab find the config vars section 
* Pick 'Reveal config vars',
* Add  'PORT' into the key field and added '8000' into the value field and click 'add'.
* In case you have credentials, for your project, you must create another config vars called 'CREDS' 
* Paste the JSON into the value field.
* In the builldpacks section click 'add buildpack'.
* Add  'Python' and 'save changes, 
* Repeat the process with 'Node',

<br>

![Python&Node](assets/herokuDeployment.png)

<br>

* Go to the Deploy tab and select 'github',
* Confirm connection to your GitHub Account.
* Search for your project repository and click to 'connect'.
* Under the deploy options, you can chose automatic deploys, 
* Choose which branch you want to deploy and click on 'Deploy Branch'.
*  After some time the app is ready,  and we can open the app by using the provided link.

<br>

![Alt text](assets/1.png)
<br> 

[Back to top](<#contents>)

# Credits

* The base for the code comes from this tutorial [YouTube tutorial](https://www.youtube.com/watch?v=yriw5Zh406s).
* This tutorail was very helpful as well [YouTube tutorial](https://www.youtube.com/watch?v=DLn3jOsNRVE&t=1147s).
* The inspiration for Read me file came from this repository on [GitHub](https://github.com/shadeofpurple79/flickers-smarticles/blob/main/README.md?plain=1).

 I also used the following online resources:

* [Code Institute](https://codeinstitute.net/ie/)
* [Slack](https://slack.com/intl/en-ie/) 
* [W3Schools.com](https://www.w3schools.com/)

 ## Acknowledgements

The quiz was completed as a Portfolio Project 3 made for the Full Stack Software Developer (e-Commerce) Diploma at the Code Institute.

I would like to thank all at the Code Institute for their help and support.
[Back to top](<#contents>)
