import matplotlib.pyplot as plt
from wzorFunkcji import wzorFunkcji


def generowanieWykresu(lewaGranica, prawaGranica, argumenty, wartosciPoczatkoweFunkcji, wartosciWielomianu, liczbaWezlow, numerFunkcji, x_pkt_inter,
                       y_pkt_inter):
    plt.plot(argumenty, wartosciPoczatkoweFunkcji, label='wykres funkcji f(x)')
    plt.title('f(x)=' + str(wzorFunkcji(numerFunkcji)))
    plt.scatter(x_pkt_inter, y_pkt_inter, label='interpolar nodes')
    plt.plot(argumenty, wartosciWielomianu, linestyle=":", label='interpolar polynomial')
    plt.legend(loc='upper right')  # tworzy legendę wykresu
    plt.xlabel("x")  # opis osi x
    plt.ylabel("y")  # opis osi y
    plt.grid(True)
    plt.show()
