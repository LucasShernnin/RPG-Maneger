
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
                 print(f"{i+1}, -")
                 print(f"Nome: ", magicos['item'])
                 print(f"Elemento: ", magicos['elemento'])
                 print(f"Efeito: ", magicos['efeito'])
                 print(f"Preço: ", magicos['preco'])
                 print('<=============>')

            escolha = int(input('Escolha um item: '))

            if escolha == 1:
                import personagens

                #print('Tem certeza que deseja este item?: ', magicos['item'])
                
                print('Valor a ser descontado: ', magicos['preco'])
                
                for personagem in lista_jogadores:
                     desconto = personagem['dinheiro'] - magicos['preco']
                     print(desconto)



            return itens_magicos[escolha-1], desconto