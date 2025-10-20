from collections import deque

def BFS(grafo_residual, fuente, sumidero, padre):
    vertices_visitados = set()
    cola = deque([fuente])
    vertices_visitados.add(fuente)
    
    while len(cola) > 0:
        vertice_actual = cola.popleft()
        for vertice, capacidad in grafo_residual.get(vertice_actual, {}).items():
            if vertice not in vertices_visitados and capacidad > 0:
                padre[vertice] = vertice_actual
                vertices_visitados.add(vertice)
                cola.append(vertice)
                if vertice == sumidero:
                    return True
    return False

def flujo_maximo_edmonds_karp(grafo, fuente, sumidero):
    grafo_residual = {}
    for vertice_actual, conexiones in grafo.items():
        grafo_residual[vertice_actual] = dict(conexiones)

    flujo_maximo = 0
    padre = {}

    while BFS(grafo_residual, fuente, sumidero, padre):
        camino_flujo = float("inf")
        vertice = sumidero
        while vertice != fuente:
            vertice_anterior = padre[vertice]
            camino_flujo = min(camino_flujo, grafo_residual[vertice_anterior][vertice])
            vertice = padre[vertice]
        
        vertice = sumidero
        while vertice != fuente:
            vertice_anterior = padre[vertice]
            grafo_residual[vertice_anterior][vertice] -= camino_flujo
            if vertice not in grafo_residual:
                grafo_residual[vertice] = {}
            grafo_residual[vertice].setdefault(vertice_anterior, 0)
            grafo_residual[vertice][vertice_anterior] += camino_flujo
            vertice = padre[vertice]
        
        flujo_maximo += camino_flujo

    return flujo_maximo

# Ejecución del Algoritmo

import sys
import ast

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    try:
        grafo = ast.literal_eval(sys.argv[1])
        fuente = sys.argv[2]
        sumidero = sys.argv[3]
    except Exception as e:
        print("Error")
        sys.exit(1)

    maximo_libros = flujo_maximo_edmonds_karp(grafo, fuente, sumidero)
    print(f"Flujo máximo de libros: {maximo_libros}")
    
'''
Ejemplo de entrada: 

    Si grafo = {'A': {'B': 10, 'C': 5}, 'B': {'E': 10, 'F': 5}, 'C': {'F': 10}, 'D': {'B': 15}, 'E': {}, 'F': {}}
    fuente = A
    y sumidero = F

    python flujo_maximo_libros.py "{'A': {'B': 10, 'C': 5}, 'B': {'E': 10, 'F': 5}, 'C': {'F': 10}, 'D': {'B': 15}, 'E': {}, 'F': {}}" "A" "F"
'''