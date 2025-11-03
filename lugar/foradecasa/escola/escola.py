from ....core import evento, helpers, lugares_vasculhados, C

def escola():
    while True:
        evento.cabecalho('narrador')
        print("Você caminha em direção à escola local, cumprimentando alguns conhecidos pelo caminho.")
        print("Ao chegar, você se dirige para a sala de aula, onde a aula já está começando.")
        print("Você se senta em sua carteira e dorme durante toda a aula.")

        evento.cabecalho('menssagem do dev')
        print("Em alguma atualização futura, adicionar mais interações na escola. DEADENDLINE")
        return