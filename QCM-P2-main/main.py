
from termcolor import colored
from menu import color, menu, sleep
import random
import string



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
    #cotation 1 classique : 
    # pré : nombre de réponses vrai 
    # post : renvoie la cotation classique finale
    i = 0
    for answer in list_of_answers:
        if answer == True:
            i+=1
        elif answer == False:
            i+=0
        elif answer == None:
            i+=0
    if i < 0:
        i = 0  
    return i 

def cotation2(list_of_answers): 
    #cotation à point négative : 
    # pré : nombre de réponse vrai (+1) et nombre de réponse fausse (-1)
    # post : renvoie la cotation à point negative finale
    i = 0
    for answer in list_of_answers:
        if answer == True:
            i+=1
        elif answer == False:
            i-=1
        elif answer == None:
            i+=0
    if i < 0:
        i = 0  
    return i
    
def cotation3(list_of_answers, super_list):
    #cotation pondérée : 
    # pré : nombre de réponse vrai (+1) et nombre de réponse fausse (- l'esperence )
    # on calcule l'esperance
    # post : renvoie la cotation à point negative pondéré finale
    i = 0
    k = 0
    for answer in list_of_answers:
        if super_list[k] == 1:
            esperancex = 0
        else:
            esperancex = -(1/(len(super_list[k]) - 1)) 
        if answer == True:
            i+=1
        elif answer == False:
            i = i + esperancex
        elif answer == None:
            i+=0
        k += 1
    if i < 0:
        i = 0    
    return i

def resultat_final(i, questions):
    # resultat final :
    # pré : cotation final 
    # post : renvoie une appréciation selon la cotation
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
        
def random_QCM(g):
    # rendre le QCM aléatoire :
    # pré : document txt 
    # post : renvoie les choix aléatoires dans une liste
    questions = build_questionnaire(f"{g}")
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
    run = True
    while run:
        g = input("Insérez le nom du fichier qui contient vos questions : \n ==>")
        menu()
        print("Wich cotation system you want to choose ? classic = 1, negative = 2, esperance = 3 ?")
        syst = input("==> ")
        if syst == "1":
            a = 0
        elif syst == "2":
            a = 1
        elif syst == "3":
            a = 2
        sleep(0.5)
        print("Good luck !")
        print("---------------------")
        questionnaire = random_QCM(g)
        
        # ici je stock toutes les questions
        
        number_of_questions = []
        super_list = []
        for i in range(0, len(questionnaire)):
            h = questionnaire[i][0]
            number_of_questions.append(h)

        place = 0
        b = 0
        x = 0
        list_of_answers = []
        for i in number_of_questions:
            number_of_things = []
            if_true = []
            for v in questionnaire[x][1]:
                if v[1] == True:
                    if_true.append("True")
            x += 1
            katre = 1
            print(i, "\n")
            number_of_answers = []
            if len(if_true) == 1:
                for y in range(0, len(questionnaire[b][1])):
                    number_of_answers.append(questionnaire[place][1][y][0])
                    number_of_things.append([questionnaire[place][1][y][0]])
                super_list.append(number_of_things)
            elif len(if_true) != 1:
                check_list = []
                for y in range(0, len(questionnaire[b][1])):
                    number_of_answers.append(questionnaire[place][1][y][0])
                    check_list.append(questionnaire[place][1][y][0])
                taille = len(check_list) - len(if_true) +1
                while len(number_of_things) < taille:
                    number_of_things.append("a")
                super_list.append(number_of_things)
            random.shuffle(number_of_answers)
            for z in number_of_answers:
                print(str(katre)+":", z)
                katre += 1
            
            if len(if_true) == 1:
                w = input("Answer ==> ")
                while w.isdigit() == False:
                    print("Ceci n'est pas un nombre")
                    w = input("Answer ==> ")
                w = int(w)
                question = number_of_answers[w - 1]
                answer = 0
                for j in questionnaire[place][1]:
                        if j[0] == question:
                            answer = j[1]
                if answer == True:
                    sleep(0.2)
                    color("IT'S RIGHT !!!!", "green")
                    print("-----------------------------------------------------------------------------")
                    list_of_answers.append(answer)
                else:
                    sleep(0.2)
                    color("WRONG !!!!", "red")
                    print("-----------------------------------------------------------------------------")
                    list_of_answers.append(answer)
                place += 1
                b +=1
            elif len(if_true) != 1:
                listing = []
                print("Il y'a plusieurs réponses possibles à cette question, entrez toutes les réponses exactes pour avoir juste !")
                print("Entrez 'YES' si vous pensez avoir toutes les réponses; autrement , entrez une réponse supplémentaire. Si vous avez entré une réponse par erreur, tappez 'REMOVE'")
                while True:
                    s = input("Answer ==> ")
                    s = s.lower()
                    alphabet = list(string.ascii_lowercase)
                    if s in alphabet:
                        print("ceci est une lettre !")
                    elif int(s) > len(number_of_answers):
                        print("Soit vous n'avez rien répondu, soit vous avez écrit n'importe quoi, soit le numéro de la réponse n'existe pas!")
                    elif s == "YES":
                        break
                    elif s == "REMOVE":
                        remove = listing[len(listing) - 1]
                        listing.remove(remove)
                        print(f"Vos réponses actuelles : {listing}")
                    elif s.isdigit() == True and len(s) == 1:
                        s = int(s)
                        listing.append(s)
                        print(f"Vos réponses actuelles : {listing}")
                # donc si la taille des réponses données = la taille des true
                if len(listing) == len(if_true):
                    #on check pour chacune de nos réponses
                    list_if_true = []
                    for i in listing:
                        i = int(i)
                        question = number_of_answers[i - 1]
                        answer = 0
                        for j in questionnaire[place][1]:
                            if j[0] == question:
                                answer = j[1]
                        if answer == True:
                            list_if_true.append(answer)
                    if len(list_if_true) == len(if_true):
                        answer = True
                        sleep(0.2)
                        color("IT'S RIGHT !!!!", "green")
                        print("-----------------------------------------------------------------------------")
                        list_of_answers.append(answer)
                    else:
                        answer = False
                        sleep(0.2)
                        color("WRONG !!!! Soit c'est la mauvaise réponse, soit vous n'avez pas trouvé TOUTES les réponses possibles ! ", "red")
                        print("-----------------------------------------------------------------------------")
                        list_of_answers.append(answer)
                elif len(s) != len(if_true):
                    answer = False
                    sleep(0.2)
                    color("WRONG !!!!", "red")
                    print("-----------------------------------------------------------------------------")
                    list_of_answers.append(answer)

                place += 1
                b += 1
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
            resultat_final(cotation3(list_of_answers, super_list), questionnaire)
        print("Try again ? y/n")
        retry = input("==> ")

        if retry.lower() == "y":
            run = True  
        elif retry.lower() == "n":
            print("Thank you and ciao")
            run = False
            break

Quizz()