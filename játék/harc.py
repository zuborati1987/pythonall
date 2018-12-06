from random import randint


ügyesség = 8
ellenfél_ügyesség = 4
életerő = 12
ellenfél_életerő = 6




def harc():
    global életerő
    global ügyesség
    global ellenfél_életerő
    global ellenfél_ügyesség
    while életerő and ellenfél_életerő > 0:
        alapérték = randint(2, 12)
        támadóerő = alapérték + ügyesség
        ellenfél_támadóerő = alapérték + ellenfél_ügyesség
        if ellenfél_támadóerő > támadóerő:
            életerő -=2
            print("Az életerőd: {}, Az ellenfél életereje: {}".format(életerő, ellenfél_életerő))
        else:
            ellenfél_életerő -=2
            print("Az életerőd: {}, Az ellenfél életereje: {}".format(életerő, ellenfél_életerő))
    if ellenfél_életerő == 0:
        győzelem = True
        print ("Legyőzted ellenfeledet!")
    else:
        győzelem = False
        print ("Vesztettél, sajnos sosem lesz belőled programozó!")
    #if győzelem = True:

harc()

