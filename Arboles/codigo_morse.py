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
        self.G = nx.DiGraph()

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

    def _construir_grafo(self, nodo, parent=None):
        if nodo is not None:
            self.G.add_node(nodo.valor)
            if parent is not None:
                self.G.add_edge(parent, nodo.valor)
            self._construir_grafo(nodo.izquierda, nodo.valor)
            self._construir_grafo(nodo.derecha, nodo.valor)

    def mostrar_arbol(self):
        self.G = nx.DiGraph()
        self._construir_grafo(self.raiz)
        pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, pos)
        node_labels = nx.get_node_attributes(self.G, 'label')
        nx.draw_networkx_labels(self.G, pos, labels=node_labels)
        plt.axis('off')
        plt.show()

    def mostrar_arbol_palabra(self, palabra):
        arbol_temporal = ArbolMorse()
        codigo_morse = self.encode_message(palabra)
        for char in codigo_morse:
            arbol_temporal.insertar(char, self._obtener_diccionario_morse().get(char, ''))

        arbol_temporal.mostrar_arbol()

    def decode_morse_code(self, morse_code):
        words = morse_code.split(' / ')
        decoded_message = ''
        for word in words:
            characters = word.split()
            decoded_word = ''
            for character in characters:
                if character in self._obtener_diccionario_morse():
                    decoded_word += self._obtener_diccionario_morse()[character]
            decoded_message += decoded_word + ' '
        return decoded_message.strip()

    def encode_message(self, message):
        encoded_message = ''
        for char in message:
            if char.upper() in self._obtener_diccionario_morse().values():
                for code, value in self._obtener_diccionario_morse().items():
                    if value == char.upper():
                        encoded_message += code + ' '
        return encoded_message.strip()

    def _obtener_diccionario_morse(self):
        morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                           '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                           '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                           '-.--': 'Y', '--..': 'Z'}
        return morse_code_dict
