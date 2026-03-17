
def player():
    jogador = input('Digite o nome do Jogador: ')
    nome = input('Digite o Nome do seu personagem: ')
    idade = int(input('Digite sua idade: '))
    return jogador, nome, idade

    
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
