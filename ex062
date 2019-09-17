print('''####################################
##Super Progressão Aritmética v3.0##
####################################''')
print('→←'*30)
prim = int(input('Digite o primeiro termo? '))
ra = int(input('Digite a Razão da PA: '))
termo = prim
cont = 10
for z in range(10):
    print(termo, end=' → ')
    termo += ra
print('PAUSE')
while True:
    pergunta = int(input('Quantos termos voce deseja ver? [0] para parar → '))
    cont += pergunta
    if pergunta > 0:
        for i in range(pergunta):
            print(termo, end=' → ')
            termo += ra
        print('PAUSE')
    else:
        print('Fim')
        print(f'Foram mostrados {cont} termos nesta PA')
        break
print('→←'*30)
