# Pedir o sexo de uma pessoa, mas só aceitar M ou F como resposta. Pedir outra resposta
# em caso de divergência
teste = True
while teste:
    n = input("Qual o sexo? Digite apenas M ou F: ").upper()

    if n not in 'MF':
        print(f'Desculpe, digite apenas M ou F')
    else:
        teste = False
