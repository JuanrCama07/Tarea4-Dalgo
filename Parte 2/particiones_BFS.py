from collections import deque

def construir_grafo_desde_archivo(nombre_archivo):
    
    grafo = {}

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split()

            if len(partes) != 3:
                continue

            a, b, c = map(int, partes)

            if a not in grafo:
                grafo[a] = {}

            grafo[a][b] = c

    return grafo

def componentes_conectados_bfs (distancias):
    
    grafo = construir_grafo_desde_archivo(distancias)
    
    vertices_visitados = set ()
    componentes = []
    
    for vertice in grafo:
        if vertice not in vertices_visitados:
            cola = deque([vertice])
            componente = set([vertice])
            vertices_visitados.add(vertice)
            
            while len(cola) > 0:
                vertice_actual = cola.popleft()
                for vecino in grafo[vertice_actual]:
                    if vecino not in vertices_visitados:
                        vertices_visitados.add(vecino)
                        componente.add(vecino)
                        cola.append(vecino)
                        
            componentes.append(componente)
            
    return componentes

# Ejecución del Algoritmo

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    nombre_archivo = sys.argv[1]
    componentes_conectados = componentes_conectados_bfs(nombre_archivo)
    print(componentes_conectados)