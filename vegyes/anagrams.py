# displays anagram files from file
# 2018.10.24

import sys

path = sys.argv[1]
file = open(path)

words = []
for line in file:
    word = line.strip()

# for word in words:
    ordered_letters = sorted(word)
    for another_word in words:
        if word == another_word:
            continue
        another_ord_lett = sorted(another_word)
        if ord_lett == another_ord_lett:
            print((word, another word))
            word.sort()

# the_word = input('Specify the word to look for its anagram: ')            
# sorted 
