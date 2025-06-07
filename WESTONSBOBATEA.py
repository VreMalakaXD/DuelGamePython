import random
import constants
WeaponStats = constants.WeaponStats
    

ConsumableStats = constants.ConsumableStats


def floatRand(lowBound,Highbound):
    return lowBound + (random.random() * (Highbound-lowBound))

def printChar(charDict : dict) -> None:
    
    print(f"Health: { charDict['HP']}")
    print(f"STR: { charDict['STR']}")
    print("   //////")
    print("  C| o 0|       /| ")
    print("   | __ |      / / ")
    print("   |__)_)     / /  ")
    print(" //--[]-\\   / /   ")
    print(" ||  []  || / /    ")
    print(" ||_ []  || //     ")
    print("[||] []  \\/B      ")
    print(" \/ //\\           ")
    print("   //  \\          ")
    print("  //    \\         ")
    print(" _||     \\__      ")
    print("(__|     |___)     ")
    
    charINV = charDict["INV"]
    charWeapon = ""
    for i in charINV.keys():
        if i in WeaponStats.keys():
            charWeapon = str(i)
        
    charConsume = []
    for i in charINV.keys():
        if i in ConsumableStats.keys():
            charConsume.append([str(i),charINV[i]["Quantity"]])
    print(f"Weapon: {charWeapon} | {charINV[charWeapon]['UsedTimes']}/{WeaponStats[charWeapon]['DUR']}")
    print("Consumables: ")
    for i in charConsume:
        print(f"\t{i[0]} | {i[1]}")
        
def actionSelect() -> int:
    print("Pick an option")
    print(" ______________________/||\________________________ ")
    print("|                       ||                         |")
    print("|                       ||                         |")
    print("|         FIGHT         ||           HEAL          |")
    print("|                       ||                         |")
    print("\_______________________/\________________________/ ")
    correct = True
    while correct:
        userIn = input("type in number:")
        try:
            userIn = int(userIn)
            if userIn == 1:
                correct = False
                return 1
            if userIn == 2:
                correct = False
                return 2
            else:
                correct= True
                print("enter 1 or 2")
        except:
            print("enter a number")

    
