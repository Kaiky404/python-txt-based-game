from ....core import evento, helpers, C, LUGARES_VASCULHADOS, MOCHILA
from .... import player
from .... import visuals

@helpers.retry_on_inventory
def trocar():

    while True:
        print(visuals.cerca)
        
        evento.cabecalho('narrador')
        
        if 'tabua' in MOCHILA:
            print(f"Você pega a tábua que tinha guardado, retira a madeira podre e a subtitui pela a tábua.")
            evento.discartar(player.char, 'tabua')
            LUGARES_VASCULHADOS['fazenda']['cerca']['trocar'] = True
            return
        else:
            print(f"Você não tem nada em sua mochila que possa usar para substituir a madeira podre. (Tente quebrar algo em seu quarto, seu pais não entram lá então não vai ser um problema).")
            return