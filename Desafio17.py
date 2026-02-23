# ler os catetos e calcular a hipotenusa
from math import sqrt
c1 = float(input("primeiro cateto -> "))
c2 = float(input("Segundo cateto -> "))

hip = sqrt(c1 ** 2 + c2 ** 2)

print(f'O triângulo de catetos {c1} e {c2} tem hipotenusa {hip:.2f}')
