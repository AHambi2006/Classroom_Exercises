from characters import *


player_1 = Player()
#player_2 = Player()
#player_3 = Player()

player_1.select_origin()

## prints all the stats that player_1 inputs. 
## (prints the variables that player_1 inputs)
print(vars(player_1))    
#print(vars(player_2))
#print(vars(player_3))

def team():
    team1 = input("would you like a team?: Y/N  ")
    if team1 == "q" or team1 == "Q":
        quit()
    elif team1 == "Y" or team1 == "y":
        generate_team()
    elif team1 == "N" or team1 == "n":
        ""
        
team()    


goblin_1 = Goblin()
#goblin_2 = Goblin()
#goblin_3 = Goblin()


print(vars(goblin_1))
#print(vars(goblin_2))
#print(vars(goblin_3))


hobgoblin_1 = Hobgoblin()
#hobgoblin_2 = Hobgoblin()
#hobgoblin_3 = Hobgoblin()

print(vars(hobgoblin_1))
#print(vars(hobgoblin_2))
#print(vars(hobgoblin_3))

generate_enemy_list()

def fight():
    while enemy_list[0].health > 0:
        attack = input("Would you like to fight?  Y/N:  ")
        if attack == "Y" or attack == "y":
            enemy_list[0].health -= player_1.attack
            if enemy_list[0].health < 0:
                enemy_list[0].health = 0
            print(enemy_list[0].health)
        if enemy_list[0].health <= 0:
            print("You have defeated your enemy! Remaining health = " + str(player_1.health))
            #for i in range(len(enemy_list)):
            #    while enemy_list[i].health > 0:
            #        attack = input("Would you like to fight?  Y/N:  ")
            #        if attack == "Y" or attack == "y":
            #            enemy_list[i].health -= player_1.attack
            #            if enemy_list[i].health < 0:
            #                enemy_list[i].health = 0
            #                print(enemy_list[i].health)
            #        if enemy_list[i].health <= 0:
            #            print("You have defeated your enemy! Remaining health = " + str(player_1.health))

fight()