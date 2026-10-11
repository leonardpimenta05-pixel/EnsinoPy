frase = 'Hoje meu dia foi corrido, estou cansado mas continuo focado nos meus estudos'
#Criando indice, a quantidade e mais vezes que a letra apareceu

i = 0
quantidade = 0
maisLetra = ''

#Iterando na string com while,
while i < len(frase):
    letra_atual = frase[i]

#Elimiando os espacos da frase, se houver.
    if letra_atual == ' ':
        #O indice deve ser posto aqui tambem, se nao criara um loop infinito, ele sempre barraria no espaco e voltaria, o codigo nunca terminaria.
        i += 1
        continue

#Usando count, que serve para contar quantas vezes tal letra, ou palavra aparece na variavel.
    qtd_atual = frase.count(letra_atual)

#Se a quantidade for menor que a atual, executa o bloco de codigo abaixo.
    if quantidade <= qtd_atual:
        quantidade = qtd_atual
        maisLetra = letra_atual

    i += 1
#Com tudo feito, o a funcao print mostrara o resultado final.
print(
    'A letra que apareceu mais vezes foi '
    f'"{maisLetra}" que apareceu '
    f'{quantidade}x'
)