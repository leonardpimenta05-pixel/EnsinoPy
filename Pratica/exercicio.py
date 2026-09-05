input('Qual seu nome: ')
int(input('Quantos anos voce tem?: '))
idade = int(input("Em que ano voce nasceu? "))

if idade == 18:
    print('Voce é de maior!')

elif idade < 18:
    print('Voce é de menor')

else:
    print('Voce nao digitou nada')