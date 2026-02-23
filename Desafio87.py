# Matriz 3 x 3 e mostrar: a) a soma de todos os pares; b)a soma dos valores da terceira
# coluna, c) O maior valor da segunda linha

matriz = []
temp = []
pares = totcol3 = maior2c = 0
# Formação da matriz 3x3
for linha in range(3):
    for coluna in range(3):
        temp.append(int(input(f"Digite o valor da linha {linha+1} e coluna {coluna+1}: ")))
    matriz.append(temp[:])
    temp.clear()

print('-=-'*20)
# Formatação da matriz e:
maior2c = matriz[1][1]
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}] ', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna] # Soma dos valores pares
        if coluna == 2:
            totcol3 += matriz[linha][coluna] # Soma dos valores da 3º coluna
        if linha == 1:
            if matriz[linha][coluna] > maior2c:
                maior2c = matriz[linha][coluna] # Verificação do maior valor da 2 linha
    print()

print('-=-'*20)

print(f'A soma dos pares digitados vale {pares}')
print(f'A soma dos valores da 3º coluna vale {totcol3}')
print(f'O maior valor da segunda linha vale {maior2c}')
# Exercício concluído com sucesso