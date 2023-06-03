import networkx as nx
import matplotlib.pyplot as plt

class NodoArbol:
    def __init__(self, valor=None):
        self.valor = valor
        self.codigo_morse = None
        self.izquierda = None
        self.derecha = None

class ArbolMorse:
    def __init__(self):
        self.raiz = NodoArbol()
        

    def insertar(self, valor, codigo):
        raiz = self.raiz
        for c in codigo:
            if c == '.':
                if raiz.izquierda is None:
                    raiz.izquierda = NodoArbol()
                raiz = raiz.izquierda
            elif c == '-':
                if raiz.derecha is None:
                    raiz.derecha = NodoArbol()
                raiz = raiz.derecha
        raiz.valor = valor
        raiz.codigo_morse = codigo

    def mostrar_arbol(self):
        G = nx.DiGraph()
        self._construir_grafo(self.raiz, G)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()
    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is None:
            return
        print("  " * nivel + "- " + str(nodo.valor))
        self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)
        self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)

    def _construir_grafo(self, nodo, G):
        if nodo is None:
            return
        G.add_node(str(nodo.valor))
        if nodo.izquierda is not None:
            G.add_edge(str(nodo.valor), str(nodo.izquierda.valor))
            self._construir_grafo(nodo.izquierda, G)
        if nodo.derecha is not None:
            G.add_edge(str(nodo.valor), str(nodo.derecha.valor))
            self._construir_grafo(nodo.derecha, G)

    def _dibujar_grafo(self):
        pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, pos)
        node_labels = nx.get_node_attributes(self.G, 'label')
        nx.draw_networkx_labels(self.G, pos, labels=node_labels)
        plt.axis('off')
        plt.show()

    def decode_morse_code(self, morse_code):
        words = morse_code.split(' / ')
        decoded_message = ''
        for word in words:
            characters = word.split()
            decoded_word = ''
            for character in characters:
                if character in self._get_morse_code_dict():
                    decoded_word += self._get_morse_code_dict()[character]
            decoded_message += decoded_word + ' '
        return decoded_message.strip()

    def encode_message(self, message):
        encoded_message = ''
        for char in message:
            if char.upper() in self._get_morse_code_dict().values():
                for code, value in self._get_morse_code_dict().items():
                    if value == char.upper():
                        encoded_message += code + ' '
        return encoded_message.strip()

    def _get_morse_code_dict(self):
        morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                           '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                           '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                           '-.--': 'Y', '--..': 'Z'}
        return morse_code_dict