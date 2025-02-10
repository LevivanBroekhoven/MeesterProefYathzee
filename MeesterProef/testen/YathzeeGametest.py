from YathzeeData2 import *
from YathzeeFunctions import *


while True:
    Worp = fivenumbergen()
    print("Eerste worp:", Worp)

    for beurt in range(3):
        
        print("Huidige worp genummerd:")
        for i, waarde in enumerate(Worp):
            print(f"Index {i}: {waarde}")

        te_vervangen = input("Geef aan welke Dobbelsteen 0 tot 4 (gescheiden door spaties) je wilt herdobbelen, of druk op Enter om te stoppen: ")

        if not te_vervangen.strip():
            break  

        try:
            te_vervangen_indexes = [int(i) for i in te_vervangen.split()]
            Worp = herdobbelen(Worp, te_vervangen_indexes)
            print("Bijgewerkte worp:", Worp)
            
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")


    categorie_gevuld = False

    if 1 in Worp and Aces_value == -1:
        if input("Wil je de Aces invullen? (ja/nee): ") == "ja":
            Aces_value = Worp.count(1)
            print("Aces ingevuld:", Aces_value)
            categorie_gevuld = True
            Yathzeebord[0]["Aces"] = Aces_value

    elif 2 in Worp and Twos_value == -1:
        if input("Wil je de Twos invullen? (ja/nee): ") == "ja":
            Twos_value = Worp.count(2) * 2
            print("Twos ingevuld:", Twos_value)
            categorie_gevuld = True
            Yathzeebord[1]["Twos"] = Twos_value

    elif 3 in Worp and Threes_value == -1:
        if input("Wil je de Threes invullen? (ja/nee): ") == "ja":
            Threes_value = Worp.count(3) * 3
            print("Threes ingevuld:", Threes_value)
            categorie_gevuld = True
            Yathzeebord[2]["Threes"] = Threes_value

    elif 4 in Worp and Fours_value == -1:
        if input("Wil je de Fours invullen? (ja/nee): ") == "ja":
            Fours_value = Worp.count(4) * 4
            print("Fours ingevuld:", Fours_value)
            categorie_gevuld = True
            Yathzeebord[3]["Fours"] = Fours_value

    elif 5 in Worp and Fives_value == -1:
        if input("Wil je de Fives invullen? (ja/nee): ") == "ja":
            Fives_value = Worp.count(5) * 5
            print("Fives ingevuld:", Fives_value)
            categorie_gevuld = True
            Yathzeebord[4]["Fives"] = Fives_value

    elif 6 in Worp and Sixes_value == -1:
        if input("Wil je de Sixes invullen? (ja/nee): ") == "ja":
            Sixes_value = Worp.count(6) * 6
            print("Sixes ingevuld:", Sixes_value)
            categorie_gevuld = True
            Yathzeebord[5]["Sixes"] = Sixes_value

    elif FullHouse_value == -1 and check_full_house(Worp):
        if input("Wil je de Full House invullen? (ja/nee): ") == "ja":
            FullHouse_value = 25
            print("Full House ingevuld:", FullHouse_value)
            categorie_gevuld = True
            Yathzeebord[6]["Full House"] = FullHouse_value

    elif SmallStraight_value == -1 and check_small_straight(Worp):
        if input("Wil je de Kleine Straat invullen? (ja/nee): ") == "ja":
            SmallStraight_value = 30
            print("Kleine Straat ingevuld:", SmallStraight_value)
            categorie_gevuld = True
            Yathzeebord[7]["Small Straight"] = SmallStraight_value

    elif LargeStraight_value == -1 and check_large_straight(Worp):
        if input("Wil je de Grote Straat invullen? (ja/nee): ") == "ja":
            LargeStraight_value = 40
            print("Grote Straat ingevuld:", LargeStraight_value)
            categorie_gevuld = True
            Yathzeebord[8]["Large Straight"] = LargeStraight_value

    elif Yahtzee_value == -1 and check_yahtzee(Worp):
        if input("Wil je de Yahtzee invullen? (ja/nee): ") == "ja":
            Yahtzee_value = 50
            print("Yahtzee ingevuld:", Yahtzee_value)
            categorie_gevuld = True
            Yathzeebord[9]["Yahtzee"] = Yahtzee_value

    elif FourOfAKind_value == -1 and check_four_of_a_kind(Worp):
        if input("Wil je de Four of a Kind invullen? (ja/nee): ") == "ja":
            FourOfAKind_value = sum(Worp)
            print("Four of a Kind ingevuld:", FourOfAKind_value)
            categorie_gevuld = True
            Yathzeebord[10]["Four of a Kind"] = FourOfAKind_value

    elif ThreeOfAKind_value == -1 and check_three_of_a_kind(Worp):
        if input("Wil je de Three of a Kind invullen? (ja/nee): ") == "ja":
            ThreeOfAKind_value = sum(Worp)
            print("Three of a Kind ingevuld:", ThreeOfAKind_value)
            categorie_gevuld = True
            Yathzeebord[11]["Three of a Kind"] = ThreeOfAKind_value

    elif Chance_value == -1:
        if input("Wil je de Chance invullen? (ja/nee): ") == "ja":
            Chance_value = sum(Worp)
            print("Chance ingevuld:", Chance_value)
            categorie_gevuld = True
            Yathzeebord[12]["Chance"] = Chance_value

    if not categorie_gevuld:
        for index, categorie in enumerate(Yathzeebord):
            naam, waarde = list(categorie.items())[0]
            if waarde == -1:
                Yathzeebord[index][naam] = 0
                print(f"Geen categorie ingevuld. {naam} is automatisch op 0 gezet.")
                break
            
    
    if alle_waarden_ingevuld(Yathzeebord):
        print("Eindscorebord:", Yathzeebord)
        break

    
