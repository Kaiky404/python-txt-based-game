from ..assets.colors import C
from ..character import mostrar_mochila
from .. import player
from .evento import cabecalho

class InventoryInterrupt(Exception):
    pass

def retry_on_inventory(func):
    """Envelopa a função em wrapper para suportar a interrupção de abrir o inventário"""
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except InventoryInterrupt:
                return
    return wrapper

def choice(prompt):
    """Permite que, durante escolhas, escrever 'inv' ou 'quit', opções fora do esperado"""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'inv':
            mostrar_mochila(player.char)
            return None
        elif user_input.lower() == 'quit':
            quit()
        return user_input.lower()
    
def pergunta(tipo: str, situação: list, opcoes: list):
    """Separa e printa as escolhas por tipo, situação e suas opções de escolha"""
    while True:
        cabecalho(tipo)
        situação_formatada = ', '.join(situação)
        print(f"{situação_formatada}")
        print(f"\nDIGITE o que você irá fazer.")
        for opcao in opcoes:
            print(f"> '{opcao}'")
    
        escolha = choice(f"{C.MAGENTA}>>{C.NORMAL} ")
        if escolha in opcoes:  
            print("\n")
            return escolha.strip().lower().replace(' ', '')

        else:
            print(f"{C.RED}tente novamente{C.NORMAL}\n")
            continue