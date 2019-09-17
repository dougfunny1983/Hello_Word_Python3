print('''########################
##Jogo do Par ou Ímpar##
########################''')
print('→←'*30)
print('='*30)
print('BANCO CEV'.center(30,'-'))
print('='*30)
valor = float(input('Que valor você quer sacar? R$ '))
nota100 = valor//100
valor %= 100
nota50 = valor//50
valor %= 50
nota20 = valor//20
valor %= 20
nota10 = valor//10
valor %= 10
nota5 = valor//5
valor %= 5
nota2 = valor//2
valor %= 2
nota1 = valor // 1
valor %= 1
lista1 = [nota100, nota50, nota20, nota10, nota5, nota2, nota1]
lista2 = ('R$ 100,00', 'R$ 50,00', 'R$ 20,00', 'R$ 10,00', 'R$ 5,00', 'R$ 2,00', 'R$ 1,00' )
plural = ''
for z in range(7):
    if lista1[z] > 1:
        plural = 's'
    if lista1[z] != 0:
        print(f'Total de {lista1[z]:.0f} cédula{plural} de {lista2[z]}')
