from ....core import evento, helpers, lugares_vasculhados, C
from .... import player
from ...rua._1_rua import rua

def escada():
    
    if not lugares_vasculhados['casa']['bronca_do_pai']:

        evento.cabecalho('narrador')

        print(
            "Você se levanta, pôe suas chinelas, e começa a descer as escadas.\n"
            "Quando você está para enxergar alguém na cozinha, outra pessoa grita com você.\n"
            f"\n???: {player.char.upper()}, VENHA CÁ, SEU MALDITO!\n"
            )
        
        lugares_vasculhados['casa']['bronca_do_pai'] = True

        print(
            "Chegando mais perto você reconhece a pessoa, é o seu velho pai, José.\n"
            "Ele olha para você com raiva, batendo o pé esperando alguma resposta..."
            )

        resposta = helpers.pergunta('diálogo', ['seu pai furioso com você'], ['dizer desculpas', 'mandar ele se foder'])

        evento.cabecalho('narrador')
        if resposta == 'dizerdesculpas':
            print(
                "José respira fundo e então fala:\n"
                f"\nJosé: tá bom... mas da próxima vez não fica até tarde dormindo não, ouviu? Agora vai pegar madeira pra consertar a cerca das cabrita.\n"
                )

        elif resposta == 'Ignorá-lo':
            print(f"\nJosé: Seu bastardo filho de uma figa! sai daqui e vê se volta com a cabeça no lugar!\n")

        else:
            helpers.erro()

    escolhaEscada = helpers.pergunta('escolha', ['opções de seguir seu dia'], ['subir escadas', 'sair de casa'])

    if escolhaEscada == 'subirescadas':
        evento.cabecalho('narrador')
        print(f'{player.char} então sobe as escadas até o seu quarto')
        pass

    elif escolhaEscada == 'sairdecasa':
        rua()
