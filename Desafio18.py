# seno, cosseno e tangente

from math import sin, cos, tan, radians

ang1 = float(input("Qual o ângulo? "))
ang = radians(ang1)
a1 = sin(ang)
a2 = cos(ang)
a3 = tan(ang)

print(f'O seno de {ang1} é {a1:.2f}, o cosseno vale {a2:.2f}, e a tangente vale {a3:.2f}')
