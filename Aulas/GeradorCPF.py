
# Gerando CPF's, calculando digitos e validando o CPF.
import random
'''
Importando a biblioteca random, para conseguir
gerar os cpf de forma aleatoria

'''

for _ in range(100):
# Definindo a quantidade de CPFs a ser gerados.

# Gerando os 9 primeiros
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

# Calculando o primeiro digito a ser verificado.
    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

# Calculando o segundo digito a ser verificado.
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
# Montando e fazendo a exibiçao dos CPFs
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)

