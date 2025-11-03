from colorama import init
init(autoreset=True)

def jogo():
    from .flow import principal

    principal()

jogo()