print('''################################
##GAME→ Pedra Papel e Tesoura###
################################''')
from random import randint
from time import sleep
empate = vitoria = derrota= 0
print('→←'*30)
print(f'Começando o jogo!!!')
sleep(2)
print('PREPARADO? ENTÃO VAMOS LÁ!!!')
sleep(2)
a = '\033[1;31m'
b = '\033[1;32m'
c = '\033[1;35m'
n = '\033[;m'
nipes = {1:f'{a}PEDRA{n}',2:f'{b}PAPEL{n}',3:f'{c}TESOURA{n}'}
while True:
    jogador = int(input(f'Escolha entre:\n'
                        f'{a}PEDRA →   [1]\n'
                        f'{b}PAPEL →   [2]\n'
                        f'{c}TESOURA → [3]{n}\n'
                        f'Faça sua escolha → '))
    computador = randint(1,3)
    sleep(2)
    print(f'Jogador: {nipes[jogador]}')
    print(f'computador: {nipes[computador]}')
    if jogador == computador:
        empate += 1
        print(f'{c}Deu Empate!!! Que peninha...{n}')
        sleep(1)
    else:
        if jogador == 1 and computador == 2 or jogador == 2 and computador == 3 or jogador == 3 and computador == 1:
            derrota += 1
            print(f'{a}Você perdeu!!!{n}')
        elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
            vitoria += 1
            print(f'{b}Você Ganhou!!!{n}')
    sleep(2)
    res = str(input('Deseja continuar? [SIM/NÃO] → ')).upper().strip()[0]
    sleep(2)
    if res in 'S':
        print('Escolha novamente...')
    else:
        sleep(2)
        print('Fim do jogo.\n'
              'Obrigado por jogar!!!')
        break
print(f'Score (Pontuação)\n'
      f'{c}{vitoria} Vitórias\n'
      f'{a}{derrota} Derrotas\n'
      f'{b}{empate}  Empate\n')
print(f'{n}→←'*30)
