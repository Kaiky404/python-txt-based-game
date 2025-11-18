from ....core import evento, helpers, C, LUGARES_VASCULHADOS, MOCHILA
from .... import player
from .... import visuals

@helpers.retry_on_inventory
def parede():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')

        if not entrou:
            print(f"{player.char} então se aproxima do rabisco da parede e tenta enxergar o que está escrito.")
            print(visuals.rabisco)
            entrou = True
        
        if not LUGARES_VASCULHADOS['fazenda']['galinheiro']['galinha_vazou']:
            print(f"Por não ter lidado com a galinha no ninho logo ao seu lado, ela o bicora na bunda e sai correndo!")
            print(visuals.galinha)
            evento.dano(player.char, 5, 'ter a bunda bicorada')
            LUGARES_VASCULHADOS['fazenda']['galinheiro']['galinha_vazou'] = True
            print(f"Você se concentrar na parede, e então lê o rabisco:\n")
            print(visuals.rabisco)
            print(f"'A galinha protege o que brilha, mas quem limpa nunca acha o que está em cima.'")
            LUGARES_VASCULHADOS['fazenda']['galinheiro']['rabisco_lido'] = True
            return
        else:
            print(f"Você se concentrar na parede, e então lê o rabisco:\n")
            print(visuals.rabisco)
            print(f"'A galinha protege o que brilha, mas quem limpa nunca acha o que está em cima.'")
            player.add('inteligencia', 1)
            LUGARES_VASCULHADOS['fazenda']['galinheiro']['rabisco_lido'] = True
            return