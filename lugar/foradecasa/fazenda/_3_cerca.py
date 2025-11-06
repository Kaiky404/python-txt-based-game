from ....core import evento, helpers, C, lugares_vasculhados
from .... import player
from ._3b_trocar import trocar
from ._3a_ajustar import ajustar

def cerca():
    entrou = False

    while True:

        if not entrou:
            evento.cabecalho('narrador')
            print(f"E então {player.char} decide checar a cerca\n"
                  f"{player.char} atravessa o paiol e logo mais descobre onde estava quebrado na cerca.\n"
                  f"Determinado a ajudar seu pai com o trabalho na fazenda, ele pensa em algumas formas de arrumar a cerca.")
            entrou = True

        situação = [f"{player.char} pode tentar"]
        opção = []

        if not lugares_vasculhados['fazenda']['cerca']['ajustar']:
            situação.append(f"ajustar a cerca")
            opção.append(f"ajustar")
        else:
            situação.append(f"ajustar a cerca (já fez isso)")

        if not lugares_vasculhados['fazenda']['cerca']['trocar']:
            situação.append(f"trocar a madeira")
            opção.append(f"trocar")
        else:
            situação.append(f"trocar a madeira (já fez isso)")
        
        situação.append(f"ou ir embora")
        opção.append(f"sair")

        
        escolhaCerca = helpers.pergunta(
            'ação',
            situação,
            opção
        )

        if escolhaCerca == 'ajustar':
            ajustar()
        elif escolhaCerca == 'trocar':
            trocar()
        elif escolhaCerca == 'sair':
            return
        else:
            helpers.erro()
        
        if (
            lugares_vasculhados['fazenda']['cerca']['trocar'] and
            lugares_vasculhados['fazenda']['cerca']['ajustar']
            ):
            lugares_vasculhados['fazenda']['cerca']['arrumada'] = True
            evento.head('info')
            print(f"Depois de trocar e ajustar a cerca no lugar, {player.char} decide fazer outra coisa.")
            return