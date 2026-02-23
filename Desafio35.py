# 3 números, e diga se formam um triângulo

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os números {a}, {b} e {c} formam um triângulo')
else:
    print('Os números digitados não formam um triângulo')
