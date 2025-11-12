from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player
from ._1a_materia import materia

def escola():
    entrou = False
    while True:
        if not entrou:
            evento.cabecalho('narrador')
            print(
                f"Você caminha em direção à escola local, cumprimentando alguns conhecidos pelo caminho.\n"
                "Entrando no perímetro dela na exata hora que o guardinha está fechando o portão\n"
                f"parece que você só vai poder sair quando participar de todas as aulas\n"
                f"Entrando no edifício, você não sabe em qual sala entrar. Mas se sentindo confiante nessa matéria, decide entrar na aula de...")
            entrou = True

        escolhaMateria = helpers.pergunta(
            'escolha',
            ["Entrar na aula de 'Geografia', 'Física', 'Português', 'História' ou 'Biologia'"],
            ['geografia', 'fisica', 'portugues', 'historia', 'biologia', 'sair']
            )

        if escolhaMateria == 'geografia':
            if LUGARES_VASCULHADOS['escola']['materia']['geo']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                LUGARES_VASCULHADOS['escola']['materia']['geo'] = True

        elif escolhaMateria == 'fisica':
            if LUGARES_VASCULHADOS['escola']['materia']['fis']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                LUGARES_VASCULHADOS['escola']['materia']['fis'] = True

        elif escolhaMateria == 'portugues':
            if LUGARES_VASCULHADOS['escola']['materia']['por']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                LUGARES_VASCULHADOS['escola']['materia']['por'] = True

        elif escolhaMateria == 'historia':
            if LUGARES_VASCULHADOS['escola']['materia']['his']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                LUGARES_VASCULHADOS['escola']['materia']['his'] = True

        elif escolhaMateria == 'biologia':
            if LUGARES_VASCULHADOS['escola']['materia']['bio']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                LUGARES_VASCULHADOS['escola']['materia']['bio'] = True
        elif escolhaMateria == 'sair':
            # cena com guardinha: opção de sair na porrada, na lábia, ou não conseguir
            pass

        print(f"Decidido então a entrar na aula de {escolhaMateria}, pensa que essa é também uma boa oportunidade de descansar um pouco.")
        escolhaEscola = helpers.pergunta('escolha', ['a opção de prestar atenção na aula ou a de descansar'], ['vou estudar', 'vou descansar'])

        if escolhaEscola == 'vouestudar':
            evento.cabecalho('narrador')
            print(f"Pensando no futuro e na necessidade de ficar mais inteligente, Você decide focar no que o professor falando e passando na lousa")
            print(f"30 Minutos se passam e é quase fim da aula, porém, antes do sinal tocar, o professor aponta para uma questão na lousa e manda você responder ela...")
            materia(escolhaMateria)

        elif escolhaEscola == 'voudescansar':
            evento.cura(player.char, 5, 'descansar durante a aula')
            continue
        
        else:
            evento.erro()
            continue
        
        if (
            LUGARES_VASCULHADOS['escola']['materia']['geo'] and
            LUGARES_VASCULHADOS['escola']['materia']['fis'] and
            LUGARES_VASCULHADOS['escola']['materia']['por'] and
            LUGARES_VASCULHADOS['escola']['materia']['his'] and
            LUGARES_VASCULHADOS['escola']['materia']['bio']
            ):
            LUGARES_VASCULHADOS['escola']['completada'] = True
            evento.cabecalho('info')
            print("Depois de passar por todas as aulas da escola, o sinal toca e você pode ir embora.")
            return