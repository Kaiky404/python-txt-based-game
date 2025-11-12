ATRIBUTOS = { 
    "vida": 100,
    "carisma": 0,
    "coragem": 0,
    "inteligência": 0,
    "força": 0
}

MOCHILA = {}

BONUS_DOS_ITENS = {
    "mangalonga": {
        "carisma": 0,
        "coragem": 0,
        "inteligência": 3,
        "força": 0,
        "corpo": "tronco",
        "equipavel": True,
        "equipado": False
    },
    "regata": {
        "carisma": 0,
        "coragem": 3,
        "inteligência": 0,
        "força": 0,
        "corpo": "tronco",
        "equipavel": True,
        "equipado": False
    },
    "blazer": {
        "carisma": 3,
        "coragem": 0,
        "inteligência": 0,
        "força": 0,
        "corpo": "tronco",
        "equipavel": True,
        "equipado": False
    },
    "pistola": {
        "carisma": 0,
        "coragem": 2,
        "inteligência": 0,
        "força": 5,
        "corpo": "mao",
        "equipavel": True,
        "equipado": False 
    },
    "faca": {
        "carisma": 0,
        "coragem": 0,
        "inteligência": 0,
        "força": 3,
        "corpo": "mao",
        "equipavel": True,
        "equipado": False
    },
    "tabua": {
        "carisma": 0,
        "coragem": 0,
        "inteligência": 0,
        "força": 2,
        "corpo": "mao",
        "equipavel": True,
        "equipado": False
    },
    "grampo": {
        "carisma": 0,
        "coragem": 0,
        "inteligência": 0,
        "força": 0,
        "corpo": None,
        "equipavel": True,
        "equipado": False
    },
    "chavecompena": {
        "carisma": 0,
        "coragem": 0,
        "inteligência": 0,
        "força": 0,
        "corpo": None,
        "equipavel": True,
        "equipado": False
    },
    "ganchodeescalada": {
        "carisma": 0,
        "coragem": 0,
        "inteligência": 0,
        "força": 0,
        "corpo": None,
        "equipavel": True,
        "equipado": False
    },
}

LUGARES_VASCULHADOS = {

    "casa": {
        "vasculhado": False,
        "bronca_do_pai": False,
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
        },
    },

    "escola": {
        "completada": False,
        "materia": {
        "feita": False,
        "geo": False,
        "fis": False,
        "por": False,
        "his": False,
        "bio": False,
        },
    },
    
    "fazenda": {
        "vasculhada": False,
        "cerca": {
            "arrumada": False,
            "ajustar": False,
            "trocar": False
        },
        "galinheiro": {
            "vasculhado": False,
            "pistola_pega": False,
            "rabisco_lido": False,
            "galinha_vazou": False,
            "atrair": {
                "casca": {
                    "usado": False,
                    "arremesado": False,
                    "largado": False
                },
                "pedra": {
                    "usado": False,
                    "arremesado": False,
                    "largado": False
                },
                "mato": {
                    "usado": False,
                    "arremesado": False,
                    "largado": False
                },
            }
        },
    },

    "floresta": {
        "vasculhada": False,
        "montanha": {
            "vasculhada": False,
            "caminho": False
        },
        "rio": {
            "vasculhado": False,
            "caverna": {
                "vasculhada": False,
                "urso_morto": False,
                "item_pego": False
            }
        },

    }
}