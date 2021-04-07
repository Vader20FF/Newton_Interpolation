from horner import horner
import numpy as np


def wartoscFunkcji(x, numerFunkcji):
    if numerFunkcji == 1:
        return x + 18
    elif numerFunkcji == 2:
        return abs(x)
    elif numerFunkcji == 3:
        return horner([4, 2, -8, 1], x)
    elif numerFunkcji == 4:
        return 8 * np.cos(x) - 2 * np.sin(x)
    elif numerFunkcji == 5:
        return abs(np.cos(x - 1) - 0.8)
    else:
        print("""
Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wartoscFunkcji" """)
        return None

