from Training_Grafos_Interfaz.Menu_Grafo import menu_Grafos
from Training_Monticulos.menu_Monticulos import menu_Monticulos
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
lottie_study = catgar_lottieurl("https://assets4.lottiefiles.com/packages/lf20_phjobus6.json")
lottie_conexion = catgar_lottieurl("https://assets10.lottiefiles.com/packages/lf20_Fdv4mj.json")
imagen_video = Image.open("src/eevee.jpg")

with st.container():
    columna_izq,columna_der = st.columns(2)

    with columna_izq:
        st.header("Motivación y Persistencia: Avanza hacia el Dominio de los Grafos, Montículos y Árboles")
        # """ --> Salto de linea
    with columna_der:
        st_lottie(lottie_codigo, height=230, key="coding2")
        
def menu():
    st.write("---")
    st.sidebar.title("Bienvenido al Training")
    st.sidebar.subheader("Por favor seleccione el tema desea aprender")
    opciones = ["Grafos","Arboles","Monticulos"]
    seleccion = st.sidebar.selectbox("Menu",opciones)
    
    if seleccion =="Grafos":
        menu_Grafos()
        
    elif seleccion =="Arboles":  
        menu_Arboles()    
    
    elif seleccion =="Monticulos":  
        menu_Monticulos()    

menu()

with st.container():
    st.write("---")
    columna_imagen,columna_texto = st.columns((1, 2))
    with columna_imagen:
        st.image(imagen_video)
    with columna_texto:
        st.write("""Motivación y Persistencia: Avanza hacia el Dominio de los Grafos, Montículos y Árboles: """)
        st.markdown("[ver video...](https://www.youtube.com/watch?v=zeS2FlxF_0s)")