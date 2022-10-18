import time


def sleep(t):
    return time.sleep(t)

def menu():
    print("---------------------------------------------------------")
    print("Welcome to this little MCQ Game !")
    sleep(1)
    print("You will have to answer to some questions but it will not be hard !")
    sleep(2.0)
    print("Are you ready to play ? y/n")
    print("---------------------------------------------------------")
    ready = ""
    while ready.lower() != "y":
        ready = input("==> ") 
        if ready == "y":
            sleep(0.5)

        else:
            print("Okay take your time !") 
            sleep(2)
            print("And now ?")   
    cotation_presentation()   


def cotation_presentation():
    print("There is three system of cotation !")
    sleep(2)
    print("The first one is the classic :")
    sleep(2)
    print("You gain a point when your answer is right")
    sleep(2)
    print("The second cotation is the negative")
    sleep(2)
    print("You gain a point when its correct and when its not right...")
    sleep(2)
    print("You lose a point !")