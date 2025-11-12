from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player
from ._2_explorar import explorar

def floresta():
    entrou = False

    while True:
        
        if not LUGARES_VASCULHADOS['floresta']['vasculhada']:

            if not entrou:
                evento.cabecalho('narrador')
                print(f"{player.char} caminha em direção à floresta próxima.\n"
                    f"Ao chegar, {player.char} se aventura entre as árvores, ouvindo os sons da natureza ao seu redor.\n"
                    f"O tempo passa e {player.char} derrepente se vê perdido na floresta.")
                entrou = True

            situação = [f"{player.char} se perdeu na floresta e pode tentar"]
            opções = []

            if not LUGARES_VASCULHADOS['floresta']['vasculhada']:
                situação.append("explorar a floresta mais a fundo")
                opções.append("explorar")
            else:
                situação.append("explorar a floresta mais a fundo (já fez isso)")

            situação.append("voltar por onde veio")
            opções.append("voltar")

            escolhaFloresta = helpers.pergunta(
                'escolha',
                situação,
                opções
            )

            if escolhaFloresta == 'explorar' and not LUGARES_VASCULHADOS['floresta']['vasculhada']:
                explorar()

            elif escolhaFloresta == 'voltar':
                pass

            else:
                helpers.erro()

        else:
            print(f"{player.char} já se perdeu na floresta e achou o caminho de volta, ele não quer mais ir lá.")
            return