import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from TDA_RojoNegro import ArbolRojoNegro

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
    st.pyplot(plt)

arbol = ArbolRojoNegro()

def arbolRN():
    st.title("Programa de Árboles")
    st.write("Este programa te permitirá conocer las partes de un árbol.")

    opciones = [
        "¿Qué es un árbol rojo-negro?",
        "Mostrar partes del árbol",
        "Mostrar altura del árbol",
        "Insertar nodo",
        "Eliminar nodo",
        "Visualizar árbol"
    ]
    st.sidebar.title("Arboles Rojo-Negro")

    opcion = st.selectbox("Menu", opciones)

    if opcion == "¿Qué es un árbol rojo-negro?":
        st.write("Un árbol rojo-negro es un tipo de árbol binario de búsqueda balanceado. Se caracteriza por tener las siguientes propiedades:")
        st.write("- Cada nodo es rojo o negro.")
        st.write("- La raíz es negra.")
        st.write("- Todas las hojas (nodos nulos) son negras.")
        st.write("- Si un nodo es rojo, entonces ambos hijos son negros.")
        st.write("- Para cada nodo, todos los caminos simples desde ese nodo hasta las hojas descendientes contienen el mismo número de nodos negros.")

    elif opcion == "Mostrar partes del árbol":
        st.write("Las partes de un árbol rojo-negro son:")
        st.write("- Nodo: Cada elemento almacenado en el árbol se representa como un nodo.")
        st.write("- Raíz: Es el nodo superior del árbol.")
        st.write("- Hoja: Es un nodo nulo que representa un valor no presente en el árbol.")
        st.write("- Padre: Es el nodo que está directamente por encima de un nodo dado.")
        st.write("- Hijo: Son los nodos que están directamente debajo de un nodo dado.")

    elif opcion == "Mostrar altura del árbol":
        st.write("La altura del árbol es:", arbol.altura())

    elif opcion == "Insertar nodo":
        st.write("Insertar nodo:")
        with st.form(key="agregar_nodo_form"):
            dato = st.text_input("Ingrese el dato del nodo:")
            submit_button = st.form_submit_button("Agregar")
            if submit_button:
                arbol.insertar(dato)
                st.success("Nodo insertado correctamente.")

    elif opcion == "Eliminar nodo":
        st.write("Eliminar nodo:")
        with st.form(key="eliminar_nodo_form"):
            dato = st.text_input("Ingrese el dato del nodo a eliminar:")
            submit_button = st.form_submit_button("Eliminar")
            if submit_button:
                arbol.eliminar(int(dato))
                st.success("Nodo eliminado correctamente.")

    elif opcion == "Visualizar árbol":
        visualizar_arbol(arbol)

if __name__ == "__main__":
    arbolRN()
