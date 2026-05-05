print("{}Bem Vindo ao AQTV{}".format(('-'*5), ('-'*5)))


def menu():
    while True:
          print('='*5)
          print("MENU")
          print('='*5)
          lista_menu  = ['Criar Personagem', 'Ver Jogadores', 'Registrar Evento', 'Loja', 'Dashboard', 'Sair']

          #---Menu---#
          for i, itens in enumerate(lista_menu):
                print(i+1, '-', itens)
          escolha = int(input("Escolha uma opção: "))

          #---Criação de Personagem---#
          if escolha == 1:
                print("===== CRIAÇÃO DE PERSONAGEM =====")
                from personagens import player
                player()
                print('='*25)

          #---Ver Personagem---#
          if escolha == 2:
               from personagens import ver_personagem, lista_jogadores
               ver_personagem(lista_jogadores)

          #---Escolha 3---#
          if escolha == 3:
            from facções import eventos
            eventos(lista_jogadores)


          if escolha ==4:
                 from loja import loja
                 loja(lista_jogadores)
menu()




