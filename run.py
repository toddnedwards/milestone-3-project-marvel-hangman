import gspread
from google.oauth2.service_account import Credentials
import os



# add text animation from pyfiglet
from pyfiglet import Figlet


# google drive credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# google sheets credentials

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('words')

# welcome to the game

def welcome_message():
    print("Welcome to Marvel Hangman! \n You will be tested on all your favourite marvel characters and items found in the movie!")

def options():
    options_answer = input("would you like to proceed? y/n ")
    if options_answer.lower() == "y":
        start_game()
    elif options_answer.lower() == "n":
        welcome_message()
        options()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Setup word and hidden list



# Loop until either the player has won or lost


# display the current boards, guessed letters, and attempts remaing


# ask the player for character


# if guessed correctly, show all matched letters and print message


# if guessed incorrectly, print fail message and increment attempts 


# if player has won, print a win message and stop loop


# if the player has lost, print fail message and stop loop


#main
welcome_message()
options()