from ....core import evento, LUGARES_VASCULHADOS, C, helpers, skill_check
from .... import player

def estabulo():
    while True:
        if LUGARES_VASCULHADOS['casa']['janela']['estabulo_vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou para o estábulo e viu tudo que havia de interessante.")
            return
        
        evento.cabecalho('narrador')
        print(f"Você pode ver alguns cavalos e galinhas no estábulo, mas além disso, {C.YELLOW}uma garota de cabelos vermelhos{C.NORMAL} acena para você")
        escolha = helpers.pergunta(
            "ação",
            ["Alguém acenou para você, você pode acenar de volta ou só ignorar"],
            ["acenar", "ignorar"])

        if escolha == 'acenar':
            LUGARES_VASCULHADOS['casa']['janela']['estabulo_vasculhado'] = True
            evento.cabecalho('narrador')
            if skill_check(player.get('coragem'), 2):
                print(
                    "Sorrindo, você acena de volta para a garota.\n"
                    "Ela acena de volta retribuindo o sorriso.")
                player.add('carisma', 1)
            else:
                print(
                    "Te faltando coragem, você não consegue se mover.\n"
                    "Ela vira as costa e vai embora")
                player.add('carisma', -1)

        elif escolha == 'ignorar':
            LUGARES_VASCULHADOS['casa']['janela']['estabulo_vasculhado'] = True
            evento.cabecalho('narrador')
            print("Você decide ignorar a garota.")
            player.add('carisma', -1)
            return
        
        else:
            evento.erro()
            continue