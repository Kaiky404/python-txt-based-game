from ....core import evento, helpers, lugares_vasculhados, C

def predio():
    while True:
        if lugares_vasculhados['casa']['janela']['predio_vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou para o prédio grande e viu tudo que havia de interessante.")
            return

        evento.cabecalho('narrador')
        print(f"Ao olhar para o prédio grande, você vê alguns trabalhadores trabalhando normalmente, mas algo chama sua atenção, {C.YELLOW}um grupo de adolescentes está maltratando um gato{C.NORMAL}.")
        escolha = helpers.pergunta("ação", ["abuso"], ["intervir", "ignorar"])

        if escolha == 'intervir':
            lugares_vasculhados['casa']['janela']['predio_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você pula da sua janeka em direção ao prédio grande, sabuga os adolescentes na porrada e salva o gato.")

            evento.cabecalho('mensagem do dev')
            print("em alguma atualização adcionar pet e stat")

            evento.cabecalho('narrador')
            print("Depois de salvar o gato, você volta pra sua casa.")
            return

        elif escolha == 'ignorar':
            lugares_vasculhados['casa']['janela']['predio_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você decide ignorar a situação, afinal, você é um covarde ou odeia gatos.")

            evento.cabecalho('mensagem do dev')
            print("em alguma atualização fazer o user escolher uma das opções")
            return
        
        else:
            evento.erro()
            continue