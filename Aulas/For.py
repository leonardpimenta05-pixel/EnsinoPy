'''
usando for para iteraçao, a variavel novoTexto, serve para
mostrar a variavel texto, com algum outro caracter por dentro dela.

'''
texto = 'Stephany'


novoTexto = ''
for letra in texto:
    novoTexto += f'*{texto}'
    print(letra)
print(novoTexto)        

'''

Usando range para intervalo de numeros
uma forma bem mais pratica de fazer o que o while fazia.

'''
numbers = range (0, 100)

for number in numbers:
    print(number)


"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)