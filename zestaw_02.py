
def zadanie_2_10(tekst):
    lista_wyrazow = tekst.split()
    return len(lista_wyrazow)

def zadanie_2_11(tekst):
    tekst_rozdzielony = "_".join(tekst)
    return tekst_rozdzielony

def zadanie_2_12(tekst):
    lista_wyrazow = tekst.split()
    pierwsze = "".join([wyraz[0] for wyraz in lista_wyrazow])
    ostatnie = "".join([wyraz[-1] for wyraz in lista_wyrazow])
    return pierwsze,ostatnie

def zadanie_2_13(tekst):
    lista_wyrazow = tekst.split()
    dlugosci_slow = [len(wyraz) for wyraz in lista_wyrazow]
    laczna_dlugosc = sum(dlugosci_slow)
    return laczna_dlugosc

def zadanie_2_14(tekst):
    lista_wyrazow = tekst.split()
    najdluzsze_slowo = max(lista_wyrazow,key=len)
    dlugosc = len(najdluzsze_slowo)
    return najdluzsze_slowo,dlugosc

def zadanie_2_15(lista):
    slowo = "".join([str(liczba) for liczba in lista])
    return slowo

def zadanie_2_16(tekst):
    nowy_tekst = tekst.replace("GvR","Guido van Rossum")
    return nowy_tekst

def zadanie_2_17(tekst):
    tekst_male = tekst.lower()
    lista_wyrazow = tekst_male.split()
    lista_alfabetycznie = sorted(lista_wyrazow)
    lista_dlugosciowo = sorted(lista_wyrazow,key=len)
    return lista_alfabetycznie, lista_dlugosciowo

def zadanie_2_18(liczba):
    liczba_str = str(liczba)
    ilosc_zer = liczba_str.count("0")
    return ilosc_zer

def zadanie_2_19(lista):
    ciag_liczb = "".join([str.zfill(str(liczba),3) for liczba in lista])
    return ciag_liczb

line = "Ala\nma\nkota\ti GvR"
L = [1,22,333,44,555,6]
slowo = "word"
duza_liczba = 1200030203

assert zadanie_2_10(line) == 5
assert zadanie_2_11(slowo) == "w_o_r_d"
assert zadanie_2_12(line) == ("AmkiG","aaaiR")
assert zadanie_2_13(line) == 13
assert zadanie_2_14(line) == ("kota",4)
assert zadanie_2_15(L) == "122333445556"
assert zadanie_2_16(line) == "Ala\nma\nkota\ti Guido van Rossum"
assert zadanie_2_17(line) == (['ala', 'gvr', 'i', 'kota', 'ma'], ['i', 'ma', 'ala', 'gvr', 'kota'])
assert zadanie_2_18(duza_liczba) == 5
assert zadanie_2_19(L) == "001022333044555006"

print("Wszystkie testy przeszły.")

















