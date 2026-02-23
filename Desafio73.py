# Tabela do brasileiro. Mostrar: a) os 5 primeiros b) os 4 rebaixados
# c) ordem alfabética d) posição de um determinado time

tabela = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo',
          'Bahia', 'São Paulo','Grêmio', 'Bragantino', 'Atlético-MG', 'Santos',
          'Corinthians', 'Vasco', 'Vitória','Internacional',
          'Ceará', 'Fortaleza', 'Juventude', 'Sport')

print(f'-=-'*30)
print(f'Lista de times do Brasileirão 2026: {tabela}')
print(f'-=-'*30)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print(f'-=-'*30)
print(f'Os 4 últimos foram: {tabela[-4:]}')
print(f'-=-'*30)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print(f'-=-'*30)
time = input("Qual o time que deseja saber a colocação? ").capitalize()
print(f'O {time} terminou o campeonato na {tabela.index(time) + 1}º colocação')
print(f'-=-'*30)
