from ....core import evento, lugares_vasculhados, helpers, C
from ._2a_predio import predio
from ._2b_parquinho import parquinho
from ._2c_estabulo import estabulo

@helpers.retry_on_inventory
def janela():
    if lugares_vasculhados['casa']['janela']['vasculhada']:
        evento.cabecalho('info')
        print("Você já olhou todos os pontos interessantes da janela.")
        return
    
    evento.cabecalho('narrador')
    print("Você se encosta no peitoril da janela")
    while True:
        evento.cabecalho('narrador')
        print(f"Em frente à sua janela, três pontos chamam sua atenção...")
        LookChoice = helpers.pergunta("pergunta", [f"um {C.YELLOW}estábulo{C.NORMAL}, um {C.YELLOW}parquinho enferrujado{C.NORMAL} e um {C.YELLOW}prédio grande{C.NORMAL}"], ["estabulo","parquinho","predio","voltar"])

        if LookChoice == "predio":
            predio()

        elif LookChoice == "parquinho":
            parquinho()

        elif LookChoice == "estabulo":
            estabulo()

        elif LookChoice == "voltar":
            evento.voltar('janela', True)
            return
        
        else:
            evento.erro()
        
        if (
            lugares_vasculhados['casa']['janela']['predio_vasculhado'] and
            lugares_vasculhados['casa']['janela']['parquinho_vasculhado'] and
            lugares_vasculhados['casa']['janela']['estabulo_vasculhado']
        ):
            lugares_vasculhados['casa']['janela']['vasculhada'] = True
            evento.cabecalho('info')
            print("Depois de observar todos os pontos interessantes da janela, você decide se afastar dela.")
            return