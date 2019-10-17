print('''########################
##Boletim com listas compostas##
########################''')
print('→←'*50)
reserva = []
lista = []
res = ''
while res != 'N':
    reserva.append(str(input('Nome: ')).upper())
    reserva.append(float(input('Nota 1: ')))
    reserva.append(float(input('nota 2: ')))
    lista.append(reserva[:])
    reserva.clear()
    res = str(input('Quer continuar? ')).upper().split()[0]
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for z in range(len(lista)):
    print(f'{z:<4}{lista[z][0]:<10}{(lista[z][1] + lista[z][1]) / 2:>6.1f}')
while True:
    print('-'*30)
    nota = int(input('Mostrar notas de qual aluno? (999 para interrromper) '))
    if nota == 999:
        print('-'*30)
        print('Fim do progama...')
        print('Volte sempre!')
        print('-'*30)
        break
    if nota >= len(lista) or nota > 999 or nota < 0:
        print(f'O número {nota} não costa na lista como aluno!')
    else:
        print(f'Notas de {lista[nota][0]} são {lista[nota][1]} e {lista[nota][2]}.')
    print('-'*30)

print('-'*30)
print()
print('→←'*30)
