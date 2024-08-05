# lista de nomes
nomes = []

#inicio do loop
while True:
    print('1 - inserir novo nome.')
    print('2 - exibir lista de nomes.')
    print('3 - exibir em ordem alfabetica.')
    print('4 - sair do programa.')

#opcao do usuario
    opcao = input('opção do usuario: ')

    #verifica a escolha
    match opcao:
        case '1':
            novo_nome = input('insira um novo nome: ').capitalize()
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso')
            continue
        case '2':
            print('\nLista de Nomes')
            for nome in nomes:
                print(nome)
            continue
        case '3':
            nomes.sort()
            for nome in nomes:
                print(nome)
            print('Lista ordenada com sucesso.')

            continue
        case '4':
            print('Programa encerrado.')
            break
        case _:
            print('Opção invalida.')
