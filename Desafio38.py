# Ler dois números e mostrar qual é o maior. Se forem iguais, informar que são iguais

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo: "))

if n1 > n2:
    print(f'O primeiro número é maior que o segundo')
elif n1 < n2:
    print(f'O segundo número é maior que o primeiro')
else:
    print(f'Os dois números são iguais')
