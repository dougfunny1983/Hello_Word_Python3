print('''########################
##Jogo do Par ou Ímpar##
########################''')
print('→←'*30)
from random import randint
resultado = ''
while True:
    comutador = randint(0,10)
    humano = int(input('Digite um numero entre 0 e 10: '))
    soma = comutador + humano
    escolha = str(input('Par ou Impar? ')).upper()[0]
    if soma % 2 == 0:
        if escolha == 'P':
            print(f'A soma deu {soma}')
            print(f'voce escolheu par')
            print(f'O computtador escolheu impar, portanto')
            print('voce venceu!!!')
        else:
            print(f'A soma deu {soma}')
            print(f'voce escolheu impar')
            print(f'O computador escolheu par, portanto')
            print('voce perdeu!!!')
            break

    if soma % 2 == 1:
        if escolha == 'I':
            print(f'A soma deu {soma}')
            print(f'voce escolheu impar')
            print(f'O computador escolheu par, portanto')
            print('voce venceu!!!')
        else:
            print(f'A soma deu {soma}')
            print(f'voce escolheu par')
            print(f'O computador escolheu impar, portanto')
            print('voce perdeu!!!')
            break
print('→←'*30)
