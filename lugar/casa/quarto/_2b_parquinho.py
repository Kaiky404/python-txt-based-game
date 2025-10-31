from ....core import game_logs, helpers, visited_places, C

def parquinho():
    while True:
        if visited_places['window']['rusty_playground_seen']:
            game_logs.head('info')
            print("Você já olhou para o parquinho enferrujado e viu tudo que havia de interessante.")
            return
        
        game_logs.head('narrador')
        print(f"Ao olhar para o parquinho enferrujado, você avista algumas crianças brincando, mas outra coisa chama sua atenção, {C.YELLOW}um grupo de crianças está praticando bullying contra uma criança de óculos{C.NORMAL}.")
        escolha = helpers.pergunta("ação", ["bullying"], ["intervir", "ignorar"])

        if escolha == 'intervir':
            visited_places['window']['rusty_playground_seen'] = True
            game_logs.head('narrador')
            print("Você pula da sua janela em direção ao parquinho enferrujado, só de se aproximar das crianças, elas fogem com medo, assim, salvando a criança de óculos.")

            game_logs.head('mensagem do dev')
            print("em alguma atualização adcionar stat de bravura e adcionar um item da criança salva")

            game_logs.head('narrador')
            print("Depois de defender a criança, você volta pra sua casa.")
            return

        elif escolha == 'ignorar':
            visited_places['window']['rusty_playground_seen'] = True
            game_logs.head('narrador')
            print("Você decide ignorar a situação, afinal, você é um covarde.")
            return
        
        else:
            game_logs.erro()
            continue
            
                
