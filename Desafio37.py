#Ler um número inteiro e escolher a base de conversão
# 1 binário, 2 octal, 3 hexadecimal

num = int(input("Digite um número qualquer: "))

conv = int(input("""Escolha agora uma base de conversão:
1 - binário
2 - octal
3 - hexadecimal
Sua opção -> """))

if conv == 1:
    print(f'O número {num} na base 2 é {bin(num)[2:]}')
elif conv == 2:
    print(f'O número {num} na base 8 é {oct(num)[2:]}')
else:
    print(f'O número {num} na base 16 é {hex(num)[2:]}')
