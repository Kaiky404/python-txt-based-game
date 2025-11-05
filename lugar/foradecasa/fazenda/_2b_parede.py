from ....core import evento, helpers, C, lugares_vasculhados
from .... import player

def parede():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')

        if not entrou:
            print(f"Decidido a usar o cérebro, {player.char} procura aos arredores algo para distrair a galinha")
            print(f"Depois de alguns minutos, ele reuniu um pedaço de casca de fruta cítrica, uma pedrinha e um punhado de mato.")
            entrou = True

        escolhaParede = helpers.pergunta()