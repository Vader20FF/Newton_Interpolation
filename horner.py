def get_polynomial_value(coefficients_list, x):
    """
    Function returning a value of a polynomial
    :param coefficients_list: polynomial coefficients in a list
    :param x: name for the argument
    :return: value of the given polynomial
    """
    result = 0
    # ?reversed
    for coefficient in (coefficients_list):
        result = result * x + coefficient
    return result
