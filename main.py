
def menu():
    print("######################################")
    print("Bienvenue dans le qcm ")
    print("Pour acceder au cotation classique appuyer sur k")
    print("Pour acceder a une cotation a points négatifs appuyer sur n")
    print("######################################")
    choice = input("=> ")

    if choice == "k":
        print("Vous aurez une cotation classique")
    
    elif choice == "n":
        print("Vous aurez une cotation négatif")
    
    print("Vous êtes prêt ? y/n")
    ready = input("=> ")

    if ready.lower() == "y":
        print("C'est parti")    
menu()



# ce que j'ai rajouté
def build_questionnaire(filename):
    """
        Construit le QCM avec les questions contenue dans le fichier donné.
        :type filename: Un string représentant le nom du fichier a charger.

        :return: Une liste de questions
    """
    questions = []
    wording = None
    choices = []
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            if '|' not in line:
                if wording or choices:
                    questions.append([wording, choices])
                wording = None
                choices = []
            else:
                parts = line.strip().split('|')
                if 1 < len(parts) < 5:
                    if parts[0] == 'Q':
                        if not wording and not choices:
                            wording = parts[1]
                            choices = []
                        else:
                            questions.append([wording, choices])
                            wording = None
                            choices = []
                    elif parts[0] == 'A':
                        if parts[2] not in ('V', 'X'):
                            print("Error when loading line:\n\t{}".format(line))
                        else:
                            choices.append([parts[1], parts[2] == 'V', parts[3] if len(parts) > 3 else ''])
                    else:
                        print("Error when loading line:\n\t{}".format(line))
                else:
                    print("Error when loading line:\n\t{}".format(line))

                if line.startswith('Q'):
                    wording = parts[1]

    if wording or choices:
        questions.append([wording, choices])
    return questions



############################################################### Martin le crack

def menu():
    name = input("What's you're name?")
    print(f"Hello, {name}!")
    print("Let's start the Quizz.")
    


def cotation1(list_of_answers):
    i = 0
    for answer in list_of_answers:
        if answer == True:
            i+=1
        elif answer == False:
            i+=0
        elif answer == None:
            i+=0
    return i 


def cotation2(list_of_answers):
    i = 0
    for answer in list_of_answers:
        if answer == True:
            i+=1
        elif answer == False:
            i-=1
        elif answer == None:
            i+=0
    return i



def resultat_final(i, questions):
    lenght = len(questions)
    if i < lenght/2:
        print(f"{i}/{lenght}")
        print("Nul.")
    elif i == lenght/2:
        print(f"{i}/{lenght}")
        print("Suffisant.")
    elif lenght > i > lenght/2:
        print(f"{i}/{lenght}")
        print("Bien.")
    elif i == lenght:
        print(f"{i}/{lenght}")
        print("Parfait !")
        

def random_QCM():
    import random
    questions = build_questionnaire("QCM.txt")
    list_random = []
    aleatoire_choice = random.choice(questions)
    list_random.append(aleatoire_choice)
    checklist= [0]
    z = 1
    while len(list_random) < len(questions):
        k = 0
        a = random.choice(questions)
        for i in checklist:
            if list_random[i] != a:
                k += 1
        if k == len(checklist):
            list_random.append(a)
            checklist.append(z)
            z += 1
    return list_random

def Quizz():
    menu()
    syst = input("Quel système de cotation voulez-vous utiliser ? 1, 2, 3 ?")
    if syst == "1":
        a = 0
    elif syst == "2":
        a = 1
    print("C'est parti, bonne chance !")
    questions = random_QCM()
    question_1 = questions[0][0]
    question_2 = questions[1][0]
    question_3 = questions[2][0]
    list_of_answers = []
    
    
    answer1 = questions[0][1][0][0]
    question_1 = input(question_1)
    if question_1 == answer1:
        print("Vous avez trouvé la bonne réponse !")
        answer1 = True
        list_of_answers.append(answer1)
    else:
        print("Ceci n'est pas la bonne réponse, il vous faut étudier plus !")
        answer1 = False
        list_of_answers.append(answer1)
    print("Question suivante :")
    
    answer2 = questions[1][1][0][0]
    question_2 = input(question_2)
    if question_2 == answer2:
        print("Vous avez trouvé la bonne réponse !")
        answer2 = True
        list_of_answers.append(answer2)
    else:
        print("Ceci n'est pas la bonne réponse, il vous faut étudier plus !")
        answer2 = False
        list_of_answers.append(answer1)
    print("Question suivante :")
    
    answer3 = questions[2][1][0][0]
    question_3 = input(question_3)
    if question_3 == answer3:
        print("Vous avez trouvé la bonne réponse !")
        answer3 = True
        list_of_answers.append(answer3)
    else:
        print("Ceci n'est pas la bonne réponse, il vous faut étudier plus !")
        answer3 = False
        list_of_answers.append(answer1)
    if a == 0:
        resultat_final(cotation1(list_of_answers), questions)
    elif a == 1:
        resultat_final(cotation2(list_of_answers), questions)
        
    
    
    
    












