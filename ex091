print('''########################
##Dicionário em Python##
########################''')
print('→←'*50)

from random import randint; from time import sleep
from operator import itemgetter as item
dados = {'jogador 1': randint(1,6), 'jogador 2': randint(1,6), 'jogador 3': randint(1,6), 'jogador 4': randint(1,6)}
for k,v  in dados.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key= item(1), reverse=True)
print('-='*30)
print('== RANKING DOS JOGADORES =='.center(10))
for k, v in enumerate(ranking):
    print(f' {k + 1}º lugar: {v[0]} com {v[1]}.'.center(10))
    sleep(1)
print('→←'*50)