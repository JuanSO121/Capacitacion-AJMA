from Arboles.codigo_morse import ArbolMorse
import streamlit as st

def mostrar_arbol(arbol, mensaje):
    mensaje_decodificado = arbol.decode_morse_code(mensaje)
    st.write("Mensaje decodificado:", mensaje_decodificado)
    arbol_temporal = ArbolMorse()
    for char in mensaje_decodificado:
        arbol_temporal.insertar(char, arbol._obtener_diccionario_morse().get(char, ''))
    arbol_temporal.mostrar_arbol()

# Crear el árbol de código Morse
arbol = ArbolMorse()
arbol.insertar('A', '.-')
arbol.insertar('B', '-...')
arbol.insertar('C', '-.-.')
arbol.insertar('D', '-..')
arbol.insertar('E', '.')
arbol.insertar('F', '..-.')
arbol.insertar('G', '--.')
arbol.insertar('H', '....')
arbol.insertar('I', '..')
arbol.insertar('J', '.---')
arbol.insertar('K', '-.-')
arbol.insertar('L', '.-..')
arbol.insertar('M', '--')
arbol.insertar('N', '-.')
arbol.insertar('O', '---')
arbol.insertar('P', '.--.')
arbol.insertar('Q', '--.-')
arbol.insertar('R', '.-.')
arbol.insertar('S', '...')
arbol.insertar('T', '-')
arbol.insertar('U', '..-')
arbol.insertar('V', '...-')
arbol.insertar('W', '.--')
arbol.insertar('X', '-..-')
arbol.insertar('Y', '-.--')
arbol.insertar('Z', '--..')

def morse():
    # Mostrar el formulario para ingresar la frase a codificar o decodificar
    modo = st.selectbox('Seleccione el modo:', ['Codificar', 'Decodificar', 'Mostrar árbol de código Morse'])
    frase = st.text_input('Ingrese la frase a codificar o decodificar en código Morse:')

    submitted = st.button('Enviar')

    if submitted:
        if frase:
            if modo == 'Codificar':
                codificado = arbol.encode_message(frase)
                st.success('Frase codificada con éxito al código Morse')
                st.code(codificado)
            elif modo == 'Decodificar':
                decodificado = arbol.decode_morse_code(frase)
                st.success('Frase decodificada al español:')
                st.write(decodificado)
            elif modo == "Mostrar árbol de código Morse":
                if frase:
                    mostrar_arbol(arbol, frase)
                else:
                    st.warning('Ingrese la frase en código Morse que desee visualizar en el árbol.')
        else:
            st.warning('Ingrese la frase que desees procesar.')
