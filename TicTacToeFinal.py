# TicTac
import os
import random
while True:
    try:
        os.system("clear")
        players = input("Single or Multiplyer mode? (S/single, M/multi): ")
        if players == "S" or players == "s" or players == "M" or players =="m":
            break
    except:
        continue
if players == "M" or players == "m":    
    os.system("clear")
    name1 = input("Enter X player name: ")
    name2 = input("Enter O player name: ")
    os.system("clear")
elif players == "S" or players == "s":
    os.system("clear")
    name1 = input("Enter X player name: ")
    name3 = "BOT"
    while True:
        try:
            os.system("clear")
            first = input("Who gonna be the first ? (I/me, B/bot): ")
            if first == "I" or first == "i" or first == "B" or first == "b":
                break
        except:
            continue
    os.system("clear")
Map = {7:" ", 8:" ", 9:" ", 4:" ", 5:" ", 6:" ", 1:" ", 2:" ", 3:" "}
# Definitions:
def Win(x):
    if str(x) == "X":
        print("{} won!".format(name1))
    elif str(x) == "O":
        print("{} won!".format(name2)) 
    elif str(x) == "bot":
        print("{} won!".format(name3)) 
def PrintMap():
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + "|" + CEND + Map[7] + CRED + "|" + CEND + Map[8] + CRED + "|" + CEND + Map[9] + CRED + "|""\n""-------""\n""|" + CEND + Map[4] + CRED+ "|" + CEND + Map[5] + CRED + "|" + CEND + Map[6] + CRED + "|""\n""-------""\n""|" + CEND + Map[1] + CRED + "|" + CEND + Map[2] + CRED + "|" + CEND + Map[3] + CRED + "|" + CEND)
def ChooseX():
    while True:
        try:
            while True:
                choose = input(name1 + ": ")
                os.system("clear")
                if str(Map[int(choose)]) != " ":
                    PrintMap()
                    print("Taken!")
                else:
                    break
            Map[int(choose)] = "X"
            PrintMap()
            break
        except:
            PrintMap()
            continue  
def ChooseO():
    while True:
        try:
            while True: 
                choose = input(name2 + ": ")
                os.system("clear")
                if str(Map[int(choose)]) != " ":
                    PrintMap()
                    print("Taken!")
                else:
                    break
            Map[int(choose)] = "O"
            PrintMap()
            break
        except:
            PrintMap()
            continue
def Game():
    PrintMap()
    while True:
        ChooseX()
        if Map[1] == "X" and Map[2] == "X" and Map[3] == "X" or Map[4] == "X" and Map[5] == "X" and Map[6] == "X" or Map[7] == "X" and Map[8] == "X" and Map[9] == "X" or Map[1] == "X" and Map[4] == "X" and Map[7] == "X" or Map[2] == "X" and Map[5] == "X" and Map[8] == "X" or Map[3] == "X" and Map[6] == "X" and Map[9] == "X" or Map[1] == "X" and Map[5] == "X" and Map[9] == "X" or Map[3] == "X" and Map[5] == "X" and Map[7] =="X":
            return Win("X")
            break
        elif Map[1]=="O" and Map[2]=="O" and Map[3]=="O" or Map[4]=="O" and Map[5]=="O" and Map[6]=="O" or Map[7]=="O" and Map[8]=="O" and Map[9]=="O" or Map[1]=="O" and Map[5]=="O" and Map[9]=="O" or Map[3]=="O" and Map[5]=="O" and Map[7]=="O" or Map[1]=="O" and Map[4]=="O" and Map[7]=="O" or Map[2]=="O" and Map[5]=="O" and Map[8]=="O" or Map[3]=="O" and Map[6]=="O" and Map[9]=="O":
            return Win("O")
            break
        elif Map[1] != " " and Map[2] != " " and Map[3] != " " and Map[4] != " " and Map[5] != " " and Map[6] != " " and Map[7] != " " and Map[8] != " " and Map[9] != " ": 
            print("Game Over!")
            break
        ChooseO()
        if Map[1] == "X" and Map[2] == "X" and Map[3] == "X" or Map[4] == "X" and Map[5] == "X" and Map[6] == "X" or Map[7] == "X" and Map[8] == "X" and Map[9] == "X" or Map[1] == "X" and Map[4] == "X" and Map[7] == "X" or Map[2] == "X" and Map[5] == "X" and Map[8] == "X" or Map[3] == "X" and Map[6] == "X" and Map[9] == "X" or Map[1] == "X" and Map[5] == "X" and Map[9] == "X" or Map[3] == "X" and Map[5] == "X" and Map[7] =="X":
            return Win("X")
            break
        elif Map[1]=="O" and Map[2]=="O" and Map[3]=="O" or Map[4]=="O" and Map[5]=="O" and Map[6]=="O" or Map[7]=="O" and Map[8]=="O" and Map[9]=="O" or Map[1]=="O" and Map[5]=="O" and Map[9]=="O" or Map[3]=="O" and Map[5]=="O" and Map[7]=="O" or Map[1]=="O" and Map[4]=="O" and Map[7]=="O" or Map[2]=="O" and Map[5]=="O" and Map[8]=="O" or Map[3]=="O" and Map[6]=="O" and Map[9]=="O":
            return Win("O")
            break
        elif Map[1] != " " and Map[2] != " " and Map[3] != " " and Map[4] != " " and Map[5] != " " and Map[6] != " " and Map[7] != " " and Map[8] != " " and Map[9] != " ": 
            print("Game Over!")
            break  
