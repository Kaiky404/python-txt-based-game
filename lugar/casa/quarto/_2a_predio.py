from ....core import game_logs, helpers, visited_places, C

def predio():
    while True:
        if visited_places['window']['big_building_seen']:
            game_logs.head('info')
            print("Você já olhou para o prédio grande e viu tudo que havia de interessante.")
            return

        game_logs.head('narrador')
        print(f"Ao olhar para o prédio grande, você vê alguns trabalhadores trabalhando normalmente, mas algo chama sua atenção, {C.YELLOW}um grupo de adolescentes está maltratando um gato{C.NORMAL}.")
        escolha = helpers.pergunta("ação", ["abuso"], ["intervir", "ignorar"])

        if escolha == 'intervir':
            visited_places['window']['big_building_seen'] = True
            game_logs.head('narrador')
            print("Você pula da sua janeka em direção ao prédio grande, sabuga os adolescentes na porrada e salva o gato.")

            game_logs.head('mensagem do dev')
            print("em alguma atualização adcionar pet e stat")

            game_logs.head('narrador')
            print("Depois de salvar o gato, você volta pra sua casa.")
            return

        elif escolha == 'ignorar':
            visited_places['window']['big_building_seen'] = True
            game_logs.head('narrador')
            print("Você decide ignorar a situação, afinal, você é um covarde ou odeia gatos.")

            game_logs.head('mensagem do dev')
            print("em alguma atualização fazer o user escolher uma das opções")
            return
        
        else:
            game_logs.erro()
            continue