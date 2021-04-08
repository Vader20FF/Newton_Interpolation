from factorial import get_factorial as factorial
import sympy as sp


def progressive_differences(tab_y):
    """
    Calculation of progressive differences
    :param tab_y: function values
    :return: a list of calculated progressive differences
    """

    delta_y = [[]]
    delta_y[0] = tab_y
    interpolation_nodes_number = len(tab_y)
    for counter in range(1, interpolation_nodes_number):
        delta_y.append([round(delta_y[counter - 1][i + 1] - delta_y[counter - 1][i], 8)
                        for i in range(interpolation_nodes_number - counter)])
    return delta_y


def forward_interpolation(interpolation_arguments, interpolation_values):
    """
    Interpolation for the first half of selected interval
    :param interpolation_arguments: a list of interpolation arguments
    :param interpolation_values: a list of interpolation values
    :return: Formula of interpolation for the first half of selected interval
    """

    delta_y = progressive_differences(interpolation_values)
    x = sp.Symbol('x')
    q = (x - interpolation_arguments[0]) / (interpolation_arguments[1] - interpolation_arguments[0])
    coefficients = []
    interpolation_nodes_number = len(interpolation_values)
    for n in range(interpolation_nodes_number):
        coefficients.append(round(delta_y[n][0] / factorial(n), 4))
    polynomial = [coefficients[0], q * coefficients[1]]
    copy_coefficients = coefficients.copy()
    coefficient = coefficients[-1]
    n = 1
    while coefficient == 0 and len(coefficients) > 1:
        del coefficients[coefficients.index(coefficient)]
        coefficient = copy_coefficients[-1 - n]
        n += 1
    q_quotient = q
    for n in range(len(coefficients) - 2):
        q_quotient -= 1
        q *= q_quotient
        polynomial.append(q * coefficients[n + 2])
    value = 0
    for item in polynomial:
        value += item
    value = sp.simplify(value)
    return value


def backwards_interpolation(interpolation_arguments, interpolation_values):
    """
     Interpolation for the second half of selected interval
    :param interpolation_arguments: a list of interpolation arguments
    :param interpolation_values: a list of interpolation values
    :return: Formula of interpolation for the second half of selected interval
     """

    x = sp.Symbol('x')
    q = (x - interpolation_arguments[-1]) / (interpolation_arguments[1] - interpolation_arguments[0])
    delta_y = progressive_differences(interpolation_values)
    coefficients = []
    interpolation_nodes_number = len(interpolation_values)
    for i in range(interpolation_nodes_number):
        coefficients.append(round(delta_y[i][-1] / factorial(i), 4))
    polynomial = [coefficients[0], q * coefficients[1]]
    copy_coefficients = coefficients.copy()
    coefficient = coefficients[-1]
    i = 1
    while coefficient == 0 and len(coefficients) > 1:
        del coefficients[coefficients.index(coefficient)]
        coefficient = copy_coefficients[-1 - i]
        i += 1
    q_quotient = q
    for i in range(len(coefficients) - 2):
        q_quotient += 1
        q *= q_quotient
        polynomial.append(q * coefficients[i + 2])
    value = 0
    for item in polynomial:
        value += item
    value = sp.simplify(value)
    return value
