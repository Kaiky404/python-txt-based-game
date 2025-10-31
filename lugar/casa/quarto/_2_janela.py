from ....core import game_logs, visited_places, helpers, C
from ._2a_predio import predio
from ._2b_parquinho import parquinho
from ._2c_estabulo import estabulo

@helpers.retry_on_inventory
def janela():
    if visited_places['window']['visited']:
        game_logs.head('info')
        print("Você já olhou todos os pontos interessantes da janela.")
        return
    
    game_logs.head('narrador')
    print("Você se encosta no peitoril da janela")
    while True:
        game_logs.head('narrador')
        print(f"Em frente à sua janela, três pontos chamam sua atenção...")
        LookChoice = helpers.pergunta("pergunta", [f"um {C.YELLOW}estábulo{C.NORMAL}, um {C.YELLOW}parquinho enferrujado{C.NORMAL} e um {C.YELLOW}prédio grande{C.NORMAL}"], ["estabulo","parquinho","predio","voltar"])

        if LookChoice == "predio":
            predio()

        elif LookChoice == "parquinho":
            parquinho()

        elif LookChoice == "estabulo":
            estabulo()

        elif LookChoice == "voltar":
            game_logs.voltar('janela', True)
            return
        
        else:
            game_logs.erro()
        
        if (
            visited_places['window']['big_building_seen'] and
            visited_places['window']['rusty_playground_seen'] and
            visited_places['window']['stable_seen']
        ):
            visited_places['window']['visited'] = True
            game_logs.head('info')
            print("Depois de observar todos os pontos interessantes da janela, você decide se afastar dela.")
            return