# Criar uma matriz 3x3 e mostrá-la formatada

# [ 1 ] [ 2 ] [ 3 ]
# [ 4 ] [ 5 ] [ 6 ]
# [ 7 ] [ 8 ] [ 9 ]


matriz = []
temp = []

for linha in range(3):
    for coluna in range(3):
        temp.append(int(input(f"Digite a linha {linha + 1} coluna {coluna + 1}: ")))
    matriz.append(temp[:])
    temp.clear()

# Show! A matriz está montada corretamente. Falta formatar

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^3}] ', end=' ')
    print()

# Formatação perfeita! Exercício concluído
