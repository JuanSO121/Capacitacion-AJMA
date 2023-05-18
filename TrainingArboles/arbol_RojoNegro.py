import networkx as nx
import matplotlib.pyplot as plt
from TrainingArboles.TDA_RojoNegro import ArbolRojoNegro
import networkx as nx

def agregar_nodos_y_enlaces(nodo, grafo, posiciones):
    if nodo is None:
        return

    agregar_nodos_y_enlaces(nodo.izquierdo, grafo, posiciones)
    agregar_nodos_y_enlaces(nodo.derecho, grafo, posiciones)

    color = "red" if nodo.color == "ROJO" else "black"
    grafo.add_node(nodo.dato, color=color)
    posiciones[nodo.dato] = (nodo.dato, 0)

    if nodo.padre is not None:
        grafo.add_edge(nodo.padre.dato, nodo.dato)

def visualizar_arbol(arbol):
    grafo = nx.Graph()
    posiciones = {}

    agregar_nodos_y_enlaces(arbol.raiz, grafo, posiciones)

    colores = [data["color"] for _, data in grafo.nodes(data=True)]

    nx.draw(grafo, posiciones, with_labels=True, node_color=colores)
    plt.show()

arbol = ArbolRojoNegro()
while True:
    print("-------- Menú Árbol Rojo-Negro --------")
    print("1. ¿Qué es un árbol rojo-negro?")
    print("2. Mostrar partes del árbol")
    print("3. Mostrar altura del árbol")
    print("4. Insertar nodo")
    print("5. Eliminar nodo")
    print("6. Visualizar árbol")
    print("7. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Un árbol rojo-negro es un tipo de árbol binario de búsqueda balanceado. Se caracteriza por tener las siguientes propiedades:")
        print("- Cada nodo es rojo o negro.")
        print("- La raíz es negra.")
        print("- Todas las hojas (nodos nulos) son negras.")
        print("- Si un nodo es rojo, entonces ambos hijos son negros.")
        print("- Para cada nodo, todos los caminos simples desde ese nodo hasta las hojas descendientes contienen el mismo número de nodos negros.")

    elif opcion == "2":
        print("Las partes de un árbol rojo-negro son:")
        print("- Nodo: Cada elemento almacenado en el árbol se representa como un nodo.")
        print("- Raíz: Es el nodo superior del árbol.")
        print("- Hoja: Es un nodo nulo que representa un valor no presente en el árbol.")
        print("- Padre: Es el nodo que está directamente por encima de un nodo dado.")
        print("- Hijo: Son los nodos que están directamente debajo de un nodo dado.")

    elif opcion == "3":
        altura = arbol.altura()
        print("La altura del árbol es:", altura)

    elif opcion == "4":
        dato = int(input("Ingrese el valor del nodo a insertar: "))
        arbol.insertar(dato)
        print("Nodo insertado correctamente.")

    elif opcion == "5":
        dato = int(input("Ingrese el valor del nodo a eliminar: "))
        if arbol.eliminar(dato):
            print("Nodo eliminado correctamente.")
        else:
            print("El nodo no existe en el árbol.")

    elif opcion == "6":
        visualizar_arbol(arbol)

    elif opcion == "7":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    print()