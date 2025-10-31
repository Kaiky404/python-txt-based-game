from .core import C, helpers, game_logs, visited_places, display_stats, set_char
from .utils.helpers import retry_on_inventory
from . import player
from .visuals import jose, maria, char

#GAME FLOW
@retry_on_inventory
def main_choice_loop():
    game_logs.head('menssagem do dev')
    print(F"{C.BLUE}Seja bem-vindo à beta de The Village")
    print(F"{C.BLUE}Este é um jogo de aventura em texto onde suas escolhas moldam a história.")

    game_logs.head('pergunta')
    set_char()

    game_logs.head('narrador')
    print(f"Você é {C.MAGENTA}{player.char}{C.NORMAL}, um jovem de 19 anos que vive em um {C.YELLOW}vilarejo conectado ao mundo exterior por um cruzamento famoso.")
    print(F"Seus pais são os fazendeiros locais, {C.YELLOW}José {C.NORMAL}e {C.YELLOW}Maria{C.NORMAL}. Eles são {C.YELLOW}filhos dos fundadores do vilarejo{C.NORMAL}. Você não tem nenhum outro parente.")
    print(jose, maria, char)
    print("Você acorda em sua cama, o sol está aparecendo em sua janela. E com isso, o som dos estudantes passando pela sua casa")
    print(f"No seu criado mudo você vê sua {C.YELLOW}camisa favorita{C.NORMAL}")
    game_logs.add_item(player.char, "favorite long-sleeve shirt")
    while True:
        game_logs.head('escolha')
        print("DIGITE:")
        print("> 'descer as escadas'")
        print("> 'olhar pela janela'")
        print("> 'procurar algo pelo quarto'")
        MainChoice = helpers.choice(">> ")

        if MainChoice is None:
            continue

        if MainChoice == "descer as escadas":
            game_logs.head('narrador')
            print("Você se levanta, pôe suas chinelas, e começa a descer as escadas.")
            print("Quando você está para enxergar alguém na cozinha, outra pessoa grita com você.")
            print(f"\n???: {player.char.upper()}, VENHA CÁ, SEU MALDITO!\n")
            print("Chegando mais perto você reconhece a pessoa, é o seu velho pai, José.")
            print("Ele olha para você com raiva, batendo o pé esperando alguma resposta...")

            game_logs.head('diálogo')
            print("DIGITE:")
            print("> 'desculpa'")
            print("> 'vai se foder'")
            answer = helpers.choice(">> ")

            game_logs.head('narrador')
            if answer == 'desculpa':
                print("José respira fundo e então fala:")
                print(f"\nJosé: tá bom... mas da próxima vez não fica até tarde dormindo não, ouviu? Agora vai pegar madeira pra consertar a cerca das cabrita.\n")
            elif answer == 'vai se foder':
                print(f"\nJosé: Seu bastardo filho de uma puta! vai pra rua agora e vê se volta com a cabeça no lugar!\n")

            game_logs.head('narrador')
            print("Você vai para fora de casa.")

            game_logs.head('escolha')
            print("DIGITE:")
            print("> 'ir para a escola'")
            print("> 'ir para o mercado'")
            print("> 'ir para a floresta'")
            choice = helpers.choice(">> ")

            if choice == "ir para a escola":
                game_logs.head('narrador')
                print("Você caminha em direção à escola local, cumprimentando alguns conhecidos pelo caminho.")
                print("Ao chegar, você se dirige para a sala de aula, onde a aula já está começando.")
                print("Você se senta em sua carteira e dorme durante toda a aula.")

                game_logs.head('menssagem do dev')
                print("Em alguma atualização futura, adicionar mais interações na escola. DEADENDLINE")
            
            elif choice == "ir para o mercado":
                game_logs.head('narrador')
                print("Você caminha em direção ao mercado local, cumprimentando alguns conhecidos pelo caminho.")
                print("Ao chegar, você vê várias barracas vendendo frutas, legumes e outros produtos.")
                print("Você decide comprar alguns mantimentos para a casa antes de voltar.")

                game_logs.head('menssagem do dev')
                print("Em alguma atualização futura, adicionar mais interações no mercado. DEADENDLINE")
            
            elif choice == "ir para a floresta":
                game_logs.head('narrador')
                print("Você caminha em direção à floresta próxima, cumprimentando alguns conhecidos pelo caminho.")
                print("Ao chegar, você se aventura entre as árvores, ouvindo os sons da natureza ao seu redor.")
                print("O tempo passa e você derrepente se vê perdido na floresta.")

                game_logs.head('menssagem do dev')
                print("Em alguma atualização futura, adicionar mais interações na floresta. DEADENDLINE")

        elif MainChoice == "olhar pela janela":
            look_window_choice()
            pass

        elif MainChoice == "procurar algo pelo quarto":
            look_room_choice()
            pass

        else:
            print("Escolha inválida. Tente novamente.")

