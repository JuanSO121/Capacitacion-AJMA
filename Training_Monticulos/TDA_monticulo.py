# TDA
import networkx as nx
import matplotlib.pyplot as plt
class Heap(object):
    # Crea un monticulo

    def __init__(self, tamano):
        # Crea el vector vacio para el montículo.
        self.tamano = 0
        self.vector = [None] * tamano

def agregar(heap, dato):
    # Agrega un dato en el montículo

    heap.vector[heap.tamano] = dato
    flotar(heap, heap.tamano)
    heap.tamano += 1

def cantidad_elementos(heap):
    # Devuelve la cantidad de elementos en el monticulo
    return heap.tamano

def heap_vacio(heap):
    # Devuelve true si el montículo esta vacio.
    return heap.tamano == 0

def heap_lleno(heap):
    # Devuelve true si el montículo esta Lleno
    return heap.tamano == len(heap.vector)

def flotar(heap, indice):
    # Flota el elemento en la posición indice
    while (indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]):
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre

def hundir(heap, indice):
    # Hunde el elemento en la posición índice.
    hijo_izq = (indice * 2) + 1
    control = True
    while (control and hijo_izq < heap.tamano):
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if (hijo_der < heap.tamano):
            if heap.vector[hijo_der] > heap.vector[hijo_izq]:
                aux = hijo_der

        if (heap.vector[indice] < heap.vector[aux]):
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False

def intercambio(vector, i, j):
    # Intercambia los elementos en las posiciones i y j del vector.
    vector[i], vector[j] = vector[j], vector[i]

def monticulizar(heap):
    # Transforma un vector en un monticulo
    for i in range(len(heap.vector) // 2, -1, -1):
        hundir(heap, i)

def arribo(heap, dato, prioridad):
    # Arriba el dato a la cola utilizando prioridad
    agregar(heap, [prioridad, dato])

def atencion(heap):
    return quitar(heap)

def quitar(heap):
    intercambio(heap.vector, 0, heap.tamano-1)
    dato = heap.vector[heap.tamano-1]
    heap.tamano -= 1
    hundir(heap, 0)
    return dato


def cambiar_prioridad(heap, indice, prioridad):
    # Cambia la prioridad de un elemento y lo acomoda en el montículo.
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if prioridad > prioridad_anterior:
        flotar(heap, indice)
    elif prioridad < prioridad_anterior:
        hundir(heap, indice)

class MonticuloColaPrioridades:
    def __init__(self):
        self.heap = Heap(100)

    def insertar(self, prioridad, tarea):
        agregar(self.heap, (prioridad, tarea))

    def extraer_maximo(self):
        return atencion(self.heap)[1]
    
    def buscar_tarea(self, prioridad):
        for tupla in self.heap.vector:
            if tupla is not None and tupla[0] == prioridad:
                return tupla[1]
        return None

    def obtener_prioridades(self):
        heap_aux = Heap(len(self.heap.vector))
        vector_aux = []
        
        # Extraer los elementos del heap original sin eliminarlos
        while not heap_vacio(self.heap):
            prioridad, tarea = self.heap.vector[0]
            vector_aux.append(prioridad)
            agregar(heap_aux, (prioridad, tarea))
            intercambio(self.heap.vector, 0, self.heap.tamano - 1)
            self.heap.tamano -= 1
            hundir(self.heap, 0)
        
        # Restaurar el heap original
        while not heap_vacio(heap_aux):
            prioridad, tarea = atencion(heap_aux)
            agregar(self.heap, (prioridad, tarea))

        return vector_aux
