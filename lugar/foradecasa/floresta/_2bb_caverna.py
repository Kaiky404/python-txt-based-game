from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player

def caverna():
    entrou = False

    while True:
        if not entrou:
            evento.cabecalho('narrador')
            print(f"{player.char} entra na caverna e logo dá de cara com um urso!.\n"
                f"Depois de molhar suas calças, o urso sente o cheiro e vai em sua direção!\n")
            entrou = True

        situação = [f"{player.char} pode tentar"]
        opções = []

        if not LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto']:
            situação.append("lutar contra o urso")
            opções.append("lutar")
            
            situação.append("voltar por onde veio (o urso não vai te deixar sair)")

        else:
            situação.append("o urso já está morto")
            opções.append("sair")
            

        if not LUGARES_VASCULHADOS['floresta']['rio']['caverna']['item_pego'] and LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto']:
            situação.append("pegar a mochila que o urso estava guardando")
            opções.append("mochila")

        else:
            situação.append("você não consegue pegar a mochila por já a ter pego ou porque tem um urso na sua frente")


        escolhaCaverna = helpers.pergunta(
            'escolha',
            situação,
            opções
        )

        if escolhaCaverna == 'lutar' and not LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto']:

            estrategias = [
                'mirar seu ataque no focinho',
                'usar o ambiente ao seu favor',
                'virar as costas e sair correndo'
            ]
            escolhas = [
                'mirar',
                'ambiente',
                'correr'
            ]
            escolhaEstrategia = helpers.pergunta(
            'ação',
            estrategias,
            escolhas
            )

            if escolhaEstrategia == 'mirar':
                if player.get('força') >= 3 and player.get('coragem') >= 3:
                    player.add('força', 1)
                    player.add('coragem', 1)
                    evento.cabecalho('narrador')
                    print(
                        f"Sem hesitar, {player.char} dá um golpe certeiro no focinho do urso com toda a sua força.\n"
                        f"Tamanha era a força, que o urso morreu na hora.")
                    LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto'] = True

                else:
                    evento.cabecalho('narrador')
                    print(
                        f"Se borrando de medo, {player.char} tenta acerta o focinho do urso com a força que tem.\n"
                        f"Desajeitado e sem confiança de que iria conseguir derrubar o bicho, ele erra o ataque.\n"
                        f"E então, o urso que já estava em sua frente lhe dá uma patada.")
                    evento.dano(player.char, 20, 'tomar uma patada do urso')
                    
            elif escolhaEstrategia == 'ambiente':
                if player.get('inteligência') >= 3 and player.get('coragem') >= 3:
                    player.add('inteligência', 1)
                    player.add('coragem', 1)
                    evento.cabecalho('narrador')
                    print(
                        f"Sem hesitar, {player.char} dá um golpe no ponto rachado da parede, fazendo com que um estalactite caia na cabeça do urso.\n"
                        f"A estalactite era pesada o suficiente para que o urso morresse na hora.")
                    LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto'] = True

                else:
                    evento.cabecalho('narrador')
                    print(
                        f"Se borrando de medo, {player.char} tenta pensar em alguma coisa para usar.\n"
                        f"Estúpido e sem confiança de que iria conseguir pensar em algo, ele não faz nada.\n"
                        f"E então, o urso que já estava em sua frente lhe dá uma patada.")
                    evento.dano(player.char, 20, 'tomar uma patada do urso')

            elif escolhaEstrategia == 'correr':
                evento.cabecalho('narrador')
                print(
                    f"Se borrando de medo, {player.char} tenta correr para fora da caverna.\n"
                    f"Mas antes de sair, o urso que já estava em sua frente lhe dá uma patada.")
                evento.dano(player.char, 20, 'tomar uma patada do urso')
            else:
                helpers.erro()

        elif escolhaCaverna == 'mochila' and not LUGARES_VASCULHADOS['floresta']['rio']['caverna']['item_pego'] and LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto']:
            evento.cabecalho('narrador')
            print(f"Com o urso fora de seu caminho, {player.char} pega uma mochila empoirada do chão")
            evento.adicionar(player.char, 'grampo')
            evento.adicionar(player.char, 'revista de sobrevivêncialismo')
            player.add('força', 2)
            player.add('inteligência', 2)
            evento.discartar(player.char, 'revista de sobrevivêncialismo')
            evento.adicionar(player.char, 'gancho de escalada')
            LUGARES_VASCULHADOS['floresta']['rio']['caverna']['item_pego'] = True

        elif escolhaCaverna == 'voltar' and LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto']:
            return

        else:
            helpers.erro()

        if (
            LUGARES_VASCULHADOS['floresta']['rio']['caverna']['item_pego'] and
            LUGARES_VASCULHADOS['floresta']['rio']['caverna']['urso_morto']
            ):
            LUGARES_VASCULHADOS['floresta']['rio']['vasculhado'] = True