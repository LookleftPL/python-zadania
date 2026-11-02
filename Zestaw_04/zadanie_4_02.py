def make_ruler(n):
    result = "|...."*n + "|"
    result = result + "\n"
    for i in range(n+1):
        result = result + str(i)
        if i <9:
            result += "    "
        elif i < 99:
            result +="   "
        elif i < 999:
            result +="  "
        elif i < 9999:
            result +=" "

    return result.rstrip()

def make_grid(rows,cols):
    wynik = ""
    parzysta_linia = "+---" * rows + "+"
    nieparzysta_linia = "|   " * rows + "|"
    for i in range(2*cols + 1):
        if i % 2 == 0:
            wynik+= parzysta_linia
        else:
            wynik+= nieparzysta_linia
        wynik+="\n"

    return wynik.rstrip()

print(make_ruler(9999))
print(make_grid(4,5))