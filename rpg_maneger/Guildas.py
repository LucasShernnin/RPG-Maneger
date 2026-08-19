def eventos(lista_jogadores):

    lista_eventos = ['Culto de Kushin', 'Rebeldes'] 

    for i, missões in enumerate(lista_eventos):
        print(i+1, '-', missões)
    escolha = int(input('Escolha uma Facção: '))

    #---Missão Culto---#
    if escolha == 1:
        print('Missão: Ajudar Ocultista')
        print('Descrição da missão...')
        r = int(input('A missão foi concluida? Digite 1 para Sim e 2 para Não: '))
        
        if r == 1:
            for personagem in lista_jogadores:
                personagem["nex"] += 2

                personagem['prestigio_culto'] += +5
                personagem['prestigio_rebeldes'] += -5

            print('Recompensa: +2 NEX')
            print('Prestigio com o Culto: +5')
            print('Prestigio com os Rebeldes: -5')
        
            
        else:
            print('Missão falhou!')

    #---Missão Rebeldes---#
    if escolha == 2:
        print('Missão: Rebelde em apuros')
        print('Descrição da missão...')

        r = int(input('A missão foi concluida? Digite 1 para Sim e 2 para Não: '))
        
        if r == 1:
            for personagem in lista_jogadores:
                personagem['nex'] += 2

                personagem['prestigio_culto'] += -5
                personagem['prestigio_rebeldes'] += +5
            
            print('Recompensa: +2 NEX')
            print('Prestigio com o Culto: -5')
            print('Prestigio com os Rebeldes: +5')
            
        else:
            print('Missão falhou!')

    return lista_jogadores



    


