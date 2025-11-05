from ....core import evento, helpers, C, lugares_vasculhados
from .... import player
from ._2a_atrair import atrair
from ._2b_parede import parede

def galinheiro():
    entrou = False

    while True:

        evento.cabecalho('narrador')

        if not entrou:
            print(f"E então {player.char} decide checar o galinheiro")
            entrou = True
        
        print(f"Ele enfia sua cabeça dentro do galinheiro, conseguindo ver algumas coisas...")
        print(f"Uma galinha e cima de seu ninho e algo rabiscado na parede do galinheiro.")

        escolhaGalinheiro = helpers.pergunta(
            'escolha',
            [f'{player.char} pode interagir com a galinha, ou tentar enxergar o que tem escrito na parede'],
            ['galinha', 'parede', 'sair']
        )

        if escolhaGalinheiro == 'galinha':

            evento.cabecalho('narrador')
            print(f"E então {player.char} decide tentar tirar a galinha de cima do ninho")
            print(f"Ele pensa em algumas alternativas como tentar empurrar a galinha ou atraí-la com algo")

            escolhaGalinha = helpers.pergunta(
                'ação',
                [f'{player.char} pode tentar chamar a atenção da galinha para longe do ninho ou deixar ela em paz'],
                ['atrair', 'sair']
            )

            if escolhaGalinha == 'atrair':
                atrair()
            
            elif escolhaGalinha == 'sair':
                print(f"{player.char} decide deixar a galinha em paz por enquanto.")
                break
            else:
                helpers.erro()

        elif escolhaGalinheiro == 'parede':
            parede()

        elif escolhaGalinheiro == 'sair':
            print(f"{player.char} decide sair do galinheiro e voltar para perto do paiol.")
            return
        else:
            helpers.erro()

        if (
            lugares_vasculhados['fazenda']['galinheiro']['pistola_pega'] and
            lugares_vasculhados['fazenda']['galinheiro']['rabisco_lido']
            ):
            lugares_vasculhados['fazenda']['galinheiro']['vasculhado'] = True
            evento.head('info')
            print(f"Depois de interagir com todos os pontos interessantes do galinheiro, {player.char} decide fazer outra coisa.")
            return
            
