from ....core import evento, helpers, C, lugares_vasculhados, mochila
from .... import player

def trocar():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')
        print(f"DEBUG: MOCHILA ATUAL: {mochila}")

        if not entrou:
            print(f"Vendo que a madeira da cerca está podre, {player.char} procura em sua mochila por algo para substituir ela.")
            entrou = True
        
        if 'tabua' in mochila:
            print(f"{player.char} pega a tábua que tinha guardado, retira a madeira podre e a subtitui pela a tábua.")
            evento.discartar(player.char, 'tabua')
            lugares_vasculhados['fazenda']['cerca']['trocar'] = True
            return
        else:
            print(f"{player.char} não tem nada em sua mochila que possa usar para substituir a madeira podre.")
            return