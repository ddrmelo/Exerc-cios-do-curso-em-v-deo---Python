# Ler vários valores e perguntar qual foi o maior e o menor, além da média deles. Perguntar
# ao final se quer continuar a digitar os valores

r = 's'
maior = menor = media = cont = 0

while r != 'N':
    n = float(input("Digite um valor qualquer: "))
    if cont == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    cont += 1
    media += n
    r = input("Quer continuar? [S/N] ").upper()

print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
print(f'Foram digitados um total de {cont} números, e sua média foi {media / cont:.2f}')
