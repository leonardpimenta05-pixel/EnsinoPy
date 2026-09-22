''''
PRATICANDO COM GPT, EVOLUINDO GRADUALMENTE

num = int(input('Digite um Numero: '))


if num < -0:
    print(f'O numero {num} é negativo.')

elif num > 0:
    print(f'O numero {num} é positivo.')

else: 
    print('Voce zerou')    

if num % 2 == 0:
    print(f'O numero {num} é par')
else:
    print(f'O numero {num} é impar.')    

'''


'''
num1 = float(input('Digite sua nota: '))
num2 = float(input('Digite sua outra nota: '))
media = (num1 + num2) / 2

print(f'Sua media foi {media:.2f}')

if media >= 7:
    print('Voce foi aprovado! Parabens!!')

elif media >=5:
    print('Voce esta de recuperaçao.')

else:
    print('Voce foi reprovado, Tente novamente.')
            
'''

login = 'caramelo'
password = '200605'   

acesso = input('Digite o seu login: ')
senha = input('Digite sua senha: ')

if login == acesso and password == senha:
    print('Login Realizado com sucesso, seja bem vindo!!')

elif login == acesso and password != senha:
    print('senha Incorreta, tente novamente.')

else:
    print('Usuario nao encontrado, tente novamente')    

    
    

