from ....core import game_logs, visited_places, C, helpers

def estabulo():
    while True:
        if visited_places['window']['stable_seen']:
            game_logs.head('info')
            print("Você já olhou para o estábulo e viu tudo que havia de interessante.")
            return
        
        game_logs.head('narrador')
        print("Você pode ver alguns cavalos e galinhas no estábulo, mas além disso, algo chama sua atenção...")
        escolha = helpers.pergunta("ação", [f"{C.YELLOW}uma garota de cabelo vermelho{C.NORMAL}"], ["acenar", "ignorar"])

        if escolha == 'acenar':
            visited_places['window']['stable_seen'] = True
            game_logs.head('narrador')
            print("Você acena para a garota de cabelo vermelho, ela sorri e acena de volta.")

            game_logs.head('mensagem do dev')
            print("em alguma atualização adcionar stat de carisma e talvez um interesse romântico")
            return

        elif escolha == 'ignorar':
            visited_places['window']['stable_seen'] = True
            game_logs.head('narrador')
            print("Você decide ignorar a garota, afinal, você gosta de ser invisível.")
            return
        
        else:
            game_logs.erro()
            continue