@helpers.retry_on_inventory
def look_window_choice():
    if visited_places['window']['visited']:
        game_logs.head('info')
        print("Você já olhou todos os pontos interessantes da janela.")
        return
    
    game_logs.head('narrador')
    print("Você se encosta no peitoril da janela")
    while True:
        print(f"À frente, três pontos chamam atenção: o{C.YELLOW} estábulo{C.NORMAL}, o {C.YELLOW}parquinho enferrujado{C.NORMAL}, e um {C.YELLOW}prédio grande{C.NORMAL}.")
        
        game_logs.head('pergunta')
        print("O que você vai olhar?")
        print("DIGITE:")
        print("> 'predio grande'")
        print("> 'parquinho enferrujado'")
        print("> 'estabulo'")
        print("> 'voltar'")
        LookChoice = helpers.choice(">> ")

        if LookChoice == "predio grande":
            if visited_places['window']['big_building_seen']:
                game_logs.head('info')
                print("Você já olhou para o prédio grande e viu tudo que havia de interessante.")
                continue

            visited_places['window']['big_building_seen'] = True
            game_logs.head('narrador')
            print(f"Ao olhar para o prédio grande, você vê alguns trabalhadores trabalhando normalmente, mas algo chama sua atenção, {C.YELLOW}um grupo de adolescentes está maltratando um gato{C.NORMAL}.")
            game_logs.head('ação')
            print("DIGITE:")
            print("> 'intervir'")
            print("> 'ignorar'")
            action = helpers.choice(">> ")

            if action == 'intervir':
                game_logs.head('narrador')
                print("Você pula da sua janeka em direção ao prédio grande, sabuga os adolescentes na porrada e salva o gato.")

                game_logs.head('mensagem do dev')
                print("em alguma atualização adcionar pet e stat")

                game_logs.head('narrador')
                print("Depois de salvar o gato, você volta pra sua casa.")
                print("Você se encosta na janela.")

            elif action == 'ignorar':
                game_logs.head('narrador')
                print("Você decide ignorar a situação, afinal, você é um covarde ou odeia gatos.")

                game_logs.head('mensagem do dev')
                print("em alguma atualização fazer o user escolher uma das opções")

                game_logs.head('narrador')
                print("Você se encosta na janela.")

        elif LookChoice == "parquinho enferrujado":
            if visited_places['window']['rusty_playground_seen']:
                game_logs.head('info')
                print("Você já olhou para o parquinho enferrujado e viu tudo que havia de interessante.")
                continue

            visited_places['window']['rusty_playground_seen'] = True
            game_logs.head('narrador')
            print(f"Ao olhar para o parquinho enferrujado, você avista algumas crianças brincando, mas outra coisa chama sua atenção, {C.YELLOW}um grupo de crianças está praticando bullying contra uma criança de óculos{C.NORMAL}.")
            game_logs.head('ação')
            print("DIGITE:")
            print("> 'intervir'")
            print("> 'ignorar'")
            action = helpers.choice(">> ")

            if action == 'intervir':
                game_logs.head('narrador')
                print("Você pula da sua janela em direção ao parquinho enferrujado, só de se aproximar das crianças, elas fogem com medo, assim, salvando a criança de óculos.")

                game_logs.head('mensagem do dev')
                print("em alguma atualização adcionar stat de bravura e adcionar um item da criança salva")

                game_logs.head('narrador')
                print("Depois de defender a criança, você volta pra sua casa.")
                print("Você se encosta na janela.")

            elif action == 'ignorar':
                game_logs.head('narrador')
                print("Você decide ignorar a situação, afinal, você é um covarde.")
                print("Você se encosta na janela.")

        elif LookChoice == "estabulo":
            if visited_places['window']['stable_seen']:
                game_logs.head('info')
                print("Você já olhou para o estábulo e viu tudo que havia de interessante.")
                continue
            
            visited_places['window']['stable_seen'] = True
            game_logs.head('narrador')
            print(f"Olhar para o estábulo, você pode ver alguns cavalos e galinhas, além disso, {C.YELLOW}uma garota de cabelo vermelho{C.NORMAL} chama sua atenção, ela está cuidando de um dos cavalos.")
            game_logs.head('ação')
            print("DIGITE:")
            print("> 'acenar'")
            print("> 'ignorar'")
            action = helpers.choice(">> ")

            if action == 'acenar':
                game_logs.head('narrador')
                print("Você acena para a garota de cabelo vermelho, ela sorri e acena de volta.")

                game_logs.head('mensagem do dev')
                print("em alguma atualização adcionar stat de carisma e talvez um interesse romântico")

                game_logs.head('narrador')
                print("Você se encosta na janela.")

            elif action == 'ignorar':
                game_logs.head('narrador')
                print("Você decide ignorar a garota, afinal, você gosta de ser invisível.")
                print("Você se encosta na janela.")

        elif LookChoice == "voltar":
            game_logs.head('narrador')
            print("Você se afasta da janela e volta para a sua cama.")
            return
        
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, 3 or 4.")
        
        if (
            visited_places['window']['big_building_seen'] and
            visited_places['window']['rusty_playground_seen'] and
            visited_places['window']['stable_seen']
        ):
            visited_places['window']['visited'] = True
            game_logs.head('info')
            print("Depois de observar todos os pontos interessantes da janela, você decide se afastar dela.")
            return

