from .core import C
from .assets.atributos_base import ATRIBUTOS
from .assets.itens import BONUS_DOS_ITENS, MOCHILA
from .utils.evento import cabecalho
from . import player

def set_char():
    player.char = input(f"{C.MAGENTA}Primeiro de tudo, qual o seu primeiro nome? {C.NORMAL}").lower().capitalize()

def calc_bonus(stat_name=None):
    if stat_name:
        total_bonus = 0
        for item, info in MOCHILA.items():
            if item in BONUS_DOS_ITENS and BONUS_DOS_ITENS[item].get("equipado", False):
                total_bonus += BONUS_DOS_ITENS[item].get(stat_name, 0)
        return total_bonus

    total = {attr: 0 for attr in ATRIBUTOS}
    for item, info in MOCHILA.items():
        if item in BONUS_DOS_ITENS and BONUS_DOS_ITENS[item].get("equipado", False):
            for attr in ATRIBUTOS:
                total[attr] += BONUS_DOS_ITENS[item].get(attr, 0)
    return total



def get_total(stat_name):
    base = ATRIBUTOS.get(stat_name, 0)
    BONUS_DOS_ITENS = calc_bonus(stat_name)
    return base + BONUS_DOS_ITENS

def estado(value):
    if value > 0:
        return C.GREEN
    elif value < 0:
        return C.RED
    else:
        return C.NORMAL

def vida_estado(value):
    if value > 75:
        return C.GREEN
    elif value > 50:
        return C.YELLOW
    else:
        return C.RED

def mostrar_atributos(char):
    cabecalho(f"ATRIBUTOS de {char}")
    todos_os_bonus = calc_bonus()
    for atributo in ATRIBUTOS:
        atributo_val = ATRIBUTOS[atributo]
        atributo_bonus = todos_os_bonus.get(atributo, 0)
        atributo_agora = atributo_val + atributo_bonus
        if atributo != 'vida':
            color = estado(atributo_agora)
            print(f"{atributo}: {color}{atributo_agora}{C.NORMAL}")
        else:
            color = vida_estado(atributo_agora)
            print(f"{atributo}: {color}{atributo_agora}{C.NORMAL}")

def mostrar_mochila(char):
    while True:
        mostrar_atributos(player.char)
        cabecalho(f"MOCHILA de {char}")
        print('DIGITE para acessar as funcionalidades de MOCHILA')
        print("> 'itens gerais'")
        print("> 'itens equipaveis'")
        print("> 'sair'")
        inv_choice = input(">> ").strip().lower().replace(" ", "")

        if inv_choice == "sair":
            return

        elif inv_choice == "itensgerais":
            itens_gerais = [item for item in MOCHILA if not BONUS_DOS_ITENS.get(item, {}).get('equipavel', False)]

            if itens_gerais:
                print("Seus itens gerais:")
                for item in itens_gerais:
                    quantidade = MOCHILA[item]
                    print(f" - {item} (x{quantidade})")
            else:
                print("Você não tem itens gerais.")

        elif inv_choice == "itensequipaveis":
            itens_equipaveis = [item for item in MOCHILA if BONUS_DOS_ITENS.get(item, {}).get('equipavel', False)]

            if itens_equipaveis:
                print("Seus itens equipavais:")
                for item in itens_equipaveis:
                    quantidade = MOCHILA[item]
                    equipado = BONUS_DOS_ITENS[item].get('equipado', False)
                    tag_equipado = f"{C.GREEN} (Equipped){C.NORMAL}" if equipado else ""
                    print(f" - {item} (x{quantidade}){tag_equipado}")

                print("Para equipar um item, digite seu nome")
                print("Pare desequipar um item, digite 'desequipar PARTE DO CORPO' (ex: 'desequipar tronco').")
                print("Digite 'esquece' para voltar para o menu")
                escolhaEquipar = input(">> ").strip().lower()
                if escolhaEquipar.lower() == 'esquece':
                    continue

                if escolhaEquipar.lower().startswith("desequipar"):
                    parte = escolhaEquipar.split()
                    if len(parte) == 2:
                        corpo = parte[1].lower()
                        achado = False
                        for item_name in itens_equipaveis:
                            if BONUS_DOS_ITENS[item_name]['corpo'].lower() == corpo:
                                BONUS_DOS_ITENS[item_name]['equipado'] = False
                                achado = True
                        if achado:
                            print(f"Todos os itens de {corpo} estão desequipados.")
                        else:
                            print(f"{C.RED}Sem itens equipados em {corpo}.{C.NORMAL}")
                    else:
                        print(f"{C.RED}Formatação inválida, tente dessa forma: 'desequipar <parte do corpo>'.{C.NORMAL}")
                    continue

                nome_item_equipado = next(
                    (item_name for item_name in itens_equipaveis if item_name.lower() == escolhaEquipar.lower()),
                    None
                )

                if nome_item_equipado:
                    corpo = BONUS_DOS_ITENS[nome_item_equipado]['corpo']
                    for item_name in itens_equipaveis:
                        if BONUS_DOS_ITENS[item_name]['corpo'] == corpo:
                            BONUS_DOS_ITENS[item_name]['equipado'] = False

                    BONUS_DOS_ITENS[nome_item_equipado]['equipado'] = True
                    print(f"Você equipou o item {nome_item_equipado}.")
                else:
                    print(f"{C.RED}Item não encontrado, ou você digitou errado.{C.NORMAL}")
            else:
                print("Você não tem itens equipáveis")

        else:
            print(f"Tente novamente.")