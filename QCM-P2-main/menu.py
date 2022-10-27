import time
from termcolor import colored

def sleep(t):
    return time.sleep(t)

def menu():
    print("---------------------------------------------------------")
    print("Welcome to this little MCQ Game !")
    sleep(1)
    print("You will have to answer to some questions but it will not be hard !")
    sleep(1)
    print("Are you ready to play ? y/n")
    print("---------------------------------------------------------")
    ready = ""
    while ready.lower() != "y":
        ready = input("==> ") 
        if ready == "y":
            sleep(0.5)
        else:
            print("Okay take your time !") 
            sleep(0.5)
            print("And now ?")   
    cotation_presentation()   

def cotation_presentation():
    print("There are three system of cotation !")
    sleep(1)
    print("1.")
    sleep(1)
    print("The first one is the classic :")
    sleep(1)
    print("You gain a point when your answer is right")
    sleep(1)
    print("2.")
    sleep(1)
    print("The second cotation is the negative one")
    sleep(1)
    print("You gain a point when its correct and when its false...")
    sleep(1)
    print("You lose a point !")
    print("3.")
    sleep(1)
    print("On calcule l'ésperance de vos réponse bref je sais pas trop comment expliquer lol")
    sleep(1)

def color(text, color):
    return print(colored(text, color, attrs=['bold', 'blink', "reverse"]))