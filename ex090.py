print('''########################
##Dicionário em Python##
########################''')
print('→←'*50)
aluno = dict()
aluno['nome'] = str(input('Nome: ')).upper()
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))
resul = ''
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO!!!'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'de RECUPERAÇÃO!!!'
else:
    aluno['situação'] = 'REPROVADO!!! ESTUDE MAIS!!!'
print(f"O aluno {aluno['nome']} tem média {aluno['média']}, portanto está {aluno['situação']}")
print()
print('→←'*30)
