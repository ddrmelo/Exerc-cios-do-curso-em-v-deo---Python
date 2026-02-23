# Ler 2 valores, criar um menu de calculadora: somar, multiplicar, qual o maior, adicionar
# novos números, ou sair

n = 0
print('-=-'*18)
print('BEM VINDO AO MEU SOFTWARE CALCULÍSTICO BOMBÁSTICO')
print('-=-'*18)
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

while n != 5:

    n = int(input("""Escolha uma das opções abaixo
    [ 1 ] - Somar os dois valores
    [ 2 ] - Multiplicar os dois valores
    [ 3 ] - Saber qual o maior valor
    [ 4 ] - informar novos valores
    [ 5 ] - Sair do programa
    -> """))

    if n == 1:
        print(f'A soma de {v1} + {v2} vale {v1+v2}')
    elif n == 2:
        print(f'A multiplicação entre {v1} e {v2} vale {v1*v2}')
    elif n == 3:
        if v1 > v2:
            print(f'{v1} é maior que {v2}')
        elif v2 > v1:
            print(f'{v2} é maior que {v1}')
        else:
            print(f'Ambos os números são iguais')
    elif n == 4:
        print('OK! Novos valores!')
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))
    else:
        print(f'Tchau tchau')
print('-=-'*10, 'Fim do programa', '-=-'*10)
