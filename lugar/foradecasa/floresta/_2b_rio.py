from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player
from ._2bb_caverna import caverna


def rio():
    entrou = False

    while True:
        if not entrou:
            evento.cabecalho('narrador')
            print(f"{player.char} decide atravessar o rio.\n"
                f"Depois de molhar seus calçados atravessando o rio.\n"
                f"Ele pode ver uma caverna a sua frente, por estar numa floresta sozinho acha que pode não ser uma boa idéia entrar nela..")
            entrou = True
        
        situação = [f"{player.char} pode tentar"]
        opções = []

        if not LUGARES_VASCULHADOS['floresta']['rio']['caverna']['vasculhada']:
            situação.append("entrar na caverna")
            opções.append("caverna")

        else:
            situação.append("entrar na caverna (já fez isso)")

        situação.append("voltar por onde veio")
        opções.append("voltar")

        escolhaExplorar = helpers.pergunta(
            'escolha',
            situação,
            opções
        )

        if escolhaExplorar == 'caverna':
            caverna()

        elif escolhaExplorar == 'voltar':
            pass

        else:
            helpers.erro()