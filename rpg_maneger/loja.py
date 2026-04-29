
def loja(lista_jogadores):

    print('-->LOJA<--')
    
    geral = ['Itens Magicos', 'Armas', 'Armaduras', 'Rituais']

    for i, seleção in enumerate (geral):
        print(i+1,'-', seleção)

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:

            print('-->Itens Magicos<--')
            print('---')

            itens_magicos =   [{
                #<--Anel Espiral-->
                'item': 'Anel Espiral',
                'elemento': 'Morte',
                'efeito':'Permite que o portador atire paranormalmente rápido, fazendo com que a desvantagem ao dar dois tiros consecutivos seja anulada, mas reduzindo o dano desse segundo ataque pela metade. O portador pode optar por usar ou não essa propriedade.',
                'preco' : 100
                },

                {
                #<--Bracelete Energetico-->
                'item':'Bracelete Energetico',
                'elemento':'Energia',
                'efeito': 'Permite ao usuário, ao Transcender com o objeto, aprender o Ritual de "Onda de Choque"',
                'preco': 150
                }]

            for i, magicos in enumerate(itens_magicos):
                 print(f"{i+1}-")
                 print(f"Nome: ", magicos['item'])
                 print(f"Elemento: ", magicos['elemento'])
                 print(f"Efeito: ", magicos['efeito'])
                 print(f"Preço: ", magicos['preco'])
                 print('<=============>')

            escolha = int(input('Escolha um item: '))

            if escolha != None:

                print('Valor a ser descontado: ', magicos['preco'])

                per_escolha = input('Qual personagem vai comprar: ')
                per_encontrado = None

                item_escolhido = itens_magicos[escolha-1]

                for personagem in lista_jogadores:

                    if personagem['nome']== per_escolha:
                        per_encontrado = personagem
                        break

                if per_encontrado:
                        per_encontrado['dinheiro'] -= item_escolhido['preco']
                        print("Compra realizada!")
                        per_encontrado['inventario'].append(item_escolhido)

                else:
                        print("Personagem não encontrado!")


            return itens_magicos[escolha-1], lista_jogadores, per_escolha, per_encontrado, item_escolhido