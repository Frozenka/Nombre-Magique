#!/usr/bin/ env python3
""" 
Programme : Nombre magique
Créateur  : Frozenk
Interet   : Entrainement
Date      : 17/01/2023
"""
#imports
import random
import colorama
import os
import importlib
#déclarations
menu_ok        =  False

#Fonction effacement console
def clear():
    if os.name == "posix": #gestion linux
        if importlib.util.find_spec("colorama") is None:
            import pip
            pip.main(['install','colorama'])
            print("installation de colorama")
            
        os.system("clear")
    else:
        ose.system("cls") #gestion  pour windows

#Affichage bienvenue
clear()
print("Bienvenue dans le jeux du chiffre magique")
print("Veuillez choisir la difficulté :")
print(colorama.Fore.BLUE + "1 : Classique")
print(colorama.Fore.RED  + "2 : Insane\n" + colorama.Style.RESET_ALL)

#fonction du principal du jeux
def Dificult(Nb_max,Nb_try,Dificile):
    clear()
    print(f"Difficulté classique : Nombres compris entre {colorama.Fore.LIGHTBLACK_EX} 0 et {Nb_max}{colorama.Style.RESET_ALL}")
    print(f"Nombres de vies : {Nb_try}")
    Nombre_magique = random.randint(1, Nb_max)
    Victoire       =  False
 


    # Gestion du cas ou un utilisateur ne rentre pas un entier
    while Victoire == False and Nb_try >= 1:
        try:
            Nb_user = int(input("Votre nombre : "))
        except ValueError:
            print(f" {colorama.Fore.YELLOW} /!\ SEULEMENT DES NOMBRES /!\ {colorama.Style.RESET_ALL} ")
            continue

       #gestion des réponses
        if Nb_user == Nombre_magique:
            print(colorama.Fore.GREEN + "\n !!!!  VICTOIRE  !!!!" + colorama.Style.RESET_ALL)
            Victoire = True
        elif Nb_user > Nb_max:
            print(f"{colorama.Fore.RED}ATTENTION le nombre maximum est {Nb_max}, {colorama.Fore.LIGHTRED_EX}vous avez perdu une vie bêtement\nil vous en restes :{Nb_try}{colorama.Style.RESET_ALL}")
        elif Nb_user < 1:
            print(f"{colorama.Fore.RED}ATTENTION le nombre minimum est 1, {colorama.Fore.LIGHTRED_EX}vous avez perdu une vie bêtement\nil vous en restes :{Nb_try}{colorama.Style.RESET_ALL}")
 
        else:
            Nb_try = Nb_try -1
            if Nb_try < 1:
                print(colorama.Fore.LIGHTRED_EX + "/!\ Vous avez perdu /!\ "+ colorama.Style.RESET_ALL)
            else:
                # Gestion couleurs :
                if Nb_try > 10:
                    color = colorama.Fore.BLUE
                elif Nb_try <= 10:
                    color = colorama.Fore.RED
                print(f"Il ne vous reste que {color}{Nb_try}{colorama.Style.RESET_ALL} essais")
                if Dificile:
                    clear()
                    
                 # Aide utilisateur 
                if Nb_user > Nombre_magique:
                    print(f"Le nombre magique est{colorama.Fore.LIGHTWHITE_EX} plus petit{colorama.Style.RESET_ALL}")
                elif Nb_user < Nombre_magique:
                    print(f"Le nombre magique est{colorama.Fore.LIGHTWHITE_EX} plus grand{colorama.Style.RESET_ALL}")

#Fonction menu       
def menu():
    Choix_difficult = (input("Votre choix :"))
    return (Choix_difficult)

# boucle du menu
while  menu_ok == False:
    choix = menu()
    if choix == "1":
        menu_ok = True
        Dificult(50,8,False)
    elif choix == "2":
        menu_ok = True
        Dificult(300,10,True)
    else:
        print("Erreur veuillez choisir un chiffre 1 ou 2")
        menu()

