print('''########################
##Jogo do Par ou Ímpar##
########################''')
print('→←'*30)
numDict = {0:"zero", 1:"um", 2:"dois", 3:"três", 4:"quatro", 5:"cinco",
           6:"seis", 7:"sete", 8:"oito", 9:"nove", 10:"dez",
           11:"onze", 12:"doze", 13:"treze", 14:"quatorze",
           15:"quinze", 16:"dezesseis", 17:"dezessete",
           18:"dezoito", 19:"dezenove", 20:"vinte"}
while True:
    perg = int(input('Digite um numero entre 0 e 20: '))
    if perg > 20:
       print('Tente novamente.')

    else:
        print(f'Você digitou o número {numDict[perg]}')
    
        break
print('→←' * 30)