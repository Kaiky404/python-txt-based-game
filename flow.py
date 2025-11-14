from .core import C, helpers, evento, set_char
from .utils.helpers import retry_on_inventory
from .lugar.core import janela, quarto
from .lugar.casa.quarto._1_escada import escada
from . import player
from . import visuals

#GAME FLOW
@retry_on_inventory
def principal():
    evento.cabecalho('menssagem do dev')
    print(F"{C.BLUE}Seja bem-vindo à beta de The Village")
    print(visuals.introdução)
    print(visuals.teste)
    print(F"{C.BLUE}Este é um jogo de aventura em texto onde suas escolhas moldam a história\n")
    print(f"Para acessar o seu inventário digite {C.YELLOW}'inv'{C.NORMAL} e para sair do jogo digite {C.YELLOW}'quit'{C.NORMAL}")

    evento.cabecalho('pergunta')
    set_char()

    evento.cabecalho('narrador')
    print(f"Você é {C.MAGENTA}{player.char}{C.NORMAL}")
    print(visuals.char)
    print(f"Um jovem de 19 anos que vive em um {C.YELLOW}vilarejo conectado ao mundo exterior por um cruzamento famoso{C.NORMAL}.")
    print(f"Seus pais são os fazendeiros locais, {C.YELLOW}José {C.NORMAL}e {C.YELLOW}Maria{C.NORMAL}.")
    print(visuals.joseEmaria)
    print(f"Eles são {C.YELLOW}filhos dos fundadores do vilarejo{C.NORMAL}. Você não tem nenhum outro parente.")
    print("Você acorda em sua cama, o sol está aparecendo em sua janela. E com isso, o som dos estudantes passando pela sua casa")
    print(f"Do seu criado mudo você pega sua {C.YELLOW}camisa favorita{C.NORMAL}")
    evento.adicionar(player.char, "mangalonga")
    while True:
        escolhaPrincipal = helpers.pergunta(
            'escolha',
            [F'Você tem lugares interessantes no seu quarto, nele você pode olhar a {C.YELLOW}janela{C.NORMAL}, olhar o {C.YELLOW}quarto{C.NORMAL} ou descer a {C.YELLOW}escada{C.NORMAL}'],
            ['janela', 'quarto', 'escada'])

        if escolhaPrincipal is None:
            continue

        elif escolhaPrincipal == "janela":
            janela()

        elif escolhaPrincipal == "quarto":
            quarto()

        elif escolhaPrincipal == "escada":
            escada()

        else:
            print("tente novamente")

principal()