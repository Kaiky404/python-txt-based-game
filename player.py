char = None

from .assets.data import ATRIBUTOS
from . import character

def get(atributo):
    return character.get_total(atributo)

def add(attr, value):
    """Aumenta o valor base do atributo (não afeta bônus)."""
    ATRIBUTOS[attr] = ATRIBUTOS.get(attr, 0) + value
    print(f"{attr.capitalize()} +{value}")
