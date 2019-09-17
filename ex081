print('''########################
##Extraindo dados de uma Lista##
########################''')
print('→←'*20)
print()
lista = []
pergunta = ''
while pergunta in 'S':
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer continuar? ')).upper().split()[0]
lista.sort(reverse=True)
print('-'*30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescentes são: {lista}')
print(f'O valor 5 {"não foi" if lista.count(5) == 0 else "foi" } encontrado na lista!')
print('→←'*20)
print()