@helpers.retry_on_inventory
def look_room_choice():
    while True:
        if visited_places['wardrobe']['visited'] and visited_places['under_bed']['visited'] and visited_places['shelves']['visited']:
            game_logs.head('info')
            print("Você já olhou ao redor do seu quarto e encontrou tudo que havia de interessante.")
            return

        game_logs.head('narrador')
        print("Enquanto você olha ao redor do seu quarto...")
        print(f"Você pode ver vários locais interessantes, como um {C.YELLOW}guarda-roupa{C.NORMAL}, {C.YELLOW}algumas prateleiras{C.NORMAL} e {C.YELLOW}debaixo da sua cama{C.NORMAL}.")

        game_logs.head('pergunta')
        print("DIGITE:")
        print("> 'guarda-roupa'")
        print("> 'debaixo da cama'")
        print("> 'prateleiras'")
        print("> 'voltar'")
        SearchChoice = helpers.choice(">> ")

        if SearchChoice == "guarda-roupa":
            wardrobe_choice()
        elif SearchChoice == "debaixo da cama":
            under_bed_choice()
        elif SearchChoice == "prateleiras":
            shelves_choice()
        elif SearchChoice == "voltar":
            return
        else:
            print(F"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, 3, or 4.")

@helpers.retry_on_inventory
def wardrobe_choice():
    CLOTHES_ITEMS = ["favorite long-sleeve shirt", "well-used dark tanktop", "good-looking blazer"]
    if visited_places['wardrobe']['visited']:
        game_logs.head('info')
        print("Você já procurou no guarda-roupa e encontrou tudo que havia de interessante.")
        return

    while True:
        game_logs.head('narrador')
        print("Você está em frente ao seu guarda-roupa")
        game_logs.head('pergunta')
        print("DIGITE:")
        print("> 'abrir porta'")
        print("> 'voltar'")
        WardrobeChoice = helpers.choice(">> ")

        if WardrobeChoice == "abrir porta":
            if visited_places['wardrobe']['broken_door']:
                game_logs.head('narrador')
                print(f"Você desvia do que era a porta do guarda-roupa, mas agora é uma {C.YELLOW}pilha de madeira{C.NORMAL}, e olha para dentro dele.")

            else:
                visited_places['wardrobe']['broken_door'] = True
                game_logs.head('narrador')
                print(f"Você força a porta do guarda-roupa, quebra ela em uma {C.YELLOW}pilha de madeira{C.NORMAL}, mas o abre.")
            print(f"Dentro do guarda-roupa há uma {C.YELLOW}coleção de roupas velhas e empoeiradas{C.NORMAL}.")

            while True:
                if visited_places['wardrobe']['w_u_d_tanktop_taken'] and visited_places['wardrobe']['g_l_blazer_taken'] and visited_places['wardrobe']['wood_plank_taken']:
                    visited_places['wardrobe']['visited'] = True
                    game_logs.head('info')
                    print("Você já pegou todas as roupas interessantes do guarda-roupa e já vasculhou a pilha de madeira.")
                    return
                
                game_logs.head('pergunta')
                print("O que você vai pegar?")
                print("DIGITE:")
                print("> 'regata preta bem usada'")
                print("> 'blazer bonito'")
                print("> 'pilha de madeira'")
                print("> 'voltar'")
                ClothesChoice = helpers.choice(">> ")

                if ClothesChoice == "regata preta bem usada":
                    if visited_places['wardrobe']['w_u_d_tanktop_taken']:
                        game_logs.head('info')
                        print("Você já pegou a regata do guarda-roupa.")
                        return
                    
                    visited_places['wardrobe']['w_u_d_tanktop_taken'] = True
                    game_logs.add_item(player.char, "well-used dark tanktop")
                    return
                
                elif ClothesChoice == "blazer bonito":
                    if visited_places['wardrobe']['g_l_blazer_taken']:
                        game_logs.head('info')
                        print("Você já pegou o blazer do guarda-roupa.")
                        return
                    
                    visited_places['wardrobe']['g_l_blazer_taken'] = True
                    game_logs.add_item(player.char, "good-looking blazer")
                    return
                
                elif ClothesChoice == "pilha de madeira":
                    if visited_places['wardrobe']['wood_plank_taken']:
                        game_logs.head('info')
                        print("Você já pegou a pilha de madeira do guarda-roupa.")
                        return

                    visited_places['wardrobe']['wood_plank_taken'] = True
                    game_logs.add_item(player.char, "wood plank")
                    return

                elif ClothesChoice == "voltar":
                    game_logs.head('narrador')
                    print("Você saiu do guarda-roupa sem pegar nenhuma roupa.")
                    return
                
                else:
                    print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2 or 3.")

        elif WardrobeChoice == "voltar":
            game_logs.head('narrador')
            print("Você decide deixar o guarda-roupa sozinho por enquanto.")
            return
        
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1 or 2.")

