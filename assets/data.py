ATRIBUTOS = { 
    "vida": 100,
    "carisma": 0,
    "coragem": 0,
    "intimidacao": 0
}

MOCHILA = []

BONUS_DOS_ITENS = { 
    "mangalonga": {
        "carisma": 0,
        "coragem": 1,
        "intimidacao": 0,
        "corpo": "tronco",
        "equipavel": True,
        "equipado": False
    },
    "regata": {
        "carisma": 0,
        "coragem": 0,
        "intimidacao": 1,
        "corpo": "tronco",
        "equipavel": True,
        "equipado": False
    },
    "blazer": {
        "carisma": 2,
        "coragem": 0,
        "intimidacao": 0,
        "corpo": "tronco",
        "equipavel": True,
        "equipado": False
    },
    "faca": {
        "carisma": 0,
        "coragem": 1,
        "intimidacao": 2,
        "corpo": "mao",
        "equipavel": True,
        "equipado": False
    },
    "grampo": {
        "carisma": 0,
        "coragem": 0,
        "intimidacao": 0,
        "corpo": None,
        "equipavel": True,
        "equipado": False
    },
    "chavecompena": {
        "carisma": 0,
        "coragem": 0,
        "intimidacao": 0,
        "corpo": None,
        "equipavel": True,
        "equipado": False
    },
    "tabua": {
        "carisma": 0,
        "coragem": 1,
        "intimidacao": 1,
        "corpo": "mao",
        "equipavel": True,
        "equipado": False
    }
}

LUGARES_VASCULHADOS = {
    "quarto": {
        "vasculhado": False
    },
    "guardaroupa": {
        "vasculhado": False,
        "portaquebrada": False,
        "regata_pega": False,
        "blazer_pego": False,
        "tabua_pega": False
    },
    "cama": {
        "vasculhada": False,
        "faca_pega": False
    },
    "prateleira": {
        "vasculhada": False,
        "grampo_pego": False,
        "chave_pega": False
    },
    "janela": {
        "vasculhada": False,
        "predio_vasculhado": False,
        "parquinho_vasculhado": False,
        "estabulo_vasculhado": False
    }
}

atributos = ATRIBUTOS.copy()
mochila = MOCHILA.copy()
bonus = BONUS_DOS_ITENS.copy()