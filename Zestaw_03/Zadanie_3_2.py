# ZADANIE 3.2
# Przyklad nr 1
#L = [3, 5, 4] ; L = L.sort()
#ODPOWIEDŹ: W tym kodzie niepoprawne jest to , że do zmiennej L przypisujemy L.sort().
# .sort() sortuje nam listę ale tylko w pamięci i zwraca None, zatem taki kod utraci
# naszą listę pierwotną. Zamiast L = L.sort() ,powinno być samo L.sort()

#Przykład nr 2
#x, y = 1, 2, 3
# ODPOWIEDŹ: Tutaj niepoprawne jest to , ze po lewej stronie mamy 2 zmienne, a po prawej stronie 3 wartości.
# Zatem będzie błąd składniowy, bo brakuje jednej zmiennej.

#Przykład nr 3

#X = 1, 2, 3 ; X[1] = 4
# ODPOWIEDŹ: X = 1,2,3 tworzy krotkę, a z definicji krotka jest niemodyfikowalna, zatem nie da się
# zrobić X[1] = 4

#Przykład nr 4
#X = [1, 2, 3] ; X[3] = 4
# ODPOWIEDŹ: Próba przypisania wartości w liscie w indeksie numer 3 jest niewykonywalne, ponieważ
# w tym przypadku najwyższy indeks jaki mamy to 2.

#Przykład nr 5
#X = "abc" ; X.append("d")
# ODPOWIEDŹ: metoda append słuźy do list, a dla stringów używa się + (konkatenacja)

#Przykład nr 6
#L = list(map(pow, range(8)))
# ODPOWIEDŹ: Funkcja pow(), potrzebuje dwóch argumentów, a dostaje tylko jeden w tej linijce