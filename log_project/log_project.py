import time
import logging
import datetime
import csv

logging.basicConfig(filename='treasureLog.log', level = logging.DEBUG)
class Player:
    def __init__(self, name, turns):
        self.name = name
        self.turns = turns

    def checkTurns(self, turns):
        if turns <= 0:
            print("You're out of turns. Please start over.")
            logging.info(f"You run out of turns.")
            time.sleep(3)
            create_csv()

#learn how to use csv    
def create_csv():
    with open('treasureLog.log') as file:
        lines = file.read().splitlines()
        lines = [lines[x:x+3] for x in range(0, len(lines), 3)]

    with open('treasureLog.csv', 'w+') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(lines)





def main():
    global start_adventure
    start_adventure = datetime.datetime.now()
    logging.info(f"The adventure begins {start_adventure}")
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    new_Username = input("Enter your name: ")
    global new_User
    new_User = Player(new_Username, 5)
    print("You're at a crossroad. Where do you want to go?")
    decision = input("Type 'left' or 'right'")
    if decision.lower() == "left" :
        logging.info(f"You ran into the house {datetime.datetime.now()}")
        print("You've run into a house. Do you choose to knock on the door?")
        decision = input("Type 'yes' or 'no'")
        if decision.lower() == "yes":
            logging.info(f"The adventure ends at the house {datetime.datetime.now()}")
            print("A monster answers and kills you. GG")
        elif decision.lower() == "no":
            logging.info(f"You run into the villager {datetime.datetime.now()}")
            print("You think the house is scary. You decide to walk a little further and run into a villager across the road. He looks homeless and sick. Do you help him?")
            decision = input("Type 'yes' or 'no'")
            if decision.lower() == "yes":
                logging.info(f"You win by helping the villager {datetime.datetime.now()}")
                print("You help the villager and he offers you enough treasure to live like a king. YOU WIN!")
            elif decision.lower() == "no":
                logging.info(f"The adventure ends from starvation {datetime.datetime.now()}")
                print("You pass the villager and walk 5 more miles not seeing anything in sight. Your body becomes incapacitated and are now left on the floor dying from lack of resources. GG")
    elif decision.lower() == "right":
        logging.info(f"The adventure moves towards the dungeon {datetime.datetime.now()}")
        print ("You are confronted with a dungeon. As you walk closer you are able to hear screams from the inside. Do you choose to go in or give up on the adventure?")
        decision = input("Type 'enter' or 'exit'")
        if decision.lower() == "enter":
            logging.info(f"You have entered the dungeon {datetime.datetime.now()}")
            print("You have entered the dungeon and you approach a wizard. His name is Merlin. He asks if you would like to see his magic? Do you choose to witness his magic, or do you choose to walk past him? type 'witness' to witness or 'walk' to walk")
            decision = input("Type 'walk' to walk past or 'witness' to witness")
            if decision.lower() == "witness":
                logging.info(f"You witness the wizards magic {datetime.datetime.now()}")
                print("The wizard casts his spell and grants you a portal to the treasure on the island. YOU WIN!")
            elif decision.lower() == "walk":
                logging.info(f"You walk past the wizard {datetime.datetime.now()}")
                print("You walk past the wizard and run into a horrifying ghoul who takes your soul. GG.")

    create_csv()

if __name__ == "__main__":
    main()
