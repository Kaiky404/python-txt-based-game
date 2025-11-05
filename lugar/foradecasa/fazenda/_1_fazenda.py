from ....core import evento, helpers, lugares_vasculhados, C
from .... import player
from ._2_galinheiro import galinheiro

def fazenda():
    entrou = False

    while True:

        situação = []
        opções = []

        if not lugares_vasculhados['fazenda']['galinheiro']['vasculhado']:
            situação.append(f"{player.char} pode checar o galinheiro")
            opções.append(f"galinheiro")
        else:
            situação.append(f"{player.char} já checou o galinheiro")

        if not lugares_vasculhados['fazenda']['cerca']['arrumada']:
            situação.append(f"consertar a cerca dos caneiros")
            opções.append(f"cerca")
        else:
            situação.append(f"já viu a parede")

        situação.append(f"ou ir embora")
        opções.append(f"sair")
        
        if not entrou:
            evento.cabecalho('narrador')
            print(f"{player.char} caminha em direção a fazenda da sua família.\n"
                  f"Ao chegar, {player.char} vê os campos verdes e os pastos cheios de gado.\n"
                  f"Parado em frente a um paiol, {player.char} decide o que fazer.")
            entrou = True
        
        escolhaFazenda = helpers.pergunta(
            'escolha',
            situação,
            opções
            )

        if escolhaFazenda == 'galinheiro':
            galinheiro()
        elif escolhaFazenda == 'cerca':
            pass
        elif escolhaFazenda == 'sair':
            return
        else:
            helpers.erro()