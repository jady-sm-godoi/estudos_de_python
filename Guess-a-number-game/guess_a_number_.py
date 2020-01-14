from funcs import playing

# o programa dá as boas-vindas e convida a pessoa a jogar
print('Olá! Bem vindo ao jogo de adivinhe o número!')

# cria o looping do jogo
while True:
    play = input('Quer jogar? (S/N) ')
    if play not in ('S', 's', 'Y', 'y'):
        print('Ok! Até mais!')
        break

    playing()
