# Ler 4 valores e guardar numa tupla. Quantas vezes apareceu o 9
# posição do primeiro número 3, quais são os pares
from sympy.polys.benchmarks.bench_solvers import a_31

a1 = int(input('Diga o primeiro valor: '))
a2 = int(input('Diga o segundo valor: '))
a3 = int(input('Diga o terceiro valor: '))
a4 = int(input('Diga o quarto valor: '))
tupla = (a1, a2, a3, a4)

# num = (int(input("primeiro valor: ")), int(input("Segundo valor: ")))
print(f'Você digitou os valores {tupla}')
print(F'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}º posição')
else:
    print(f'O valor 3 não apareceu na lista')
tot = 0
for c in tupla:
    if c % 2 == 0:
       tot += 1
print(F'Foram {tot} valores pares digitados, são eles: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c}', end=' ')
