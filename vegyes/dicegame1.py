from random import randint

player_count = 2
max_score = 100
player = 0
score = 0
save_score = player_count * [0]

while max(save_score) < max_score:
    print("player: {}, save_score: {}, score: {}".format(player,save_score[player], score))
    rolling = input("Do you want to roll? (Y)es, or (n)o?" )
    rolling = rolling.strip().lower()
    if rolling in ["y", '']:
        rolled = randint(1, 6)
        print("rolled %i".format(rolled))
        if rolled == 1:
            print("Bust! You lose {}, but you still keep your previous {}".format(score, save_score[player]))
            score = 0
            player = (player + 1) % player_count
        else:
            score += rolled
    else:
        save_score[player] += score
        if save_score[player] >= max_score:
            break
        print("Sticking with {}".format(save_score[player]))
        score = 0
        player = (player + 1) % player_count

print("Player {} wins with the score of {}".format(player, save_score[player]))