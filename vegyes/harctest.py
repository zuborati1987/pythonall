import random

items = ["pálinka", "kalandkönyv", "pénz", "energiaital", "pendrive", "fegyver", "egér", "cigi", "kaja"]
owned = []
ugyesseg = int(random.randint(1, 5) + 6)
eletero = int(random.randint(2, 11) + 12)
szerencse = int(random.randint(1, 5) + 6)

ellenfél_életerő = 0
ellenfél_ügyesség = 0


def pali():
    global ellenfél_életerő
    global ellenfél_ügyesség
    ellenfél_életerő = 8
    ellenfél_ügyesség = 4
    return ellenfél_életerő, ellenfél_ügyesség

def dumblermain():
    global ellenfél_életerő
    global ellenfél_ügyesség
    ellenfél_életerő = 50
    ellenfél_ügyesség = 30
    return ellenfél_életerő, ellenfél_ügyesség

def harc(eletero, ugyesseg, ellenfél_életerő, ellenfél_ügyesség):
    print(" Az életerőd: {}, Az ellenfél életereje: {}".format(eletero, ellenfél_életerő))
    while eletero > 0 and ellenfél_életerő > 0:
        alapérték = random.randint(2, 12)
        támadóerő = alapérték + ugyesseg
        ellenfél_támadóerő = alapérték + ellenfél_ügyesség
        if ellenfél_támadóerő > támadóerő:
            eletero -=2
            print(" Az életerőd: {}, Az ellenfél életereje: {}".format(eletero, ellenfél_életerő))
        else:
            ellenfél_életerő -=2
            print(" Az életerőd: {}, Az ellenfél életereje: {}".format(eletero, ellenfél_életerő))
        
    if ellenfél_életerő == 0:
        print ("Legyőzted ellenfeledet!")
    else:
        print ("Vesztettél, sajnos sosem lesz belőled programozó!")

    return eletero

pali()
harc(eletero, ugyesseg, ellenfél_életerő, ellenfél_ügyesség)
dumblermain()
harc(eletero, ugyesseg, ellenfél_életerő, ellenfél_ügyesség)