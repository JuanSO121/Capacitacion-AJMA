import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from TrainingArboles.TDA_Arbol import Arbol, Nodo, dfs_preorden, mostrar_arbol, mostrar_arbol_con_networkx

arbol = Arbol(Nodo("raiz"))

# st.set_option('deprecation.showDuplicateWidgetID', False)



def practica():
    st.title("Programa de Árboles")
    st.write("Este programa te permitirá conocer las partes de un árbol.")
    
    opciones = {
        "Agregar nodo": "1",
        "Eliminar nodo": "2",
        "Buscar nodo": "3",
        "Visualizar árbol": "4",
        "Mostrar partes del árbol": "5",
    }
    st.sidebar.title("Practica Arboles")
    
    while True:
        
        descripcion_opciones = list(opciones.keys())
        opcion_seleccionada = st.selectbox("Seleccione una opción:", descripcion_opciones, key="menu_opcion")

        opcion = opciones[opcion_seleccionada]
        
        if opcion == "1":
            valor = st.text_input("Ingrese el valor del nodo:", key="agregar_valor")
            padre_valor = st.text_input("Ingrese el valor del padre (Inicial: raiz):", key="agregar_padre")
            if padre_valor == "raiz":
                arbol.agregar_nodo(valor, arbol.raiz)
            else:
                padre = arbol.buscar_nodo(padre_valor)
                if padre is not None:
                    arbol.agregar_nodo(valor, padre)
                else:
                    st.write("El nodo padre no existe")
                    
        elif opcion == "2":
            valor = st.text_input("Ingrese el valor del nodo a eliminar:", key="eliminar_valor")
            nodo = arbol.buscar_nodo(valor)
            if nodo is not None:
                arbol.eliminar_nodo(nodo)
            else:
                st.write("El nodo no existe")
        elif opcion == "3":
            valor = st.text_input("Ingrese el valor del nodo a buscar:", key="buscar_valor")
            nodo = arbol.buscar_nodo(valor)
            if nodo is not None:
                st.write("Nodo encontrado")
            else:
                st.write("Nodo no encontrado")
        elif opcion == "4":
            fig = mostrar_arbol_con_networkx(arbol)
            st.pyplot(fig)
        elif opcion == "5":
            mostrar_arbol(arbol)

