from TDA_monticulo import MonticuloColaPrioridades,Heap, heap_lleno, heap_vacio, agregar, atencion
from random import randint
cola_prioridades = MonticuloColaPrioridades()

def menu():
    while True:
        print("\n=== Cola de Prioridades ===")
        print("1. Insertar tarea")
        print("2. Extraer tarea con mayor prioridad")
        print("3. Obtener todas las prioridades")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            prioridad = input("Ingrese la prioridad de la tarea: ")
            tarea = input("Ingrese la descripción de la tarea: ")
            cola_prioridades.insertar(int(prioridad), tarea)
            print(f"Tarea '{tarea}' con prioridad {prioridad} insertada con éxito.")

        elif opcion == "2":
            if not heap_vacio(cola_prioridades.heap):
                maxima_tarea = cola_prioridades.extraer_maximo()
                print("Tarea con la mayor prioridad:", maxima_tarea)
            else:
                print("La cola de prioridades está vacía.")

        elif opcion == "3":
            prioridades = cola_prioridades.obtener_prioridades()
            tareas = [(prioridad, cola_prioridades.buscar_tarea(prioridad)) for prioridad in prioridades]
            print("Prioridades:")
            for prioridad, tarea in tareas:
                print(f"Prioridad: {prioridad}, Tarea: {tarea}")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()


