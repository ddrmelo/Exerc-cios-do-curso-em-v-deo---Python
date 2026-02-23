# ler o ano e dizer se vai se alistar. Usar o date.today().year pra verificar
# dizer quanto tempo falta, ou quanto tempo passou do prazo

from datetime import date
ano = int(input('Qual o ano de nascimento? '))

atual = date.today().year
idade = atual - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {atual + 18 - idade}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {atual + 18 - idade}.')
else:
    print(f'Ano de alistamento. Vá a junta de alistamento do seu estado.')