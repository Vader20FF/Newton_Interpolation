def horner(listaWspolczynnikow, x):
    wynik = 0
    for wspolczynnik in listaWspolczynnikow:
        wynik = wynik * x + wspolczynnik
    return wynik
