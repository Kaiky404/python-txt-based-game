from ....core import evento, LUGARES_VASCULHADOS, helpers, C
from ._2a_predio import predio
from ._2b_parquinho import parquinho
from ._2c_estabulo import estabulo
from .... import player

@helpers.retry_on_inventory
def janela():
    if LUGARES_VASCULHADOS['casa']['janela']['vasculhada']:
        evento.cabecalho('info')
        print("Você já olhou todos os pontos interessantes da janela.")
        return
    
    evento.cabecalho('narrador')
    print("Você se encosta no peitoril da janela")
    while True:
        evento.cabecalho('narrador')
        print(f"Em frente à sua janela, três pontos chamam sua atenção...")
        LookChoice = helpers.pergunta(
            "pergunta",
            [f"Você pode olhar o {C.YELLOW}estábulo{C.NORMAL}, o {C.YELLOW}parquinho enferrujado{C.NORMAL} ou o {C.YELLOW}prédio grande{C.NORMAL}"],
            ["estabulo", "parquinho", "predio", "sair"])

        if LookChoice == "predio":
            predio()

        elif LookChoice == "parquinho":
            parquinho()

        elif LookChoice == "estabulo":
            estabulo()

        elif LookChoice == "sair":
            print(f"Você decide não olhar mais nada.")
            return
        
        else:
            evento.erro()
        
        if (
            LUGARES_VASCULHADOS['casa']['janela']['predio_vasculhado'] and
            LUGARES_VASCULHADOS['casa']['janela']['parquinho_vasculhado'] and
            LUGARES_VASCULHADOS['casa']['janela']['estabulo_vasculhado']
        ):
            LUGARES_VASCULHADOS['casa']['janela']['vasculhada'] = True
            evento.cabecalho('info')
            print("Depois de observar todos os pontos interessantes da janela, você decide se afastar dela.")
            return