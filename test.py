# Google API imported with thanks to Code Institute Tutorial 'Love Sandwiches' by Anna Greaves.

import json #https://docs.python.org/3/library/json.html
import gspread #https://docs.gspread.org/en/latest/
import requests #https://docs.python-requests.org/en/latest/
import html #https://docs.python.org/3/library/html.html
import random #https://docs.python.org/3/library/random.html
import os #https://docs.python.org/3/library/os.html
import sys
# from package_python import personality
# from package_python import finalreport
from google.oauth2.service_account import Credentials
from pprint import pprint
from prettytable import PrettyTable
x = PrettyTable()

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

CREDS = Credentials.from_service_account_file('creds.json') # creds.json is a file that is not pushed to github
SCOPED_CREDS = CREDS.with_scopes(SCOPE) #creds.with_scopes is a method that takes in the scope variable. The scope variable is a list of API's that we want to access.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) # gspread.authorize is a method that takes in the SCOPED_CREDS variable. This variable is the credentials we created to access the API's.
SHEET = GSPREAD_CLIENT.open('Steam_Test') # name of the spreadsheet

class SubjectScore:
    """
    Update the score in the local variable, using a class to update
    player1. updateScore += 1
    """
    def __init__(self, scoreScience, scoreTechnology, scoreEnglish, scoreArt, scoreMath, scoreTotal):
        self.scoreScience = scoreScience
        self.scoreTechnology = scoreTechnology
        self.scoreEnglish = scoreEnglish
        self.scoreArt = scoreArt
        self.scoreMath = scoreMath
        self.scoreTotal = scoreTotal
    
    def updateScienceScore(self):
        self.scoreScience += 1
        return self.scoreScience
    
    def updateTechnologyScore(self):
        self.scoreTechnology += 1
        return self.scoreTechnology
    
    def updateEnglishScore(self):
        self.scoreEnglish += 1
        return self.scoreEnglish
    
    def updateArtScore(self):
        self.scoreArt += 1
        return self.scoreArt
    
    def updateMathScore(self):
        self.scoreMath += 1
        return self.scoreMath
    
    def updateTotalScore(self):
        self.scoreTotal += 1
        return self.scoreTotal
    
    def resetAllScores(self):
        self.scoreScience = 0
        self.scoreTechnology = 0
        self.scoreEnglish = 0
        self.scoreArt = 0
        self.scoreMath = 0
        self.scoreTotal = 0
        return self.scoreScience, self.scoreTechnology, self.scoreEnglish, self.scoreArt, self.scoreMath, self.scoreTotal

subject_scores = SubjectScore(0,0,0,0,0,0)

username_str = "Betty56"

def generate_comparison_data_main():
    """
    Collects columns of data from score worksheet, collecting the last 5 entries for each sandwich and returns the data as a list of lists.

    “Prettytable.” PyPI, 11 Sept. 2023, pypi.org/project/prettytable/. Accessed 1 Oct. 2023.
    """
    calculateHighestSTEAMScore()
    calculateHighestOCEANScore()

def calculateHighestSTEAMScore():
    worksheet = SHEET.worksheet('score')  # Access worksheet
    data = worksheet.get_all_values()  # Read data
    table = PrettyTable()  # Create PrettyTable object
    table.field_names = data[0]  # Set field names
    all_user_info = []
    for row in data[1:]:  # Populate table and collect user info
        table.add_row(row)
        userinfo = dict(zip(table.field_names, row))
        all_user_info.append(userinfo)
    localuser_data = next((item for item in all_user_info if item["Username"] == username_str), None)    # Filter out the data for username
    if localuser_data:
        # Extract STEAM scores and find the highest category
        steam_categories = ["S", "T", "E", "A", "M"]
        highest_score = -1
        highest_category = ""
        for category in steam_categories:
            score = int(localuser_data[category])
            if score > highest_score:
                highest_score = score
                highest_category = category
            if highest_category == "S":
                highest_category = "Science"
            elif highest_category == "T":
                highest_category = "Technology"
            elif highest_category == "E":
                highest_category = "English"
            elif highest_category == "A":
                highest_category = "Art"
            elif highest_category == "M":
                highest_category = "Math"
        
        print(f"You scored highest in {highest_category}")
    else:
        print(f"Username {username_str} not found")

    #“How to Sort a List of Dictionaries by a Value of the Dictionary in Python?” Stack Overflow, 2023, stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python. Accessed 5 Oct. 2023.
    #“Sort a List of Objects in Python | FavTutor.” FavTutor, 2022, favtutor.com/blogs/sort-list-of-objects-python. Accessed 5 Oct. 2023.

def calculateHighestOCEANScore():
    worksheet = SHEET.worksheet('personality')  # Access 'personality' worksheet
    data = worksheet.get_all_values()  # Read data
    table = PrettyTable()  # Create PrettyTable object
    table.field_names = data[0]  # Set field names
    all_user_info = []

    for row in data[1:]:  # Populate table and collect user info
        table.add_row(row)
        userinfo = dict(zip(table.field_names, row))
        all_user_info.append(userinfo)

    # Filter out the data for the specific username
    localuser_data = next((item for item in all_user_info if item["Username"] == username_str), None)

    if localuser_data:
        # Extract OCEAN scores and find the highest category
        ocean_categories = ["O", "C", "E", "A", "N"]
        highest_score = -1
        highest_category = ""

        for category in ocean_categories:
            score = int(localuser_data[category])
            if score > highest_score:
                highest_score = score
                highest_category = category
            if highest_category == "O":
                highest_category = "Openness"
            elif highest_category == "C":
                highest_category = "Conscientiousness"
            elif highest_category == "E":
                highest_category = "Extraversion"
            elif highest_category == "A":
                highest_category = "Agreeableness"
            elif highest_category == "N":
                highest_category = "Neuroticism"

        print(f"You scored highest in {highest_category}")
    else:
        print(f"Username {username_str} not found")

generate_comparison_data_main()