import random

def kopapir():
    sajatkopap = input("Kő, papír, olló? ")
    if sajatkopap == "kő": 
        print("Választásod: " + sajatkopap)
    elif sajatkopap == "papír": 
        print("Választásod: " + sajatkopap)
    elif sajatkopap == "olló": 
        print("Választásod: " + sajatkopap)
    else:
        print("Nincs ilyen opció!")
        kopapir()
    kopap = ["kő", "papír", "olló"]
    x = random.randint(0, 2)
    ellenkopap = kopap[x]
    print("Ellenfeled választása: " + ellenkopap)
    if ellenkopap == "kő" and sajatkopap == "papír":
        print("Kivédted a sebzést!")
    elif ellenkopap == "papír" and sajatkopap == "olló":
        print("Kivédted a sebzést!")
    elif ellenkopap == "olló" and sajatkopap == "kő":
        print("Kivédted a sebzést!")
    elif ellenkopap == sajatkopap:
        print("Új menet! ")
        kopapir()
    else: 
        print("Plusz két sebzés!")
        életerő -=4

kopapir()

