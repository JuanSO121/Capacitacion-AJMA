import streamlit as st 
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from PIL import Image
from Training_Monticulos.practica_Monticulo import practica
from Training_Monticulos.Explicacion_Monticulos import explicacion
# funcion animacion
# Configuración de la página de la aplicación web
def catgar_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_codigo = catgar_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")
imagen_video = Image.open("src/eevee.jpg")

def menu_Monticulos():

    st.title("Training Monticulos")
    opciones = ["Inicio","Explicacion","Practica"]
    seleccion = st.selectbox("Menu monticulos",opciones)
    st.write("---")
    if seleccion =="Explicacion":
        with st.container():
            st.subheader("Bienvenido al Training")
            st.title("Introduccion sobre Monticulos")
            explicacion()

    elif seleccion =="Practica":
        with st.container():
            st.title("Practica tus saberes sobre Monticulos")
            practica()