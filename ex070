print('''########################
##Estatísticas em produtos##
########################''')
'''fiz com uma estrutura de dicionario, 
para forçar minha mente criar outra forma
de resolver a questão'''
print('→←'*30)
print()
print('-'*30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'*30)
perg = ''
lista1 = []
lista2 = list()
dados = dict()
while perg != 'N':
    nome = str(input('Nome do produto: '))
    dado = int(input('Preço: R$ '))
    lista1.append(nome)
    lista2.append(dado)

    perg = str(input('Quer continuar? ')).upper().split()[0]

print('FIM DO PROGRAMA'.center(30,'-'))

for con in range(len(lista1)):
    dados[lista1[con]] = lista2[con]

contMaior = contmenor = 0
men = sorted(dados.values())[0]
chave = ''

for k, v in dados.items():
    if v >= 1000:
        contMaior += 1
    if v == men:
        chave = k

print(f'O total da compra foi R$ {sum(dados.values()):.2f}')
print(f'Temos {contMaior} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi a {chave} e custa R$ {men:.2f}')



