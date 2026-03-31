import sqlite3

conexão = sqlite3.connect("Banco de dados.db")
cursor = conexão.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS criação_de_personagens(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            jogador TEXT NOT NULL,
            personagem TEXT NOT NULL UNIQUE,
            nex INTEGER NOT NULL,
            classe INTEGER NOT NULL,
            p_culto INTEGER NOT NULL,
            p_rebeldes INTEGER NOT NULL
            
)""")

cursor.execute(""" INSERT INTO criação_de_personagens 
               (jogador, personagem, classe, nex, p_culto, p_rebeldes) VALUES
               ('player','nome', 'classe', 'nex', 'prestigio_culto', 'prestigio_rebeldes'  )

""")

import personagens

print("{}Bem Vindo ao AQTV{}".format(('-'*5), ('-'*5)))

lista_jogadores = []

def menu():
    while True:
          print('='*5)
          print("MENU")
          print('='*5)
          lista_menu  = ['Criar Personagem', 'Ver Jogadores', 'Registrar Evento', 'Dashboard', 'Sair']

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
                        print(f"Player: {usuario['player']}")
                        print(f"Nome do Personagem: {usuario['nome']}")
                        print(f"Classe: {usuario['classe']}")
                        print(f"NEX: {usuario['nex']}")
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

menu()




