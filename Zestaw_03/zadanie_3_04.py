while True:
    x = input("Podaj liczbę rzeczywistą:")
    if x == "stop":
        break
    try:
        x = float(x)
        print(x)
        print(x**3)
    except ValueError:
        print("Błąd, Wprowadzono napis!")
