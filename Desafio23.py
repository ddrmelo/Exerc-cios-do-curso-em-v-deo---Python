# Ler um número de 0 a 9999, e mostrar a quantidade de dígitos separados
# 1834 -> unidade: 4, dezena: 3, centena: 8, milhar: 1

num = int(input("Digite um número: "))

unidade = num%10
print(f'Unidade: {unidade}')

num = num//10
dezena = num%10
print(f'Dezena: {dezena}')

num = num//10
centena = num%10
print(f'Centena: {centena}')

num = num//10
milhar = num%10
print(f'Milhar: {milhar}')


teste =  input()
for i in range(len(teste)):
    print(teste[i])