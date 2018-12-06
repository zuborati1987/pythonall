# game book writing
# 2018.10.25

import random
import subprocess

items = [
    "pálinka",
    "kalandkönyv",
    "pénz",
    "energiaital",
    "pendrive",
    "fegyver",
    "egér",
    "cigi",
    "kaja"]
owned = []
ügyesség = int(random.randint(1, 5) + 6)
életerő = int(random.randint(2, 11) + 12)
szerencse = int(random.randint(1, 5) + 6)
actual_choice = "choice1"
ellenfél_életerő = 0
ellenfél_ügyesség = 0
ellenfél = ""


def stats(eletero, ugyesseg, szerencse):
    print(
        "Életerőd: {}, Ügyességed: {}, Szerencséd {}".format(
            eletero,
            ugyesseg,
            szerencse))


def pali():
    global ellenfél_életerő
    ellenfél_életerő = 8
    global ellenfél_ügyesség
    ellenfél_ügyesség = 6
    global ellenfél
    ellenfél = "pali"
    return ellenfél_életerő, ellenfél_ügyesség, ellenfél


def robi():
    global ellenfél_életerő
    ellenfél_életerő = 7
    global ellenfél_ügyesség
    ellenfél_ügyesség = 5
    ellenfél = "robi"
    return ellenfél_életerő, ellenfél_ügyesség, ellenfél


def imi():
    global ellenfél_életerő
    ellenfél_életerő = 8
    global ellenfél_ügyesség
    ellenfél_ügyesség = 6
    global ellenfél
    ellenfél = "imi"
    return ellenfél_életerő, ellenfél_ügyesség, ellenfél


def portas():
    global ellenfél_életerő
    ellenfél_életerő = 5
    global ellenfél_ügyesség
    ellenfél_ügyesség = 5
    global ellenfél
    ellenfél = "portas"
    return ellenfél_életerő, ellenfél_ügyesség


def random_coder():
    global ellenfél_életerő
    ellenfél_életerő = 4
    global ellenfél_ügyesség
    ellenfél_ügyesség = 5
    global ellenfél
    ellenfél = "random_coder"
    return ellenfél_életerő, ellenfél_ügyesség


def dumblermain():
    global ellenfél_életerő
    ellenfél_életerő = 50
    global ellenfél_ügyesség
    ellenfél_ügyesség = 30
    global ellenfél
    ellenfél = "dumblermain"
    return ellenfél_életerő, ellenfél_ügyesség, ellenfél


def peba():
    global ellenfél_életerő
    ellenfél_életerő = 20
    global ellenfél_ügyesség
    ellenfél_ügyesség = 7
    global ellenfél
    ellenfél = "peba"
    return ellenfél_életerő, ellenfél_ügyesség


def codecool_kapitany():
    global ellenfél_életerő
    ellenfél_életerő = 30
    global ellenfél_ügyesség
    ellenfél_ügyesség = 10
    global ellenfél
    ellenfél = "coder_kapitány"
    return ellenfél_életerő, ellenfél_ügyesség, ellenfél


def kopapir():
    global életerő
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
        életerő -= 4
    return életerő


def harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél):
    global életerő
    global ügyesség
    siker = int(random.randint(1, 2))
    luck = int(random.randint(1, 2))
    if ellenfél != 'coder_kapitány':
        if ellenfél != 'dumblermain':
            valasz = input("Harcra kerül a sor, használsz varázslatot? ")
            if valasz == "igen":
                valasz = input(
                    'Varázslataid: cast ruby, cast java, cast python. Válassz: ')
                if valasz == 'cast ruby':
                    if ellenfél == 'pali':
                        print(
                            "Pali már így is rubint keménységű, így nem hat rá a varázslatod. A harc folytatódik.")
                    else:
                        if luck == siker:
                            print(
                                "Ellenfeledet rubinttá változtattad! Ő ennek nem örül.")
                            return
                        else:
                            print(
                                "Besült a varázslatod, elvesztettél 5 életerőt, kezdődik a harc.")
                            életerő -= 5
                elif valasz == 'cast java':
                    if ellenfél == 'imi':
                        print("Imi megeszi őket reggelire.")
                    else:
                        if luck == siker:
                            print(
                                "Megidézel egy csapat java-t a tatooine-ról, akik megtámadják ellenfeledet")
                            return
                        else:
                            print(
                                "Besült a varázslatod, elvesztettél 5 életerőt, kezdődik a harc.")
                elif valasz == 'cast python':
                    if ellenfél == 'robi':
                        print(
                            "Mit akarsz ezekkel a sziszegő szarokkal? A varázslatod hatástalan, folytatódik a harc.")
                    else:
                        if luck == siker:
                            print(
                                "Megidézel egy zsák mérges pitont, akik megeszik az ellenfeled!")
                            return
                        else:
                            print(
                                "Besült a varázslatod, elvesztettél 5 életerőt, kezdődik a harc.")
                            életerő -= 5
            else:
                print("Megkezdődik a harc!")
        else:
            print("Megkezdődik a harc!")
    else:
        print("Megkezdődik a harc!")
    print(
        " Az életerőd: {}, ügyességed {}, Az ellenfél életereje: {}, az ellenfél ügyessége {}".format(
            életerő,
            ügyesség,
            ellenfél_életerő,
            ellenfél_ügyesség))
    while életerő > 0 and ellenfél_életerő > 0:
        valasz = input('Mit csinálsz? Harc vagy menekülés? ')
        if valasz == 'menekülés':
            életerő -= 10
            print("Elvesztettél 10 életerőt te gyökér.")
            return
        alapérték = random.randint(2, 12)
        támadóerő = alapérték + ügyesség
        ellenfél_támadóerő = alapérték + ellenfél_ügyesség
        print(
            "Támadóerőd: ",
            támadóerő,
            "Az ellenfél támadóereje: ",
            ellenfél_támadóerő)
        if ellenfél_támadóerő > támadóerő:
            answer = input("Ellenfeled két sebzést okozna, egy kő-papír-olló játékkal kivédheted,\n\
            de akár meg is duplázhatod. Kockáztatsz? ")
            if answer == 'igen':
                kopapir()
            elif answer == 'nem':
                életerő -= 2
            else:
                print(
                    "Hogy akarsz programozó lenni, ha ezt sem érted? Minusz 2 életerő.")
                életerő -= 2
            print(
                " Az életerőd: {}, Az ellenfél életereje: {}".format(
                    életerő, ellenfél_életerő))
        else:
            ellenfél_életerő -= 2
            print(
                " Az életerőd: {}, Az ellenfél életereje: {}".format(
                    életerő, ellenfél_életerő))

    if ellenfél_életerő <= 0:
        print("Legyőzted ellenfeledet!")
    elif életerő <= 0:
        print("Vesztettél, sajnos sosem lesz belőled programozó!")

    return életerő


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
    while j <= 5:
        c = input('Választásod? ')
        for i in range(len(items)):
            if c == items[i]:
                owned.append(c)
                j += 1


def use():
    used = input('Mit szeretnél használni? ')
    if used == 'pálinka':
        if 'pálinka' in owned:
            palinka(életerő)
            owned.remove('pálinka')
            print(
                "Felszívtad az összes pálinkát, te rohadt tintás! De legalább kaptál 2 életerő pontot")
        else:
            print("Nincs nálad ilyen.")

    if used == 'energiaital':
        if 'energiaital' in owned:
            nrg(életerő, ügyesség)
            owned.remove('energiaital')
            print("Négy dupla presszó adagját ittad meg egyszerre, számolj vissza mikor áll le a szíved!\n\
            Elvesztettél 2 életpontyot, kaptál 3 ügyességet.")
        else:
            print("Nincs ilyen tárgyad.")

    if used == 'fegyver':
        if 'fegyver' in owned:
            fegyver(ügyesség)
            owned.remove('fegyver')
            print("Kiürült a tárad, eldobtad a fegyvered, mert lusta vagy másikat keresni.\n\
            Legalább kaptál 7 ügyi pontot.")
        else:
            print("Nincs nálad ilyen.")

    if used == 'cigi':
        if 'cigi' in owned:
            cigi(életerő, szerencse)
            owned.remove('cigi')
            print("Sikerült elszívnod egy egész dobozzal te láncdohányos! Elvesztetted a tüdőd felét 2,\n\
            de kaptál 2 életpontot.")
        else:
            print("Nincs ilyen tárgyad.")

    if used == 'kaja':
        if 'kaja' in owned:
            kaja(életerő)
            owned.remove('kaja')
            print(
                "Telezabáltad magad, fáj a hasad, el kell menned wc-re, de legalább gyógyultál 5 pontot!")
        else:
            print("Éhen fogsz pusztulni, hehe!")


def targy():
    valasz = input("Szeretnél tárgyat használni?")
    if valasz == "igen":
        stats(életerő, ügyesség, szerencse)
        use()
    else:
        input('Nyomj ENTER-t a továbblépéshez')


