
# Classe tem características e comportamentos = métodos

class Cachorro:
    # características ou atributos
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # comportamentos ou métodos
    def latir(self):
        print("auau")

    def dormir(self):
        self.acordado = False
        print("Zzzz...")

# Objeto: precisamos instanciar o objeto da classe para poder utilizá-lo

cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("aladim", "branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)

