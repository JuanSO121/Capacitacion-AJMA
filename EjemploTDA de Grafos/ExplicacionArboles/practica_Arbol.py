import networkx as nx
import matplotlib.pyplot as plt
from TDA_Arbol import Arbol, Nodo,dfs_preorden,mostrar_arbol

def mostrar_menu():
    print("¡Bienvenido al programa de árboles!")
    print("Este programa te permitirá conocer las partes de un árbol.")
    print("Por favor, sigue las instrucciones y utiliza las opciones del menú para interactuar con el programa.")
    arbol = Arbol(Nodo("raiz"))
    while True:
        print()
        print("-------- MENÚ ---------")
        print("1. Agregar nodo")
        print("2. Eliminar nodo")
        print("3. Buscar nodo")
        print("4. Visualizar árbol")
        print("5. Mostrar partes del árbol")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            valor = input("Ingrese el valor del nodo: ")
            padre_valor = input("Ingrese el valor del padre (o presione Enter si el nodo es la raíz): ")
            if padre_valor == "":
                arbol.agregar_nodo(valor, arbol.raiz)
            else:
                padre = arbol.buscar_nodo(padre_valor)
                if padre is not None:
                    arbol.agregar_nodo(valor, padre)
                else:
                    print("El nodo padre no existe")
        elif opcion == "2":
            valor = input("Ingrese el valor del nodo a eliminar: ")
            nodo = arbol.buscar_nodo(valor)
            if nodo is not None:
                arbol.eliminar_nodo(nodo)
            else:
                print("El nodo no existe")
        elif opcion == "3":
            valor = input("Ingrese el valor del nodo a buscar: ")
            nodo = arbol.buscar_nodo(valor)
            if nodo is not None:
                print("Nodo encontrado")
            else:
                print("Nodo no encontrado")
        elif opcion == "4":
            G = nx.DiGraph()
            for nodo in dfs_preorden(arbol.raiz):
                G.add_node(nodo.valor)
                if nodo.padre is not None:
                    G.add_edge(nodo.padre.valor, nodo.valor)
            pos = nx.spring_layout(G)
            nx.draw_networkx(G, pos, with_labels=True, arrows=True)
            plt.show()
        elif opcion == "5":
            mostrar_arbol(arbol)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")
            
mostrar_menu()