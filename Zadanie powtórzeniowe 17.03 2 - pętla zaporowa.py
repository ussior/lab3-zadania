num = int(input("Witaj w pętli zaporowej, podaj liczbę całkowitą dodatnią: "))
while num == 0 or num < 0:
  num = int(input("Liczba miała być dodatnia. Podaj liczbę dodatnią: "))
print("Okej, teraz się zgadza.", num)