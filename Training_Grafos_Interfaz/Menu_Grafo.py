from Training_Grafos_Interfaz.Explicacion_Grafo import explicacion
from Training_Grafos_Interfaz.practica_Grafo import practica
from Training_Grafos_Interfaz.grafos_Puertos import puerto
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


def menu_Grafos():

    st.title("Training Grafos")
    opciones = ["Inicio","Explicacion","Practica","Practica Puertos"]
    
    seleccion = st.selectbox("Menu",opciones)
    st.write("---")
    
    if seleccion =="Explicacion":
        with st.container():
            st.subheader("Bienvenido al Training")
            st.title("Introduccion sobre Grafos")
            explicacion()
            st.write("lo que sea")
            st.write("[Mas informacion>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")
    elif seleccion =="Practica":
        with st.container():
            
            st.title("Practica tus saberes sobre Grafos")
            practica()
            
    elif seleccion =="Practica Puertos":
        with st.container():
            
            st.title("Practica tus saberes sobre Grafos aplicandolos de una forma practica")
            puerto()




        
