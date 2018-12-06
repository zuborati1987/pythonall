# adds -ing at the end of verbs
# 2018.10.23

x = input("Give me a verb, or type fin: ")
verbs = []

a = 0
b = 0
c = 0


def wordlenght():
    a = x[-1]
    b = x[-2]
    c = x[-3]
    return a, b, c, x



wordlenght()

def ingform(a, b, c, x, verbs):
    if x == "fin":
        exit()
    if x == "be" or "see" or "flee" or "knee":
        verbs.append(x + "ing")
    elif x.endswith('ie'):
        verbs.append(x[:-2] + "ying")
    elif (a == "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "x" or "z" or "w" or "y") and (b == "a" or "e" or "i" or "o" or "u") and (c == "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "x" or "z" or "w" or "y"):
        verbs.append(x + a + "ing")
    elif x.endswith('e'):
        verbs.append(x[:-1] + "ing")
    else:
        verbs.append(x + "ing")
    print (verbs)

ingform(a, b, c, x, verbs)
#verbs.append(input("Give me a verb: "))
#verbs = [verb + "ing" for verb in verbs]
#print (verbs)
