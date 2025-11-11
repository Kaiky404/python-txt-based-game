from ....core import evento, helpers, lugares_vasculhados, C
from .... import player

def montanha():
    while True:
        evento.cabecalho('narrador')
        print(f"{player.char} decide subir a montanha.\n"
            f"Passando sobre algumas arvores mortas e alguns buracos ele sobe toda a montanha.\n"
            f"E de lá de cima enxerga uma rota para sair da floresta.")
        lugares_vasculhados['floresta']['montanha']['caminho'] = True
        lugares_vasculhados['floresta']['montanha'] = True
        return