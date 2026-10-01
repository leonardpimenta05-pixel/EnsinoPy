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
        
'''

'''
compra = int(input('Digite o valor da sua compra: '))

if compra <= 0:
    print('Numero invalido para desconto.')

elif compra >= 500:
    desconto = compra * 0.20
    valorFinal = compra - desconto
    print('Voce recebeu um desconto de 20%')
    print(f'Valor final: {valorFinal:.2f}')

elif compra >= 100:
    desconto = compra * 0.10
    valorFinal = compra - desconto
    print('Voce recebeu um desconto de 10%')
    print(f'Valor final: {valorFinal:.2f}')

else:
    print('Sem desconto.')          

'''

'''
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

if idade >= 12 and altura >= 1.40:
    print('Entrada permitida, Divirta-se!!!')

elif idade < 12 and altura < 1.40:
    print('Idade e altura insuficientes.')

elif idade < 12:
    print('Idade insuficiente')

else:
    print('Altura insuficiente.')
'''

'''
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salario: '))

if idade >= 18 and salario >= 2000:
    print('Emprestimo aprovado.')
    emprestimo = float(input('Digite o valor do emprestimo: '))
    print(f'Emprestimo de R${emprestimo:.2f} aprovado!')

elif idade < 18  and salario < 2000:
    print('Emprestimo negado: Idade e Salario insuficientes.')

elif idade < 18:
    print('Emprestimo negado: Idade insuficiente.')

else:
    print('Emprestimo negado: Salario insuficiente.')            

'''
'''
senhaCorreta = '200605'

while True:
    senha = input('Digite sua senha: ')
    if len(senha) < 2:
        print('Digite mais de 1 numero')
        continue

    elif senha != senhaCorreta:
        print('Senha incorreta. Tente novamente.')
        continue
    else:
        print('Acesso permitido.')
        break
        
'''
'''
senhaCorreta = 200605
tentativas = 3

while tentativas > 0:
    senha = int(input('Digite sua senha: '))
    if senha == senhaCorreta:
        print('Acesso permitido.')
        break

    else:
        tentativas -= 1

        if tentativas != 0:
            print(f'Tentativas restantes: {tentativas}')
            

        else:
            print('Acesso bloqueado.')
            break
            
'''

'''
total = 0

while True:
    numero = int(input('Digite um numero: '))
    if numero == 0:
        print('Programa encerrado.')
        print(f'Soma total: {total}')
        break

    total += numero
'''

compras = []

produto1 = input('Digite o primeiro produto: ')
compras.append(produto1)

produto2 = input('Digite o segundo produto: ')
compras.append(produto2)

produto3 = input('Digite o terceiro produto: ')
compras.append(produto3)
        
print(f'Quantidade de produtos: {len(compras)}')
print(f'O primeiro produto: {compras[0]} ')
print(f'Ultimo produto: {compras[-1]}')


    
    