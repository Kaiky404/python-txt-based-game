from ....core import evento, helpers, C, lugares_vasculhados
from .... import player

def atrair():
    entrou = False

    while True:
        
        evento.cabecalho('narrador')

        if not entrou:
            print(f"Decidido a usar o cérebro, {player.char} procura aos arredores algo para distrair a galinha")
            print(f"Depois de alguns minutos, ele reuniu um pedaço de casca de fruta cítrica, uma pedrinha e um punhado de mato.")
            entrou = True

        escolhaAtrair = helpers.pergunta(
            'escolha',
            [f'Para distrair a galinha, {player.char} pode usar o pedaço de casca, a pedrinha ou o punhado de mato'],
            ['casca', 'pedra', 'mato', 'sair']
        )

        evento.cabecalho('narrador')
        print(f"{player.char} pega a/o {escolhaAtrair} na mão e pensa se é melhor arremessar ou deixá-la/o perto da galinha")        
        
        if escolhaAtrair == 'casca':

            escolhaAcao = helpers.pergunta(
                'ação',
                [f'{player.char} pode arremessar a {escolhaAtrair} ou deixá-la perto da galinha.'],
                ['arremessar', 'deixar']
            )

            evento.cabecalho('narrador')
            if escolhaAcao == 'arremessar':
                print(f"E então {player.char} arremessa a {escolhaAtrair} em direção da galinha.\n" 
                      f"A galinha cheira a {escolhaAtrair} um pouco e cisca pra longe, meio que espirrando.")
                sucesso = True

            elif escolhaAcao == 'deixar':
                print(f"E então {player.char} deixa a {escolhaAtrair} perto da galinha.\n" 
                      f"A galinha ignora completamente a {escolhaAtrair}.")
                sucesso = False

            else:
                helpers.erro()

        elif escolhaAtrair == 'pedra':

            escolhaAcao = helpers.pergunta(
                'ação',
                [f'{player.char} pode arremessar a {escolhaAtrair} ou deixá-la perto da galinha.'],
                ['arremessar', 'deixar']
            )

            evento.cabecalho('narrador')
            if escolhaAcao == 'arremessar':
                print(f"E então {player.char} arremessa a {escolhaAtrair} em direção da galinha.\n" 
                      f"A galinha recebe a {escolhaAtrair} em cheio, olha em direção do {player.char} e começa a correr.\n"
                      f"{player.char} sem saber o que fazer, fica parado igual a uma planta.\n"
                      f"A galinha então o ataca, e bicora um de seu olhos, o arrancando-os fora!")
                evento.dano(player.char, 50, 'ter o olho arrancado')
                sucesso = False

            elif escolhaAcao == 'deixar':
                print(f"E então {player.char} deixa a {escolhaAtrair} perto da galinha.\n" 
                      f"A galinha ignora completamente a {escolhaAtrair}.")
                sucesso = False

            else:
                helpers.erro()

        elif escolhaAtrair == 'mato':

            escolhaAcao = helpers.pergunta(
                'ação',
                [f'{player.char} pode arremessar o {escolhaAtrair} ou deixá-lo perto da galinha.'],
                ['arremessar', 'deixar']
            )

            evento.cabecalho('narrador')
            if escolhaAcao == 'arremessar':
                print(f"E então {player.char} arremessa o {escolhaAtrair} em direção da galinha.\n" 
                      f"O {escolhaAtrair} se desfaz no ar assim que sai de sua mão.")
                sucesso = False

            elif escolhaAcao == 'deixar':
                print(f"E então {player.char} deixa o {escolhaAtrair} perto da galinha.\n" 
                      f"A galinha, curiosa, sobe em cima do {escolhaAtrair} e começa a ciscar.")
                sucesso = True

            else:
                helpers.erro()

        elif escolhaAtrair == 'sair':
            return

        else:
            helpers.erro()
            
        if sucesso:
            evento.cabecalho('narrador')
            print(f"{player.char} consegue afastar a galinha do ninho e o que eram para ser ovos, é na verdade uma caixa trancada")
            escolhaCaixa = helpers.pergunta(
                'ação',
                [f'{player.char} tenta abrir a caixa?'],
                ['abrir', 'sair']
            )

            evento.cabecalho('narrador')
            if escolhaCaixa == 'abrir':
                if lugares_vasculhados['prateleira']['chave_pega']:
                    print(f"{player.char} abre a caixa com a chave que havia encontrado e dentro dela encontra uma Pistola.")
                    evento.adicionar(player.char, 'pistola')
                    lugares_vasculhados['fazenda']['galinheiro']['pistola_pega'] = True
                    return
                print(f"{player.char} não consegue abrir a caixa já que não tem a chave correspondente.")

            elif escolhaCaixa == 'sair':
                print(f"{player.char} decide deixar a caixa lá por agora.")

            else:
                helpers.erro()



