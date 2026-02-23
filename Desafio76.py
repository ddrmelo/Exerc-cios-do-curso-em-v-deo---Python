# tupla única com nomes de produtos e seus respectivos preços. Mostrar a listagem
# em ordem tabular

# Lápis................ R$ 1.75
# Borracha............. R$ 2.00

tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)


print(f'-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

for contador in range(0, len(tupla), 2):
    print(f'{tupla[contador]:.<30} R${tupla[contador+1]:>8.2f}')

