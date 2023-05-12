import matplotlib.pyplot as plt
import networkx as nx

# Creamos un grafo vacío
G = nx.DiGraph()

# Agregamos nodos al grafo
G.add_node(1, label="Nodo 1")
G.add_node(2, label="Nodo 2")
G.add_node(3, label="Nodo 3")

# Agregamos aristas (también llamadas "vértices") al grafo
G.add_edge(1, 2, label="Arista 1-2")
G.add_edge(2, 3, label="Arista 2-3")

# Asignamos pesos a las aristas
G[1][2]['weight'] = 0.5
G[2][3]['weight'] = 1.2

# Creamos el menú
menu = {
    "1": "¿Qué es un Arbol?",
    "2": "¿Qué es un nodo?",
    "3": "¿Qué es una raiz?",
    "4": "¿Qué es una hoja?",
    "5": "¿Qué es un padre?",
    "6": "¿Qué es un hijo?",
    "7": "¿Qué es una rama?",
    "8": "¿Qué es un subárbol?",
    "9": "Mostrar árbol",
    "0": "Salir"
}
# Funciónes que definen y muestran cada parte de un arbol
def Def_Arbol():
    print ("\nEs una estructura jerárquica compuesta por nodos y aristas, donde cada nodo tiene un nodo padre y cero o más nodos hijos.")
    print ("Se utilizan ampliamente en ciencias de la computación y programación debido a su capacidad para representar estructuras jerárquicas y relaciones entre elementos.")

def mostrar_nodo():
    print("\nUn nodo es un elemento en un árbol, es decir una entidad que contiene información y está conectada a otros nodos, formando así la estructura jerárquica del árbol.", G.nodes())

def mostrar_raiz():
    print("\nEs el nodo principal y el nivel superior del árbol. Es el único nodo que no tiene un nodo padre y sirve como punto de partida para acceder a todos los demás nodos del árbol.")

def mostrar_hoja():
    hojas = [nodo for nodo in G.nodes() if G.out_degree(nodo) == 0]
    print("\nUna hoja en un árbol es un nodo final o terminal que no tiene hijos ni ramificaciones adicionales, en este arbol las hojas son:", hojas)

def mostrar_padre():
    padres = [nodo for nodo in G.nodes() if G.in_degree(nodo) > 0]
    print("\nUn padre es un nodo en un árbol que tiene al menos un hijo. En este árbol los padres son:", padres)

def mostrar_hijo():
    hijos = [nodo for nodo in G.nodes() if G.out_degree(nodo) > 0]
    print("\nUn hijo en un árbol es un nodo cuya escala jerarquica es inferior al nodo que está conectado directamente, el cual se llama nodo padre, en este arbol los hijos son:", hijos)

def mostrar_rama():
    print("\nuna rama en un árbol es un camino o secuencia de nodos que se extiende desde un nodo padre hasta uno de sus nodos hijos.")
    print("Representa una conexión jerárquica y proporciona una ruta para recorrer la estructura del árbol,"+"\n"+ "En este arbol las ramas son:")
    
def mostrar_subarbol():
    print("\nUn subárbol es una porción de un árbol más grande que se deriva de un nodo raíz específico y que incluye a ese nodo y a todos sus descendientes.")
    print("Es decir que son los posibles caminos a recorrer en un arbol a partir de un punto de partida y destino especificado.")

# Función para mostrar el árbol
def mostrar_arbol():
    # Dibujamos el árbol
    pos = nx.spring_layout(G, seed=42)

    # Colores de los nodos, aristas y peso
    node_color = 'lightblue'
    edge_color = 'black'
    weight_color = 'red'
    node_label_color = 'white'
    edge_label_color = 'black'

    # Dibujamos los nodos
    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=500, label="Nodos")

    # Dibujamos las aristas
    nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=2, alpha=0.7, label="Aristas")

    # Etiquetas de los nodos
    node_labels = {node: G.nodes[node]['label'] for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=14, font_color=node_label_color)

    # Etiquetas de las aristas con los pesos
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges() if 'weight' in G[u][v]}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=12, font_color=edge_label_color)

    # Legendas
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

    # Mostramos el árbol
    plt.axis('off')
    plt.show()

# Funcion del menú
def explicacion():
    # Bucle principal del programa
    while True:
        # Mostramos el menú
        print("\n-- Bienvenido al entrenamiento de Árboles --")
        print("-- En este capítulo aprenderás sobre las partes de un árbol --")
        print("\n")
        for opcion, descripcion in menu.items():
            print(opcion, "-", descripcion)
        opcion = input("Selecciona una opción: ")

        # Ejecutamos la opción seleccionada
        if opcion == "1":
            Def_Arbol()
        elif opcion == "2":
            mostrar_nodo()
        elif opcion == "3":
            mostrar_raiz()
        elif opcion == "4":
            mostrar_hoja()
        elif opcion == "5":
            mostrar_padre()
        elif opcion == "6":
            mostrar_hijo()
        elif opcion == "7":
            mostrar_rama()
        elif opcion == "8":
            mostrar_subarbol()
        elif opcion == "9":
            mostrar_arbol()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida, por favor selecciona otra.")

explicacion()
