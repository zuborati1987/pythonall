from random import randint

playercount = 2
maxscore = 100
safescore = [0] * playercount
player = 0
score = 0

while max(safescore) < maxscore:
    print('Player {}: safescore: {}, current_score: {}'
            .format(player, safescore[player], score))
    rolling = input(' Do you want to Roll? (y)es or (n)?')
    rolling = rolling.strip().lower()
    if rolling in ['y', '']:
        rolled = randint(1, 6)
        print(' Rolled {}'.format(rolled))
        if rolled == 1:
            print('Bust! You lose {} but still keep your previous {}'
                .format(score, safescore[player]))
            score = 0
            player = (player + 1) % playercount
        else:
            score += rolled
    else:
        safescore[player] += score
        if safescore[player] >= maxscore:
            break
        print(" Sticking with {}"
            .format(safescore[player]))
        score = 0
        player = (player + 1) % playercount

print ("\nPlyer {} wins with a score of {}"
        .format(player, safescore[player]))