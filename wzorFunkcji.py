from horner import horner
import sympy as sp


def wzorFunkcji(numerFunkcji):
    x = sp.Symbol('x')
    if numerFunkcji == 1:
        return x + 18
    elif numerFunkcji == 2:
        return abs(x)
    elif numerFunkcji == 3:
        return horner([4, 2, -8, 1], x)
    elif numerFunkcji == 4:
        return 8 * sp.cos(x) - 2 * sp.sin(x)
    elif numerFunkcji == 5:
        return abs(sp.cos(x - 1) - 0.8)
    else:
        print("""
    Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wartoscFunkcji" """)
        return None