def BotChoose():
    while True:
        c = random.choice(range(1,9))
        if Map[7] == "O" and Map[4] == "O" and Map[1] ==" " or Map[9] == "O" and Map[5] == "O" and Map[1] ==" " or Map[2] == "O" and Map[3] == "O" and Map[1] ==" ":                             #74(1)
            c = 1               
        elif Map[8] == "O" and Map[5] == "O" and Map[2] ==" " or Map[1] == "O" and Map[3] == "O" and Map[2] ==" ":                           #85(2)
            c = 2        
        elif Map[9] == "O" and Map[6] == "O" and Map[3] ==" " or  Map[7] == "O" and Map[5] == "O" and Map[3] ==" " or Map[1] == "O" and Map[2] == "O" and Map[3] ==" ":                           #96(3)
            c = 3           
        elif Map[1] == "O" and Map[7] == "O" and Map[4] ==" " or Map[5] == "O" and Map[6] == "O" and Map[4] ==" ":                           #17(4)
            c = 4       
        elif Map[2] == "O" and Map[8] == "O" and Map[5] ==" " or Map[7] == "O" and Map[3] == "O" and Map[5] ==" " or Map[1] == "O" and Map[9] == "O" and Map[5] ==" " or Map[4] == "O" and Map[6] == "O" and Map[5] ==" ":                           #28(5)
            c = 5   
        elif Map[3] == "O" and Map[9] == "O" and Map[6] ==" " or Map[4] == "O" and Map[5] == "O" and Map[6] ==" ":                           #39(6)
            c = 6 
        elif Map[1] == "O" and Map[4] == "O" and Map[7] ==" " or Map[3] == "O" and Map[5] == "O" and Map[7] ==" " or Map[8] == "O" and Map[9] == "O" and Map[7] ==" ":                           #14(7)
            c = 7  
        elif Map[2] == "O" and Map[5] == "O" and Map[8] ==" " or Map[7] == "O" and Map[9] == "O" and Map[8] ==" ":                           #25(8)
            c = 8  
        elif Map[3] == "O" and Map[6] == "O" and Map[9] ==" " or Map[1] == "O" and Map[5] == "O" and Map[9] ==" " or Map[7] == "O" and Map[8] == "O" and Map[9] ==" ":                           #36(9)
            c = 9  
        #védekezik
        elif Map [7] == "X" and Map[4] == "X" and Map[1] == " " or Map[9] == "X" and Map[5] == "X" and Map[1] == " " or Map[2] == "X" and Map[3] == "X" and Map[1] == " ":                             #74(1)
            c = 1               
        elif Map[8] == "X" and Map[5] == "X" and Map[2] == " " or Map[1] == "X" and Map[3] == "X" and Map[2] == " ":                           #85(2)
            c = 2        
        elif Map[9] == "X" and Map[6] == "X" and Map[3] == " " or Map[7] == "X" and Map[5] == "X" and Map[3] == " " or Map[1] == "X" and Map[2] == "X" and Map[3] == " ":                           #96(3)
            c = 3           
        elif Map[5] == "X" and Map[6] == "X" and Map[4] == " " or Map[1] == "X" and Map[7] == "X" and Map[4] == " ":                           #17(4)
            c = 4       
        elif Map[2] == "X" and Map[8] == "X" and Map[5] == " " or Map[7] == "X" and Map[3] == "X" and Map[5] == " " or Map[1] == "X" and Map[9] == "X" and Map[5] == " " or Map[4] == "X" and Map[6] == "X" and Map[5] == " ":                           #28(5)
            c = 5   
        elif Map[3] == "X" and Map[9] == "X" and Map[6] == " " or Map[4] == "X" and Map[5] == "X" and Map[6] == " ":                           #39(6)
            c = 6 
        elif Map[1] == "X" and Map[4] == "X" and Map[7] == " " or Map[3] == "X" and Map[5] == "X" and Map[7] == " " or Map[8] == "X" and Map[9] == "X" and Map[7] == " ":                           #14(7)
            c = 7  
        elif Map[2] == "X" and Map[5] == "X" and Map[8] == " " or Map[7] == "X" and Map[9] == "X" and Map[8] == " ":                           #25(8)
            c = 8  
        elif Map[3] == "X" and Map[6] == "X" and Map[9] == " " or Map[1] == "X" and Map[5] == "X" and Map[9] == " " or Map[7] == "X" and Map[8] == "X" and Map[9] == " ":                           #36(9)
            c = 9
        os.system("clear")

        if str(Map[c]) != " ":
            continue
        else:

            Map[int(c)] = "O"
            PrintMap()
            break
