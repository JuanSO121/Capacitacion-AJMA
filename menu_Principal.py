from Training_Grafos_Interfaz.Menu_Grafo import menu_Grafos
from TrainingArboles.menu_Arbol import menu_Arboles
import streamlit as st 
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from PIL import Image

# funcion animacion
# Configuración de la página de la aplicación web

def catgar_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_codigo = catgar_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")
imagen_video = Image.open("src/eevee.jpg")

def menu():
    st.sidebar.title("Bienvenido al Training")
    st.sidebar.subheader("Por favor seleccione el tema desea aprender")
    opciones = ["Grafos","Arboles","Monticulos"]
    seleccion = st.sidebar.selectbox("Menu",opciones)
    if seleccion =="Grafos":
        menu_Grafos()
        st.write("lo que sea")
        st.write("[Mas informacion>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")
    elif seleccion =="Arboles":  
        menu_Arboles()    
        st.write("lo que sea")
        st.write("[Mas informacion>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")

menu()

with st.container():
    st.write("---")
    columna_izq,columna_der = st.columns(2)

    with columna_izq:
        st.header("Primero")
        # """ --> Salto de linea
        st.write("""Lo que tengamos que poner""")
        st.write("[Video>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")
        
    with columna_der:
        st_lottie(lottie_codigo, height=300, key="coding")
        
with st.container():
    st.write("---")
    columna_imagen,columna_texto = st.columns((1, 2))
    with columna_imagen:
        st.image(imagen_video)
    with columna_texto:
        st.write("""Aqui se ponen cosas""")
        st.markdown("[ver video...](https://www.youtube.com/watch?v=zeS2FlxF_0s)")


    
