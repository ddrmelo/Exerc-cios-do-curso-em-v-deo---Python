# Digitar vários números e mostrar sua soma e quantos foram digitados. Encerra com 999

soma = cont = 0

x = 1
while x != 999:
    x = int(input("Digite um número: "))
    if x != 999:
        soma += x
        cont += 1

print(f'Foram digitados {cont} números, com uma soma de {soma}')
