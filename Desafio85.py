# 7 valores numa lista e depois, separar em par e ímpar. Duas listas internas

lista = list()
pares = []
impares = []
for i in range(7):
    n = int(input(f'Digite o {i+1}º valor:'))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()
lista.append(pares[:])
lista.append(impares[:])

print('-='*30)
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')
# Exercício completo