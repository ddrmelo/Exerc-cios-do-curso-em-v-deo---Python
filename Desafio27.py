# Ler um nome, e mostrar o primeiro e o último nome

nome = input("Nome completo: ").strip().split()
inicio = nome[0]
fim = nome[len(nome)-1]

print(f'Seu primeiro nome é {inicio} e o último é {fim}')