def BotGame():
    PrintMap()
    while True:
        ChooseX()
        if Map[1] == "X" and Map[2] == "X" and Map[3] == "X" or Map[4] == "X" and Map[5] == "X" and Map[6] == "X" or Map[7] == "X" and Map[8] == "X" and Map[9] == "X" or Map[1] == "X" and Map[4] == "X" and Map[7] == "X" or Map[2] == "X" and Map[5] == "X" and Map[8] == "X" or Map[3] == "X" and Map[6] == "X" and Map[9] == "X" or Map[1] == "X" and Map[5] == "X" and Map[9] == "X" or Map[3] == "X" and Map[5] == "X" and Map[7] =="X":
            return Win("X")
            break
        elif Map[1]=="O" and Map[2]=="O" and Map[3]=="O" or Map[4]=="O" and Map[5]=="O" and Map[6]=="O" or Map[7]=="O" and Map[8]=="O" and Map[9]=="O" or Map[1]=="O" and Map[5]=="O" and Map[9]=="O" or Map[3]=="O" and Map[5]=="O" and Map[7]=="O" or Map[1]=="O" and Map[4]=="O" and Map[7]=="O" or Map[2]=="O" and Map[5]=="O" and Map[8]=="O" or Map[3]=="O" and Map[6]=="O" and Map[9]=="O":
            return Win("bot")
            break
        elif Map[1] != " " and Map[2] != " " and Map[3] != " " and Map[4] != " " and Map[5] != " " and Map[6] != " " and Map[7] != " " and Map[8] != " " and Map[9] != " ": 
            print("Game Over!")
            break
        BotChoose()
        if Map[1] == "X" and Map[2] == "X" and Map[3] == "X" or Map[4] == "X" and Map[5] == "X" and Map[6] == "X" or Map[7] == "X" and Map[8] == "X" and Map[9] == "X" or Map[1] == "X" and Map[4] == "X" and Map[7] == "X" or Map[2] == "X" and Map[5] == "X" and Map[8] == "X" or Map[3] == "X" and Map[6] == "X" and Map[9] == "X" or Map[1] == "X" and Map[5] == "X" and Map[9] == "X" or Map[3] == "X" and Map[5] == "X" and Map[7] =="X":
            return Win("X")
            break
        elif Map[1]=="O" and Map[2]=="O" and Map[3]=="O" or Map[4]=="O" and Map[5]=="O" and Map[6]=="O" or Map[7]=="O" and Map[8]=="O" and Map[9]=="O" or Map[1]=="O" and Map[5]=="O" and Map[9]=="O" or Map[3]=="O" and Map[5]=="O" and Map[7]=="O" or Map[1]=="O" and Map[4]=="O" and Map[7]=="O" or Map[2]=="O" and Map[5]=="O" and Map[8]=="O" or Map[3]=="O" and Map[6]=="O" and Map[9]=="O":
            return Win("bot")
            break         
