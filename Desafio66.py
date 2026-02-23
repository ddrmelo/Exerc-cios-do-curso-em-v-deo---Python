# com o break, digitar vários números, e parar com 999. Quantos e sua soma

soma = cont = 0

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}')
