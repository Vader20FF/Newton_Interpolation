from horner import get_polynomial_value
import sympy as sp


def get_function_formula(function_number):
    """
    Function returning a formula from a number of built-in function
    :param function_number: a number of the given function
    :return: formula of the given function number
    """
    x = sp.Symbol('x')
    if function_number == 1:
        return x - 3
    elif function_number == 2:
        return abs(x)
    elif function_number == 3:
        return get_polynomial_value([2, 1, -3, 7], x)
    elif function_number == 4:
        return 4 * sp.cos(x) + 6 * sp.sin(x)
    elif function_number == 5:
        return abs(sp.sin(x + 2) - 1.6)
    else:
        print("""
    Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wartoscFunkcji" """)
        return None
