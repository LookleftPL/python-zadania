def zadanie_3_8(lista1,lista2):
    zbior1 = set(lista1)
    zbior2 = set(lista2)

    przeciecie = zbior1 & zbior2
    suma_zbiorow = zbior1 | zbior2

    return list(przeciecie), list(suma_zbiorow)


lista1 = [1,5,10,15,20]
lista2 = [0,2,4,6,8,10,12,14,16,18,20]

assert zadanie_3_8(lista1,lista2) == ([10, 20], [0, 1, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20])
print(zadanie_3_8(lista1,lista2))