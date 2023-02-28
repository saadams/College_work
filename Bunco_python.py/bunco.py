import random

#round = 0

#Get a dice roll 
def roll_die():
    dice_roll = random.randint(1,6)
    return dice_roll


def point_calc(dice1, dice2, dice3, round):
    #game logic for points
    points = 0 
    #check for buncos
    if ((dice1 == dice2) and (dice2 == dice3)):
        if(dice1 == round):
            points += 21
        elif(dice1 == dice2) and (dice1 == dice3) and (dice1 != round):
            points+= 5  
        else: #check for matching die points
            if(dice1 == round):
                points += 1
            if(dice2 == round):
                points += 1
            if(dice3 == round):
                points += 1
    
    return(points)

#testing
#print(point_calc(dice1=1,dice2=2,dice3=1,round=1))



#print(roll_die())

def play_game():
    #initilize variables
    dice1 = None
    dice2 = None
    dice3 = None
    user_points = 0
    comp_one_points = 0
    comp_two_points = 0
    comp_three_points = 0
    #This is a janky way to get around the problems with the conditinals that check for buncos.
    user_total = 0
    comp_three_total = 0
    comp_two_total = 0
    comp_one_total = 0
    user_name = input("What is your name user: ")
    #Game loop for 6 rounds
    for r in range(1,7):
        print("--------------------------------------------")
        print(f"\n Round {r} of bunco {user_name}!")
        print("--------------------------------------------")
        user_roll_q = input(f"{user_name} would you like to roll? (Y/N)")
        print("--------------------------------------------")
        if(user_roll_q == 'y' or user_roll_q == 'Y'):
            dice1 = roll_die()
            dice2 = roll_die()
            dice3 = roll_die()
            print(f"A dice is rolled it lands on {dice1}.")
            print(f"A dice is rolled it lands on {dice2}.")
            print(f"A dice is rolled it lands on {dice3}.")
            user_points = point_calc(dice1=dice1,dice2=dice2,dice3=dice3, round=r)
            if(user_points == 21):
                print("Bunco!!!")
            if(user_points == 5):
                print("Mini Bunco!!!")
            user_total = (user_points+user_total) #The += method was not working so I gave up and did this
            print(f"{user_name} scored {user_points}")
        else:
            print("Rolling the dice anyway anyway!")
            dice1 = roll_die()
            dice2 = roll_die()
            dice3 = roll_die()
            print(f"A dice is rolled it lands on {dice1}.")
            print(f"A dice is rolled it lands on {dice2}.")
            print(f"A dice is rolled it lands on {dice3}.")
            user_points = point_calc(dice1=dice1,dice2=dice2,dice3=dice3, round=r)
            if(user_points == 21):
                print("Bunco!!!")
            if(user_points == 5):
                print("Mini Bunco!!!")
            user_total = (user_points+user_total)
            print(f"{user_name} scored {user_points}")
        
        #comp1 goes
        print("-------------------")
        dice1 = roll_die()
        dice2 = roll_die()
        dice3 = roll_die()
        print(f"A dice is rolled it lands on {dice1}.")
        print(f"A dice is rolled it lands on {dice2}.")
        print(f"A dice is rolled it lands on {dice3}.")
        comp_one_points = point_calc(dice1=dice1,dice2=dice2,dice3=dice3, round=r)
        if(comp_one_points == 21):
            print("Bunco!!!")
        if(comp_one_points == 5):
            print("Mini Bunco!!!")
        comp_one_total = (comp_one_points+comp_one_total)
        print(f"Computer 1 scored {comp_one_points}")

        #comp2 goes
        print("-------------------")
        dice1 = roll_die()
        dice2 = roll_die()
        dice3 = roll_die()
        print(f"A dice is rolled it lands on {dice1}.")
        print(f"A dice is rolled it lands on {dice2}.")
        print(f"A dice is rolled it lands on {dice3}.")
        comp_two_points = point_calc(dice1=dice1,dice2=dice2,dice3=dice3, round=r)
        if(comp_two_points == 21):
            print("Bunco!!!")
        if(comp_two_points == 5):
            print("Mini Bunco!!!")
        comp_two_total = (comp_two_points+comp_two_total)
        print(f"Computer 2 scored {comp_two_points}")

        #comp3 goes
        print("-------------------")
        dice1 = roll_die()
        dice2 = roll_die()
        dice3 = roll_die()
        print(f"A dice is rolled it lands on {dice1}.")
        print(f"A dice is rolled it lands on {dice2}.")
        print(f"A dice is rolled it lands on {dice3}.")
        comp_three_points = point_calc(dice1=dice1,dice2=dice2,dice3=dice3, round=r)
        if(comp_three_points == 21):
            print("Bunco!!!")
        if(comp_three_points == 5):
            print("Mini Bunco!!!")
        comp_three_total = (comp_three_points + comp_three_total)
        print(f"Computer 3 scored {comp_three_points}")

        #print(r)
    
    print("------------------------------------")
    print(f"{user_name} scored {user_total} total points!")
    print(f"Computer 1 scored {comp_one_total} total points!")
    print(f"Computer 2 scored {comp_two_total} total points!")
    print(f"Computer 3 scored {comp_three_total} total points!")
    print("------------------------------------")
    print("------------------------------------")
    print("Game over!")
    print("------------------------------------")
    

#print(point_calc(dice1=2,dice2=2,dice3=1, round=3))
play_game()

