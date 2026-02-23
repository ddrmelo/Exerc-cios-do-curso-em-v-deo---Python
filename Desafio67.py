# Tabuada de vários números. Parar quando um valor for negativo

while True:
    n = int(input(f'Quer ver a tabudada de que valor? '))
    if n < 0:
        break

    print('-'*30)
    for i in range(11):
        print(f'{n} x {i:} = {n*i}')
    print('-'*30)
print(f'Programa TABUADA ENCERRADO. Volte sempre!')
