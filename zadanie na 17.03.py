items = input("Podaj przedmioty, które posiadasz (oddzielając je przecinkami): ")
items = tuple(items.split(","))
import random
eq_weight = 0
for item in items:
    weight = random.randint(1, 5)
    eq_weight += weight
print(items)
print("Twój ekwipunek waży ", eq_weight, "kg")
if eq_weight > 15:
    print("Niestety, musisz pozbyć się któregoś z przedmiotów - twój ekwipunek jest za ciężki")
else:
    print("Jesteś w stanie unieść swój ekwipunek!")