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

        situação = [f"Dentro do galinheiro, {player.char} pode ver"]
        ação = []

        if not lugares_vasculhados['fazenda']['galinheiro']['galinha_vazou']:
            situação.append(f"uma galinha emcima de seu ninho")
            ação.append('galinha')
        else:
            situação.append(f"uma caixa em cima de um ninho")
            ação.append('caixa')

        if not lugares_vasculhados['fazenda']['galinheiro']['rabisco_lido']:
            situação.append(f"ou algo rabiscado na parede do galinheiro")
            ação.append('parede')
        else:
            situação.append(f"ou algo rabiscado na parede do galinheiro (já leu o rabisco)")
        
        ação.append('sair')

        escolhaGalinheiro = helpers.pergunta(
            'escolha',
            situação,
            ação
        )

        if escolhaGalinheiro in ('galinha', 'caixa'):

            if not lugares_vasculhados['fazenda']['galinheiro']['galinha_vazou']: 
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
            else:
                escolhaCaixa = helpers.pergunta(
                'ação',
                [f'{player.char} tenta abrir a caixa?'],
                ['abrir', 'sair']
                )

                evento.cabecalho('narrador')
                if escolhaCaixa == 'abrir':
                    if lugares_vasculhados.get('prateleira', {}).get('chave_pega'):
                        print(f"{player.char} abre a caixa com a chave que havia encontrado e dentro dela encontra uma Pistola.")
                        evento.adicionar(player.char, 'pistola')
                        lugares_vasculhados['fazenda']['galinheiro']['pistola_pega'] = True
                        return
                    print(f"{player.char} não consegue abrir a caixa já que não tem a chave correspondente.")

                elif escolhaCaixa == 'sair':
                    print(f"{player.char} decide largar a caixa lá por agora.")

                else:
                    helpers.erro()

        elif escolhaGalinheiro == 'parede' and not lugares_vasculhados['fazenda']['galinheiro']['rabisco_lido']:
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
            
