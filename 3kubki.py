#gra w 3 kubki

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

mylist = ["","O",""]

shuffle_list(mylist)

def player_guess():
    
    guess=""
    
    while guess not in ["0","1","2"]:
        guess = input("Pick a number: 0, 1 or 2 ")
    
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

#Inital list
mylist = ["","O",""]
#Shuffle list
mixedup_list = shuffle_list(mylist)
#User guess
guess = player_guess()
#Check guess
check_guess(mixedup_list,guess)

input("End of the game")