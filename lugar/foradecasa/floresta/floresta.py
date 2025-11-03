from ....core import evento, helpers, lugares_vasculhados, C

def floresta():
    while True:
        evento.cabecalho('narrador')
        print("Você caminha em direção à floresta próxima, cumprimentando alguns conhecidos pelo caminho.")
        print("Ao chegar, você se aventura entre as árvores, ouvindo os sons da natureza ao seu redor.")
        print("O tempo passa e você derrepente se vê perdido na floresta.")

        evento.cabecalho('menssagem do dev')
        print("Em alguma atualização futura, adicionar mais interações na floresta. DEADENDLINE")
        return