# Tupla com várias palavras. Mostrar suas vogais

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO'
         , 'PROGRAMADOR', 'FUTURO')

for c in tupla:
    print(f'Na palavra {c} temos as vogais: ', end='')
    for i in range(len(c)):
        if c[i] in 'AEIOU':
            print(f'{c[i].lower()}', end=' ')
    print()