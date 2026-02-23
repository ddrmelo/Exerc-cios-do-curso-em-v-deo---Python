# ler o nome de uma pessoa, e se ela tem silva no nome

nome = input("Qual é o seu nome completo? ").strip().lower()

silva = nome.find("silva")
if 'silva' in nome:
    print("Você possui Silva no nome")
