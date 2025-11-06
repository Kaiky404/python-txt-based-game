from ....core import evento, helpers, C, lugares_vasculhados, mochila
from .... import player

def ajustar():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')

        if not entrou:
            print(f"Vendo que a madeira da cerca está podre, {player.char} pensa consigo que é melhor trocar ela antes de ajusta-lá.")
            entrou = True
        
        if lugares_vasculhados['fazenda']['cerca']['trocar']:
            print(f"{player.char} ajusta a tábua que tinha trocado, pregando-a no lugar, assim nenhum carneiro pode fugir.")
            lugares_vasculhados['fazenda']['cerca']['ajustar'] = True
            return
        else:
            print(f"{player.char} então se levanta para ver a melhor forma de resolver a cerca.")
            return