def choice1(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    global életerő
    actual_choice = "choice1"
    print("Elérkezett a nagy nap. Elhatároztad, hogy programozó leszel. Hogyan fogsz neki a tanulásnak?\n\
    a, Elmegyek a Greenfoxba.\n\
    b, Elmegyek az egyetemre.\n\
    c, Megtanulom magamtól.\n\
    d, A Codecoolt választom.")
    chosen = input('Melyiket választod? ')
    if chosen == "a":
        print("Zöld rókák nem léteznek.\n")
        choice1(ellenfél_életerő, ellenfél_ügyesség)
    elif chosen == "b":
        print("3 éven át tanulod a számítástechnika történelmét és a matekot.\n\
        Már egész jól kiismered magadat pascalban. Vesztesz 10 életerőt.\n")
        életerő -= 10
        choice1(ellenfél_életerő, ellenfél_ügyesség)
    elif chosen == "c":
        print("De mi az a _name__=__main_?\n\
        Megjelenik Dumblermain varázsló!\n")
        dumblermain()
        proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
        harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
        proc1.kill()
        életerő = int(random.randint(2, 11) + 12)
        choice1(ellenfél_életerő, ellenfél_ügyesség)
    elif chosen == "d":
        print("Úgy döntesz, hogy a codecool az egyetlen helyes megoldás.\n")
    else:
        print("Hogy akarsz programozó lenni, ha ezt sem érted?\n")
        choice1(ellenfél_életerő, ellenfél_ügyesség)

    return életerő, actual_choice


def choice2(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    actual_choice = "choice2"
    print("Elérkezik a felvételi napja. A kapunál a biztonsági őr fogad.\n\
    Van mágneskártyád?")
    portas()
    proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
    harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
    proc1.kill()

    return életerő


def choice3(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    actual_choice = "choice3"
    print("A felvételin bemutatkozik nektek Robi, ő vizsgáztat titeket.\n\
    /Egy programozónak érvényesíteni kell tudnia az érdekeit a felhasználókkal szemben,\n\
    ezért most teszteljük, hogyan tudjátok megvédeni magatokat!/\n")
    proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
    robi()
    harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
    proc1.kill()

    return életerő, actual_choice


def choice4(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    actual_choice = "choice4"
    print("A felvételi továbbhalad a többi jelentkezővel, egyszercsak megjelenik Imi:\n\
    “Na mi van, itt csicskultok a csicskítóban ti csicskák?”\n\
    Azt se tudod, hol vagy, hirtelen csak annyit tudsz kinyögni: “Tessék...?”\n\
    “Ne vitatkozz velem, te csicska!”\n")
    proc1 = subprocess.Popen(['mpg321', '-q', "ff7.mp3"])
    imi()
    harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
    proc1.kill()
    return életerő, actual_choice


def choice5(ellenfél_életerő, ellenfél_ügyesség, owned):
    global actual_choice
    actual_choice = "choice5"
    print("Sikeresen átmentél a felvételin. Az első nap a kapuban a biztonsági őr fogad.\n\
    Ajjaj, sürgősen szerezni kell egy mágneskártyát.\n")
    proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
    harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
    proc1.kill()
    if 'egér' in owned:
        actual_choice = "choice6"
    else:
        choice7(owned, életerő)

    return actual_choice


def choice6(ellenfél_életerő, ellenfél_ügyesség, owned):
    global actual_choice
    actual_choice = "choice6"
    print("Megkezdődik az első tanítási nap. Épphogycsak helyet foglalsz,\n\
    amikor a magaddal hozott egér kiszökik a táskádból, Robi észreveszi:\n\
    “Ki mondta, hogy lehet állatot behozni?”\n")
    proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
    robi()
    harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
    proc1.kill()
    choice7(owned, életerő)

    return actual_choice


def choice7(owned, életerő):  # nincs külön hívása
    global actual_choice
    actual_choice = "choice7"
    print("Elérkezik az ebédszünet ideje. Ha hoztál magaddal ételt, megebédelhetsz,\n\
    vagy ha van nálad pénz, kimehetsz a büfébe venni valamit.\n\
    a, megebédelek\n\
    b, veszek egy csokit\n\
    c, sajnos nem hoztam magammal egyiket sem\n")
    chosen = input()
    if chosen == "a":
        if 'kaja' in owned:
            kaja(életerő)
            print("Jóllakottan folytatod a napot.")
        else:
            print("Dehát nincs is nálad kaja!")
            choice7(owned, életerő)
    elif chosen == "b":
        if 'pénz' in owned:
            kaja(életerő)
            print("Jóllakottan folytatod a napot.")
        else:
            print("Dehát nincs is pénzed!")
            choice7(owned, életerő)
    elif chosen == "c":
        print("Sajnos üres gyomorral kell folytatnod a napot. Minusz 5 életerő.")
        életerő -= 5
    else:
        print("Sajnos üres gyomorral kell folytatnod a napot. Minusz 5 életerő.")
        életerő -= 5

    return életerő, actual_choice


def choice8(ellenfél_életerő, ellenfél_ügyesség, owned):
    global actual_choice
    actual_choice = "choice8"
    print("Az ebédidő után a mágneskártyák kerülnek kiosztásra,\n\
    de sajnos neked nem jut belőle. Kibírod nélküle, vagy megpróbálod megszerezni valakiét?\n\
    a, igen\n\
    b, megvagyok nélküle")
    chosen = input()
    if chosen == "a":
        random_coder()
        proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
        harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
        proc1.kill()
        owned.append("mágneskártya")
    elif chosen == "b":
        print("Úgy gondolod, hogy majd bejutsz valahogy.")
    else:
        print("Hogy akarsz programozó lenni, ha ezt sem érted?")
    return actual_choice


def choice9(owned):
    global actual_choice
    global ügyesség
    actual_choice = "choice9"
    print("Az ubuntud abbahagyja a működést. Hoztál pen driveot?")
    print("a, Hoztam, persze, aha!\n\
    b, Nem, sajnos nincsen nálam.")
    chosen = input()
    if chosen == "a":
        if 'pendrive' in owned:
            print(
                "Újrarakod az Ubuntut, és útközben tanulsz is valamit! Plusz 2 ügyesség.")
            ügyesség += 2
        else:
            print("Te kis hazug geci! Ügyesség minusz 4,ezt most jól elszúrtad...")
            ügyesség -= 4
    elif chosen == "b":
        if 'pendrive' in owned:
            print(
                "Egy Commodore 64-nek is több memóriája van, mint neked! Minusz 4 ügyesség.")
            ügyesség -= 4
        else:
            print(
                "Felbaszol egy windowst a picsába. Minusz két ügyesség. Ki nem szarja le.")
            ügyesség -= 2
    else:
        print("Hogy akarsz programozó lenni, ha ezt sem érted?")
        choice9(owned)

    return ügyesség, actual_choice


def choice11(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    actual_choice = "choice11"
    print("Pali soft skill előadást tart, de te kicsit elkalandozol,\n\
    az agyad már az elkövetkező feladatokon, programsorokon jár.\n\
    Ő ezt észreveszi, és kiszúr magának.\n\
    'Tehát mi a lényeg?' - kérdezi.")
    answer = input()
    if answer == "Asszertivitás" and "asszertivitás" and "az asszertivitás":
        print("Mákod van öregem.")
    elif answer == "Az asszertivitás":
        print("Mákod van öregem.")
    elif answer == "asszertivitás":
        print("Mákod van öregem.")
    elif answer == "az asszertivitás":
        print("Mákod van öregem.")
    else:
        print("Nem tudod? Akkor most megláthatjátok hogyan kell a problémákat kezelni.\n\
        Akkor most addig verlek ameddig asszertív nem leszel!")
        pali()
        proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
        harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
        proc1.kill()
    return actual_choice


def choice12(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    actual_choice = "choice12"
    print("Véget ért az első nap, holnap új megpróbáltatások várnak.")
    print("A második nap reggelén, ismét kéri a mágneskártyádat.")
    if 'mágneskártya' not in owned:
        proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
        harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
        proc1.kill()
    else:
        print("Szerencséd van, az öreg mosolyogva beengedett.")
    return actual_choice


def choice13():
    global actual_choice
    actual_choice = "choice13"
    print("Az első feladatotok egy mentorbot elkészítése. Kit kérsz meg a feladatra?\n\
    a, Palit\n\
    b, Robit\n\
    c, Imit\n\
    d, Peba")
    chosen = input()
    if chosen == 'a':
        print("Pali asszertívan közli veled: Nem.\n")
        choice13()
    elif chosen == 'b':
        print(
            "Robi azt válaszolja: Hallod, szerintem kérdezd meg discordon, hogy ráérek-e!\n")
        choice13()
    elif chosen == 'c':
        print("Imi kipiszkál a foga közül egy sikertelen jelentkezőt és ráérősen közli:\n\
        Nem érek rá, még el kell költenem a múlt havi fizetésem, mindjárt jön a másik, \n\
        a bankszámlámra meg már nem fér több.\n")
        choice13()
    elif chosen == 'd':
        print("Végül Peba mellett döntesz,\n\
        de valahogy balsejtelmed van a dologgal kapcsolatban...\n")
    else:
        print("Hogy akarsz programozó lenni, ha ezt sem érted?\n")
        choice13()

    return actual_choice


def choice14(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    actual_choice = "choice14"
    print("A mentorbot program elpróbálásakor Peba programkódjában váratlan hiba lép fel.\n\
    \n\
    Látsz egy megvadult Pebabotot.\n\
    Harcolsz vele?")
    answer = input()
    if answer == "igen":
        peba()
        proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
        harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
        proc1.kill()
    elif answer == "nem":
        print("Kötekedősre itta magát, nagyon dühös, nem tudsz előle elmenekülni!")
        peba()
        proc1 = subprocess.Popen(['mpg321', '-q', "tds.mp3"])
        harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
        proc1.kill()
    elif answer == "use pálinka":
        print("Látsz egy szelíd Pebabotot.")
        actual_choice = "choice15"
    else:
        print("Hogy akarsz programozó lenni, ha ezt sem érted?")
        choice14(ellenfél_életerő, ellenfél_ügyesség)
    return actual_choice


def choice15(ellenfél_életerő, ellenfél_ügyesség):
    global actual_choice
    actual_choice = "choice15"
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
    proc1 = subprocess.Popen(['mpg321', '-q', "ff7.mp3"])
    harc(ellenfél_életerő, ellenfél_ügyesség, ellenfél)
    proc1.kill()
    choice16()
    return actual_choice


def choice16():
    global actual_choice
    actual_choice = "choice16"
    print("A nehézségek ellenére sikerül elkezdened a képzést,\n\
    és a mentorbot prezentációd is jól sikerül.\n\
    Talán egyszer még programozó is lesz belőled...\n\
    Te is így gondolod?")
    answer = input()
    if answer == 'sudo igen':
        print("Talán van egy kis esélyed...")
    elif answer == 'nem':
        print("Hát, szerintem sem.")
        choice16()
    elif answer == 'igen':
        print("Persze, álmodozz csak. Nem mondtad, hogy Simon mondja.")
        choice16()
    else:
        print("Nincs ilyen opciód.")
        choice16()
    return actual_choice


def choicex():
    d = input('Megnyitottad a fejlesztői részt! Ird be a kellő rész kódját: ')
    if int(d) == 1:
        choice1(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 2:
        choice2(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 3:
        choice3(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 4:
        choice4(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 5:
        choice5(ellenfél_életerő, ellenfél_ügyesség, owned)
        return
    elif int(d) == 6:
        choice6(ellenfél_életerő, ellenfél_ügyesség, owned)
    elif int(d) == 7:
        choice7(owned, életerő)
    elif int(d) == 8:
        choice8(ellenfél_életerő, ellenfél_ügyesség, owned)
    elif int(d) == 9:
        choice9(owned)
    elif int(d) == 11:
        choice11(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 12:
        choice12(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 13:
        choice13()
    elif int(d) == 14:
        choice14(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 15:
        choice15(ellenfél_életerő, ellenfél_ügyesség)
    elif int(d) == 16:
        choice16()
    else:
        return


def main():
    k = input('Kezdődjön a játék!')
    if k == 'choicex':
        choicex()
    else:
        global actual_choice
        stats(életerő, ügyesség, szerencse)
        lista()
        dumblermain()
        choice1(ellenfél_életerő, ellenfél_ügyesség)
        input('Nyomj ENTER-t a továbblépéshez')
        portas()
        choice2(ellenfél_életerő, ellenfél_ügyesség)
        targy()
        robi()
        choice3(ellenfél_életerő, ellenfél_ügyesség)
        targy()
        imi()
        choice4(ellenfél_életerő, ellenfél_ügyesség)
        targy()
        portas()
        choice5(ellenfél_életerő, ellenfél_ügyesség, owned)
        targy()
        if actual_choice == 'choice6':
            robi()
            choice6(ellenfél_életerő, ellenfél_ügyesség, owned)
        random_coder()
        choice8(ellenfél_életerő, ellenfél_ügyesség, owned)
        targy()
        choice9(owned)
        targy()
        pali()
        choice11(ellenfél_életerő, ellenfél_ügyesség)
        targy()
        portas()
        choice12(ellenfél_életerő, ellenfél_ügyesség)
        targy()
        choice13()
        targy()
        peba()
        choice14(ellenfél_életerő, ellenfél_ügyesség)
        targy()
        if actual_choice == 'choice15':
            codecool_kapitany()
            choice15(ellenfél_életerő, ellenfél_ügyesség)
        choice16()


if __name__ == '__main__':
    main()
