import random
nummers = (1,2,3,4,5,6)

def numbergen():
    randomnummer = random.choice(nummers)
    return randomnummer

def fivenumbergen():
    numberslist = []
    for x in range(5):
        randomnummer = random.choice(nummers)
        numberslist.append(randomnummer)
    return numberslist


def herdobbelen(worp, te_vervangen_indexes):
    for index in te_vervangen_indexes:
        worp[index] = random.randint(1, 6) 
    return worp

def check_full_house(Worp):
    unique_counts = {Worp.count(x) for x in Worp}
    return unique_counts == {2, 3}

def check_small_straight(Worp):
    unique = sorted(set(Worp))
    return any(unique[i:i+4] == list(range(unique[i], unique[i]+4)) for i in range(len(unique) - 3))

def check_large_straight(Worp):
    unique = sorted(set(Worp))
    return unique == [1, 2, 3, 4, 5] or unique == [2, 3, 4, 5, 6]

def check_yahtzee(Worp):
    return len(set(Worp)) == 1

def check_four_of_a_kind(Worp):
    return any(Worp.count(x) >= 4 for x in Worp)

def check_three_of_a_kind(Worp):
    return any(Worp.count(x) >= 3 for x in Worp)

def alle_waarden_ingevuld(bord):
    return all(list(categorie.values())[0] != -1 for categorie in bord)
