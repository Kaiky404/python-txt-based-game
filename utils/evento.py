from ..core import C
from ..assets.data import atributos, mochila, bonus

LAST_LOG_HEAD = None

def cabecalho(type: str):
        global LAST_LOG_HEAD

        if type.upper() != LAST_LOG_HEAD:
            print(f"\n[{type.upper()}]\n")

            LAST_LOG_HEAD = type.upper()

def dano(char, qtd: int, razao: str):
    cabecalho('damage')
    atributos['vida'] -= qtd
    if atributos['vida'] <= 0:
        atributos['vida'] = 0
        print(f"{char} tomou {qtd} de dano por {razao}.")
        print(f"{char} morreu!")
    else:
        print(f"{char} tomou {qtd} de dano por {razao}.")
        print(f"{char} está com {atributos['vida']} de vida.")

def cura(char, qtd, razao):
    cabecalho('heal')
    atributos['vida'] += qtd
    print(f"{char} curou {qtd} vida por {razao}.")
    print(f"{char} está com {atributos['vida']} de vida.")

def adicionar(char, item):
    cabecalho('Item guardado na mochila')
    mochila.append(item)
    print(f"{char} obteve {item}")

def discartar(char, item):
    if item in mochila:
        cabecalho('Item descartado da mochila')
        mochila.remove(item)
        print(f"{char} discartou {item}")
    else:
        print(f"{char} não tem {item} na mochila")

def equipar(char, item):
    if item in bonus:
        cabecalho('Item equipado')
        bonus[item]['equipado'] = True
        bonus_output = "Bônus desse item: \n"

        for key, value in bonus[item].items():
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
            bonus_output += line
        print(f"{char} equipou {item}")
        print(bonus_output)
    else:
        print(f"{char} não tem {item} na mochila.")

def desequipar(char, item, bonus):
    if item in bonus:  
        cabecalho('Item desequipado')
        bonus[item]['equipado'] = False
        bonus_output = "Bônus desse item: \n"

        for key, value in bonus[item].items():
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
            bonus_output += line
        print(f"{char} desequipou {item}")
        print(bonus_output)
    else:
        print(f"'{item}' não tem bônus")

def voltar(local_no_singular: str, plural: bool):
    artigo = {
        "parquinho": "do",
        "estabulo": "do",
        "predio": "do",
        "cama": "da",
        "prateleira": "da",
        "janela": "da"
    }
    d = artigo.get(local_no_singular, "de")

    cabecalho('narrador')
    if plural:
        print(f"Você se afasta {d}s {local_no_singular}s e volta para onde estava.")
    else:
        print(f"Você se afasta {d} {local_no_singular} e volta para onde estava.")

def erro():
    cabecalho('Mensagem de Erro')
    print(f"Escolha inválida! Por favor, digite uma das opções apresentadas.")
