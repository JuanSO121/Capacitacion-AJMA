import networkx as nx
import matplotlib.pyplot as plt
from Training_Monticulos.TDA_monticulo import MonticuloColaPrioridades, heap_vacio
import streamlit as st

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
    st.pyplot(fig)


def practica():
    st.title("Programa de Monticulos")
    st.write("Este programa te permitir reforzar tus conocimientos sobre monticulos .")
    
    opciones = [
        "Insertar tarea",
        "Extraer tarea con mayor prioridad",
        "Obtener todas las prioridades",
        "Mostrar gráfico"
    ]

    opcion = st.selectbox("Menu", opciones)
    
    if opcion == "Insertar tarea":
        st.subheader("Insertar tarea")
        form = st.form(key="insertar_tarea_form")
        with form:
            prioridad = st.text_input("Ingrese la prioridad de la tarea:")
            tarea = st.text_input("Ingrese la descripción de la tarea:")
            submit_button = st.form_submit_button(label="Enviar")
        if submit_button:
            cola_prioridades.insertar(int(prioridad), tarea)
            st.success(f"Tarea '{tarea}' con prioridad {prioridad} insertada con éxito.")

    elif opcion == "Extraer tarea con mayor prioridad":
        st.subheader("Extraer tarea con mayor prioridad")
        if not heap_vacio(cola_prioridades.heap):
            maxima_tarea = cola_prioridades.extraer_maximo()
            st.write("Tarea con la mayor prioridad:", maxima_tarea)
        else:
            st.write("La cola de prioridades está vacía.")

    elif opcion == "Obtener todas las prioridades":
        st.subheader("Obtener todas las prioridades")
        prioridades = cola_prioridades.obtener_prioridades()
        tareas = [(prioridad, cola_prioridades.buscar_tarea(prioridad)) for prioridad in prioridades]
        st.write("Prioridades:")
        for prioridad, tarea in tareas:
            st.write(f"Prioridad: {prioridad}, Tarea: {tarea}")

    elif opcion == "Mostrar gráfico":
        st.subheader("Mostrar gráfico")
        mostrar_grafo()

    else:
        st.write("Opción inválida. Por favor, seleccione una opción válida.")
