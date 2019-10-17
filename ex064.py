print('''################################
##Tratando vários valores v1.0##
################################''')
print('→←'*30)
soma = cont = 0
res = 0
while True:
    n = int(input('Digite um numero [flag 999]: '))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print(f'Voce digitou {cont} numeros')
print(f'A soma deles é {soma}')
print('→←'*30)
