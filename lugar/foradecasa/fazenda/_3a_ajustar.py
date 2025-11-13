from ....core import evento, helpers, C, LUGARES_VASCULHADOS, MOCHILA
from .... import player

def ajustar():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')

        if not entrou:
            print(f"Vendo que a madeira da cerca está podre, você que é melhor trocar ela antes de ajusta-lá.")
            entrou = True
        
        if LUGARES_VASCULHADOS['fazenda']['cerca']['trocar']:
            print(f"Você ajusta a tábua que tinha trocado, pregando-a no lugar, assim nenhum carneiro pode fugir.")
            LUGARES_VASCULHADOS['fazenda']['cerca']['ajustar'] = True
            return
        else:
            print(f"Você se levanta para ver a melhor forma de resolver a cerca.")
            return