
from personagens import player
from personagens import ver_personagem, lista_jogadores
from facções import eventos
from loja import loja

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
                player()
                print('='*25)

          #---Ver Personagem---#
          elif escolha == 2:
               ver_personagem(lista_jogadores)

          #---Escolha 3---#
          elif escolha == 3:
            eventos(lista_jogadores)


          elif escolha == 4:
                 loja(lista_jogadores)

          elif escolha == 6:
               print('Sistema Fechado!')
               break
menu()




