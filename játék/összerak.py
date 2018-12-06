import random

items = ["pálinka", "kalandkönyv", "pénz", "energiaital", "pendrive", "fegyver", "egér", "cigi", "kaja"]
owned = []
ugyesseg = int(random.randint(1, 5) + 6)
eletero = int(random.randint(2, 11) + 12)
szerencse = int(random.randint(1, 5) + 6)


def ellenfel():
    ellenfél_életerő = 0
    ellenfél_ügyesség = 0
    return ellenfél_életerő, ellenfél_ügyesség

def stats(eletero, ugyesseg, szerencse):
    print("Életerőd: {}, Ügyességed: {}, Szerencséd {}".format(eletero, ugyesseg, szerencse))

def pali():
    global ellenfél_életerő
    ellenfél_életerő = 8
    global ellenfél_ügyesség
    ellenfél_ügyesség = 4
    return ellenfél_életerő, ellenfél_ügyesség

def robi():
    ellenfél_életerő = 7
    ellenfél_ügyesség = 5
    return ellenfél_életerő, ellenfél_ügyesség

def imi():
    ellenfél_életerő = 8
    ellenfél_ügyesség = 5
    return ellenfél_életerő, ellenfél_ügyesség

def portas():
    ellenfél_életerő = 5
    ellenfél_ügyesség = 3
    return ellenfél_életerő, ellenfél_ügyesség

def random_coder():
    ellenfél_életerő = 4
    ellenfél_ügyesség = 4
    return ellenfél_életerő, ellenfél_ügyesség

def dumblermain():
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

def palinka(eletero):
    eletero += 2
    return eletero

def nrg(eletero, ugyesseg):
    eletero -= 2
    ugyesseg += 3
    return eletero, ugyesseg

def fegyver(ugyesseg):
    ugyesseg += 7
    return ugyesseg

def cigi(eletero, szerencse):
    eletero -= 2
    szerencse += 2
    return eletero, szerencse

def kaja(eletero):
    eletero += 5
    return eletero

def lista():
    j = 1
    print("Kalandod elején válaszd ki mi nehezítse táskádat: ")
    for i in range(len(items)):
        print(items[i])
    while j <= 5 :
        c = input('Választásod? ')
        for i in range(len(items)):
            if c == items[i]:
                owned.append(c)
                j += 1        

def use():
    used = input('Mit szeretnél használni? ')
    if used == 'pálinka':
        if 'pálinka' in owned:
            palinka(eletero)
            owned.remove('pálinka')
            print("Felszívtad az összes pálinkát, te rohadt tintás!")
        else:
            print("Nincs nálad ilyen.")
    
    if used == 'energiaital':
        if 'energiaital' in owned:
            nrg(eletero, ugyesseg)
            owned.remove('energiaital')
            print("Négy dupla presszó adagját ittad meg egyszerre, számolj vissza mikor áll le a szíved!")
        else:
            print("Nincs ilyen tárgyad.")
    
    if used == 'fegyver':
        if 'fegyver' in owned:
            fegyver(ugyesseg)
            owned.remove('fegyver')
            print("Kiürült a tárad, eldobtad a fegyvered, mert lusta vagy másikat keresni.")
        else:
            print("Nincs nálad ilyen.")
    
    if used == 'cigi':
        if 'cigi' in owned:
            cigi(eletero, szerencse)
            owned.remove('cigi')
            print("Sikerült elszívnod egy egész dobozzal te láncdohányos!")
        else:
            print("Nincs ilyen tárgyad.")
    
    if used == 'kaja':
        if 'kaja' in owned:
            kaja(eletero)
            owned.remove('kaja')
            print("Telezabáltad magad, fáj a hasad, el kell menned wc-re, de legalább gyógyultál!")
        else:
            print("Éhen fogsz pusztulni, hehe!")

def main():
    stats(eletero, ugyesseg, szerencse)
    lista()
    pali()
    harc(eletero, ugyesseg, ellenfél_életerő, ellenfél_ügyesség)

if __name__ == '__main__':
    main()

print("CODECOOL RPG")

