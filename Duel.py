import random
import time
import WESTONSBOBATEA as g
import constants
WeaponStats = constants.WeaponStats
    

ConsumableStats = constants.ConsumableStats
print("Duel")


'''
    Entity
        Health
        STR
        INV = {}
        
        
'''
Player = {
    "HP" : 15,
    "STR" : 5,
    "INV" : {
         
        }
    }

intFlag = True
while intFlag:
    inputHP = input("How many health points will your character have? ")
    try:
        inputHP = int(inputHP)
        if inputHP< 1:
            inputHP = 1
        intFlag = False
    except:
        print("Please choose a whole number")
Player["HP"] = inputHP

intFlag = True
while intFlag:
    inputSTR = input("How much strength points will your character have? ")
    try:
        inputSTR = int(inputSTR)
        if inputSTR < 1:
            inputSTR = 1
        intFlag = False
    except:
        print("Please choose a whole number")
Player["STR"] = inputSTR

intFlag = True
while intFlag:
    for i in range(len(WeaponStats.keys())):
        print(f"{i+1} : {list(WeaponStats.keys())[i]}")
    inputWeapon = input("Which Weapon will your character have? ")
    try:
        inputWeapon = int(inputWeapon)
        if inputWeapon > 0 and inputWeapon <= len(WeaponStats.keys()):
            inputWeapon =  inputWeapon-1
            intFlag = False
        else:
            raise Exception("Put the right Nuber")
    except:
        print("Please enter Whole number shown in the list above only")
Player["INV"][list(WeaponStats.keys())[inputWeapon]] = {"Quantity":1,"UsedTimes":0}

intFlag = True
while intFlag:
    for i in range(len(ConsumableStats.keys())):
        print(f"{i+1} : {list(ConsumableStats.keys())[i]}")
    inputConsumable = input("Which Consumable will your character have? ")
    try:
        inputConsumable = int(inputConsumable)
        if inputConsumable > 0 and inputConsumable <= len(ConsumableStats.keys()):
            inputConsumable =  inputConsumable-1
            intFlag = False
        else:
            raise Exception("Put the right Nuber")
    except:
        print("Please enter Whole number shown in the list above only")
Player["INV"][list(ConsumableStats.keys())[inputConsumable]] = {"Quantity":max(round(random.gauss(5,3)),1)}


Enemy = {
    "HP" : max(random.randrange(
            round(Player["HP"]-(Player["HP"]*0.5)),
            round(Player["HP"]+(Player["HP"]*0.3))
                           ),10),
    "STR" : random.randrange(
            round(Player["STR"]-(Player["STR"]*0.5)),
            round(Player["STR"]+(Player["STR"]*0.3)),
                            ),
    "INV" : {
            random.choice(list(WeaponStats.keys())) : {"Quantity" : 1, "UsedTimes":0},
            random.choice(list(ConsumableStats.keys())) : {"Quantity" :max(round(random.gauss(5,3)),1)}
        }
    }
