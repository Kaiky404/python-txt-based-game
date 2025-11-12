from ..core import C
from ..assets.atributos_base import ATRIBUTOS
from ..assets.itens import BONUS_DOS_ITENS, MOCHILA

LAST_LOG_HEAD = None

def cabecalho(type: str):
        global LAST_LOG_HEAD

        if type.upper() != LAST_LOG_HEAD:
            print(f"\n[{type.upper()}]\n")

            LAST_LOG_HEAD = type.upper()

def skill_check(tenho, preciso):
    if tenho >= preciso:
        return True
    else:
        return False

def dano(char, qtd: int, razao: str):
    cabecalho('dano')
    ATRIBUTOS['vida'] -= qtd
    if ATRIBUTOS['vida'] <= 0:
        ATRIBUTOS['vida'] = 0
        print(f"{char} tomou {qtd} de dano por {razao}.")
        print(f"{char} morreu!")
    else:
        print(f"{char} tomou {qtd} de dano por {razao}.")
        print(f"{char} está com {ATRIBUTOS['vida']} de vida.")

def cura(char, qtd, razao):
    cabecalho('heal')
    ATRIBUTOS['vida'] += qtd
    print(f"{char} curou {qtd} vida por {razao}.")
    print(f"{char} está com {ATRIBUTOS['vida']} de vida.")

def adicionar(char, item):
    cabecalho('Item guardado na MOCHILA')
    MOCHILA[item] = MOCHILA.get(item, 0) + 1
    print(f"{char} obteve {item}")

def discartar(char, item):
    if item in MOCHILA and MOCHILA[item] > 0:
        MOCHILA[item] -= 1
        if MOCHILA[item] == 0:
            del MOCHILA[item]
        cabecalho('Item descartado da MOCHILA')
        print(f"{char} discartou {item}")
    else:
        print(f"{char} não tem {item} na MOCHILA")

def equipar(char, item):
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