@helpers.retry_on_inventory
def under_bed_choice():
    if visited_places['under_bed']['visited']:
        game_logs.head('info')
        print("Você já vasculhou debaixo da cama e não encontrou nada.")
        return
    
    while True:
        game_logs.head('narrador')
        print(F"Quando você move o pescoço para ver debaixo da cama, {C.RED}seu pescoço dói{C.NORMAL}. Passando a mão sobre ele, {C.RED}você nota um hematoma{C.NORMAL}. Tocar nele faz a dor piorar.")
        
        game_logs.head('escolha')
        print("Você vai olhar debaixo da cama?")
        print("DIGITE:")
        print("> 'sim'")
        print("> 'nao'")
        BedChoice = helpers.choice(">> ")

        if BedChoice == "sim":
            game_logs.head('narrador')
            print("Quando você move a cabeça para ver debaixo da cama, seu pescoço dói, mas você ignora.")

            game_logs.damage(player.char, 10, "forçar o pescoço apesar da dor")

            game_logs.head('narrador')
            print(f"Lá, embaixo do seu colchão, {C.YELLOW}você nota algo escuro{C.NORMAL}.")

            while True:
                game_logs.head('pergunta')
                print("Você vai mover a cabeça mais perto?")
                print("DIGITE:")
                print("> 'sim'")
                print("> 'nao'")
                SecondBedChoice = helpers.choice(">> ")

                if SecondBedChoice == "sim":
                    game_logs.head('narrador')
                    print("Quando você move a cabeça mais perto, seu pescoço dói mais.")

                    game_logs.damage(player.char, 20, "forçar o pescoço novamente apesar da dor")

                    game_logs.head('narrador')
                    print(f"Mas então, você descobre que a coisa escura era uma {C.YELLOW}faca enferrujada e ensanguentada{C.NORMAL}.")

                    game_logs.add_item(player.char, "blooded rusty knife")
                    visited_places['under_bed']['knife_taken'] = True

                    game_logs.head('narrador')
                    print("Você pega a faca e deixa o fundo da sua cama.")

                    visited_places['under_bed']['visited'] = True 
                    return

                elif SecondBedChoice == "nao":
                    game_logs.head('narrador')
                    print("Você decide que a dor não vale a pena e retira a cabeça.")
                    return
                
                else:
                    print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

        elif BedChoice == "nao":
            game_logs.head('narrador')
            print("Você decide que a dor não vale a pena e se deita novamente.")
            return

        else:
            print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