def choice1():
    actual_choice = choice1
    print ("Elérkezett a nagy nap. Elhatároztad, hogy programozó leszel. Hogyan fogsz neki a tanulásnak?\n\
a, Elmegyek a Greenfoxba.\n\
b, Elmegyek az egyetemre.\n\
c, Megtanulom magamtól.\n\
d, A Codecoolt választom.")
    chosen = input()
    if chosen == "a":
        print("Zöld rókák nem léteznek.")
        choice1()
    elif chosen == "b":
        print("3 éven át tanulod a számítástechnika történelmét és a matekot.\n\
Már egész jól kiismered magadat pascalban. Vesztesz 10 életerőt.")
        életerő -= 10
        choice1()
    elif chosen == "c":
        print("De mi az a _name__=__main_?\n\
Megjelenik Dumblermain varázsló!")
        harc()
        choice1()
    elif chosen == "d":
        print("Úgy döntesz, hogy a codecool az egyetlen helyes megoldás.")
        choice2()
    else:
        print ("Hogy akarsz programozó lenni, ha ezt sem érted?")
        choice1()



def choice2():
    actual_choice = choice2
    print ("Elérkezik a felvételi napja. A kapunál a biztonsági őr fogad.\n\
Van mágneskártyád?")
    harc()
    choice3()



def choice3():
    actual_choice = choice3
    print ("A felvételin bemutatkozik nektek Robi, ő vizsgáztat titeket.\n\
\"Egy programozónak érvényesíteni kell tudnia az érdekeit a felhasználókkal szemben,\n\
ezért most teszteljük, hogyan tudjátok megvédeni magatokat!\"")
    harc()
    choice4()

def choice4():
    actual_choice = choice4
    print("A felvételi továbbhalad a többi jelentkezővel, egyszercsak megjelenik Imi:\n\
“Na mi van, itt csicskultok a csicskítóban ti csicskák?”\n\
Azt se tudod, hol vagy, hirtelen csak annyit tudsz kinyögni: “Tessék...?”\n\
“Ne vitatkozz velem, te csicska!”")
    harc()
    choice5()

def choice5():
    actual_choice = choice5
    print("Sikeresen átmentél a felvételin. Az első nap a kapuban a biztonsági őr fogad.\n\
Ajjaj, sürgősen szerezni kell egy mágneskártyát.")
    harc()
    if egér in owned:
        choice6()
    else:
        choice7()

def choice6():
    actual_choice = choice6
    print("Megkezdődik az első tanítási nap. Épphogycsak helyet foglalsz,\n\
amikor a magaddal hozott egér kiszökik a táskádból, Robi észreveszi:\n\
“Ki mondta, hogy lehet állatot behozni?”")
    harc()
    choice7()

def choice7():
    actual_choice = choice7
    print ("Elérkezik az ebédszünet ideje. Ha hoztál magaddal ételt, megebédelhetsz,\n\
vagy ha van nálad pénz, kimehetsz a büfébe venni valamit.")
    print ("a, megebédelek\n\
b, veszek egy csokit\n\
c, sajnos nem hoztam magammal egyiket sem")
    chosen = input()
    if chosen == "a":
        if kaja in owned:
            kaja()
            print ("Jóllakottan folytatod a napot.")
        else:
            print("Dehát nincs is nálad kaja!")
            choice7()    
    elif chosen == "b":
        if pénz in owned:
            kaja()
            print ("Jóllakottan folytatod a napot.")
        else: 
            print("Dehát nincs is pénzed!")
            choice7()
    elif chosen == "c":
        print ("Sajnos üres gyomorral kell folytatnod a napot. Minusz 5 életerő.")
        életerő -= 5
    else:
        print ("Sajnos üres gyomorral kell folytatnod a napot. Minusz 5 életerő.")
        életerő -= 5
    choice8()

def choice8():
    actual_choice = choice8
    print ("Az ebédidő után a mágneskártyák kerülnek kiosztásra,\n\
de sajnos neked nem jut belőle. Kibírod nélküle, vagy megpróbálod megszerezni valakiét?")
    print("a, igen\n\
b, megvagyok nélküle")
    chosen = input()
    if chosen == "a":
        harc()
    elif chosen == "b":
        print("Úgy gondolod, hogy majd bejutsz valahogy.")
    choice9()

def choice9():
	actual_choice = choice9
	print("Az ubuntud abbahagyja a működést. Hoztál pen driveot?")
	print("a, Hoztam, persze, aha!\n\
b, Nem, sajnos nincsen nálam.")
	chosen = input()
	if chosen == "a":
		if pendrive in owned:
			print("Újrarakod az Ubuntut, és útközben tanulsz is valamit! Plusz 2 ügyesség.")
			ügyesség +=2
		else:
			print("Te kis hazug geci! Ügyesség minusz 4,ezt most jól elszúrtad...")
			ügyesség -=4
	elif chosen == "b":
		if pendrive in owned:
			print("Egy Commodore 64-nek is több memóriája van, mint neked! Minusz 4 ügyesség.")
			ügyesség -=4
		else:
			print("Felbaszol egy windowst a picsába. Minusz két ügyesség. Ki nem szarja le.")
			ügyesség -=2
	choice10()

