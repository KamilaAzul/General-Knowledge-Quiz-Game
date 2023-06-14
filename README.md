# General Knowledge Quiz: 3rd Project

<br/>  

## Introduction <a name="introduction"></a>  

My third project is a General Knowledge Quiz. It's a small game for people who have the willingness to learn new things and like to test their knowledge.

<br/>

[Visit the General Knowledge Quiz.](https://herokuapp.com/)  

[Visit the General Knowledge Quiz. Repository](https://github.com....)

<br/>    

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [Site Structure](<#site-structure>)

* [**Features**](<#features>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
*  [**Acknowledgements**](<#acknowledgements>)

## User Experience UX

## UX Strategy

Game is designed using Python default view in black screen.

<br/> 

## User Stories

 * As a user I want to understand how to play the game.
   * Quiz is very simple to understand. Instruction about the choices is given to the player.
 * As a user I want to play the game.
   * Quiz works with no problems.
 * As a user I want to see if my answer was correct.
   * After answering, the player can see whether his answer was correct or not.
 * As a user I want at the end of the game see my score.
   * After the last answer is given, the player's final score will be displayed.
 * As a user I want to have the possibility to play one more time.
   * After answering all the answers, the player has the option to start the game again.

[Back to top](<#contents>)

## Features

  * User is welcome with the short welcoming message,
  * User is asked to put the name,
  * User is greeting “Good Luck” message,
  * The quiz starts and the user will see after giving the answer if it was right or wrong,
  * If the answer is anything other (A, B,C or D)will be given, a while loop has been implemented that keeps asking the player to enter the correct input'
  * After giving all the answers the user will see obtained score together with all correct answers,
  * Once the game is completed a user will have an option to play one more time or to quit.

## Quiz Flow

The flowchart shows the entire cycle of the game and the planning process.

![Game Flow](<assets/Games starts.png>)

 ### Student Template
 This Template has been provided by the Code Institute and has been used within this quiz. 

## Technologies Used

- [Python](https://www.python.org) is used as the back-end programming language.
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) is used as a cloud-based for game development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.

[Back to top](<#contents>)

### Classes & Functions

The primary functions used on this application are:

- `def start_game()`
* Starts the game, shows questions and answer options and checks player inputs. 
- `def verify_score()` 
* Verifies how many correct answers the player got.
- `def  show_scoree()` 
* Shows the score for the player together with the correct answers.
- `def restart_game()` 
* Gives the player the option to restart the game.

[Back to top](<#contents>)

### Future Features possible to implement:

* Registration and Login- creating an account will allow user to track past scores and games.
* Select Level of Difficulty 
* Game Progression- adding more question, creating different levels of difficulty.

[Back to top](<#contents>)

## Testing

I tested my project on PEP8 as suggested in the course.

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
* Go to the Deploy tab and select 'github',
* Confirm connection to your GitHub Account.
* Search for your project repository and click to 'connect'.
* Under the deploy options, you can chose automatic deploys, 
* Choose which branch you want to deploy and click on 'Deploy Branch'.
*  After some time the app is ready,  and we can open the app by using the provided link.
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
