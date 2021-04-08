import matplotlib.pyplot as plt
from function_formula import get_function_formula


def generate_graph(function_arguments, function_values, polynomial_values, function_number, interpolation_arguments,
                   interpolation_values):
    plt.plot(function_arguments, function_values, label='wykres funkcji f(x)')
    plt.title('f(x)=' + str(get_function_formula(function_number)))
    plt.scatter(interpolation_arguments, interpolation_values, label='węzły interpolacji')
    plt.plot(function_arguments, polynomial_values, linestyle=":", label='wielomian interpolacji')
    plt.legend(loc='best')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
