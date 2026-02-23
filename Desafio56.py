# Nome, idade e sexo de 4 pessoas. Mostrar no final:
# média da idade, nome do homem mais velho, e quantas mulheres tem menos de 20 anos

media = totm = maiorIdade = 0
maior = ''
for i in range(4):
    print('-'*5, f'{i+1}º PESSOA', '-'*5)
    nome = input(f"Digite o nome da {i+1}º pessoa: ")
    idade = int(input(f"A idade da {i+1}º pessoa: "))
    sexo = input("Masculino ou Feminino? ")[0].upper().strip()
    print('-' * 21)
    media += idade
    if sexo == 'M':
        if i == 0:
            maior = nome
            maiorIdade = idade
        else:
            if idade > maiorIdade:
                maior = nome
                maiorIdade = idade

    if sexo == 'F' and idade < 20:
        totm += 1

print(f'A média de idade do grupo é de {media/4:.2f} anos')
print(f'O homem mais velho se chama {maior} e tem {maiorIdade} anos')
print(f'{totm} mulheres tem menos de 20 anos')
