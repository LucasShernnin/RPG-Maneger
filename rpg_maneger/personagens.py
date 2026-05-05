
#---Player---#
lista_jogadores = []
def player():
    jogador = input('Digite o nome do Jogador: ')
    nome = input('Digite o Nome do seu personagem: ')
    idade = int(input('Digite sua idade: '))
    nex_atual = int(input('Digite o seu NEX: '))
    din_Anterior = int(input('Digite quanto trouxe da ultima jornada: '))
    din = 0
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
         'prestigio_rebeldes': rebeldes,
         'inventario': []

    }
    print('='*25)
    print(f'Personagem Criado!\nNome: {nome}\nIdade: {idade}\nClasse: {classe} \nNEX:{nex_atual} \nBem vindo ao Mundo Jogador: {jogador}')

    lista_jogadores.append(personagem)
    
    return personagem, lista_jogadores

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

def ver_personagem(lista_jogadores):
     for i, usuario in enumerate(lista_jogadores):
                        print(f"{i+1} - Personagem:")
                        print(f"Player: {usuario['user']}")
                        print(f"Nome do Personagem: {usuario['nome']}")
                        print(f"Classe: {usuario['classe']}")
                        print(f"NEX: {usuario['nex']}")
                        print(f"Dinheiro: {usuario['dinheiro']}")
                        print(' ')
                        print(f"Prestigio com o Culto: {usuario['prestigio_culto']}")
                        print(f"Prestigio com os Rebeldes: {usuario['prestigio_rebeldes']}")
                        print('----//----')

                        print("Seus itens:")
                        for itens in usuario['inventario']:
                              print(f"Item: {itens['item']}")
                              print(f"Elemento: {itens['elemento']}")
                              print(f"Efeito: {itens['efeito']}")
                              print('<-->')

                              return usuario
