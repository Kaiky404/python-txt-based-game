from ..core import C
from ..assets.atributos_base import ATRIBUTOS
from ..assets.itens import BONUS_DOS_ITENS, MOCHILA

LAST_LOG_HEAD = None

def cabecalho(type: str):
    """Printa uma espécie de header para separar cada tipo de output"""
    global LAST_LOG_HEAD

    if type.upper() != LAST_LOG_HEAD:
        print(f"\n[{C.MAGENTA}{type.upper()}{C.NORMAL}]\n")

        LAST_LOG_HEAD = type.upper()

def skill_check(tenho, preciso):
    """Checa se o atributo que o personagem tem é o bastante para o que for preciso"""
    if tenho >= preciso:
        return True
    else:
        return False

def dano(char, qtd: int, razao: str):
    """Reduz a vida do personagem com base na quantidade"""
    cabecalho('dano')
    ATRIBUTOS['vida'] -= qtd
    if ATRIBUTOS['vida'] <= 0:
        ATRIBUTOS['vida'] = 0
        print(f"{char} tomou {qtd} de dano por {razao}.")
        print(f"{char} morreu!")
        quit()
    else:
        print(f"{char} tomou {qtd} de dano por {razao}.")
        print(f"{char} está com {ATRIBUTOS['vida']} de vida.")

def cura(char, qtd, razao):
    """Aumenta a vida do personagem com base na quantidade"""
    cabecalho('cura')
    ATRIBUTOS['vida'] += qtd
    if ATRIBUTOS['vida'] >= 100:
        ATRIBUTOS['vida'] = 100
    print(f"{char} curou {qtd} vida por {razao}.")
    print(f"{char} está com {ATRIBUTOS['vida']} de vida.")

def adicionar(char, item):
    """Adiciona um item no dicionário de mochila do personagem"""
    cabecalho('Item guardado na MOCHILA')
    MOCHILA[item] = MOCHILA.get(item, 0) + 1
    print(f"{char} obteve {C.YELLOW}{item}{C.NORMAL}")

def discartar(char, item):
    """Discarta um item no dicionário de mochila do personagem"""
    if item in MOCHILA and MOCHILA[item] > 0:
        MOCHILA[item] -= 1
        if MOCHILA[item] == 0:
            del MOCHILA[item]
        cabecalho('Item descartado da MOCHILA')
        print(f"{char} discartou {C.RED}{item}{C.NORMAL}")
    else:
        print(f"{char} {C.RED}não tem {item}{C.NORMAL} na MOCHILA")

def equipar(char, item):
    """Equipa um item da mochila do personagem"""
    if item in BONUS_DOS_ITENS:
        cabecalho('Item equipado')
        BONUS_DOS_ITENS[item]['equipado'] = True
        BONUS_DOS_ITENS_output = "Bônus desse item: \n"

        for key, value in BONUS_DOS_ITENS[item].items():
            if key in ('equipado', 'equipavel'):
                continue

            line = ""
            if value:
                if isinstance(value, (int, float)):
                    if value > 0:
                        line = f"- {key}: +{value}\n"
                    else:
                        line = f"- {key}: {value}\n"
                elif isinstance(value, str):
                    if key == 'corpo':
                        line = f"- Parte do corpo: {value}"
            BONUS_DOS_ITENS_output += line
        print(f"{char} equipou {item}")
        print(BONUS_DOS_ITENS_output)
    else:
        print(f"{char} não tem {item} na MOCHILA.")

def desequipar(char, item, BONUS_DOS_ITENS):
    """Desequipa um item da mochila do personagem"""
    if item in BONUS_DOS_ITENS:  
        cabecalho('Item desequipado')
        BONUS_DOS_ITENS[item]['equipado'] = False
        BONUS_DOS_ITENS_output = "Bônus desse item: \n"

        for key, value in BONUS_DOS_ITENS[item].items():
            if key in ('equipado', 'equipavel'):
                continue

            line = ""
            if value:
                if isinstance(value, (int, float)):
                    if value > 0:
                        line = f"- {key}: +{value}\n"
                    else:
                        line = f"- {key}: {value}\n"
                elif isinstance(value, str):
                    if key == 'corpo':
                        line = f"- Parte do corpo: {value}"
            BONUS_DOS_ITENS_output += line
        print(f"{char} desequipou {item}")
        print(BONUS_DOS_ITENS_output)
    else:
        print(f"'{item}' não tem bônus")
