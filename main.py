import time
from menu import menu

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
    
def cotation3(list_of_answers, number_of_answers):
    # on calcule l'esperance
    esperancex = -(1/(len(number_of_answers) - 1)) 
    i = 0
    for answer in list_of_answers:
        if answer == True:
            i+=1
        elif answer == False:
            i = i + esperancex
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
    print("Wich cotation system you want to choose ? classic = 1, negative = 2, 3 ?")
    syst = input("==> ")
    if syst == "1":
        a = 0
    elif syst == "2":
        a = 1
    elif syst == "3":
        a = 2
    print("Good luck !")
    questionnaire = random_QCM()
    # ici je stock toutes les questions
    number_of_questions = []
    for i in range(0, len(questionnaire)):
        h = questionnaire[i][0]
        number_of_questions.append(h)
    list_of_answers = []
    place = 0
    for i in number_of_questions:
        question = input(i)
        answer = questionnaire[place][1][0][0]
        if question == answer:
            print("Vous avez trouvé la bonne réponse !")
            answer = True
            list_of_answers.append(answer)
        else:
            print("Ceci n'est pas la bonne réponse, il vous faut étudier plus !")
            answer = False
            list_of_answers.append(answer)
        place += 1
    # ici je définis le nombre de réponses possible
    number_of_questions = []
    for y in range (0, len(questionnaire)):
        b = len(questionnaire[y][1])
        number_of_questions.append(b)
    if a == 0:
        resultat_final(cotation1(list_of_answers), questionnaire)
    elif a == 1:
        resultat_final(cotation2(list_of_answers), questionnaire)
    elif a == 2:
        resultat_final(cotation3(list_of_answers, number_of_questions), questionnaire)
Quizz()