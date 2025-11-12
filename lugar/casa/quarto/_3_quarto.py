from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from ._3a_guardaroupa import guardaroupa
from ._3b_prateleira import prateleira
from ._3c_cama import cama

@helpers.retry_on_inventory
def quarto():
    while True:
        if LUGARES_VASCULHADOS['casa']['vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou tudo do seu quarto e encontrou tudo que havia de interessante nele.")
            return

        evento.cabecalho('narrador')
        print("Enquanto você olha ao redor do seu quarto...")
        escolhaQuarto = helpers.pergunta(
            "escolha",
            [f"um {C.YELLOW}guarda-roupa{C.NORMAL}, {C.YELLOW}algumas prateleiras{C.NORMAL} e {C.YELLOW}debaixo da sua cama{C.NORMAL}."],
            ["guardaroupa", "cama", "prateleira", "voltar"])

        if escolhaQuarto == "guardaroupa":
            guardaroupa()

        elif escolhaQuarto == "prateleira":
            prateleira()

        elif escolhaQuarto == "cama":
            cama()

        elif escolhaQuarto == "voltar":
            print(f"Você decide não olhar mais nada.")
            return
        
        else:
            evento.erro()

        if (
            LUGARES_VASCULHADOS['casa']['guardaroupa']['vasculhado'] and
            LUGARES_VASCULHADOS['casa']['cama']['vasculhada'] and
            LUGARES_VASCULHADOS['casa']['prateleira']['vasculhada']
            ):
            LUGARES_VASCULHADOS['casa']['vasculhado'] = True
            evento.cabecalho('info')
            print("Depois de observar todos os pontos interessantes do quarto, você decide fazer outra coisa.")
            return