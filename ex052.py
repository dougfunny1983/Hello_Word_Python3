print('''##################
##Números primos##
##################''')
print('←→'*30)
n = int(input('Digite um número: '))
vermelho ='\033[1;31m'
azul = '\033[1;36m'
neutro = '\033[m'
cont = 0
for i in range(1, n+1):
    if n % i == 0:
        print(f'{azul}',end='')
        cont += 1
    else:
        print(f'{vermelho}',end='')
    print(f'{i} ',end='')
print()
if cont == 2:
    print(f'{azul}O número {n} é PRIMO, pois é divisível por 1 e por ele mesmo com resto igual á 0.{neutro}')
else:
    print(f'{vermelho}O numero {n} não é PRIMO.{neutro}')
print('←→'*30)
