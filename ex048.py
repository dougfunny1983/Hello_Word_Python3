print('''##################################
##Soma ímpares múltiplos de três##
##################################''')
print('→←'*30)
cont = soma = 0
for n in range(3,501,3):
    if n % 2 != 0:
        soma += n
        cont += 1
print(f'Existem {cont} multiplos de 3 entre 0 e 500. A soma de todos os termos resulta em {soma} ')
print('→←'*30)
