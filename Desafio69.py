# ler idade e sexo de várias pessoas. Perguntar se quer continuar
# quantas > 18, quantos homens, quantas mlheres < 20
maior18 = qtdh = mulhermenor20 = 0

while True:
    print(f'-'*25)
    print(f'{"CADASTRE UMA PESSOA":>20}')
    print(f'-' * 25)
    age = int(input('Idade: '))
    if age > 18:
        maior18 += 1
    sexo = input("Sexo [M/F]: ").upper()
    while sexo not in 'MF':
        sexo = (input('Sexo [M/F]: ')).upper()
    if sexo == 'F' and age < 20:
        mulhermenor20 += 1
    if sexo == 'M':
        qtdh += 1

    r = ' '
    while r not in 'SN':
        r = input("Quer continuar? [S/N]").upper()
    if r == 'N':
         break

print('='*8, ' FIM DO PROGRAMA ', '='*8)
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {qtdh} homens cadastrados')
print(f'E temos {mulhermenor20} mulheres com menos de 20 anos.')
