secreta = 'Stephany'
letras_acertadas = ''
tentativa = 0

while True:

    letra = input('Digite uma letra: ')

    if len(letra) >1:
        print('Digite apenas uma letra.')
        continue

    tentativa += 1

    if letra in secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra_secreta in secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra: ', palavra_formada)

    if palavra_formada == secreta:
        print('=' * 30)
        print('PARABENS VOCE ACERTOU')
        print(f'A palavra secreta era {secreta}')
        print(f'As tentavias foram: {tentativa}')
        break    

