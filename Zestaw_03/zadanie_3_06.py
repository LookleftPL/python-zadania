def zadanie_3_6(x,y):
    wynik = ""
    parzysta_linia = "+---" * x + "+"
    nieparzysta_linia = "|   " * x + "|"
    for i in range(2*y + 1):
        if i % 2 == 0:
            wynik+= parzysta_linia
        else:
            wynik+= nieparzysta_linia
        wynik+="\n"

    return wynik.rstrip()

print(zadanie_3_6(4,5))