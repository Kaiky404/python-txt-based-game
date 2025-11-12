from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player

def montanha():
    while True:
        evento.cabecalho('narrador')
        print(f"{player.char} decide subir a montanha.\n"
            f"Passando sobre algumas arvores mortas e alguns buracos ele sobe toda a montanha.\n"
            f"E de lá de cima enxerga uma rota para sair da floresta.")
        LUGARES_VASCULHADOS['floresta']['montanha']['caminho'] = True
        LUGARES_VASCULHADOS['floresta']['montanha'] = True
        return