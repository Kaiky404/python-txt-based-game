from ....core import evento, helpers, C, LUGARES_VASCULHADOS, MOCHILA
from .... import player
from .... import visuals

def ajustar():

    while True:
        print(visuals.cerca)
        
        evento.cabecalho('narrador')
        
        if LUGARES_VASCULHADOS['fazenda']['cerca']['trocar']:
            print(f"Você ajusta a tábua que tinha trocado, pregando-a no lugar, assim nenhum carneiro pode fugir.")
            LUGARES_VASCULHADOS['fazenda']['cerca']['ajustar'] = True
            return
        else:
            print(f"Você se levanta para ver a melhor forma de resolver a cerca. (Tente trocar a madeira podre antes de ajustá-la)")
            return