def sum_seq(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Argument musi być listą lub krotką.")

    suma = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            suma = suma + sum_seq(element)
        else:
            suma = suma + element

    return suma


assert sum_seq([]) == 0
assert sum_seq([1, 2, 3]) == 6
assert sum_seq([1, (2, 3), 4]) == 10
assert sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == 45

print("testy przeszły.")