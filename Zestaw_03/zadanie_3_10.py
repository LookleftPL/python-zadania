# Róźne sposoby tworzenia słownika

slownik1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}

slownik2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

slownik3 = dict([('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)])

slownik4 = dict(zip(['I','V','X','L','C','D','M'],[1,5,10,50,100,500,1000]))

def rzym_do_arab(liczba_rzym,slownik):
    suma = 0
    for i in range(len(liczba_rzym)):
        if (i == len(liczba_rzym) - 1) or slownik[liczba_rzym[i]] >= slownik[liczba_rzym[i+1]]:
            suma = suma + slownik[liczba_rzym[i]]
        else:
            suma = suma - slownik(liczba_rzym[i])

    return suma


assert rzym_do_arab("MMXXVI",slownik1) == 2026
print(rzym_do_arab("MMXXVI",slownik1))
