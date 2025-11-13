from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player
from ...rua._1_rua import rua

def escada():
    
    if not LUGARES_VASCULHADOS['casa']['bronca_do_pai']:

        evento.cabecalho('narrador')

        print(
            "Você se levanta, pôe suas chinelas, e começa a descer as escadas.\n"
            "Quando você está para enxergar alguém na cozinha, outra pessoa grita com você.\n"
            f"\n???: {player.char.upper()}, VENHA CÁ!!\n"
            )
        
        LUGARES_VASCULHADOS['casa']['bronca_do_pai'] = True

        print(
            "Chegando mais perto você reconhece a pessoa, é o seu velho pai, José.\n"
            "Ele olha para você com raiva, batendo o pé esperando alguma resposta..."
            )

        resposta = helpers.pergunta(
            'diálogo',
            ['seu pai está furioso com você por ter acordado tarde, você pode dizer desculpas ou só ignorar ele.'],
            ['desculpa', 'ignorar'])

        evento.cabecalho('narrador')
        if resposta == 'desculpa':
            print(
                "José respira fundo e então fala:\n"
                f"\nJosé: tá bom... mas da próxima vez não fica até tarde dormindo não, ouviu? Agora vai consertar a cerca dos carneiros.\n"
                )
            player.add('força', 1)

        elif resposta == 'ignorar':
            print(f"\nJosé: Seu inútil! sai daqui e vê se volta com a cabeça no lugar!\n")
            player.add('coragem', -1)

        else:
            helpers.erro()

    escolhaEscada = helpers.pergunta(
        'escolha',
        ['você pode voltar para o seu quarto ou sair de casa'],
        ['escada', 'sair'])

    if escolhaEscada == 'escada':
        evento.cabecalho('narrador')
        print(f'Você então sobe as escadas até o seu quarto')
        pass

    elif escolhaEscada == 'sair':
        print(f"Você decide sair de casa.")
        rua()
