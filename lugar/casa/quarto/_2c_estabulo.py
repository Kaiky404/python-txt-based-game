from ....core import evento, lugares_vasculhados, C, helpers

def estabulo():
    while True:
        if lugares_vasculhados['janela']['estabulo_vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou para o estábulo e viu tudo que havia de interessante.")
            return
        
        evento.cabecalho('narrador')
        print("Você pode ver alguns cavalos e galinhas no estábulo, mas além disso, algo chama sua atenção...")
        escolha = helpers.pergunta("ação", [f"{C.YELLOW}uma garota de cabelo vermelho{C.NORMAL}"], ["acenar", "ignorar"])

        if escolha == 'acenar':
            lugares_vasculhados['janela']['estabulo_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você acena para a garota de cabelo vermelho, ela sorri e acena de volta.")

            evento.cabecalho('mensagem do dev')
            print("em alguma atualização adcionar stat de carisma e talvez um interesse romântico")
            return

        elif escolha == 'ignorar':
            lugares_vasculhados['janela']['estabulo_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você decide ignorar a garota, afinal, você gosta de ser invisível.")
            return
        
        else:
            evento.erro()
            continue