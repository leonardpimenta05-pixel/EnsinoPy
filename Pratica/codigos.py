
'''
str = 'Leonardo Pimenta'

i = 0 

while i < len(str):
    letra = str[i]

    print(letra)
    i += 1

'''

num = input('Digite um numero para ser contado: ')
numInt = int(num)

contador = numInt

while contador <= 100:
    contador += 1

    if contador == 50:
        print('Nao vou contar este numero.')
        continue


    if contador == 100:
        print('Impossivel contar.')
        break
    print(contador)

print('Acabou.')

