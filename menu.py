import time
from termcolor import colored

def sleep(t):
    return time.sleep(t)

def menu():
    print("---------------------------------------------------------")
    print("Welcome to this little MCQ Game !")
    sleep(0)
    print("You will have to answer to some questions but it will not be hard !")
    sleep(0)
    print("Are you ready to play ? y/n")
    print("---------------------------------------------------------")
    ready = ""
    while ready.lower() != "y":
        ready = input("==> ") 
        if ready == "y":
            sleep(0)
        else:
            print("Okay take your time !") 
            sleep(0)
            print("And now ?")   
    cotation_presentation()   

def cotation_presentation():
    print("There are three system of cotation !")
    sleep(0)
    print("The first one is the classic :")
    sleep(0)
    print("You gain a point when your answer is right")
    sleep(0)
    print("The second cotation is the negative one")
    sleep(0)
    print("You gain a point when its correct and when its false...")
    sleep(0)
    print("You lose a point !")

def color(text, color):
    return print(colored(text, color, attrs=['bold', 'blink', "reverse"]))