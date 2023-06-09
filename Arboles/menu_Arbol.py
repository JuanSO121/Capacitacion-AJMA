from Arboles.explicacion_Arbol import explicacion
from Arboles.practica_Arbol import practica
from Arboles.menu_morse import morse
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
imagen_video = Image.open("src/Ajma.jpeg")

def menu_Arboles():
    
    st.title("Capacitación de Arboles")
    opciones = ["Inicio","Explicacion","Practica","Practica Codificacion Morse"]
    seleccion = st.selectbox("Menu",opciones)
    st.write("---")
    
    if seleccion =="Explicacion":
        with st.container():
            st.subheader("Bienvenido, aqui podras aprender sobre arboles y sus posibles aplicaciones")
            st.title("Introduccion sobre Arboles")
            explicacion()
            
    elif seleccion =="Practica":
        with st.container():
            
            st.title("Practica tus saberes sobre Arboles")
            practica()
            
    elif seleccion =="Practica Codificacion Morse":
        with st.container():
            
            st.title("Aplicando Arboles en Codificacion Morse")
            morse()