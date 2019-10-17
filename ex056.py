print('''#######################
##Analisador completo##
#######################''')
print('→←'*30)
censo = [[],[],[],[]]
soma = maior = idade = cont = 0
nomes = list()
for n in range(0, 4):
    print(f'-========={n+1}ª pessoa==========-')
    censo[n].append(str(input('Nome → ')).upper())
    censo[n].append(int(input('Idade → ')))
    censo[n].append(str(input('Sexo → ')).upper()[0])
for z in censo:
    soma += z[1]
    media = soma / 4
    if z[2] == 'M':
        if z[1] > idade:
            maior = z[0]
            idade = z[1]
    else:
        if z[1] < 20:
            cont += 1
            nomes.append(z[0])
print('-'*40)
print(f'A média de idade deste grupo é {media:.1f} anos.')
print()
print(f'O homem mais velho é o {maior} e tem {idade} anos.')
print()
print(f'Existem {cont} mulheres com menos de 20 anos, e são elas:')
for l in nomes:
    print(f'* {l} *')
print('→←'*30)