while Player["HP"] > 0 and Enemy["HP"] > 0:
    print("Player: ")
    g.printChar(Player)
    print("Enemy ")
    g.printChar(Enemy)
    turnUsed = False
    while not turnUsed:
        PlayerAction = g.actionSelect()
        if PlayerAction == 1:
            charWeapon = ""
            for i in Player["INV"].keys():
                if i in WeaponStats.keys():
                    charWeapon = str(i)
            if Player["INV"][charWeapon]["UsedTimes"] < WeaponStats[charWeapon]["DUR"]:
                Enemy["HP"] -= WeaponStats[charWeapon]["DMG"] * Player["STR"]
                Player["INV"][charWeapon]["UsedTimes"] += 1
                if Player["INV"][charWeapon]["UsedTimes"] >= WeaponStats[charWeapon]["DUR"]:
                    del Player["INV"][charWeapon]
                    Player["INV"]["Fists"] = {"Quantity" : 1, "UsedTimes" : 0}
                turnUsed = True
        else:
            charConsume = []
            for i in Player["INV"].items():
                if i[0] in list(ConsumableStats.keys()):
                    charConsume.append(i)
            print("what would you want to consume in thy stomach")
            for i in range(len(charConsume)):
                print(f"{i+1}. {charConsume[i][0]} | Left: {charConsume[i][1]['Quantity']}")
            print(f"{len(charConsume)+1}. Return")
            ConsumeInputFlag = True
            while ConsumeInputFlag:
                selection = input("pick a number from the list:")
                try:
                    selection = int(selection)-1 
                    if selection == len(charConsume):
                        print("Returning")
                        ConsumeInputFlag = False
                    elif selection >= 0 and selection <= len(charConsume):
                        itemSelection = charConsume[selection][0]
                        Player["INV"][itemSelection]["Quantity"] -= 1
                        Player["HP"] += ConsumableStats[itemSelection]["HEAL"]
                        Player["STR"] += ConsumableStats[itemSelection]["STR"]
                        if Player["INV"][itemSelection]["Quantity"] <= 0:
                            del Player["INV"][itemSelection]
                        turnUsed= True 
                        ConsumeInputFlag = False
                    else:
                        print("INCORRECT input")
                        ConsumeInputFlag = True
                except:
                    print("Try again")
                    ConsumeInputFlag = True
                    
    if Player["HP"] > 0 and Enemy["HP"] > 0:                
        while turnUsed:
            print("enemy Turn")
            Aggro = Enemy["HP"] - Enemy["STR"] / (Enemy["HP"] + Enemy["STR"])
            HealthPercent = Enemy["HP"]/Player["HP"]
            if "Potassium" in Enemy['INV'].keys() and HealthPercent > 0.99:
                Enemy['INV']["Potassium"] -= 1
                if Enemy['INV']["Potassium"] <=0:
                    del Enemy['INV']["Potassium"]
                Enemy["STR"] += ConsumableStats['Potassium']["STR"]
                Enemy["HP"] += ConsumableStats['Potassium']["HEAL"]
                print("Enemy has used Potassium")
                time.sleep(constants.Delay)
                turnUsed = False
            
            if HealthPercent < 3.52 and turnUsed:
                consumes = []
                for i in Enemy["INV"].keys():
                    if i in ConsumableStats.keys():
                        consumes.append(i)
                if len(consumes) > 0:
                    selection = random.choice(consumes)
                    Enemy["HP"] += ConsumableStats[selection]
                    Enemy["STR"] += ConsumableStats[selection]
                    Enemy["INV"][selection]["Quantity"] -= 1 
                    if Enemy["INV"][selection]["Quantity"] <= 0:
                        del Enemy['INV'][selection]
                        print("Enemy has Healed")
                        time.sleep(constants.Delay)
                        turnUsed = False
            if turnUsed:
                attacks = []
                for i in Enemy["INV"].keys():
                    if i in WeaponStats.keys():
                        attacks.append(i)
                if len(attacks) > 0:
                    selection = random.choice(attacks)
                    Enemy["HP"] -= WeaponStats[selection]["DMG"] * Enemy["STR"]
                    Enemy["INV"][selection]["UsedTimes"] += 1
                    if Enemy["INV"][selection]["UsedTimes"] >= WeaponStats[selection]["DUR"]:
                        del Enemy['INV'][selection]
                        Enemy["INV"]["Fists"] = {"Quantity" : 1, "UsedTimes" : 0}
                    print("Enemy Attacks")
                    time.sleep(constants.Delay)
                    turnUsed = False
print("Player: ")
g.printChar(Player)
print("Enemy ")
g.printChar(Enemy)

if Player["HP"] > 0 and Enemy["HP"] < 0:
    print("You won you dont get a medal")
elif Enemy["HP"] > 0 and Player["HP"] < 0:
    print("You'll get em next time")
