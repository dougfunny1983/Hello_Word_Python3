print('''########################
##Validando expressões matemáticas##
########################''')
print('→←'*30)
print()
expr = str(input('Digite a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
res = ''
if len(pilha) == 0:
    res = 'Sua expressão é válida!'
else:
    res = 'Sua expressão está errada!'
print('-='*30)
print(res)
print('-='*30)
print()
print('→←'*30)
    