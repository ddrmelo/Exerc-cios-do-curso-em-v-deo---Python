# Ler 5 valores e guardar numa lista
# Maior e menor, e suas respectivas posições
lista = list()

for i in range(5):
    k = int(input(f"Digite um valor para a posição {i}: "))
    lista.append(k)

print(f'=-'*30)
print(f'Você digitou os valores {lista}')
maior = menor = lista[0]

for c in lista:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for c in range(5):
    if maior == lista[c]:
        print(f'{c}', end='... ')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for c in range(5):
    if menor == lista[c]:
        print(f'{c}', end='... ')
