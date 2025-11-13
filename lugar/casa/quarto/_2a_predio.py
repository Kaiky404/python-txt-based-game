from ....core import evento, helpers, LUGARES_VASCULHADOS, C, skill_check
from .... import player

def predio():
    while True:
        if LUGARES_VASCULHADOS['casa']['janela']['predio_vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou para o prédio grande e viu tudo que havia de interessante.")
            return

        evento.cabecalho('narrador')
        print(f"Ao olhar para o prédio grande, você vê alguns trabalhadores trabalhando normalmente, mas algo chama sua atenção, {C.YELLOW}um grupo de adolescentes está maltratando um gato{C.NORMAL}.")
        escolha = helpers.pergunta(
            "ação",
            [f"Você pode tentar intervir ou só ignorar"],
            ["intervir", "ignorar"])

        if escolha == 'intervir':
            LUGARES_VASCULHADOS['casa']['janela']['predio_vasculhado'] = True
            evento.cabecalho('narrador')
            print(
                "Você pula da janela em corre em direção ao prédio grande\n"
                "Chegando lá, você tenta impedir os adolecentes de continuarem a maltratar o gato.")
                   
            if skill_check(player.get('força'), 2):
                print(
                    "Com toda a força que tem, você dá uma lição nos adolecente e salva o gatinho."
                    "Ele lhe agradeçe ronronando.")
                player.add('coragem', 1)
            else:
                print("Te faltando força, você não consegue impedir os adolecentes e apanha.")
                evento.dano(player.char, 5, 'apanhar de adolecentes')

            evento.cabecalho('narrador')
            print("Depois disso, você volta pra sua casa.")
            return

        elif escolha == 'ignorar':
            LUGARES_VASCULHADOS['casa']['janela']['predio_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você decide ignorar a situação, e os adolecente continuaram maltratando o gato até o fim da tarde.")
            player.add('coragem', -1)
            return
        
        else:
            evento.erro()
            continue