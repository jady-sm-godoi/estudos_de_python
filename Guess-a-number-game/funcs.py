# CRIA UMA FUNÇÃO PARA PENSAR:
def thinking():
    import random
    from time import sleep

    print('deixe-me pensar em um número de 0 a 99')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    sleep(1)
    print('Ok! Já escolhi!')
    return random.randrange(0,99)


# CRIA UMA FUNÇÃO PARA O JOGO
    # o programa pede um palpite
    # verifica se o palpite é igual, maior ou menor que o número
    # se for maior escreve 'o número que eu pensei é menor' e pede outro palpite
    # se for menor escreve 'o número que eu pensei é maior' e pede outro palpite
    # se for igual escreve 'parabéns! você acertou em X tentativas'
def playing():
    # o programa escolhe um número 0 a 99  executa:
    num = thinking()
    n = 1

    while num:
        guess = int(input('Qual é o número que pensei? '))
        if guess > num:
            print('O número que pensei é menor')
            n = n + 1
        elif guess < num:
            print('O número que pensei é maior')
            n = n + 1
        else:
            print(f'Parabéns! Você acertou em {n} tentativas')
            break