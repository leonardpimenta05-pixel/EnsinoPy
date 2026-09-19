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