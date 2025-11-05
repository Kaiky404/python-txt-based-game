from ....core import evento, helpers, lugares_vasculhados, C
from .... import player
from ...foradecasa.escola._1_escola import escola
from ...foradecasa.fazenda._1_fazenda import fazenda
from ...foradecasa.floresta._1_floresta import floresta

def escada():
    evento.cabecalho('narrador')
    print("Você se levanta, pôe suas chinelas, e começa a descer as escadas.")
    print("Quando você está para enxergar alguém na cozinha, outra pessoa grita com você.")
    print(f"\n???: {player.char.upper()}, VENHA CÁ, SEU MALDITO!\n")
    print("Chegando mais perto você reconhece a pessoa, é o seu velho pai, José.")
    print("Ele olha para você com raiva, batendo o pé esperando alguma resposta...")

    resposta = helpers.pergunta('diálogo', ['seu pai furioso com você'], ['dizer desculpas', 'mandar ele se foder'])

    evento.cabecalho('narrador')
    if resposta == 'dizerdesculpas':
        print("José respira fundo e então fala:")
        print(f"\nJosé: tá bom... mas da próxima vez não fica até tarde dormindo não, ouviu? Agora vai pegar madeira pra consertar a cerca das cabrita.\n")

    elif resposta == 'mandarelesefoder':
        print(f"\nJosé: Seu bastardo filho de uma puta! vai pra rua agora e vê se volta com a cabeça no lugar!\n")

    else:
        helpers.erro()

    escolhaEscada = helpers.pergunta('escolha', ['opções de seguir seu dia'], ['subir escadas', 'sair de casa'])

    if escolhaEscada == 'subirescadas':
        evento.cabecalho('mensagem do dev')
        print('vou fazer isso após a refatoração para o português')
        pass

    elif escolhaEscada == 'sairdecasa':

        evento.cabecalho('narrador')
        print("Você vai para fora de casa.")

        caminho = helpers.pergunta('escolha', ['o caminho para ir para a escola, sua fazenda ou floresta'], ['escola', 'fazenda', 'floresta'])

        if caminho == "escola":
            escola()
            pass
        
        elif caminho == "fazenda":
            fazenda()
            pass
        
        elif caminho == "floresta":
            floresta()
            pass
