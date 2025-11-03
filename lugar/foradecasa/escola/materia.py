from ....core import evento, helpers, lugares_vasculhados, C
from .... import player

def materia(materia):
    while True:
        if materia == 'geografia':
            evento.cabecalho('narrador')
            print("Helena, que é a sua professora de geografia, te faz a seguinte pergunta: ")
            respostaMateria = helpers.pergunta(
                'Diálogo',
                ['Helena pergunta: Por que o Sol nasce mais cedo conforme ele viaja para o leste?'],
                ['por causa da curvatura da terra',
                 'por causa da sua composição quimica',
                 'por causa da altitude',
                 'porque o sol gira em torno da terra',
                 'por causa da inclinação do eixo da terra']
                )
            if respostaMateria == 'porcausadacurvaturadaterra':
                evento.cabecalho('narrador')
                print(f"Helena dá um sorriso para {player.char} e diz: Parabéns, {player.char}, é exatamente isso! O sol nasce mais cedo a leste porque a Terra é esférica e a terra viaja de oeste para leste, fazendo com que o pessoal que mora no leste enxergue o sol primeiro.")
                return
            else:
                evento.cabecalho('narrador')
                print(f"Helena olha para {player.char} com desdém e diz: Claro que não {player.char}! O sol nasce mais cedo a leste porque a Terra é esférica e a terra viaja de oeste para leste, fazendo com que o pessoal que mora no leste enxergue o sol primeiro.")
                return




        elif materia == 'fisica':
            evento.cabecalho('narrador')
            print("Gustav, que é seu professor de física, te faz a seguinte pergunta: ")
            respostaMateria = helpers.pergunta(
                'Diálogo',
                ['Gustav pergunta: Por que a temperatura diminui conforme alguém sobe a montanha?'],
                ['porque a terra e plana',
                 'por causa da altitude',
                 'por causa da gravidade',
                 'porque o sol está mais distante',
                 'por causa da sua composição quimica']
                )
            if respostaMateria == 'porcausadaaltitude':
                evento.cabecalho('narrador')
                print(f"Helena dá um sorriso para {player.char} e diz: Parabéns, {player.char}, é exatamente isso! A temperatura diminui com a altitude porque o ar fica menos denso e tem menor capacidade de reter calor — o calor vem mais do chão aquecido do que do ar em si.")
                return
            else:
                evento.cabecalho('narrador')
                print(f"Helena olha para {player.char} com desdém e diz: Claro que não {player.char}! O sol nasce mais cedo a leste porque a Terra é esférica e a terra viaja de oeste para leste, fazendo com que o pessoal que mora no leste enxergue o sol primeiro.")
                return




        elif materia == 'portugues':
            evento.cabecalho('narrador')
            print("Clarice, que é a sua professora de português, te faz a seguinte pergunta: ")
            respostaMateria = helpers.pergunta(
                'Diálogo',
                ['Clarice pergunta: Se numa conversa e alguém diz:\n    “O ser humano evoluiu tanto, mas ainda tropeça nas próprias palavras.”\nQual é a figura de linguagem usada na parte “tropeça nas próprias palavras”?'],
                ['hiperbole',
                 'ironia',
                 'metonimia',
                 'metafora',
                 'mitologia']
                )
            if respostaMateria == 'metafora':
                evento.cabecalho('narrador')
                print(f"Helena dá um sorriso para {player.char} e diz: Parabéns, {player.char}, é exatamente isso! É uma metáfora, sim! Usar “tropeçar” no sentido figurado pra “errar ao falar”.")
                return
            else:
                evento.cabecalho('narrador')
                print(f"Helena olha para {player.char} com desdém e diz: Claro que não {player.char}! O sol nasce mais cedo a leste porque a Terra é esférica e a terra viaja de oeste para leste, fazendo com que o pessoal que mora no leste enxergue o sol primeiro.")
                return




        elif materia == 'historia':
            evento.cabecalho('narrador')
            print("Artur, que é seu professor de história, te faz a seguinte pergunta: ")
            respostaMateria = helpers.pergunta(
                'Diálogo',
                ['Artur pergunta: Em qual período histórico começaram a surgir as primeiras escolas formais parecidas com as de hoje?'],
                ['idade media',
                 'egito',
                 'renascimento',
                 'antiguidade classica',
                 'pre historica']
                )
            if respostaMateria == 'idademedia':
                evento.cabecalho('narrador')
                print(f"Helena dá um sorriso para {player.char} e diz: Parabéns, {player.char}, é exatamente isso! As escolas com professores, alunos e ensino organizado começaram mesmo a se formar na Idade Média, principalmente ligadas à Igreja Católica (as escolas monásticas e depois as universidades medievais).")
                return
            else:
                evento.cabecalho('narrador')
                print(f"Helena olha para {player.char} com desdém e diz: Claro que não {player.char}! O sol nasce mais cedo a leste porque a Terra é esférica e a terra viaja de oeste para leste, fazendo com que o pessoal que mora no leste enxergue o sol primeiro.")
                return




        elif materia == 'biologia':
            evento.cabecalho('narrador')
            print("Marina, que é a sua professora de biologia, te faz a seguinte pergunta: ")
            respostaMateria = helpers.pergunta(
                'Diálogo',
                ['Marina pergunta: Que característica biológica diferencia o ser humano dos outros animais e permite desenvolver linguagem e pensamento abstrato?'],
                ['bipedismo',
                 'escamas',
                 'o cóccix',
                 'desenvolvimento do cerebro',
                 'focinho alongado']
                )
            if respostaMateria == 'desenvolvimentodocerebro':
                evento.cabecalho('narrador')
                print(f"Helena dá um sorriso para {player.char} e diz: Parabéns, {player.char}, é exatamente isso! A principal característica que permite linguagem e pensamento é o desenvolvimento do cérebro (córtex cerebral altamente desenvolvido).")
                return
            else:
                evento.cabecalho('narrador')
                print(f"Helena olha para {player.char} com desdém e diz: Claro que não {player.char}! O sol nasce mais cedo a leste porque a Terra é esférica e a terra viaja de oeste para leste, fazendo com que o pessoal que mora no leste enxergue o sol primeiro.")
                return
        
        else:
            helpers.erro()