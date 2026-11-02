
def odwracanie_iterycjnie(L, left,right):
    if left > right or right >= len(L) or left >= len(L) or left < 0 or right < 0:
        raise IndexError("Niepoprawne indeksy.")
    gorny_indeks = right
    for i in range(left,right+1):
        if i >= gorny_indeks:
            break
        tymczasowa = L[i]
        L[i] = L[gorny_indeks]
        L[gorny_indeks] =  tymczasowa
        gorny_indeks = gorny_indeks -1

    return None

def odwracanie_rekurencyjnie(L, left, right):
    if left < 0 or right >= len(L):
        raise IndexError("Niepoprawne indeksy.")

    if left >= right:
        return None

    tymczasowa = L[left]
    L[left] = L[right]
    L[right] = tymczasowa

    return odwracanie_rekurencyjnie(L, left + 1, right - 1)
L1 = [1, 2, 3, 4]
odwracanie_iterycjnie(L1, 0, 3)
assert L1 == [4, 3, 2, 1]

L2 = [10, 20, 30, 40, 50, 60]
odwracanie_iterycjnie(L2, 1, 4)
assert L2 == [10, 50, 40, 30, 20, 60]

L3 = [1, 2, 3]
odwracanie_iterycjnie(L3, 1, 1)
assert L3 == [1, 2, 3]

L4 = [1, 2, 3, 4]
odwracanie_rekurencyjnie(L4, 0, 3)
assert L4 == [4, 3, 2, 1]

L5 = [10, 20, 30, 40, 50, 60]
odwracanie_rekurencyjnie(L5, 1, 4)
assert L5 == [10, 50, 40, 30, 20, 60]

L6 = ["a", "b", "c"]
odwracanie_rekurencyjnie(L6, 1, 1)
assert L6 == ["a", "b", "c"]

print("Testy przeszły")