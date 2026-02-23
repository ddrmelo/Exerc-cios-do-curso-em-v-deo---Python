# Ler uma frase e dizer se é um palíndromo, desconsiderando os espaços e acentos

frase = input("Digite uma frase: ").strip().upper().split()
frase = ''.join(frase)

inverso = frase[::-1]

print(f"Você digitou {frase}, e seu inverso é {inverso}")
if frase == inverso:
    print(f'Formam um palíndromo')
else:
    print('Não formam um palíndromo')