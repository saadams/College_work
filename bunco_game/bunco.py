import random
import player as p
#import dice as d

def roll_die():
    dice_roll = random.randint(1, 6)
    return dice_roll


user_player = p.Player()
comp_one = p.Player()
comp_two = p.Player()
comp_three = p.Player()
ammount_rounds = input("How many rounds do your want to play? ")


def get_players():
    user_player.name = input("What is ur name? ")
    comp_one.name = "Computer1"
    comp_two.name = "Computer2"
    comp_three.name = "Computer3"


def player_reset():
    comp_one.round_points = 0
    comp_two.round_points = 0
    comp_three.round_points = 0
    user_player.round_points = 0


def point_calc(dice1, dice2, dice3, round):
    # game logic for points
    points = 0
    # check for buncos
    if ((dice1 == dice2) and (dice2 == dice3)):
        if (dice1 == round):
            points += 21
            print("Bunco!")
        elif (dice1 == dice2) and (dice1 == dice3) and (dice1 != round):
            points += 5
            print("Mini Bunco!")
        else:  # check for matching die points
            if (dice1 == round):
                points += 1
            if (dice2 == round):
                points += 1
            if (dice3 == round):
                points += 1

    return (points)


#get_players()

# print(user_player.name)


def player_turn(round, player):
    
    dice1 = None
    dice2 = None
    dice3 = None

    dice1 = roll_die()
    dice2 = roll_die()
    dice3 = roll_die()
    print(f"{player} is rolling!")
    print(f"A dice is rolled it lands on {dice1}.")
    print(f"A dice is rolled it lands on {dice2}.")
    print(f"A dice is rolled it lands on {dice3}.")
    points = point_calc(dice1=dice1, dice2=dice2, dice3=dice3, round=round)
    return points


#comp_one.round_points = player_turn(1, comp_one.name)
#print(comp_one.round_points)


def play_round(r):

   
    print(f"Round  {r}")
    while (comp_one.round_points != 21) and (comp_two.round_points != 21) and (comp_three.round_points != 21) and (user_player.round_points != 21):
        user_player.round_points = player_turn(r, user_player.name)
        print(user_player.round_points)
        comp_one.round_points = player_turn(r, comp_one.name)
        comp_two.round_points = player_turn(r, comp_two.name)
        comp_three.round_points = player_turn(r, comp_three.name)

    #play_round()

def play_game():
    get_players()
    for r in range(1,int(ammount_rounds)+1):
        player_reset()
        play_round(r)
        if comp_one.round_points >= 21:
            comp_one.rounds_won += 1
            print(comp_one.name + " wins round ")
            print("-------------------------------------")
            continue
        if comp_two.round_points >= 21:
            comp_two.rounds_won += 1
            print(comp_two.name + " wins round ")
            print("-------------------------------------")
            continue
        if comp_three.round_points >= 21:
            comp_three.rounds_won += 1
            print(comp_three.name + " wins round ")
            print("-------------------------------------")
            continue
        if user_player.round_points >= 21:
            user_player.rounds_won += 1
            print(user_player.name + " wins round ")
            print("-------------------------------------")
            continue
    print(f"{user_player.name} won {user_player.rounds_won} rounds" )
    print(f"{comp_one.name} won {comp_one.rounds_won} rounds" )
    print(f"{comp_two.name} won {comp_two.rounds_won} rounds" )
    print(f"{comp_three.name} won {comp_three.rounds_won} rounds" )

#play_game()