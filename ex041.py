print('''#########################
##Classificando Atletas##
#########################''')
from datetime import date
print('→←'*30)
ano = int(input('Digite o ano de seu nascimento: '))
print('-='*30)
print('''- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER''')
print('-='*30)
idade = date.today().year - ano
if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JÚNIOR'
elif idade > 19 and idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'Sua idade atual é de {idade} anos.')
print(f'Portanto sua categoria é {categoria}.')
print('→←'*30)

