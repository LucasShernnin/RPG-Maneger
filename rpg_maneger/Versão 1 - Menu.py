import personagens

print("{}Bem Vindo ao AQTV{}".format(('-'*5), ('-'*5)))

lista_jogadores = []
nex_atual = None

def menu():
    while True:
          print("MENU")
          lista_menu  = ['Criar Personagem', 'Ver Jogadores', 'Registrar Evento', 'Dashboard', 'Sair']

          #---Menu---
          for i, itens in enumerate(lista_menu):
                print(i+1, '-', itens)
          escolha = int(input("Escolha uma opção: "))

          #---Escolha 1---
          if escolha == 1:
                print("===== PERSONAGEM =====")
                personagem = personagens.player()
                lista_jogadores.append(personagem)
                print('='*25)

          #---Escolha 2---
          if escolha == 2:
                 for i, usuario in enumerate(lista_jogadores):
                        print(f"{i+1} - Personagem:")
                        print('--'*5)
                        print(f"Player: {usuario['player']}")
                        print(f"Nome do Personagem: {usuario['nome']}")
                        print(f"Classe: {usuario['classe']}")
                        print(f"NEX: {usuario['nex']}")
                        print('----//----')
          #---Escolha 3---

          if escolha == 3:
            import facções
            
            if personagem['nex'] is None:
                 print("Crie um personagem primeiro!")
            elif personagem['nex'] != None:
                 personagem = facções.eventos(personagem)

menu()




