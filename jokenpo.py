#Jokenpo
import random


try:
    escolha = int(input('1 = pedra | 2 = papel | 3 = tesoura\nescolha: '))
    
    print('-'*30)
    
    pedra = 1
    papel = 2
    tesoura = 3
    
    sorteio = random.randint(1, 3)
    
    if sorteio == escolha:              #se o programa sortear o mesmo numeoro que o usuario, empate
        print(f'O programa escolheu: {escolha}')
        print('Empate!')
    
    elif sorteio == 1 and escolha == 2: #se o programa sortear pedra (1) e o usuario escolher papel (2) o usuario ganha
        print('O programa escolheu: pedra')
        print('Você ganhou!')
        
    elif sorteio == 1 and escolha == 3: #se o programa sortear pedra (1) e o usuario escolher tesoura (3) o programa ganha
        print('O programa escolheu: pedra')
        print('Você perdeu!')
        
    elif sorteio == 2 and escolha == 1: #se o programa sortear papel (2) e o usuario escolher pedra (1) o programa ganha
        print('O programa escolheu: papel')
        print('Você perdeu!')
        
    elif sorteio == 2 and escolha == 3:
        print('O programa escolheu: papel')
        print('Você ganhou!')
        
    elif sorteio == 3 and escolha == 1:
        print('O programa escolheu: tesoura')
        print('Você ganhou!')
        
    elif sorteio == 3 and escolha == 2:
        print('O programa escolheu: tesoura')
        print('Você perdeu')
        
    else:
        print('Digite apenas numeros entre 1 e 3!')

except:
    print('Digite apenas numeros entre 1 e 3!')




    