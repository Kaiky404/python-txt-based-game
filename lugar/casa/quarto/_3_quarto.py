from ....core import evento, helpers, lugares_vasculhados, C
from ._3a_guardaroupa import guardaroupa
from ._3b_prateleira import prateleira
from ._3c_cama import cama

@helpers.retry_on_inventory
def quarto():
    while True:
        if lugares_vasculhados['casa']['vasculhado']:
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
            return
        
        else:
            evento.erro()

        if (
            lugares_vasculhados['casa']['guardaroupa']['vasculhado'] and
            lugares_vasculhados['casa']['cama']['vasculhada'] and
            lugares_vasculhados['casa']['prateleira']['vasculhada']
            ):
            lugares_vasculhados['casa']['vasculhado'] = True
            evento.cabecalho('info')
            print("Depois de observar todos os pontos interessantes do quarto, você decide fazer outra coisa.")
            return