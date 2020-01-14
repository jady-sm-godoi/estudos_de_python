
# o programa dá as boas-vindas e convida a pessoa a jogar
print(80 * '-')
print('Bem-vindo ao jogo "descubra o número"')
print(80 * '-')
play = input('quer jogar comigo? (S/N) ')

# função pensando um número
def thinking():
    '''
    finge que está pensando num número
    e escolhe um número de 0 a 99
    '''

    import random
    from time import sleep

    print('deixe eu escolher um número de 0 a 99')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    sleep(1)
    print('Ok! Escolhi!')
    # o programa escolhe um número 0 a 99
    return random.randrange(0,99)


# criar a função do jogo
def playing():
    '''
    cria um while loop até que o 
    número seja encontrado
    '''
    
    # pensando um número...
    num = thinking()
    n = 1

    # cria um while loop (outra possibilidade está abaixo no código)
    while num:
        # o programa pede um palpite
        guess = int(input('qual é o número que pensei? '))
    
        # se for maior escreve 'o número que eu pensei é menor' e pede outro palpite
        if guess > num:
            print('o número que eu pensei é menor')
            n += 1

        # se for menor escreve 'o número que eu pensei é maior' e pede outro palpite
        elif guess < num:
            print('o número que eu pensei é maior')
            n += 1

        # se for igual escreve 'parabéns! você acertou em X tentativas'
        else:
            print(f'parabéns! você acertou em {n} tentativas')
            break

    
# 2 - em caso de sim segue para 3 / caso não vai para 11
# if play == 'S' or play == 's' or 
while play in ('S', 's', 'Y', 'y'):
    # chama a função do jogo (playing)
    playing()
    # 3.7 - pergunta se quer jogar outra vez
    print(80 * '-')
    play = input('quer jogar de novo? (S/N) ')
    if play not in ('S', 's', 'Y', 'y'):
        print('até mais!')
        break
