import networkx as nx
import matplotlib.pyplot as plt
from TDA_monticulo import MonticuloColaPrioridades, heap_vacio, agregar, atencion

cola_prioridades = MonticuloColaPrioridades()

def pos_jerarquica(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcentro=0.5):
    pos = {}

    def _pos_jerarquica(G, root, width=1., vert_gap=0.2, vert_loc=0, xcentro=0.5, pos=None, padre=None, analizado=[]):
        if pos is None:
            pos = {root: (xcentro, vert_loc)}
        else:
            pos[root] = (xcentro, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and padre is not None:
            children.remove(padre)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcentro - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _pos_jerarquica(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcentro=nextx, pos=pos,
                                     padre=root, analizado=analizado)
        return pos

    if root is None:
        root = next(iter(G))
    return _pos_jerarquica(G, root, width, vert_gap, vert_loc, xcentro)

def construir_grafo():
    G = nx.DiGraph()
    heap_aux = cola_prioridades.heap
    for i in range(heap_aux.tamano):
        prioridad, tarea = heap_aux.vector[i]
        G.add_node(tarea, priority=prioridad)
        if i != 0:
            padre = (i - 1) // 2
            prioridad_padre, tarea_padre = heap_aux.vector[padre]
            G.add_edge(tarea_padre, tarea)
    return G

def mostrar_grafo():
    G = construir_grafo()
    pos = pos_jerarquica(G)
    
    fig, ax = plt.subplots()
    nx.draw_networkx(G, pos, with_labels=True, arrows=True, ax=ax)
    plt.show()

def menu():
    while True:
        print("\n=== Cola de Prioridades ===")
        print("1. Insertar tarea")
        print("2. Extraer tarea con mayor prioridad")
        print("3. Obtener todas las prioridades")
        print("4. Mostrar gráfico")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            prioridad = input("Ingrese la prioridad de la tarea: ")
            tarea = input("Ingrese la descripción de la tarea: ")
            cola_prioridades.insertar(int(prioridad), tarea)
            print(f"Tarea '{tarea}' con prioridad {prioridad} insertada con éxito.")

        elif opcion == "2":
            if not heap_vacio(cola_prioridades.heap):
                maxima_tarea = cola_prioridades.extraer_maximo()
                print("Tarea con la mayor prioridad:", maxima_tarea)
            else:
                print("La cola de prioridades está vacía.")

        elif opcion == "3":
            prioridades = cola_prioridades.obtener_prioridades()
            tareas = [(prioridad, cola_prioridades.buscar_tarea(prioridad)) for prioridad in prioridades]
            print("Prioridades:")
            for prioridad, tarea in tareas:
                print(f"Prioridad: {prioridad}, Tarea: {tarea}")

        elif opcion == "4":
            mostrar_grafo()

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
