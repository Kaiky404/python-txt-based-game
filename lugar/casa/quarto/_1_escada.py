from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player
from ...rua._1_rua import rua
from .... import visuals

@helpers.retry_on_inventory
def escada():
    if not LUGARES_VASCULHADOS['casa']['bronca_do_pai']:
        print("Quando você está para sair de casa, alguém grita com você.\n")
        print(visuals.jose_bronca)
        print(f"\n???: {player.char.upper()}, VENHA CÁ!! PORQUÊ VOCÊ NÃO ESTÁ NA ESCOLA AINDA? \n")
        
        LUGARES_VASCULHADOS['casa']['bronca_do_pai'] = True

        print(
            "Chegando mais perto você reconhece a pessoa, é o seu velho pai, José.\n"
            "Ele olha para você com raiva, batendo o pé esperando alguma resposta..."
            )

        resposta = helpers.pergunta(
            'diálogo',
            ['seu pai está furioso, você pode dizer desculpas ou só ignorar ele.'],
            ['desculpa', 'ignorar'])

        evento.cabecalho('narrador')
        if resposta == 'desculpa':
            print("José parece surpreso com sua atitude")
            print(visuals.jose_surpreso)
            print("Ele respira fundo e então fala:\n")
            print(visuals.jose)
            print("\nJosé: tá bom... mas da próxima vez não fica até tarde dormindo não, ouviu? Agora vai consertar a cerca dos carneiros.\n")
            player.add('força', 1)

        elif resposta == 'ignorar':
            print("José fica ainda mais bravo com sua atitude")
            print(visuals.jose_bronca)
            print(f"\nJosé: Seu inútil! sai daqui e vê se volta com a cabeça no lugar!\n")
            player.add('coragem', -1)

        else:
            print(f"{C.RED}Tente novamente.{C.NORMAL}")

    escolhaEscada = helpers.pergunta(
        'escolha',
        ['você pode voltar para o seu quarto ou sair de casa'],
        ['escada', 'sair'])

    if escolhaEscada == 'escada':
        evento.cabecalho('narrador')
        print("Você decide subir as escadas")
        print(visuals.escadas_subindo)
        return "voltar"

    elif escolhaEscada == 'sair':
        evento.cabecalho('narrador')
        print(f"Você decide sair de casa.")
        print(visuals.porta)
        return rua()
