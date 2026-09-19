print('=' * 30)
print(' ' * 9, 'CADASTRO!!')
print('=' * 30)

while True:
    
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')

    if len(nome) < 3:
        print('Seu nome e muito pequeno, por favor digite mais.')
        continue

    elif len(senha) <= 1:
        print('IMPOSSIVEL!\nsenha muito curta.')
        continue



    