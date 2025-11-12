from ...core import evento, helpers, C
from ..foradecasa.escola._1_escola import escola
from ..foradecasa.fazenda._1_fazenda import fazenda
from ..foradecasa.floresta._1_floresta import floresta

def rua():
    from ..casa.quarto._1_escada import escada
    while True:
        evento.cabecalho('narrador')
        print("Você está fora de casa.")

        caminho = helpers.pergunta(
            'escolha',
            ['o caminho para ir para a escola, sua fazenda, floresta ou casa'],
            ['escola', 'fazenda', 'floresta', 'casa'])

        if caminho == "escola":
            escola()
        
        elif caminho == "fazenda":
            fazenda()
        
        elif caminho == "floresta":
            floresta()
        
        elif caminho == "casa":
            escada()

        else:
            helpers.erro()
        