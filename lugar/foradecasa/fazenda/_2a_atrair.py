from ....core import evento, helpers, C, LUGARES_VASCULHADOS
from .... import player

def atrair():
    entrou = False

    while True:
        sucesso = False
        evento.cabecalho('narrador')

        if not entrou:
            print(f"Decidido a usar o cérebro, {player.char} procura aos arredores algo para distrair a galinha")
            print(f"Depois de alguns minutos, ele reuniu um pedaço de casca de fruta cítrica, uma pedrinha e um punhado de mato.")
            entrou = True

            situação = [f"Para distrair a galinha, {player.char} pode "]
            opção = []

            if not LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['casca']['usado']:
                situação.append(f"usar o pedaço de casca cítrica")
                opção.append("casca")
            else:
                situação.append(f"usar o pedaço de casca cítrica (já fez isso)")

            if not LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['pedra']['usado']:
                situação.append(f"usar a pedrinha")
                opção.append("pedra")
            else:
                situação.append(f"usar a pedrinha (já fez isso)")

            if not LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['mato']['usado']:
                situação.append(f"usar o punhado de mato")
                opção.append("mato")
            else:
                situação.append(f"usar o punhado de mato (já fez isso)")

            situação.append(f"ou ir embora")
            opção.append("sair")

        escolhaAtrair = helpers.pergunta(
            'escolha',
            situação,
            opção
        )

        ações = [f'Você pode arremessar o/a {escolhaAtrair} ou larga-lo/a perto da galinha.']
        opções = ['arremessar', 'largar']

        arremessar = f"E então você arremessa o/a {escolhaAtrair} em direção da galinha.\n"
        largar = f"E então você larga o/a {escolhaAtrair} perto da galinha.\n"

        evento.cabecalho('narrador')
        print(f"{player.char} pega o/a {escolhaAtrair} na mão e pensa se é melhor arremessar ou deixá-lo/a perto da galinha")        
        
        if escolhaAtrair == 'casca' and not LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['casca']['usado']:

            escolhaAcao = helpers.pergunta(
                'ação',
                ações,
                opções
            )

            evento.cabecalho('narrador')
            if escolhaAcao == 'arremessar':
                print(f"{arremessar}\n"
                      f"A galinha cheira a {escolhaAtrair} um pouco e cisca pra longe, meio que espirrando.")
                player.add('força', 1)
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['casca']['arremessado'] = True
                sucesso = True

            elif escolhaAcao == 'largar':
                print(f"{largar}\n"
                      f"A galinha ignora completamente a {escolhaAtrair}.")
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['casca']['largado'] = True

            else:
                helpers.erro()
            
            if (LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['casca']['arremessado'] or
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['casca']['largado']):
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['casca']['usado'] = True

        elif escolhaAtrair == 'pedra' and not LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['pedra']['usado']:

            escolhaAcao = helpers.pergunta(
                'ação',
                ações,
                opções
            )

            evento.cabecalho('narrador')
            if escolhaAcao == 'arremessar':
                print(f"{arremessar}\n"
                      f"A galinha recebe a {escolhaAtrair} em cheio, olha em direção do {player.char} e começa a correr.\n"
                      f"{player.char} sem saber o que fazer, fica parado igual a uma planta.\n"
                      f"A galinha então o ataca, bicando um de seus olhos e arrancando-o fora!")
                player.add('coragem', 1)
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['pedra']['arremessado'] = True
                evento.dano(player.char, 50, 'ter o olho arrancado')

            elif escolhaAcao == 'largar':
                print(f"{largar}\n"
                      f"A galinha ignora completamente a {escolhaAtrair}.")
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['pedra']['largado'] = True

            else:
                helpers.erro()

            if (LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['pedra']['arremessado'] or
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['pedra']['largado']):
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['pedra']['usado'] = True

        elif escolhaAtrair == 'mato' and not LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['mato']['usado']:

            escolhaAcao = helpers.pergunta(
                'ação',
                ações,
                opções
            )

            evento.cabecalho('narrador')
            if escolhaAcao == 'arremessar':
                print(f"{arremessar}\n"
                      f"O {escolhaAtrair} se desfaz no ar assim que sai de sua mão.")
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['mato']['arremessado'] = True

            elif escolhaAcao == 'largar':
                print(f"{largar}\n"
                      f"A galinha, curiosa, sobe em cima do {escolhaAtrair} e começa a ciscar.")
                player.add('inteligência', 1)
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['mato']['largado'] = True
                sucesso = True

            else:
                helpers.erro()

            if (LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['mato']['arremessado'] or
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['mato']['largado']):
                LUGARES_VASCULHADOS['fazenda']['galinheiro']['atrair']['mato']['usado'] = True

        elif escolhaAtrair == 'sair':
            return

        else:
            helpers.erro()
            
        if sucesso:
            evento.cabecalho('narrador')
            print(f"{player.char} consegue afastar a galinha do ninho e o que eram para ser ovos, é na verdade uma caixa trancada")
            LUGARES_VASCULHADOS['fazenda']['galinheiro']['galinha_vazou'] = True
            escolhaCaixa = helpers.pergunta(
                'ação',
                [f'Você tenta abrir a caixa?'],
                ['abrir', 'sair']
            )

            evento.cabecalho('narrador')
            if escolhaCaixa == 'abrir':
                if LUGARES_VASCULHADOS.get('prateleira', {}).get('chave_pega'):
                    print(f"{player.char} abre a caixa com a chave que havia encontrado e dentro dela encontra uma Pistola.")
                    evento.adicionar(player.char, 'pistola')
                    LUGARES_VASCULHADOS['fazenda']['galinheiro']['pistola_pega'] = True
                    return
                print(f"{player.char} não consegue abrir a caixa já que não tem a chave correspondente.")

            elif escolhaCaixa == 'sair':
                print(f"{player.char} decide largar a caixa lá por agora.")

            else:
                helpers.erro()



