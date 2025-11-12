from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player
from ._2a_montanha import montanha
from ._2b_rio import rio

def explorar():
    entrou = False

    while True:
        if not entrou:
            evento.cabecalho('narrador')
            print(f"{player.char} decide explorar a floresta.\n"
                f"E depois de caminha por um tempo ele se encontra numa encruzilhada.\n"
                f"À esquerda uma montanha de pedra, e à direira um caminho atravessando um rio.")
            entrou = True
        
        situação = [f"{player.char} pode tentar"]
        opções = []

        if not LUGARES_VASCULHADOS['floresta']['montanha']['vasculhada']:
            situação.append("subir a montanha")
            opções.append("montanha")
        else:
            situação.append("subir a montanha (já fez isso)")

        if not LUGARES_VASCULHADOS['floresta']['rio']['vasculhado']:
            situação.append("atravessar rio")
            opções.append("rio")
        else:
            situação.append("atravessar rio (já fez isso)")
        
        if not LUGARES_VASCULHADOS['floresta']['montanha']['caminho']:
            situação.append(f"voltar por onde veio ({player.char} está perdido e não sabe por onde veio)")
        else:
            situação.append("voltar por onde veio")
            opções.append("voltar")

        escolhaExplorar = helpers.pergunta(
            'escolha',
            situação,
            opções
        )

        if escolhaExplorar == 'montanha' and not LUGARES_VASCULHADOS['floresta']['montanha']['vasculhada']:
            montanha()

        elif escolhaExplorar == 'rio' and not LUGARES_VASCULHADOS['floresta']['rio']['vasculhado']:
            rio()

        elif escolhaExplorar == 'voltar' and not LUGARES_VASCULHADOS['floresta']['montanha']['caminho']:
            pass

        else:
            helpers.erro()
        
        if (
            LUGARES_VASCULHADOS['floresta']['montanha']['vasculhada'] and
            LUGARES_VASCULHADOS['floresta']['rio']['vasculhado']
            ):
            LUGARES_VASCULHADOS['floresta']['vasculhada'] = True