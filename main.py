from sys import exit as exitProgram
from graph import generate_graph
from function_value import get_function_value
from horner import get_polynomial_value
from interpolation_functions import forward_interpolation, backwards_interpolation
import numpy as np
import sympy as sp


def menu():
    while True:
        print("""
        
-------------------------------------------------------------------------        
Metoda interpolacji Newtona dla węzłów równoodległych
Lukasz Janiszewski, Maciej Kubis""")
        print("""
Wybierz opcję:
1. Rozpocznij program
2. Zakończ program""")
        user_choice = int(input("""
Wybór: """))
        if user_choice == 1:
            data_load()
        elif user_choice == 2:
            exitProgram()
        else:
            print("""Wybrano nieprawidlowa opcje!""")


def data_load():
    print("""
Wybierz numer funkcji ktorej chcesz uzyc w programie:
    1. FUNKCJA LINIOWA: x + 18
    2. FUNKCJA: |x|
    3. FUNKCJA WIELOMIANOWA:  4 * x^3 + 2 * x^2 - 8 * x + 4
    4. FUNKCJA TRYGONOMETRYCZNA:  8 * cos(x) - 2 * sin(x)
    5. FUNKCJA ZŁOŻONA:  |cos(x - 1) - 0.8|""")
    function_number = int(input("""
Wybór: """))
    while function_number not in [1, 2, 3, 4, 5]:
        valid_number = False
        while not valid_number:
            function_number = int(input("""
                Wybierz jeszcze raz numer funkcji: """))
            if function_number in [1, 2, 3, 4, 5]:
                valid_number = True

    left_border = float(input("""
Podaj lewa granice przedziału interpolacji: """))
    right_border = float(input("""Podaj prawa granice przedziału interpolacji: """))

    nodes_number = int(input("""
Podaj liczbę węzłów interpolacji: """))
    while nodes_number < 1:
        print("Podaj liczbę węzłów interpolacji większą od 1!")
        nodes_number = int(input("""
Podaj liczbę węzłów interpolacji: """))

    function_arguments = list(np.linspace(left_border, right_border, 1000))

    function_values = []
    for x in function_arguments:
        function_values.append(get_function_value(x, function_number))

    interpolation_arguments = np.linspace(left_border, right_border, nodes_number)
    interpolation_values = list(get_function_value(interpolation_arguments, function_number))
    interpolation_arguments = list(interpolation_arguments)

    polynomial_values = calculations(function_arguments, interpolation_arguments, interpolation_values)

    presentation(function_arguments, function_values, polynomial_values, function_number, interpolation_arguments,
                 interpolation_values)


def calculations(function_arguments, interpolation_arguments, interpolation_values):
    x = sp.Symbol('x')
    forward_interpolation_formula = forward_interpolation(interpolation_arguments, interpolation_values)
    print(forward_interpolation_formula)
    backward_interpolation_formula = backwards_interpolation(interpolation_arguments, interpolation_values)
    print(backward_interpolation_formula)
    forward_interpolation_coefficients = sp.Poly(forward_interpolation_formula, x).all_coeffs()
    print(forward_interpolation_coefficients)
    backward_interpolation_coefficients = sp.Poly(backward_interpolation_formula, x).all_coeffs()
    print(backward_interpolation_coefficients)
    polynomial_values = []
    for argument in function_arguments:
        if argument < (function_arguments[-1] + function_arguments[0]) / 2:
            polynomial_values.append(get_polynomial_value(forward_interpolation_coefficients, argument))
        else:
            polynomial_values.append(get_polynomial_value(backward_interpolation_coefficients, argument))
    return polynomial_values


def presentation(function_arguments, function_values, polynomial_values, function_number, interpolation_arguments,
                 interpolation_values):
    generate_graph(function_arguments, function_values, polynomial_values, function_number, interpolation_arguments,
                   interpolation_values)


##########################################################################
# START
##########################################################################
menu()
