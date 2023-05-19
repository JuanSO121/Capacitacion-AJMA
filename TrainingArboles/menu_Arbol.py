from TrainingArboles.explicacion_Arbol import explicacion
from TrainingArboles.practica_Arbol import practica
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

def menu_Arboles():
    
    st.title("Training Arboles")
    opciones = ["Inicio","Explicacion","Practica"]
    seleccion = st.selectbox("Menu",opciones)
    st.write("---")
    
    if seleccion =="Explicacion":
        with st.container():
            st.subheader("Bienvenido al Training")
            st.title("Introduccion sobre Arboles")
            explicacion()
            
    elif seleccion =="Practica":
        with st.container():
            
            st.title("Practica tus saberes sobre Arboles")
            practica()