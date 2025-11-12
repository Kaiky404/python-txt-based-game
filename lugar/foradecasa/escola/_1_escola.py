from ....core import evento, helpers, lugares_vasculhados, C
from .... import player
from ._1a_materia import materia

def escola():
    entrou = False
    while True:
        if not entrou:
            evento.cabecalho('narrador')
            print(
                f"{player.char} caminha em direção à escola local, cumprimentando alguns conhecidos pelo caminho.\n"
                "Entrando no perímetro dela na exata hora que o guardinha está fechando o portão\n"
                f"parece que {player.char} só vai poder sair quando participar de todas as aulas\n"
                f"Entrando no edifício, {player.char} não sabe em qual sala entrar. Mas se sentindo confiante nessa matéria, {player.char} decide entrar na aula de..."
                )
            entrou = True

        escolhaMateria = helpers.pergunta(
            'escolha',
            ["Entrar na aula de 'Geografia', 'Física', 'Português', 'História' ou 'Biologia'"],
            ['geografia', 'fisica', 'portugues', 'historia', 'biologia', 'sair']
            )

        if escolhaMateria == 'geografia':
            if lugares_vasculhados['escola']['materia']['geo']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                lugares_vasculhados['escola']['materia']['geo'] = True

        elif escolhaMateria == 'fisica':
            if lugares_vasculhados['escola']['materia']['fis']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                lugares_vasculhados['escola']['materia']['fis'] = True

        elif escolhaMateria == 'portugues':
            if lugares_vasculhados['escola']['materia']['por']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                lugares_vasculhados['escola']['materia']['por'] = True

        elif escolhaMateria == 'historia':
            if lugares_vasculhados['escola']['materia']['his']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                lugares_vasculhados['escola']['materia']['his'] = True

        elif escolhaMateria == 'biologia':
            if lugares_vasculhados['escola']['materia']['bio']:
                print(f"{player.char} já participou da matéria de {escolhaMateria}.")
                continue
            else:
                lugares_vasculhados['escola']['materia']['bio'] = True
        elif escolhaMateria == 'sair':
            # cena com guardinha: opção de sair na porrada, na lábia, ou não conseguir
            pass

        print(f"{player.char}, decidido então a entrar na aula de {escolhaMateria}, pensa que essa é também uma boa oportunidade de descansar um pouco.")
        escolhaEscola = helpers.pergunta('escolha', ['a opção de prestar atenção na aula ou a de descansar'], ['vou estudar', 'vou descansar'])

        if escolhaEscola == 'vouestudar':
            evento.cabecalho('narrador')
            print(f"Pensando no futuro e na necessidade de ficar mais inteligente, {player.char} decide focar no que o professor falando e passando na lousa")
            print(f"30 Minutos se passam e é quase fim da aula, porém, antes do sinal tocar, o professor aponta para uma questão na lousa e manda você responder ela...")
            materia(escolhaMateria)

        elif escolhaEscola == 'voudescansar':
            evento.cura(player.char, 5, 'descansar durante a aula')
            continue
        
        else:
            evento.erro()
            continue
        
        if (
            lugares_vasculhados['escola']['materia']['geo'] and
            lugares_vasculhados['escola']['materia']['fis'] and
            lugares_vasculhados['escola']['materia']['por'] and
            lugares_vasculhados['escola']['materia']['his'] and
            lugares_vasculhados['escola']['materia']['bio']
            ):
            lugares_vasculhados['escola']['completada'] = True
            evento.cabecalho('info')
            print("Depois de passar por todas as aulas da escola, o sinal toca e você pode ir embora.")
            return