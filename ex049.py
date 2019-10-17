#################
##Tabuada v.2.0##
#################
print('\033[1;35m→←'*30)
cont = soma = 0
while cont <= 10:
    print('-'*30)
    print(f'Multiplicação de {cont}')
    print('-'*30)
    for primeiro in range(0,11):
        print(f'{cont} X {primeiro} = {(primeiro*cont)}'.center(10))
    cont += 1
print('→←'*30)
