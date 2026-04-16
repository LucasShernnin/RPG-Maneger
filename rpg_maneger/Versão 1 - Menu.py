
import personagens

print("{}Bem Vindo ao AQTV{}".format(('-'*5), ('-'*5)))

lista_jogadores = []

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
                personagem = personagens.player()
                lista_jogadores.append(personagem)
                print('='*25)

          #---Ver Personagem---#
          if escolha == 2:
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

                        for itens in personagem['inventario']:
                              print(personagem)
          #---Escolha 3---#
          if escolha == 3:
            import facções
            
            if personagem['nex'] is None:
                 print("Crie um personagem primeiro!")
            elif personagem['nex'] != None:
                 facções.eventos(lista_jogadores)


          if escolha ==4:
                 from loja import loja
                 loja(lista_jogadores)
menu()




