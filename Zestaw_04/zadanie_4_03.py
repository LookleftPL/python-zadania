
def factorial(n):
    """Iteracyjne obliczanie funkcji silnia n!"""
    if n < 0:
        raise ValueError("Wartość n nie może być ujemna.")
    suma = 1
    for i in range(2,n+1):
        suma = suma * i
    return suma

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(4) == 24
print("Testy przeszły")
