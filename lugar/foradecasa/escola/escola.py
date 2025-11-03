from ....core import evento, helpers, lugares_vasculhados, C
from .... import player
from .materia import materia

def escola():
    while True:
        evento.cabecalho('narrador')
        print(f"{player.char} caminha em direção à escola local, cumprimentando alguns conhecidos pelo caminho.")
        print(f"Ao chegar, {player.char} não sabe em qual sala entrar. Mas se sentindo confiante nessa matéria, {player.char} decide entrar na aula de...")

        escolhaMateria = helpers.pergunta('escolha',
         ["a opção de começar por 'Geografia', 'Física', 'Português', 'História' ou 'Biologia'"], ['geografia', 'fisica', 'portugues', 'historia', 'biologia'])

        if escolhaMateria == 'geografia':
            lugares_vasculhados['materia']['geo'] = True

        elif escolhaMateria == 'fisica':
            lugares_vasculhados['materia']['fis'] = True

        elif escolhaMateria == 'portugues':
            lugares_vasculhados['materia']['por'] = True

        elif escolhaMateria == 'historia':
            lugares_vasculhados['materia']['his'] = True

        elif escolhaMateria == 'biologia':
            lugares_vasculhados['materia']['bio'] = True

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
            lugares_vasculhados['materia']['geo'] and
            lugares_vasculhados['materia']['fis'] and
            lugares_vasculhados['materia']['por'] and
            lugares_vasculhados['materia']['his'] and
            lugares_vasculhados['materia']['bio']
            ):
            lugares_vasculhados['materia']['feita'] = True
            evento.head('info')
            print("Depois de passar por todas as aulas da escola, o sinal toca e você pode ir embora.")
            return
            