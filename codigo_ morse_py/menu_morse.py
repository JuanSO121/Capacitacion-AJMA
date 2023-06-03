from codigo_morse import ArbolMorse

def mostrar_menu():
    print("MENU")
    print("1. Decodificar mensaje en código Morse")
    print("2. Codificar mensaje en código Morse")
    print("3. Mostrar árbol de código Morse")
    print("4. Salir")

def decodificar_mensaje(arbol):
    codigo_morse = input("Ingrese el mensaje en código Morse: ")
    mensaje_decodificado = arbol.decode_morse_code(codigo_morse)
    print("Mensaje decodificado:", mensaje_decodificado)

def codificar_mensaje(arbol):
    mensaje = input("Ingrese el mensaje a codificar: ")
    mensaje_codificado = arbol.encode_message(mensaje)
    print("Mensaje codificado en código Morse:", mensaje_codificado)

def mostrar_arbol(arbol):
    arbol.mostrar_arbol()


arbol = ArbolMorse()

# Insertar los caracteres en el árbol de código Morse
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

# Menú principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        decodificar_mensaje(arbol)
    elif opcion == '2':
        codificar_mensaje(arbol)
    elif opcion == '3':
        mostrar_arbol(arbol)
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
