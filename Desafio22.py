# Ler o nome completo de uma pessoa e mostre:
# nome com letras maiúsculas; minúsculas; Quantas letras ao total, sem espaços, Quantas letras tem o primeiro nome

nome = input("Qual o seu nome completo? ").strip()
print(f'Maiúscula: {nome.upper()}')
print(f'Minúscula: {nome.lower()}')
print(f'Total de letras com espaços: {len(nome)}')
nome = nome.split()
dividido = nome[0]
nome = ''.join(nome)
print(f'Total de letras sem espaços: {len(nome)}')
print(f'O seu primeiro nome, {dividido}, possui {len(dividido)} letras.')
