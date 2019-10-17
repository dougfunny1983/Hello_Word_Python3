print('''################
##Ano Bissexto##
################''')
from datetime import date
print('→←'*30)
ano = int(input('Digite o ano. Se for o atual, digite 0: '))
if ano == 0:
    ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano atual ({ano}) é bissesto')
    else:
        print(f'O ano atual ({ano}) não é bissesto')
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'\033[1;32mO ano de {ano} é bissesto!!!')

    else:
        print(f'\033[1;31mO ano de {ano} não é bissesto')
print('\033[m→←'*30)
