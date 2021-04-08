def get_polynomial_value(coefficients_list, x):
    result = 0
    for coefficient in coefficients_list:
        result = result * x + coefficient
    return result
