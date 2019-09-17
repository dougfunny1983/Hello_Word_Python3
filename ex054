print('''#######################
##Grupo da Maioridade##
#######################''')
print('→←'*30)
from datetime import date
branco = '\033[m'
azul = '\033[1;36m'
vermelho = '\033[1;31m'
idade = list()
cont = cont1 = 0
for p in range(1, 8):
    nascimento = int(input(f'Digite o ANO DE NASCIMENTO da {p}º pessoa → '))
    idade.append(date.today().year - nascimento)
print(idade)
for i in idade:
    if i < 18:
        cont += 1
    else:
        cont1 += 1
print(f'{azul}Existem {cont1} pessoas com maior idade.{branco}')
print(f'{vermelho}Existem {cont} pessoas com menor idade.{branco}')
print('→←'*30)
