class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def buscar_nodo(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo.valor == valor:
            return nodo

        for hijo in nodo.hijos:
            nodo_encontrado = self.buscar_nodo(valor, hijo)
            if nodo_encontrado is not None:
                return nodo_encontrado

        return None

    def agregar_nodo(self, valor, padre):
        hijo = Nodo(valor)
        padre.agregar_hijo(hijo)

    def eliminar_nodo(self, nodo):
        if nodo.padre is None:
            self.raiz = None
        else:
            nodo.padre.hijos.remove(nodo)
            
def dfs_preorden(nodo):
    visitados = [nodo]
    for hijo in nodo.hijos:
        visitados.extend(dfs_preorden(hijo))
    return visitados

def mostrar_arbol(arbol):
    def mostrar_nodo(nodo, nivel):
        print("  "*nivel + f"{nodo.valor}")
        for hijo in nodo.hijos:
            mostrar_nodo(hijo, nivel+1)
   
    mostrar_nodo(arbol.raiz, 0)