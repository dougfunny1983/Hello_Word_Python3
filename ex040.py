print('''############################
##Aquele clássico da Média##
############################''')
azul = '\033[1;36m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
branco = '\033[m'
print('→←'*30)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print(f'Sua notas formam {nota1} e {nota2}...')
media = (nota2 + nota1) / 2
print(f'Sua média foi {media:.1f} neste período, portanto...')
print('-='*30)
if media < 5.0:
    print(f'{vermelho}Você está REPROVADO!!! Estude mais...{branco}')
elif media > 7.0:
    print(f'{azul}Você foi APROVADO!!!{branco}')
else:
    print(f'{verde}Você está de RECUPERAÇÃO!!! Ainda dá tempo...{branco}')
print('→←'*30)
