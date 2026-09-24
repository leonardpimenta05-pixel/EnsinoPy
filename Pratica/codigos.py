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

'''

'''

saldo = 1000
print(f'Seu saldo é de R${saldo:.2f}')

saque = float(input('Quanto que voce deseja sacar?: '))

if saque <= 0:
    print('Valor do saque invalido.')

elif saque > saldo:
    print('Saldo insuficiente.')

else:
    valorSaque = saldo - saque


    print('Saque realizado com sucesso!')
    print(f'O valor restante é de R${valorSaque}')        

'''

'''
          
num = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num > num2 and num > num3:
    print(f'O primeiro numero é maior {num}')

elif num2 > num and num2 > num3:
    print(f'O segundo numero é maior {num2}')

else:
    print(f'O terceiro numero é maior {num3}')        
        
'''

age = int(input('Digite sua idade: '))

if age < 0:
    print('Digite uma idade valida.')

elif age <= 12: 
    print('Voce é uma crianca.')

elif age <= 17:
    print('Voce é um adolescente.')
elif age <= 59:
    print('Voce ja é um adulto.')

else:
    print('Voce é um idoso.')    
        
    

