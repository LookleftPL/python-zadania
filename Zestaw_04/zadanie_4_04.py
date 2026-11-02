
def fibonacci(n):
    """Ciąg Fibonacciego iteracyjnie."""
    if n < 0:
        raise ValueError("Wartość n nie może być ujemna!")
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(2,n+1):
        tymczasowa = a + b
        a = b
        b = tymczasowa

    return b

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
print("Testy przeszly.")
