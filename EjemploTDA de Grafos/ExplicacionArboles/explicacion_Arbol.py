import matplotlib.pyplot as plt
import networkx as nx
from TDA_Arbol import Arbol, Nodo, dfs_preorden, mostrar_arbol

def mostrar_arbol_con_networkx(arbol):
    G = nx.DiGraph()
    for nodo in dfs_preorden(arbol.raiz):
        G.add_node(nodo.valor)
        if nodo.padre is not None:
            G.add_edge(nodo.padre.valor, nodo.valor)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, arrows=True)
    plt.show()
    
# Creamos el árbol
raiz = Nodo("raiz")
nodo1 = Nodo("nodo1")
nodo2 = Nodo("nodo2")
nodo3 = Nodo("nodo3")
nodo4 = Nodo("nodo4")
nodo5 = Nodo("nodo5")

arbol = Arbol(raiz)
arbol.agregar_nodo("nodo1", arbol.raiz)
arbol.agregar_nodo("nodo2", arbol.raiz)
padre = arbol.buscar_nodo("nodo1")
arbol.agregar_nodo("nodo3", padre)
arbol.agregar_nodo("nodo4", padre)
padre = arbol.buscar_nodo("nodo2")
arbol.agregar_nodo("nodo5", padre)

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
    print("\nUn nodo es un elemento en un árbol, es decir una entidad que contiene información y está conectada a otros nodos, formando así la estructura jerárquica del árbol.")

def mostrar_raiz():
    print("\nEs el nodo principal y el nivel superior del árbol. Es el único nodo que no tiene un nodo padre y sirve como punto de partida para acceder a todos los demás nodos del árbol.")

def mostrar_hoja():
    
    print("\nUna hoja en un árbol es un nodo final o terminal que no tiene hijos ni ramificaciones adicionales, en este arbol las hojas son:")

def mostrar_padre():
    print("\nUn padre es un nodo en un árbol que tiene al menos un hijo. En este árbol los padres son:")

def mostrar_hijo():
    
    print("\nUn hijo en un árbol es un nodo cuya escala jerarquica es inferior al nodo que está conectado directamente, el cual se llama nodo padre, en este arbol los hijos son:")

def mostrar_rama():
    print("\nuna rama en un árbol es un camino o secuencia de nodos que se extiende desde un nodo padre hasta uno de sus nodos hijos.")
    print("Representa una conexión jerárquica y proporciona una ruta para recorrer la estructura del árbol,"+"\n"+ "En este arbol las ramas son:")
    
def mostrar_subarbol():
    print("\nUn subárbol es una porción de un árbol más grande que se deriva de un nodo raíz específico y que incluye a ese nodo y a todos sus descendientes.")
    print("Es decir que son los posibles caminos a recorrer en un arbol a partir de un punto de partida y destino especificado.")

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
            mostrar_arbol_con_networkx(arbol)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida, por favor selecciona otra.")

explicacion()
