print('''########################
##Análise de dados do grupo##
########################''')
print('→←'*30)
print()
homem = 0
mulher = 0
idade18 = 0
veri_mu = ''
veri_ho = ''
plural = ''
while True:
    print('-' * 30)
    print(f'CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo =input('Sexo: ').upper()[0]
    if idade >= 18:
        idade18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    print('-' * 30)
    pergunta = input('Quer continuar? ').upper()[0]
    print('-' * 30)
    if pergunta in 'nN':
        break

if homem > 1:
    veri_ho = 'Homens'
    plural = 's'
else:
    veri_ho = 'Homem'
if mulher > 1:
    veri_mu = 'mulheres'
else:
    veri_mu = ' mulher'

print(f'Total de pessoas com mais de 18 anos → {idade18};')
print(f'Ao todo, temos {homem} {veri_ho} cadastrado{plural};')
print(f'E temos {mulher}{veri_mu} com menos de 20 anos.')
print('→←'*30)

