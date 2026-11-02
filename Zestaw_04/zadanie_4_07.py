def flatten(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Argument musi być listą lub krotką.")

    wynik = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            podlista = flatten(element)
            for x in podlista:
                wynik.append(x)
        else:
            wynik.append(element)

    return wynik


assert flatten([]) == []
assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([1, (2, 3), 4]) == [1, 2, 3, 4]

sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
assert flatten(sequence) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("testy przeszly.")