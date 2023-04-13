#
# Python: 3.6.4
#
# Author: Quiana S. Holder
#
# Purpose: the tech academy- Python course, creating my first
#          program together demonstrating how to pass variables
#          from function to function while producing a functional game.
#
#          Remember, function_name(variable) means that we pass in the variable.
#          return variable means that we are returning the variable back to
#          the calling function

    

def start(nice=0,mean=0,name=""):
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    if name !="":
        print("\nThank you for playing again. {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nwhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M)\n>>>:").lower()
        if pick == "n":
            print("\nWow, you made a stranger smile today!...")
            nice =(nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nWith sadness in their eyes and walks off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n{}, Nice,and ({}, Mean)".format(name,nice,mean))
def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win! \nYou are a sweetheart. \nYour kindness towards others will take you far! Keep it going!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhhh too bad,game over! \n{}, Always remember what goes around comes around. \nTreat others the way you would like to be treated!".format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice =="n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'Yes', (N) for 'No':\n>>>")

            
    

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)

if __name__=="__main__":
    start()
