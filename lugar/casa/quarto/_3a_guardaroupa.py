from ....core import evento, helpers, LUGARES_VASCULHADOS, C
from .... import player

@helpers.retry_on_inventory
def guardaroupa():
    if LUGARES_VASCULHADOS['casa']['guardaroupa']['vasculhado']:
        evento.cabecalho('info')
        print("Você já procurou no guarda-roupa e encontrou tudo que havia de interessante.")
        return

    while True:
        evento.cabecalho('narrador')
        print("Você está em frente ao seu guarda-roupa")
        escolhaGuardaroupa = helpers.pergunta('ação', ['Uma forma de abrir a porta'], ['abrir porta', 'voltar'])

        if escolhaGuardaroupa == "abrirporta":
            if LUGARES_VASCULHADOS['casa']['guardaroupa']['portaquebrada']:
                evento.cabecalho('narrador')
                print(f"Você desvia do que era a porta do guarda-roupa, mas agora é uma {C.YELLOW}pilha de madeira{C.NORMAL}, e olha para dentro dele.")

            else:
                LUGARES_VASCULHADOS['casa']['guardaroupa']['portaquebrada'] = True
                evento.cabecalho('narrador')
                print(f"Você força a porta do guarda-roupa, quebra ela em uma {C.YELLOW}pilha de madeira{C.NORMAL}, mas o abre.")
            print(f"Dentro do guarda-roupa há uma {C.YELLOW}coleção de roupas velhas e empoeiradas{C.NORMAL}.")

            while True:
                if (
                    LUGARES_VASCULHADOS['casa']['guardaroupa']['regata_pega'] and
                    LUGARES_VASCULHADOS['casa']['guardaroupa']['blazer_pego'] and
                    LUGARES_VASCULHADOS['casa']['guardaroupa']['tabua_pega']
                    ):
                    LUGARES_VASCULHADOS['casa']['guardaroupa']['vasculhado'] = True
                    evento.cabecalho('info')
                    print("Você já pegou todas as roupas interessantes do guarda-roupa e já vasculhou a pilha de madeira.")
                    return
                
                escolhaRoupa = helpers.pergunta(
                    'pergunta',
                    ['No guarda-roupa tem algumas roupas que você pode pegar'],
                    ['regata', 'blazer', 'tabua', 'voltar'] )

                if escolhaRoupa == "regata":
                    if LUGARES_VASCULHADOS['casa']['guardaroupa']['regata_pega']:
                        evento.cabecalho('info')
                        print("Você já pegou a regata do guarda-roupa.")
                        return
                    
                    LUGARES_VASCULHADOS['casa']['guardaroupa']['regata_pega'] = True
                    evento.adicionar(player.char, "regata")
                    return
                
                elif escolhaRoupa == "blazer":
                    if LUGARES_VASCULHADOS['casa']['guardaroupa']['blazer_pego']:
                        evento.cabecalho('info')
                        print("Você já pegou o blazer do guarda-roupa.")
                        return
                    
                    LUGARES_VASCULHADOS['casa']['guardaroupa']['blazer_pego'] = True
                    evento.adicionar(player.char, "blazer")
                    return
                
                elif escolhaRoupa == "tabua":
                    if LUGARES_VASCULHADOS['casa']['guardaroupa']['tabua_pega']:
                        evento.cabecalho('info')
                        print("Você já pegou a tabua da pilha de madeira do guarda-roupa.")
                        return

                    LUGARES_VASCULHADOS['casa']['guardaroupa']['tabua_pega'] = True
                    evento.adicionar(player.char, "tabua")
                    return

                elif escolhaRoupa == "voltar":
                    evento.cabecalho('narrador')
                    print("Você saiu do guarda-roupa sem pegar nenhuma roupa.")
                    return
                
                else:
                    helpers.erro

        elif escolhaGuardaroupa == "voltar":
            evento.cabecalho('narrador')
            print("Você decide deixar o guarda-roupa sozinho por enquanto.")
            return
        
        else:
            helpers.erro