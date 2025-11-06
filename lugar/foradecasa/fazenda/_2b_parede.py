from ....core import evento, helpers, C, lugares_vasculhados, mochila
from .... import player

def parede():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')

        if not entrou:
            print(f"{player.char} então se aproxima do rabisco da parede e tenta enxergar o que está escrito.")
            entrou = True
        
        if not lugares_vasculhados['fazenda']['galinheiro']['galinha_vazou']:
            print(f"Por não ter lidado com a galinha no ninho logo ao seu lado, ela o bicora na bunda e sai correndo!")
            evento.dano(player.char, 5, 'ter a bunda bicorada')
            lugares_vasculhados['fazenda']['galinheiro']['galinha_vazou'] = True
            print(f"Depois disso, você volta a se concentrar na parede, e então lê o rabisco:\n"
                  f"'A galinha protege o que brilha, mas quem limpa nunca acha o que está em cima.'")
            lugares_vasculhados['fazenda']['galinheiro']['rabisco_lido'] = True
            return
        else:
            print(f"Depois disso, você volta a se concentrar na parede, e então lê o rabisco:\n"
                  f"'A galinha protege o que brilha, mas quem limpa nunca acha o que está em cima.'")
            lugares_vasculhados['fazenda']['galinheiro']['rabisco_lido'] = True
            return