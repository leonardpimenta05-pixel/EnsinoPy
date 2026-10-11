import os
compras = []

while True:
    os.system('cls')
    print('Selecione uma opçao:\n ' '\n[i] inserir\n[a] apagar\n[l] listar\n[s] sair ')
    opcao = input('Digite uma opçao: ') 

    if opcao == 'i':
        adicionar = input('Qual item deseja inserir?: ')
        compras.append(adicionar)
        print('Item adicionado com sucesso!!')
        input('\nPressione Enter para continuar...')
        

    elif opcao == 'l':
        for indice, item in enumerate(compras):
            print(f'{indice} - {item}')
        input('\nPressione Enter para continuar...')

    elif opcao == 'a':
        try:
            apagar = int(input('Qual indice voce deseja apagar: '))
            del compras[apagar]
            print('Item apagado com sucesso!!')

        except IndexError:
            print('Indice inexistente.')
        except ValueError:
            print('Erro, Digite um numero')   
        input('\nPressione Enter para continuar...')

    elif opcao == 's':
        print('Voce saiu do programa, Obrigado.')
        break

    else:
        print('Opçao invalida, tente novamente')
        input('\nPressione Enter para continuar...')
        
        

            