import personagens 

print("{}Bem Vindo ao AQTV{}".format(('-'*5), ('-'*5)))

lista_jogadores = []

def menu():
    while True:
          print("MENU")
          lista_menu  = ['Criar Personagem', 'Ver Jogadores', 'Registrar Evento', 'Dashboard', 'Sair']
          
          for i, itens in enumerate(lista_menu):
                print(i+1, '-', itens)
          escolha = int(input("Escolha uma opção: "))
          if escolha == 1:
                print("===== PERSONAGEM =====")
                jogador, nome, idade = personagens.player()
                classe = personagens.classes()
                lista_jogadores.append([jogador, nome, idade, classe])
                print('='*25)
                print(f'Personagem Criado!\nNome: {nome}\nIdade: {idade}\nClasse: {classe} \nBem vindo ao Mundo Jogador: {jogador}!')

          if escolha == 2:
            for i, usuario in enumerate(lista_jogadores):
                      print(i+1, '-', usuario)
menu()




