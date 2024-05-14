class Filosofo:
    def __init__(self, nome, esquerda, direita):
        self.nome = nome
        self.esquerda = esquerda
        self.direita = direita

    def comer(self):
        print(f"{self.nome} está comendo.")

    def pensar(self):
        print(f"{self.nome} está pensando.")

    def tentar_comer(self, garfo_esquerda, garfo_direita):
        if not garfo_esquerda.is_usado and not garfo_direita.is_usado:
            garfo_esquerda.is_usado = True
            garfo_direita.is_usado = True
            self.comer()
            return True
        else:
            self.pensar()
            return False

class Garfo:
    def __init__(self):
        self.is_usado = False

def main():
    filosofos = [
        Filosofo("Filósofo 1", Garfo(), Garfo()),
        Filosofo("Filósofo 2", Garfo(), Garfo()),
        Filosofo("Filósofo 3", Garfo(), Garfo()),
        Filosofo("Filósofo 4", Garfo(), Garfo()),
        Filosofo("Filósofo 5", Garfo(), Garfo())
    ]

    # Cada filósofo tenta comer cinco vezes
    for i in range(5):
        for filosofo in filosofos:
            # Obter os garfos vizinhos
            garfo_esquerda = filosofo.esquerda
            garfo_direita = filosofo.direita

            # Tentar comer
            filosofo.tentar_comer(garfo_esquerda, garfo_direita)

            # Liberar garfos
            garfo_esquerda.is_usado = False
            garfo_direita.is_usado = False

if __name__ == "__main__":
    main()
