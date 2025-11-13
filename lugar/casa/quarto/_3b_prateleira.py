from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player

@helpers.retry_on_inventory
def prateleira():
    if LUGARES_VASCULHADOS['casa']['prateleira']['vasculhada']:
        evento.cabecalho('info')
        print("Você já vasculhou as prateleiras e não encontrou mais nada.")
        return
    
    while True:
        evento.cabecalho('narrador')
        print("Enquanto você passa a mão por alguns livros e outros objetos que você guardou lá, você nota alguns interessantes.")
        print(f"Na prateleira vermelha, há uma {C.YELLOW}chave com uma pena presa{C.NORMAL} e uma {C.YELLOW}prisilía de cabelo{C.NORMAL}.")
        print("Porém essa prateleira é muito alta para alcançá-la normalmente, então você vai e pega um banquinho de madeira para alcançá-la.")

        escolhaPrateleira = helpers.pergunta(
            'escolha',
            ['Você pode pegar ambas a chave e o grampo'],
            ['chave', 'grampo', 'voltar'])

        if escolhaPrateleira == "chave":
            if LUGARES_VASCULHADOS['casa']['prateleira']['chave_pega']:
                evento.cabecalho('info')
                print("Você já pegou a chave da prateleira.")

            else:
                LUGARES_VASCULHADOS['casa']['prateleira']['chave_pega'] = True
                evento.adicionar(player.char, "chavecompena")

            escolhaUsarbanquinho = helpers.pergunta('escolha', ['o grampo de cabelo'], ['pegar', 'nao pegar'])

            if escolhaUsarbanquinho == "pegar":
                if LUGARES_VASCULHADOS['casa']['prateleira']['grampo_pego']:
                    evento.cabecalho('info')
                    print("Você já pegou o prisilia de cabelo da prateleira.")

                else:
                    LUGARES_VASCULHADOS['casa']['prateleira']['grampo_pego'] = True
                    evento.adicionar(player.char, "grampo")
                
                evento.cabecalho('narrador')
                print("Mas quando você tenta descer, o banquinho quebra e você cai no chão.")

                evento.dano(player.char, 15, "cair do banquinho")

                evento.cabecalho('narrador')
                print("Você se levanta e sai de perto da prateleira.")

                if (
                    LUGARES_VASCULHADOS['casa']['prateleira']['grampo_pego'] and
                    LUGARES_VASCULHADOS['casa']['prateleira']['chave_pega']
                    ):
                    LUGARES_VASCULHADOS['casa']['prateleira']['vasculhada'] = True
                    evento.cabecalho('info')
                    print("Você já pegou todos os itens interessantes da prateleira.")
                return
            
            elif escolhaUsarbanquinho == "naopegar":
                evento.cabecalho('narrador')
                print("Você decide deixar o grampo onde está.")
                return
            
            else:
                helpers.erro()

        elif escolhaPrateleira == "grampo":
            if LUGARES_VASCULHADOS['casa']['prateleira']['grampo_pego']:
                evento.cabecalho('info')
                print("Você já pegou a prisilia de cabelo da prateleira.")

            else:
                LUGARES_VASCULHADOS['casa']['prateleira']['grampo_pego'] = True
                evento.adicionar(player.char, "grampo")

            escolhaUsarbanquinho = helpers.pergunta(
                'pergunta',
                ['Em cima da prateleira tem uma chave decorada com uma pena'],
                ['pegar', 'sair'])

            if escolhaUsarbanquinho == "pegar":
                if LUGARES_VASCULHADOS['casa']['prateleira']['chave_pega']:
                    evento.cabecalho('info')
                    print("Você já pegou a chave com pena presa da prateleira.")

                else:
                    LUGARES_VASCULHADOS['casa']['prateleira']['chave_pega'] = True
                    evento.adicionar(player.char, "chavecompena")

                evento.cabecalho('narrador')
                print("Mas quando você tenta descer, o banquinho quebra e você cai no chão.")

                evento.dano(player.char, 15, "cair do banquinho")

                evento.cabecalho('narrador')
                print("Você se levanta e sai de perto da prateleira.")

                if (
                    LUGARES_VASCULHADOS['casa']['prateleira']['grampo_pego'] and
                    LUGARES_VASCULHADOS['casa']['prateleira']['chave_pega']
                    ):
                    LUGARES_VASCULHADOS['casa']['prateleira']['vasculhada'] = True
                    evento.cabecalho('info')
                    print("Você pegou todos os itens interessantes da prateleira.")
                return

            elif escolhaUsarbanquinho == "sair":
                evento.cabecalho('narrador')
                print("Você decide deixar a chave onde está.")
                return
            
            else:
                helpers.erro()

        elif escolhaPrateleira == "voltar":
            evento.cabecalho('narrador')
            print("Você decide deixar os itens onde estão.")
            return
        
        else:
            helpers.erro()