@helpers.retry_on_inventory
def shelves_choice():
    if visited_places['shelves']['visited']:
        game_logs.head('info')
        print("Você já vasculhou as prateleiras e não encontrou mais nada.")
        return
    
    while True:
        game_logs.head('narrador')
        print("Enquanto você passa a mão por alguns livros e outros objetos que você guardou lá, você nota alguns interessantes.")
        print(f"Na prateleira vermelha, há uma {C.YELLOW}chave com uma pena presa{C.NORMAL} e uma {C.YELLOW}prisilía de cabelo{C.NORMAL}.")
        print("Porém essa prateleira é muito alta para alcançá-la normalmente, então você vai e pega um banquinho de madeira para alcançá-la.")

        game_logs.head('escolha')
        print("Você vai tentar pegar algo?")
        print("DIGITE:")
        print("> 'chave com pena presa'")
        print("> 'prisilia de cabelo'")
        print("> 'voltar'")
        ShelvesChoice = helpers.choice(">> ")

        if ShelvesChoice == "chave com pena presa":
            if visited_places['shelves']['key_taken']:
                game_logs.head('info')
                print("Você já pegou a chave com pena presa da prateleira.")

            else:
                visited_places['shelves']['key_taken'] = True
                game_logs.add_item(player.char, "key with feather attached")

            game_logs.head('escolha')
            print(f"Você vai tentar pegar a {C.YELLOW}prisilia de cabelo{C.NORMAL}?")
            print("DIGITE:")
            print("> 'sim'")
            print("> 'nao'")
            StoolChoice = helpers.choice(">> ")

            if StoolChoice == "sim":
                if visited_places['shelves']['hair_clip_taken']:
                    game_logs.head('info')
                    print("Você já pegou o prisilia de cabelo da prateleira.")

                else:
                    visited_places['shelves']['hair_clip_taken'] = True
                    game_logs.add_item(player.char, "hair clip")
                
                game_logs.head('narrador')
                print("Mas quando você tenta descer, o banquinho quebra e você cai no chão.")

                game_logs.damage(player.char, 15, "Cair do banquinho")

                game_logs.head('narrador')
                print("Você se levanta e sai da prateleira.")

                if visited_places['shelves']['hair_clip_taken'] and visited_places['shelves']['key_taken']:
                    visited_places['shelves']['visited'] = True
                    game_logs.head('info')
                    print("Você já pegou todos os itens interessantes da prateleira.")
                return
            
            elif StoolChoice == "nao":
                game_logs.head('narrador')
                print("Você decide deixar a prisilia de cabelo lá.")
                return
            
            else:
                print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

        elif ShelvesChoice == "prisilia de cabelo":
            if visited_places['shelves']['hair_clip_taken']:
                game_logs.head('info')
                print("Você já pegou a prisilia de cabelo da prateleira.")

            else:
                visited_places['shelves']['hair_clip_taken'] = True
                game_logs.add_item(player.char, "hair clip")

            game_logs.head('pergunta')
            print(f"Você vai tentar pegar a {C.YELLOW}chave com pena presa{C.NORMAL}?")
            print("DIGITE:")
            print("> 'sim'")
            print("> 'nao'")
            StoolChoice = helpers.choice(">> ")

            if StoolChoice == "sim":
                if visited_places['shelves']['key_taken']:
                    game_logs.head('info')
                    print("Você já pegou a chave com pena presa da prateleira.")

                else:
                    visited_places['shelves']['key_taken'] = True
                    game_logs.add_item(player.char, "key with feather attached")

                game_logs.head('narrador')
                print("Mas quando você tenta descer, o banquinho quebra e você cai no chão.")

                game_logs.damage(player.char, 15, "cair do banquinho")

                game_logs.head('narrador')
                print("Você se levanta e sai da prateleira.")

                if visited_places['shelves']['hair_clip_taken'] and visited_places['shelves']['key_taken']:
                    visited_places['shelves']['visited'] = True
                    game_logs.head('info')
                    print("Você pegou todos os itens interessantes da prateleira.")
                return

            elif StoolChoice == "nao":
                game_logs.head('narrador')
                print("Você decide deixar a chave com pena presa lá.")
                return
            
            else:
                print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

        elif ShelvesChoice == "3":
            game_logs.head('narrador')
            print("Você decide deixar os itens onde estão.")
            return
        
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, or 3.")

main_choice_loop()