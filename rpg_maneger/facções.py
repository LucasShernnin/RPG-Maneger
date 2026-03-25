import personagens

#def lista_fac():

#    culto_kushin = -10
#    rebeldes = 0
#lista_fac()

def eventos(personagem):
    lista_eventos = ['Culto de Kushin', 'Rebeldes'] 

    for i, missões in enumerate(lista_eventos):
        print(i+1, '-', missões)
    escolha = int(input('Escolha uma Facção: '))

    if escolha == 1:
        print('Missão: Ajudar Ocultista')
        print('Descrição da missão...')
        r = int(input('A missão foi concluida? Digite 1 para Sim e 2 para Não: '))
        
        if r == 1:
            personagem["nex"] += 2
            print('Recompensa: +2 NEX')
            
        else:
            personagem['nex'] += 0
            print('Missão falhou!')

    if escolha == 2:
        print('Missão: Rebelde em apuros')
        print('Descrição da missão...')

        r = int(input('A missão foi concluida? Digite 1 para Sim e 2 para Não: '))
        
        if r == 1:
            personagem['nex'] += 2
            print('Recompensa: +2 NEX')
            
        else:
            personagem['nex'] += 0
            print('Missão falhou!')

    return personagem

            




    


