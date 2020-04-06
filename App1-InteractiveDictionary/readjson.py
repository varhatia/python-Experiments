import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json", "r"))


while True:
    userWord = input("Enter word :")
    
    if(userWord == "Bye"):
        break
    
    elif(data.__contains__(userWord.lower())):
        output = data[userWord.lower()]
    elif(data.__contains__(userWord.upper())):
        output = data[userWord.upper()]
    elif(data.__contains__(userWord.title())):
        output = data[userWord.title()]
    else:
        print("Word not found!!!. Do you want to search one of the matching words below ?")
        
        print(get_close_matches(userWord.lower(), data.keys()))
        
        userChoice = input("Enter Choice, Yes or No !!! : ")
        
        if(userChoice == "Yes"):
            continue
        else:
            print("Sorry, we couldn't help. Thanks for checking!!! Please come again")
            break

    
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
