from sys import exit as exitProgram
from wykres import generowanieWykresu
from wartoscFunkcji import wartoscFunkcji
from horner import horner
from interpolacja import *
import numpy as np


def menu():
    while True:
        print("""
        
-------------------------------------------------------------------------        
Metoda interpolacji Newtona dla węzłów równoodległych
Lukasz Janiszewski, Maciej Kubis""")
        print("""
Wybierz opcje:
1. Rozpocznij program
2. Zakończ program""")
        wyborUzytkownika = int(input("""
Wybór: """))
        if wyborUzytkownika == 1:
            wczytywanieDanych()
        elif wyborUzytkownika == 2:
            exitProgram()
        else:
            print("""Wybrano nieprawidlowa opcje!""")


def wczytywanieDanych():
    print("""
Wybierz numer funkcji ktorej chcesz uzyc w programie:
    1. FUNKCJA LINIOWA: x + 18
    2. FUNKCJA: |x|
    3. FUNKCJA WIELOMIANOWA:  4 * x^3 + 2 * x^2 - 8 * x + 4
    4. FUNKCJA TRYGONOMETRYCZNA:  8 * cos(x) - 2 * sin(x)
    5. FUNKCJA ZŁOŻONA:  |cos(x - 1) - 0.8|""")
    numerFunkcji = int(input("""
Wybór: """))
    while numerFunkcji not in [1, 2, 3, 4, 5]:
        poprawnaLiczba = False
        while not poprawnaLiczba:
            numerFunkcji = int(input("""
                Wybierz jeszcze raz numer funkcji: """))
            if numerFunkcji in [1, 2, 3, 4, 5]:
                poprawnaLiczba = True

    lewaGranica = float(input("""
Podaj lewa granice przedziału interpolacji: """))
    prawaGranica = float(input("""Podaj prawa granice przedziału interpolacji: """))

    liczbaWezlow = int(input("""
Podaj liczbę węzłów interpolacji: """))
    while liczbaWezlow < 1:
        print("Podaj liczbę węzłów interpolacji większą od 1!")
        liczbaWezlow = int(input("""
Podaj liczbę węzłów interpolacji: """))

    argumenty = list(np.linspace(lewaGranica, prawaGranica, 1000))

    wartosciFunkcji = []
    for x in argumenty:
        wartosciFunkcji.append(wartoscFunkcji(x, numerFunkcji))

    x_pkt_inter = np.linspace(lewaGranica, prawaGranica, liczbaWezlow)
    y_pkt_inter = list(wartoscFunkcji(x_pkt_inter, numerFunkcji))
    x_pkt_inter = list(x_pkt_inter)

    wartosciWielomianu = obliczenia(lewaGranica, prawaGranica, liczbaWezlow, numerFunkcji, argumenty, x_pkt_inter,
                                   y_pkt_inter)

    prezentacja(lewaGranica, prawaGranica, argumenty, wartosciFunkcji, wartosciWielomianu, liczbaWezlow, numerFunkcji,
                x_pkt_inter, y_pkt_inter)


def obliczenia(lewaGranica, prawaGranica, liczbaWezlow, numerFunkcji, argumenty, x_pkt_inter, y_pkt_inter):
    x = sp.Symbol('x')
    wzor_interpolacji_wprzod = interpolacja_wprzod(x_pkt_inter, y_pkt_inter)
    wzor_interpolacji_wstecz = interpolacja_wstecz(x_pkt_inter, y_pkt_inter)
    wspolczynniki_interpolacji_wprzod = sp.Poly(wzor_interpolacji_wprzod, x).all_coeffs()
    wspolczynniki_interpolacji_wstecz = sp.Poly(wzor_interpolacji_wstecz, x).all_coeffs()
    wartosci = []
    for argument in argumenty:
        if argument < (argumenty[-1] + argumenty[0]) / 2:
            wartosci.append(horner(wspolczynniki_interpolacji_wprzod, argument))
        else:
            wartosci.append(horner(wspolczynniki_interpolacji_wstecz, argument))

    return wartosci


def prezentacja(lewaGranica, prawaGranica, argumenty, wartosciFunkcji, wartosciWielomianu, liczbaWezlow, numerFunkcji,
                x_pkt_inter, y_pkt_inter):
    generowanieWykresu(lewaGranica, prawaGranica, argumenty, wartosciFunkcji, wartosciWielomianu, liczbaWezlow,
                       numerFunkcji, x_pkt_inter, y_pkt_inter)


##########################################################################
# START
##########################################################################
menu()
