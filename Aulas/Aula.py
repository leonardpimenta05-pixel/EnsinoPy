# nome = 'Leonardo Pimenta'
# altura = 1.84
# peso = 80
# imc = peso / (altura ** 2 )
# imcf = f'{imc:.2f}'
# texto = f'{nome} tem {altura:.2f} e seu peso é: '
# print(texto)

# print(imcf)

# numero1 = input('Digite um numero: ')
# numero2 = input('Digite um numero: ')

# numeroint = int(numero1)
# numeroint2 = int(numero2)

# print(f'A soma dos numeros é:  {numeroint + numeroint2}')

# if / elif     / else
# se / se nao se / se nao

# entrada = input('Voce quer "entrar" ou "sair"? ')

# if entrada == 'entrar':
#     print('Voce entrou no sistema')

# elif entrada == 'sair':
#     print('Voce saiu do sistema')   

# else:
#     print('Voce nao digitou nenhuma opçao. ')      
# valor1 = input('Digite um valor: ')
# valor2 = input('Digite outro valor: ')
# textoMaior = f'O "{valor1}" é maior que o "{valor2}"'
# textoMenor = f'O "{valor1}" é menor que o "{valor2}"'

# if valor1 >= valor2:
#     print(textoMaior)

# elif valor1 < valor2:
#         print(textoMenor)

senha = input('Senha: ') or 'Sem senha'
print(senha)