def choice11():
	actual_choice = choice11
	print("Pali soft skill előadást tart, de te kicsit elkalandozol,\n\
az agyad már az elkövetkező feladatokon, programsorokon jár.\n\
Ő ezt észreveszi, és kiszúr magának.\n\
'Tehát mi a lényeg?' - kérdezi.")
	answer = input()
	if answer == "Asszertivitás" or "Az asszertivitás" or "asszertivitás" or "az asszertivitás":
		print("Mákod van öregem.")
	else:
		print("Nem tudod? Akkor most megláthatjátok hogyan kell a problémákat kezelni.\n\
Akkor most addig verlek ameddig asszertív nem leszel!")
		harc()
	choice12()

def choice12():
	actual_choice = choice12
	print("Véget ért az első nap, holnap új megpróbáltatások várnak.\n\
What a horrible night to have a curse.\n\
")
	choice13()
	
def choice13():
    próba = 0
    actual_choice = choice13
    print("The morning sun has vanquished the horrible night\n\
Az első feladatotok egy mentorbot elkészítése. Kit kérsz meg a feladatra?\n\
a, Palit\n\
b, Robit\n\
c, Imit")
    chosen = input()
    if chosen == a:
        print("Pali asszertívat közli veled: Nem.")
        próba += 1
        choice13()
    elif chosen == b:
        print("Robi azt válaszolja: Hallod, szerintem kérdezd meg discordon, hogy ráérek-e!")
        próba += 1
        choice13()
    elif chosen == c:
        print("Imi kipiszkál a foga közül egy sikertelen jelentkezőt és ráérősen közli:\n\
Nem érek rá, még el kell költenem a múlt havi fizetésem, mindjárt jön a másik, \n\
a bankszámlámra meg már nem fér több.")
        próba += 1
        choice13()
    elif próba == 3:
        print("Nem maradt számodra más, csak Peba,\n\
de valahogy balsejtelmed van a dologgal kapcsolatban...")
        choice14()

def choice14():
    actual_choice = choice14()
    print("A mentorbot program elpróbálásakor Peba programkódjában váratlan hiba lép fel.\n\
\n\
Látsz egy megvadult Pebabotot.\n\
Harcolsz vele?")
    answer = input()
    if answer == "igen" or "Igen":
        harc()
    elif answer == "nem" or "Nem":
        print("Kötekedősre itta magát, nagyon dühös, nem tudsz előle elmenekülni!")
        harc()
    elif answer == "use pálinka":
        print("Látsz egy szelíd Pebabotot.")
    choice15()



def choice15():
    actual_choice = choice15()
    print("A mentorok egyöntetűen tornyosulnak feléd,\n\
mint a Rushmore-hegy óriási mogorva elnökarcai,\n\
és azt kérdezik:\n\
'Hogy merészeltél az oktatásra alkoholt hozni?'\n\
Ekkor valami különös dolog történik, a mentorok elkezdenek\n\
egyszerre furcsa módon hadonászni és kiáltozni:\n\
Pali azt kiáltja: 'Python'\n\
Robi azt ordítja: 'Ruby'\n\
Imi azt üvölti: 'IBM basic'\n\
Peba azt bömböli: 'Pascal'\n\
Erre rögtön felhangzik egy földöntúli hang:\n\
Egyesített hatalmatokból én vagyok a Codecool kapitánya!")
    harc()
    choice16()

def choice16():
    actual_choice = choice16
    print("A nehézségek ellenére sikerül elkezdened a képzést,\n\
és a mentorbot prezentációd is jól sikerül.\n\
Talán egyszer még programozó is lesz belőled...\n\
Te is így gondolod?")
    answer = input()
    if answer == "igen" or "Igen":
        print("Persze, álmodozz csak. Nem mondtad, hogy Simon mondja.")
        choice16()
    elif answer == "nem" or "Nem":
        print("Hát, szerintem sem.")
        choice16()
    elif answer == "sudo igen":
        print("Talán van egy kis esélyed...")
    else:
        print("Nincs ilyen opciód.")
        choice16()

choice1()
exit()