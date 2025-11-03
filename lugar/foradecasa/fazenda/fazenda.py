from ....core import evento, helpers, lugares_vasculhados, C

def fazenda():
    while True:
        evento.cabecalho('narrador')
        print("Você caminha em direção ao mercado local, cumprimentando alguns conhecidos pelo caminho.")
        print("Ao chegar, você vê várias barracas vendendo frutas, legumes e outros produtos.")
        print("Você decide comprar alguns mantimentos para a casa antes de voltar.")

        evento.cabecalho('menssagem do dev')
        print("Em alguma atualização futura, adicionar mais interações no mercado. DEADENDLINE")
        return