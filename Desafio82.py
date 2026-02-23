# Vários números e colocar numa lista. Criar duas listas extras e colocar os pares e sos ímpares
# Mostrar as 3 listas

lista = []
pares = []
impares = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    r = ' '
    while r not in 'SN':
        r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if r == 'N':
        break

print("-"*30)
print(f'A lista digitada foi {lista}')
print(f'A lista de pares foi {pares}')
print(f'A lista de impares foi {impares}')
