import requests
import random
import string
import json
import argparse
import os
from apitester import get_cookie, signup_user, make_api_call

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
     print(
        "  _______ _                 _     _       _     _ _   _             \n"
        " |__   __| |               | |   (_)     | |   | | | (_)            \n"
        "    | |  | |__   __ _ _ __ | |__  _ _ __ | |__ | | |_ _  ___  _ __  \n"
        "    | |  | '_ \ / _` | '_ \| '_ \| | '_ \| '_ \| | __| |/ _ \| '_ \ \n"
        "    | |  | | | | (_| | |_) | | | | | |_) | | | | | |_| | (_) | | | |\n"
        "    |_|  |_| |_|\__,_| .__/|_| |_|_| .__/|_| |_|_|\__|_|\___/|_| |_|\n"
        "                     | |             | |                            \n"
        "                     |_|             |_|                            \n")
     

def main():
    print("Welcome to terminalPong!")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    fullname = input("Please enter your fullname: ")
    email = input("Please enter your email: ")

    cookie = get_cookie()
    jwt_token = signup_user(username, password, fullname, email, cookie)
    
    if not jwt_token:
            print("Failed to signup user. Please try again.")

    clear_terminal()

    display_welcome()

    print("Welcome to terminalPong!")
    print("Enter 'help' to see a list of commands.")
    print("Enter 'exit' to exit the game.")
    print("Enter 'play' to play the game.")
    print("Enter 'leaderboard' to see the leaderboard.")
    print("Enter 'logout' to logout.")

    while True:
         selection = input("Please enter a command: ")

if __name__ == '__main__':
    main()