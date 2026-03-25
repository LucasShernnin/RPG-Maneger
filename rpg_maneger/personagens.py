
def player():
    jogador = input('Digite o nome do Jogador: ')
    nome = input('Digite o Nome do seu personagem: ')
    idade = int(input('Digite sua idade: '))
    nex_atual = int(input('Digite o seu NEX: '))

    classe = classes()

    personagem = {
         'player': jogador,
         'nome': nome,
         'idade': idade,
         'nex': nex_atual,
         'classe': classe
    }
    print(f'Personagem Criado!\nNome: {nome}\nIdade: {idade}\nClasse: {classe} \nNEX:{nex_atual} \nBem vindo ao Mundo Jogador: {jogador}')

    return personagem

    
def classes ():
        lista_classes= [ 'Combatente', 'Especialista', 'Ocultista']
        
        for i, classe in enumerate(lista_classes):
            print(i+1, '-', classe)
        
        if classe == 1:
             print('Combatente')
        if classe == 2:
             print('Especialista')
        if classe == 3:
             print('Ocultista')

        escolha =int((input('Escolha sua classe: ')))
        return lista_classes[escolha -1]
