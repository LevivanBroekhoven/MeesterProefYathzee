Yathzeebord = [
    {"Aces": -1}, {"Twos": -1}, {"Threes": -1}, {"Fours": -1}, {"Fives": -1}, {"Sixes": -1},
    {"Full House": -1}, {"Small Straight": -1}, {"Large Straight": -1}, {"Yahtzee": -1},
    {"Four of a Kind": -1}, {"Three of a Kind": -1}, {"Chance": -1}]

Aces_value = Yathzeebord[0]["Aces"]
Twos_value = Yathzeebord[1]["Twos"]
Threes_value = Yathzeebord[2]["Threes"]
Fours_value = Yathzeebord[3]["Fours"]
Fives_value = Yathzeebord[4]["Fives"]
Sixes_value = Yathzeebord[5]["Sixes"]

FullHouse_value = Yathzeebord[6]["Full House"]
SmallStraight_value = Yathzeebord[7]["Small Straight"]
LargeStraight_value = Yathzeebord[8]["Large Straight"]
Yahtzee_value = Yathzeebord[9]["Yahtzee"]
FourOfAKind_value = Yathzeebord[10]["Four of a Kind"]
ThreeOfAKind_value = Yathzeebord[11]["Three of a Kind"]
Chance_value = Yathzeebord[12]["Chance"]


# def invullen_upper_section(getal, naam, index, worp, yathzeebord, categorie_gevuld):
#     """
#     Probeert een getal (1-6) in te vullen op het Yahtzee-scorebord als aan de voorwaarden wordt voldaan.
#     """
#     if getal in worp and not categorie_gevuld and yathzeebord[index][naam] == -1:
#         if input(f"Wil je de {naam} invullen? (ja/nee): ") == "ja":
#             yathzeebord[index][naam] = worp.count(getal) * getal
#             print(f"{naam} ingevuld:", yathzeebord[index][naam])
#             return True  # categorie_gevuld wordt True
#     return categorie_gevuld

# # Roep de functie aan voor elk getal van 1 t/m 6
# categorie_gevuld = invullen_upper_section(1, "Aces", 0, Worp, Yathzeebord, categorie_gevuld)
# categorie_gevuld = invullen_upper_section(2, "Twos", 1, Worp, Yathzeebord, categorie_gevuld)
# categorie_gevuld = invullen_upper_section(3, "Threes", 2, Worp, Yathzeebord, categorie_gevuld)
# categorie_gevuld = invullen_upper_section(4, "Fours", 3, Worp, Yathzeebord, categorie_gevuld)
# categorie_gevuld = invullen_upper_section(5, "Fives", 4, Worp, Yathzeebord, categorie_gevuld)
# categorie_gevuld = invullen_upper_section(6, "Sixes", 5, Worp, Yathzeebord, categorie_gevuld)
