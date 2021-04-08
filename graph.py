import matplotlib.pyplot as plt
from function_formula import get_function_formula


def generate_graph(function_arguments, function_values, polynomial_values, function_number, interpolation_arguments,
                   interpolation_values):
    """
    Function generating a graph with given data
    :param function_arguments: arguments for the whole graph
    :param function_values: values for the function graph
    :param polynomial_values: values for the polynomial graph
    :param function_number: a number of the given function
    :param interpolation_arguments: arguments for interpolations nodes points
    :param interpolation_values: values for interpolations nodes points
    :return: None
    """
    plt.plot(function_arguments, function_values, label='wykres funkcji f(x)')
    plt.title('f(x)=' + str(get_function_formula(function_number)))
    plt.scatter(interpolation_arguments, interpolation_values, label='węzły interpolacji')
    plt.plot(function_arguments, polynomial_values, linestyle=":", label='wielomian interpolacji')
    plt.legend(loc='best')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
