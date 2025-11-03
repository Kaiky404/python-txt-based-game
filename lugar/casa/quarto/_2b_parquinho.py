from ....core import evento, helpers, lugares_vasculhados, C

def parquinho():
    while True:
        if lugares_vasculhados['janela']['parquinho_vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou para o parquinho enferrujado e viu tudo que havia de interessante.")
            return
        
        evento.cabecalho('narrador')
        print(f"Ao olhar para o parquinho enferrujado, você avista algumas crianças brincando, mas outra coisa chama sua atenção, {C.YELLOW}um grupo de crianças está praticando bullying contra uma criança de óculos{C.NORMAL}.")
        escolha = helpers.pergunta("ação", ["bullying"], ["intervir", "ignorar"])

        if escolha == 'intervir':
            lugares_vasculhados['janela']['parquinho_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você pula da sua janela em direção ao parquinho enferrujado, só de se aproximar das crianças, elas fogem com medo, assim, salvando a criança de óculos.")

            evento.cabecalho('mensagem do dev')
            print("em alguma atualização adcionar stat de bravura e adcionar um item da criança salva")

            evento.cabecalho('narrador')
            print("Depois de defender a criança, você volta pra sua casa.")
            return

        elif escolha == 'ignorar':
            lugares_vasculhados['janela']['parquinho_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você decide ignorar a situação, afinal, você é um covarde.")
            return
        
        else:
            evento.erro()
            continue
            
                
