import personagens

print("{}Bem Vindo ao AQTV{}".format(('-'*5), ('-'*5)))

lista_jogadores = []
nex_atual = None

def menu():
    while True:
          print("MENU")
          lista_menu  = ['Criar Personagem', 'Ver Jogadores', 'Registrar Evento', 'Dashboard', 'Sair']

         #---Escolha 1---
          for i, itens in enumerate(lista_menu):
                print(i+1, '-', itens)
          escolha = int(input("Escolha uma opção: "))
          if escolha == 1:
                print("===== PERSONAGEM =====")
                jogador, nome, idade, nex_atual = personagens.player()
                classe = personagens.classes()
                lista_jogadores.append([jogador, nome, idade, classe, nex_atual])
                print('='*25)
                print(f'Personagem Criado!\nNome: {nome}\nIdade: {idade}\nClasse: {classe} \nNEX:{nex_atual} \nBem vindo ao Mundo Jogador: {jogador}')

          #---Escolha 2---
          if escolha == 2:
            for i, usuario in enumerate(lista_jogadores):
                      print(i+1, '- Personagem')
                      print(f'Player: {usuario[0]} \nNome do Personagem: {usuario[1]} \nClasse: {usuario[3]} \nNEX:{nex_atual}')
                      print('---//---')
          #---Escolha 3---
          if escolha == 3:
            import facções
            
            if nex_atual is None:
                 print("Crie um personagem primeiro!")
            if nex_atual != None:
                 nex_atual = facções.eventos(nex_atual)
menu()




