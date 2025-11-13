from ....core import evento, helpers, C, LUGARES_VASCULHADOS, MOCHILA
from .... import player

def trocar():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')

        if not entrou:
            print(f"Vendo que a madeira da cerca está podre, você procura em sua mochila por algo para substituir ela.")
            entrou = True
        
        if 'tabua' in MOCHILA:
            print(f"Você pega a tábua que tinha guardado, retira a madeira podre e a subtitui pela a tábua.")
            evento.discartar(player.char, 'tabua')
            LUGARES_VASCULHADOS['fazenda']['cerca']['trocar'] = True
            return
        else:
            print(f"Você não tem nada em sua mochila que possa usar para substituir a madeira podre.")
            return