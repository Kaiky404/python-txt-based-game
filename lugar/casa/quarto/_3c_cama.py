from ....core import evento, helpers, lugares_vasculhados, C
from .... import player

@helpers.retry_on_inventory
def cama():
    if lugares_vasculhados['cama']['vasculhada']:
        evento.cabecalho('info')
        print("Você já vasculhou debaixo da cama e não encontrou nada.")
        return
    
    while True:
        evento.cabecalho('narrador')
        print(F"Quando você move o pescoço para ver debaixo da cama, {C.RED}seu pescoço dói{C.NORMAL}. Passando a mão sobre ele, {C.RED}você nota um hematoma{C.NORMAL}. Tocar nele faz a dor piorar.")
        
        escolhaCama = helpers.pergunta('escolha', ['debaixo da cama'], ['olhar debaixo', 'nao olhar'])

        if escolhaCama == "olhardebaixo":
            evento.cabecalho('narrador')
            print("Quando você move a cabeça para ver debaixo da cama, seu pescoço dói, mas você ignora.")

            evento.dano(player.char, 10, "forçar o pescoço apesar da dor")

            evento.cabecalho('narrador')
            print(f"Lá, embaixo do seu colchão, {C.YELLOW}você nota algo escuro{C.NORMAL}.")

            while True:
                escolhaCoisaescura = helpers.pergunta('pergunta', ['algo escuro'], ['esticar pescoco', 'desistir da coisa'])

                if escolhaCoisaescura == "esticarpescoco":
                    evento.cabecalho('narrador')
                    print("Quando você move a cabeça mais perto, seu pescoço dói mais.")

                    evento.dano(player.char, 20, "forçar o pescoço novamente apesar da dor")

                    evento.cabecalho('narrador')
                    print(f"Mas então, você descobre que a coisa escura era uma {C.YELLOW}faca enferrujada e ensanguentada{C.NORMAL}.")

                    evento.adicionar(player.char, "faca")
                    lugares_vasculhados['cama']['faca_pega'] = True

                    evento.cabecalho('narrador')
                    print("Você pega a faca e deixa o fundo de sua cama.")

                    lugares_vasculhados['cama']['visited'] = True 
                    return

                elif escolhaCoisaescura == "desistirdacoisa":
                    evento.cabecalho('narrador')
                    print("Você decide que a dor não vale a pena e retira a cabeça.")
                    return
                
                else:
                    helpers.erro()

        elif escolhaCama == "naoolhar":
            evento.cabecalho('narrador')
            print("Você decide que a dor não vale a pena e se deita novamente.")
            return

        else:
            helpers.erro()