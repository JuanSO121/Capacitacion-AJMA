# streamlit run app.py
import streamlit as st 
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from PIL import Image

# funcion animacion
def catgar_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_codigo = catgar_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")
imagen_video = Image.open("EjemploTDA de Grafos/ImplementacionGrafos/src/eevee.jpg")

with st.container():
    st.subheader("Bienvenido al Training")
    st.title("Introduccion sobre grafos")
    st.write("lo que sea")
    st.write("[Mas informacion>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")

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
        # """ --> Salto de linea
        st.write("""Lo que tengamos que poner""")
        st.write("[Video>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")