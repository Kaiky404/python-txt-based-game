from ..assets.colors import C
from ..character import mostrar_mochila
from .. import player
from .evento import cabecalho, erro

class InventoryInterrupt(Exception):
    pass

def retry_on_inventory(func):
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
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'inv':
            mostrar_mochila(player.char)
            return None
        return user_input.lower()
    
def pergunta(escolha_acao_dialogo: str, situação: list, opcoes: list):
    while True:
        cabecalho(escolha_acao_dialogo)
        situação_formatada = ', '.join(situação)
        print(f"você pode ver {situação_formatada}, DIGITE o que você irá fazer.")
        for opcao in opcoes:
            print(f"> '{opcao}'")
        
        escolha = choice(">> ")
        if escolha in opcoes:
            return escolha.strip().lower().replace(' ', '')
        else:
            erro()
            continue
