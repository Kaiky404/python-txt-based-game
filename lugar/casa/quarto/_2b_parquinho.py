from ....core import evento, helpers, LUGARES_VASCULHADOS, C, skill_check
from .... import player
from .... import visuals

@helpers.retry_on_inventory
def parquinho():
    while True:
        if LUGARES_VASCULHADOS['casa']['janela']['parquinho_vasculhado']:
            evento.cabecalho('info')
            print("Você já olhou para o parquinho enferrujado e viu tudo que havia de interessante.")
            return
        
        evento.cabecalho('narrador')
        print(f"Ao olhar para o parquinho enferrujado, você avista {C.YELLOW}um grupo de crianças está praticando bullying contra uma criança de óculos{C.NORMAL}.")
        
        print(visuals.parquinho_bullying)
        
        escolha = helpers.pergunta(
            "ação",
            ["Você pode tentar intervir ou só ignorar"],
            ["intervir", "ignorar"])

        if escolha == 'intervir':
            LUGARES_VASCULHADOS['casa']['janela']['parquinho_vasculhado'] = True

            evento.cabecalho('narrador')
            print(
                "Você pula da sua janela e corre em direção ao parquinho enferrujado\n"
                "Chegando lá, você tenta impedir as crianças de praticarem bullying com a criança de óculos.")

            if skill_check(player.get('força'), 2):
                print(visuals.parquinho_garoto_salvo)
                print(
                    "Com toda a força que tem, você dá uma lição no grupo de crianças e salva a criança de óculos.\n"
                    "Ela lhe agradeçe e te dá uma revista de quadrinho da Madame Atômo.")
                player.add('inteligência', 1)
            else:
                print(visuals.parquinho_apanhando)
                print("Te faltando força, você não consegue impedir o grupo de crianças e apanha.")
                evento.dano(player.char, 5, 'apanhar de crianças')

            evento.cabecalho('narrador')
            print("Depois disso, você volta pra sua casa.")
            return

        elif escolha == 'ignorar':
            LUGARES_VASCULHADOS['casa']['janela']['parquinho_vasculhado'] = True
            print(visuals.parquinho_bullying)
            evento.cabecalho('narrador')
            print("Você decide ignorar a situação, e o grupo de crianças continuaram a praticar bullying até quebrarem o óculos do garoto.")
            player.add('coragem', -1)
            return
        
        else:
            evento.erro()
            continue
            
                
