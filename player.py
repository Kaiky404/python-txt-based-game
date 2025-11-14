char = None

from .assets.atributos_base import ATRIBUTOS
from . import character

def get(atributo):
    """Pega o valor do atributo atual do personagem"""
    return character.get_total(atributo)

def add(atributo, value):
    """Aumenta o valor base do atributo"""
    ATRIBUTOS[atributo] = ATRIBUTOS.get(atributo, 0) + value
    sinal = '+' if value >= 0 else ''
    print(f"{atributo.capitalize()} {sinal}{value}")
