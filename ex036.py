print('''\033[32m########################
##Aprovando Empréstimo##
########################''')
print()
print('→←'*30)
casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual é o seu salário: R$ '))
tempo = int(input('Em quantos anos voce quer pagar: '))
meses = tempo * 12
prestacoes = casa / meses
condicao = ( salario * 30 / 100)
print(f'Valor da casa → R$ {casa:.2f}')
print(f'Seu salário → R$ {salario:.2f}')
print(f'Tempo do financiamento → {meses} Meses')
print(f'Valor das prestaçoes → R$ {prestacoes:.2f}')
if prestacoes >= condicao:
    print(f'As suas prestações equivalem a {prestacoes / salario * 100:.2f}% do seu salário')
    print(f'\033[1;31mSeu empréstimo é mais do que 30% do valor do seu salário.\nPortanto seu empréstimo foi NEGADO!!!')
else:
    print(f'As suas prestaçoes equivalem a {prestacoes / salario * 100:.2f}% do seu salário.')
    print('\033[1;36mPortanto seu empréstimo foi APROVADO!!!')
print()
print('\033[32m→←'*30)
