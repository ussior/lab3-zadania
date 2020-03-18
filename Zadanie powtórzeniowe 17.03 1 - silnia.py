number = int(input("Witaj w programie, który pomoże ci obliczyć silnię. Wprowadź liczbę całkowitą: "))
silnia = 1
for i in range (1, number+1):
    silnia = silnia*i
print("silnia z ", number, "wynosi ", silnia)