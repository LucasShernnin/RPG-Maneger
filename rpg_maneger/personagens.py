
#---Player---#
def player():
    jogador = input('Digite o nome do Jogador: ')
    nome = input('Digite o Nome do seu personagem: ')
    idade = int(input('Digite sua idade: '))
    nex_atual = int(input('Digite o seu NEX: '))
    din = 0
    din_Anterior = int(input('Digite quanto trouxe da ultima jornada: '))
    din_atual = din + din_Anterior
    culto_kushin = -10
    rebeldes = 0

    classe = classes()

    personagem = {
         'user': jogador,
         'nome': nome,
         'idade': idade,
         'dinheiro': din_atual,
         'nex': nex_atual,
         'classe': classe,
         'prestigio_culto': culto_kushin,
         'prestigio_rebeldes': rebeldes

    }
    print('='*25)
    print(f'Personagem Criado!\nNome: {nome}\nIdade: {idade}\nClasse: {classe} \nNEX:{nex_atual} \nBem vindo ao Mundo Jogador: {jogador}')

    return personagem

#---Classes---#
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