def BotGame2():
    PrintMap()
    while True:
        BotChoose()
        if Map[1] == "X" and Map[2] == "X" and Map[3] == "X" or Map[4] == "X" and Map[5] == "X" and Map[6] == "X" or Map[7] == "X" and Map[8] == "X" and Map[9] == "X" or Map[1] == "X" and Map[4] == "X" and Map[7] == "X" or Map[2] == "X" and Map[5] == "X" and Map[8] == "X" or Map[3] == "X" and Map[6] == "X" and Map[9] == "X" or Map[1] == "X" and Map[5] == "X" and Map[9] == "X" or Map[3] == "X" and Map[5] == "X" and Map[7] =="X":
            return Win("X")
            break
        elif Map[1]=="O" and Map[2]=="O" and Map[3]=="O" or Map[4]=="O" and Map[5]=="O" and Map[6]=="O" or Map[7]=="O" and Map[8]=="O" and Map[9]=="O" or Map[1]=="O" and Map[5]=="O" and Map[9]=="O" or Map[3]=="O" and Map[5]=="O" and Map[7]=="O" or Map[1]=="O" and Map[4]=="O" and Map[7]=="O" or Map[2]=="O" and Map[5]=="O" and Map[8]=="O" or Map[3]=="O" and Map[6]=="O" and Map[9]=="O":
            return Win("bot")
            break
        elif Map[1] != " " and Map[2] != " " and Map[3] != " " and Map[4] != " " and Map[5] != " " and Map[6] != " " and Map[7] != " " and Map[8] != " " and Map[9] != " ": 
            print("Game Over!")
            break
        ChooseX()
        if Map[1] == "X" and Map[2] == "X" and Map[3] == "X" or Map[4] == "X" and Map[5] == "X" and Map[6] == "X" or Map[7] == "X" and Map[8] == "X" and Map[9] == "X" or Map[1] == "X" and Map[4] == "X" and Map[7] == "X" or Map[2] == "X" and Map[5] == "X" and Map[8] == "X" or Map[3] == "X" and Map[6] == "X" and Map[9] == "X" or Map[1] == "X" and Map[5] == "X" and Map[9] == "X" or Map[3] == "X" and Map[5] == "X" and Map[7] =="X":
            return Win("X")
            break
        elif Map[1]=="O" and Map[2]=="O" and Map[3]=="O" or Map[4]=="O" and Map[5]=="O" and Map[6]=="O" or Map[7]=="O" and Map[8]=="O" and Map[9]=="O" or Map[1]=="O" and Map[5]=="O" and Map[9]=="O" or Map[3]=="O" and Map[5]=="O" and Map[7]=="O" or Map[1]=="O" and Map[4]=="O" and Map[7]=="O" or Map[2]=="O" and Map[5]=="O" and Map[8]=="O" or Map[3]=="O" and Map[6]=="O" and Map[9]=="O":
            return Win("bot")
            break
# Action Start
if players == "M" or players == "m":
    Game()
    while True:
        while True:
            try:
                again = input("Do you want to play again ? (Y/yes; N/no): ")
                if again == "Y" or again == "y" or again == "N" or again =="n":
                    break
            except:
                continue
            os.system("clear")
            PrintMap()
        if again == "y" or again == "Y":
            os.system("clear")
            Map = {7:" ", 8:" ", 9:" ", 4:" ", 5:" ", 6:" ", 1:" ", 2:" ", 3:" "}
            Game()
        elif again == "n" or "N":
            print("Bye")
            break
elif players == "S" or players == "s":
    if first == "I" or first == "i":
        BotGame()
        while True:
            while True:
                try:
                    again = input("Do you want to play again ? (Y/yes; N/no): ")
                    if again == "Y" or again == "y" or again == "N" or again =="n":
                        break
                except:
                    continue
                os.system("clear")
                PrintMap()
            if again == "y" or again == "Y":
                os.system("clear")
                Map = {7:" ", 8:" ", 9:" ", 4:" ", 5:" ", 6:" ", 1:" ", 2:" ", 3:" "}
                BotGame()
            elif again == "n" or "N":
                print("Bye")
                break
    elif first == "B" or "b":
        BotGame2()
        while True:
            while True:
                try:
                    again = input("Do you want to play again ? (Y/yes; N/no): ")
                    if again == "Y" or again == "y" or again == "N" or again =="n":
                        break
                except:
                    continue
                os.system("clear")
                PrintMap()
            if again == "y" or again == "Y":
                os.system("clear")
                Map = {7:" ", 8:" ", 9:" ", 4:" ", 5:" ", 6:" ", 1:" ", 2:" ", 3:" "}
                BotGame2()
            elif again == "n" or "N":
                print("Bye")
                break
             
             
            