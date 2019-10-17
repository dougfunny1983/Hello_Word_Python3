print('''\033[36m#############################
###Dissecando uma Variável###
#############################''')
print('-='*30)
a = input('Digite algo... ')
print(f'Que tipo primitivo foi digitado? {type(a)} ')
print(f'Só tem espaços? {a.isspace()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está captalizada? {a.istitle()}')
print('-='*30)
