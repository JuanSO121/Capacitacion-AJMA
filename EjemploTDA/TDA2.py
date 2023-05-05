class Grafo:
    def __init__(self):
        self.nodos_set = set()  # se cambio el nombre del atributo nodos a nodos_set
        self.aristas_dict = dict()

    def agregar_nodo(self, valor):
        self.nodos_set.add(valor)
        if valor not in self.aristas_dict:
            self.aristas_dict[valor] = dict()

    def agregar_arista(self, inicio, fin, peso=None):
        self.agregar_nodo(inicio)
        self.agregar_nodo(fin)

        if peso:
            self.aristas_dict[inicio][fin] = peso
            self.aristas_dict[fin][inicio] = peso
        else:
            self.aristas_dict[inicio][fin] = None
            self.aristas_dict[fin][inicio] = None

    def nodos(self):
        return list(self.nodos_set)

    def aristas(self):
        resultado = set()
        for inicio in self.aristas_dict:
            for fin in self.aristas_dict[inicio]:
                resultado.add((inicio, fin))
        return list(resultado)

    def aristas_con_pesos(self):
        resultado = set()
        for inicio in self.aristas_dict:
            for fin in self.aristas_dict[inicio]:
                if self.aristas_dict[inicio][fin] is not None:
                    resultado.add((inicio, fin, self.aristas_dict[inicio][fin]))
        return list(resultado)