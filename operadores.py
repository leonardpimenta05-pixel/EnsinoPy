# adicao = 10 + 10
# print('Adicao: ', adicao)

# subtracao = 10 - 5
# print('Subtracao: ', subtracao)

# multiplicacao = 10*10
# print('Multiplicacao: ', multiplicacao)

# divisao = 10 / 3
# print('Divisao:', divisao)
# #sempre retornara numero inteiro, independente
# divisao_inteira = 10 // 2.2
# print('Divisao inteira: ', divisao_inteira)

# exponenciacao = 2 ** 10
# print('Exponenciacao: ', exponenciacao)



'''
Resto da divisao, é o que vem depois
pode ser usado para descobrir se o numero é divisivel pelo outro
com a funçao bool, se o resultado for 0 ou true, 
ele é divisivel.
'''



# modulo = 10 % 5 
# print('Modulo: ', modulo)
# print(18 % 8 == 0)
# print(12 % 6 == 0)

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
# isto seria a ordem que uma conta devera ser feita.


"""
Operadores de comparaçao (relacionais)
>      Maior       2 > 1
>=     Maior ou igual      2 >= 2
<      Menor        1 < 2
<=     Menor ou igual 2 <= 2
==     Igual        'a' == 'a'
!=     Diferente        'a' != 'b'

"""


# Operadores lógicos
# and (e) or (ou) (not) nao
# and =  todas condicoes precisam ser verdadeiras

"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '251098'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')  

"""

# Operador lógico 'Or'

"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '251098'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair') 

senha = input('Senha: ') or 'Sem senha'
print(senha)
"""          

# Operador lógico 'Not'

"""

senha = input('Senha: ')
if not senha:
    print('Voce nao digitou nada')

"""

nome = input('Digite seu nome: ')
encontrar = input('Digita o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')    