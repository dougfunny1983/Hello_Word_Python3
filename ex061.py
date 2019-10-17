print('''###############################
## Progressão Aritmética v2.0##
###############################''')
print('→←'*30)
cont = 0
termos = 0
primeiro = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão da PA: '))
print(primeiro,end=' → ')
while True:
    termos += ra
    print(f'{termos+primeiro}', end=' → ')
    cont += 1
    if cont == 9:
        print('fim')
        break
print('→←')
