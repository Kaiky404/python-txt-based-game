from .core import C, helpers, evento, set_char
from .utils.helpers import retry_on_inventory
from .lugar.core import janela, quarto, escada
from . import player
from .visuals import jose, maria, char

#GAME FLOW
@retry_on_inventory
def principal():
    evento.cabecalho('menssagem do dev')
    print(F"{C.BLUE}Seja bem-vindo à beta de The Village")
    print(F"{C.BLUE}Este é um jogo de aventura em texto onde suas escolhas moldam a história.")

    evento.cabecalho('pergunta')
    set_char()

    evento.cabecalho('narrador')
    print(f"Você é {C.MAGENTA}{player.char}{C.NORMAL}, um jovem de 19 anos que vive em um {C.YELLOW}vilarejo conectado ao mundo exterior por um cruzamento famoso.")
    print(F"Seus pais são os fazendeiros locais, {C.YELLOW}José {C.NORMAL}e {C.YELLOW}Maria{C.NORMAL}. Eles são {C.YELLOW}filhos dos fundadores do vilarejo{C.NORMAL}. Você não tem nenhum outro parente.")
    print(jose, maria, char)
    print("Você acorda em sua cama, o sol está aparecendo em sua janela. E com isso, o som dos estudantes passando pela sua casa")
    print(f"No seu criado mudo você vê sua {C.YELLOW}camisa favorita{C.NORMAL}")
    evento.adicionar(player.char, "mangalonga")
    while True:
        escolhaPrincipal = helpers.pergunta('escolha', ['lugares interessantes no seu quarto'], ['descer escadas', 'olhar janela', 'olhar quarto'])

        if escolhaPrincipal is None:
            continue

        if escolhaPrincipal == "descerescadas":
            escada()
            pass

        elif escolhaPrincipal == "olharjanela":
            janela()
            pass

        elif escolhaPrincipal == "olharquarto":
            quarto()
            pass

        else:
            helpers.erro()

principal()