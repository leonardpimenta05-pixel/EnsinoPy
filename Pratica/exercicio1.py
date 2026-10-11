while True:
    #Entrada de dados, numeros e operadores da calculadora.
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    #None, para saber posteriormente se o que foi digitado sera valido.
    numeros_validos = None

    #Validando os dados com try, execept E convertendo as variaveis para Float.
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    #Caso None, continue sendo None, executara esta barra de codigo.    
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        #continue: retornara o codigo ao inicio, por nao ter validado o que foi digitado
        continue

        
    operadores_permitidos = '+-/*'
    #Se o operador digitado nao tiver na varivael operadores_permitidos, executara a barra de codigo e voltara ao inicio.
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    #Verifica se voce digitou mais de 1 operador, se sim, executara o codigo abaixo e retornara ao inicio    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    #Se tudo for validado de forma correta, executara a funcao print.
    print('Foi realizada a sua operação. Confira o resultado abaixo!')
    #Fazendo as contas, comparando os dados de entrada, e executando print com f'string
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('Nunca deve chegar aqui.')

    #Saida da calculadora, com break e checagem inical de letra e formato.
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break

  

    
        

