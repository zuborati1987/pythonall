import random


draw_deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 
                7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10
                ]
player_deck = [-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6, 
                "-+1", "-+2", "-+3", "-+4", "-+5", "-+6", "2f4", "3f6", "D", "TB"
                ]
enemy_deck = [-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6, 
                "-+1", "-+2", "-+3", "-+4", "-+5", "-+6", "2f4", "3f6", "D", "TB"
                ]
draw_deck_use = []
player_deck_use = []
enemy_deck_use = []
enemy_draw_deck_use = []
y = 0
w = 0

def buildlist(listname, newlist, x):
    newlist = [listname[random.randrange(len(listname))] for card in range(x)]
    for card in newlist:
        if card in listname:
            listname.remove(card)
    return listname, newlist

"""def buildlist(listname, newlist, x):
    for i in range(x):
        newlist.append(listname[random.randint(0, len(listname))])
        for j in newlist:
            listname.remove(j)
    return listname, newlist"""

#buildlist(draw_deck, draw_deck_use, 4)
player_deck, player_deck_use = buildlist(player_deck, player_deck_use, 4)
enemy_deck, enemy_deck_use = buildlist(enemy_deck, enemy_deck_use, 4)


def deal_cards_player(draw_deck, draw_deck_use, y):
    draw_deck, draw_deck_use = buildlist(draw_deck, draw_deck_use, 1)
    y += draw_deck_use[0]
    print((draw_deck, draw_deck_use, enemy_draw_deck_use))
    print("Your sum is", y)
    return draw_deck, draw_deck_use, enemy_draw_deck_use, y

def deal_cards_enemy(draw_deck, enemy_draw_deck_use, w):    
    draw_deck, enemy_draw_deck_use = buildlist(draw_deck, enemy_draw_deck_use, 1)    
    w += enemy_draw_deck_use[0]
    print((draw_deck, draw_deck_use, enemy_draw_deck_use))
    print("Enemy sum is", w)
    return draw_deck, draw_deck_use, enemy_draw_deck_use, w

def end_turn():
    end_turn = input("Would you like to end your turn? ")
    if end_turn == "yes":
        return True

def enemy_end_turn():
    if end_turn == "yes":
        return True
   

def play(draw_deck, draw_deck_use, enemy_draw_deck_use, y, w): 
    end_turn = "no"
    end_turn = input("End turn? " )
    while end_turn != "yes" or end_turn_enemy != "yes":
        draw_deck, draw_deck_use, enemy_draw_deck_use, y, w = deal_cards_player(draw_deck, draw_deck_use, y)
        if y >= 21:
            end_turn = "yes"
            print("You went over, you lose!")
        else:
            end_turn = input("End turn? " )
    while

def ai(enemy_deck_use, y, w):
    end_turn_enemy = "no"
    if w >= 21:
        end_turn_enemy = "yes"
        print("Enemy went over, you win!")
    elif w >= 17:
        if w <= y:
            f = len(enemy_deck_use)
            if (enemy_deck_use[f] + w) > y:
                w += enemy_deck_use[f]
            end_turn_enemy = "yes"
    return enemy_deck_use, y, w
            
#draw_deck, draw_deck_use = buildlist(draw_deck, draw_deck_use, 1)
#draw_deck, enemy_draw_deck_use = buildlist(draw_deck, enemy_draw_deck_use, 1)

play(draw_deck, draw_deck_use, enemy_draw_deck_use, y, w)