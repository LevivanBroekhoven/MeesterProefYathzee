from Yathzee import *

EersteWorp = fivenumbergen()
print(EersteWorp)

for x in range(3):
    redobble = input("Wil je herdobbelen? ")

    if redobble == ("ja"):
        hoeveeldobble= int(input("Hoeveel wil je herdobbelen? "))
        for x in range(0, hoeveeldobble):
            welkedobble = int(input("Welke wil je herdobbelen?** "))
            EersteWorp.remove(welkedobble)
            newnumber = numbergen()
            EersteWorp.append(newnumber)
            print(EersteWorp)
        break
    if redobble == ("nee"):
        break
print("Test")

