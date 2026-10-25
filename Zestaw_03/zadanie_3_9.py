def zadanie_3_9(sekwencje):
    sumy_z_sekwencji = [sum(sekwencja) for sekwencja in sekwencje]
    return sumy_z_sekwencji


sekwencje = [[],[4],(1,2),[3,4],(5,6,7)]
assert zadanie_3_9(sekwencje) == [0, 4, 3, 7, 18]
print(zadanie_3_9(sekwencje))
