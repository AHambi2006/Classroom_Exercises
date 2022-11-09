from random import randint
enemy_list = []

def Menu():
    global isPlaying
    choice = input("Do you want to play?:  Y/N  ")
    if choice == "Y" or choice == "y":
        isPlaying = True
    elif choice == "q" or choice == "Q":
        quit(
            )
    elif choice == "N" or choice == "n":
        quit()
    else:
        isPlaying = True
Menu()


class Player():
## self allows player_1 and player_2 to access the player class or blueprint    
    def __init__(self):                                 
        self.name = input("Please enter a name:  ")
        if self.name == "q" or self.name == "Q":
            quit()
        self.level = 1
        self.health = randint(75, 120)
        self.attack = randint(10, 25)
        self.defence = randint(75, 120)
        self.role = ""

    def select_origin(self):
        origin = {
            "Dragon": ":  health = " + str(self.health),
            "Zombie" : ":  health = " + str(self.health),
            "vampire" : ":  health = " + str(self.health),
            "Dinosaur" : ":  health = " + str(self.health),
            "elf" : ":  health = " + str(self.health),
            "Fairy" : ":  health = " + str(self.health),
            "Troll" : ":  health = " + str(self.health),
            "Doll" : ":  health = " + str(self.health),
        }
        for item,value in origin.items():
            print(item,value)
        self.role = input("Please enter your character's role or origin:  ")
        self.health

        print("You have chosen the origin" + str(self.role))


class Goblin():
    def __init__(self):                                 
        self.name = "Lolo"
        self.level = 1
        self.health = randint(45,60)
        self.attack = randint(9,12)
        self.defence = randint(30,45)

class Hobgoblin(Goblin):
    ## hobgoblin takes attributes from parent class(goblin) then edits them for
    ## its own use
    def __init__(self):             
            Goblin.__init__(self)
            self.name = "Lolar"
            self.level = randint(1,4)
            self.health = self.health * 1.25
            self.attack = self.attack * 1.25
            self.defence = self.defence * 1.25

def generate_enemy_list():
## asks user for the number of enemies they would like to generate, 
## then populates the list with required number
    number_of_enemies = 0
    number_of_enemies = int(input("how many enemies would you like to create:"
                                 ))
    if number_of_enemies == "q" or number_of_enemies == "Q":
        quit()
    for i in range(number_of_enemies):
        enemy_select = randint(0,1)
        if enemy_select == 1:
            enemy_list.append(Hobgoblin())
        else:
            enemy_list.append(Goblin())
       

    for j in range(len(enemy_list)):
## checks the length of the list (should match number of enemies chosen
## and print the attributes of each object stored in the list)
        print(vars(enemy_list[j]))

def generate_team() :
    team_1 = Player()
    team_2 = Player()



    