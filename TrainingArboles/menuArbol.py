from explicacion_Arbol import explicacion
from practica_Arbol import practica
# streamlit run app.py
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
    st.title("Training Arboles")
    opciones = ["Inicio","Explicacion","Practica"]
    seleccion = st.sidebar.selectbox("Menu",opciones)
    if seleccion =="Explicacion":
        with st.container():
            st.subheader("Bienvenido al Training")
            st.title("Introduccion sobre Arboles")
            explicacion()
            st.write("lo que sea")
            st.write("[Mas informacion>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")
    elif seleccion =="Practica":
        with st.container():
            
            st.title("Practica tus saberes sobre Arboles")
            practica()
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


    
