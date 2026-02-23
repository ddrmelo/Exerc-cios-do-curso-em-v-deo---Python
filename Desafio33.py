# 3 números, qual é o maior e qual o menor

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

maior = a
menor = a

if b > a:
    if b > c:
        maior = b
    else:
        maior = c

if b < a:
    if b < c:
        menor = b
    else:
        menor = c

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
