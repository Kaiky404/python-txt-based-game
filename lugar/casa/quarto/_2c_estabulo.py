from ....core import evento, LUGARES_VASCULHADOS, C, helpers, skill_check
from .... import player
from .... import visuals

@helpers.retry_on_inventory
def estabulo():
    while True:
        print(visuals.estabulo)
        if LUGARES_VASCULHADOS['casa']['janela']['estabulo_vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou para o estábulo e viu tudo que havia de interessante.")
            return
        
        evento.cabecalho('narrador')
        print(f"Você pode ver {C.YELLOW}uma garota de cabelos vermelhos{C.NORMAL} acena para você")
        escolha = helpers.pergunta(
            "ação",
            ["Você pode acenar de volta ou só ignorar"],
            ["acenar", "ignorar"])

        if escolha == 'acenar':
            LUGARES_VASCULHADOS['casa']['janela']['estabulo_vasculhado'] = True
            evento.cabecalho('narrador')
            if skill_check(player.get('coragem'), 2):
                print(visuals.estabulo_acenando)
                print(
                    "Sorrindo, você acena de volta para a garota.\n"
                    "Ela acena de volta retribuindo o sorriso.")
                player.add('carisma', 1)
                return
            else:
                print(visuals.estabulo_decepcionada)
                print(
                    "Te faltando coragem, você não consegue se mover.\n"
                    "Ela vira as costa e vai embora")
                player.add('carisma', -1)
                return

        elif escolha == 'ignorar':
            LUGARES_VASCULHADOS['casa']['janela']['estabulo_vasculhado'] = True
            print(visuals.estabulo_decepcionada)
            evento.cabecalho('narrador')
            print("Você decide ignorar a garota.")
            player.add('carisma', -1)
            return
        
        else:
            evento.erro()
            continue