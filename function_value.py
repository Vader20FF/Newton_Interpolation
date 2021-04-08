from horner import get_polynomial_value
import numpy as np


def get_function_value(x, function_number):
    """
    Function returning a value of a function given by it's number
    :param x: name for the argument
    :param function_number: a number of the given function
    :return: value of the given function
    """
    if function_number == 1:
        return x + 18
    elif function_number == 2:
        return abs(x)
    elif function_number == 3:
        return get_polynomial_value([4, 2, -8, 1], x)
    elif function_number == 4:
        return 8 * np.cos(x) - 2 * np.sin(x)
    elif function_number == 5:
        return abs(np.cos(x - 1) - 0.8)
    else:
        print("""
Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wartoscFunkcji" """)
        return None

