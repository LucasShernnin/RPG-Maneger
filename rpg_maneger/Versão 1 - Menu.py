import sqlite3
import personagens

conexão = sqlite3.connect("Banco de dados.db")
cursor = conexão.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS criacão_de_personagens(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            jogador TEXT NOT NULL,
            personagem TEXT NOT NULL,
            nex INTEGER NOT NULL,
            classe TEXT NOT NULL,
            p_culto INTEGER NOT NULL,
            p_rebeldes INTEGER NOT NULL
            )""")

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

      #--Banco de Dados (Criação de personagem)---#
          #cursor.execute(""" INSERT INTO criacão_de_personagens
                        #(jogador, personagem, classe, nex, p_culto, p_rebeldes) VALUES
                        #(?, ?, ?, ?, ?, ?)""",
                  #(
                        #personagem['user'],
                        #personagem['nome'],
                        #personagem['classe'],
                        #personagem['nex'],
                        #personagem['prestigio_culto'],
                        #personagem['prestigio_rebeldes']
                  #))

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
          #---Escolha 3---#
          if escolha == 3:
            import facções
            
            if personagem['nex'] is None:
                 print("Crie um personagem primeiro!")
            elif personagem['nex'] != None:
                 facções.eventos(lista_jogadores)

            #--Banco de Dados (Atualização de informações)---#

            #cursor.execute(""" INSERT INTO criacão_de_personagens 
                  #(nex, p_culto, p_rebeldes) VALUES
                  #(?, ?, ?)""",
                  #(
                  #personagem['nex'],
                  #personagem['prestigio_culto'],
                  #personagem['prestigio_rebeldes'],
            #))
          if escolha == 4:
                from loja import loja
                loja(lista_jogadores)
                


#conexão.commit()
menu()




