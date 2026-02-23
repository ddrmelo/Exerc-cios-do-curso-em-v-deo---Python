# Aluguel de carros 60 reais por dia + 0.15/km
import emoji

print(f'emoji.emojize("Hello World, :earth_americas:", use_aliases=True)')
dias = int(input("Por quantos dias você alugou? "))
km = int(input("E quantos km rodados? "))

tot = dias*60 + 0.15*km

print(f'O total a pagar é de R${tot:.2f}')
