print('''########################
##Mais sobre Matriz em Python##
########################''')
print('→←'*20)
print()
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(3):
    for c in range(3):
        matriz[c][l] = int(input(f'Digite um valor para [{l}, {c}] → '))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*30)
pares = 0
somac = 0
maior = 0
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
for l in range(3):
    somac = matriz[l][2] + somac
    print(matriz[l][2])
for l in range(3):
    maior = max(matriz[1])
print('-='*30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maior}')
print()
print('→←'*20)
