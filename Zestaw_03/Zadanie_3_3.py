def zadanie3_3_for():
    wynik = ""
    for i in range(31):
        if i % 3 == 0:
            continue
        wynik = wynik + str(i) +"\n"
    return wynik

def zadanie3_3_while():
    wynik = ""
    i = 0
    while i <= 30:
        if i % 3 == 0:
            i+=1
            continue
        wynik = wynik + str(i) + "\n"
        i+=1
    return wynik

assert zadanie3_3_for() == "1\n2\n4\n5\n7\n8\n10\n11\n13\n14\n16\n17\n19\n20\n22\n23\n25\n26\n28\n29\n"
assert zadanie3_3_while() == "1\n2\n4\n5\n7\n8\n10\n11\n13\n14\n16\n17\n19\n20\n22\n23\n25\n26\n28\n29\n"
print("Testy przeszły.")