'''
Param: Archivo conexiones.txt
Return: Grafo de conexiones
'''
import heapq
import time


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

#---------------------------------------------------------------------------------------------------
# DIJKSTRA
#---------------------------------------------------------------------------------------------------

'''
Param: Recibe el grafo de conexiones y un vértice elegido como inicio.
Return: Retorna el diccionario de costos minimos de todo vértice i a todo vértice j.
'''
import heapq
import time

def hallar_costos_minimos_dijkstra(grafo, inicio):

    costos_minimos = {}

    for v in grafo:
        costos_minimos[v] = float('inf')
    costos_minimos[inicio] = 0

    cola = [(0, inicio)]

    while cola:
        costo_actual, vertice_actual = heapq.heappop(cola)

        if costo_actual > costos_minimos[vertice_actual]:
            continue

        for vecino, peso in grafo[vertice_actual].items():
            nuevo_costo = costo_actual + peso

            if nuevo_costo < costos_minimos[vecino]:
                costos_minimos[vecino] = nuevo_costo
                heapq.heappush(cola, (nuevo_costo, vecino))

    return costos_minimos


def matriz_costos_minimos_dijkstra(archivo):
    inicio_tiempo = time.time()

    grafo = construir_grafo_desde_archivo(archivo)
    vertices = sorted(grafo.keys())
    n = len(vertices)
    
    indice = {}

    for i, v in enumerate(vertices):
        indice[v] = i

    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(float('inf'))
    
        matriz.append(fila)

    for i, vertice in enumerate(vertices):
        costos_minimos = hallar_costos_minimos_dijkstra(grafo, vertice)
        for j, destino in enumerate(vertices):
            matriz[i][j] = costos_minimos.get(destino, float('inf'))

    fin_tiempo = time.time()
    tiempo_total = (fin_tiempo - inicio_tiempo) * 1000
    print(f"Tiempo total de ejecución: {tiempo_total:.6f} ms")

    return matriz


#---------------------------------------------------------------------------------------------------
# BELLMAN-FORD
#---------------------------------------------------------------------------------------------------

import time
import math

def matriz_costos_minimos_bellmanford(archivo):
    inicio_tiempo = time.time()

    grafo = construir_grafo_desde_archivo(archivo)
    
    vertices_totales = set()

    for vertice in grafo.keys():
        vertices_totales.add(vertice)

    for vecinos in grafo.values():
        for destino in vecinos:
            vertices_totales.add(destino)

    vertices = sorted(vertices_totales)
    
    n = len(vertices)

    indice = {}

    for i, vertice in enumerate(vertices):

        indice[vertice] = i
    
    matriz_costos = []

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(math.inf)

        matriz_costos.append(fila)
    
    for i in range(n):
        matriz_costos[i][i] = 0
        
    aristas = []
    for vertice_actual, vecinos in grafo.items():
        for vertice_destino, costo in vecinos.items():
            aristas.append((indice[vertice_actual], indice[vertice_destino], costo))

    for i in range(n):
        dist = matriz_costos[i]
        dist[i] = 0

        for _ in range(n - 1):
            respuesta_actualizada = False
            for vertice_actual, vertice_destino, costo in aristas:
                if dist[vertice_actual] != math.inf and dist[vertice_actual] + costo < dist[vertice_destino]:
                    dist[vertice_destino] = dist[vertice_actual] + costo
                    respuesta_actualizada = True
            if not respuesta_actualizada:
                break

    fin_tiempo = time.time()
    print(f"Tiempo total de ejecución: {(fin_tiempo - inicio_tiempo) * 1000:.6f} ms")

    #imprimir_matriz = True

    if globals().get("imprimir_matriz", False):
        for i, origen in enumerate(vertices):
            print(f"Desde {origen}: ", fin="")
            for j, destino in enumerate(vertices):
                costo = matriz_costos[i][j]
                if costo == math.inf:
                    print(f"{destino}: No conecta", fin="  ")
                else:
                    print(f"{destino}: {costo}", fin="  ")
            print()

    return matriz_costos

#---------------------------------------------------------------------------------------------------
# FLOYD-WARSHALL
#---------------------------------------------------------------------------------------------------

def matriz_costos_minimos_floydwarshall(archivo):
    
    inicio_tiempo = time.time()
    
    grafo = construir_grafo_desde_archivo(archivo)
    
    vertices = list(grafo.keys())
    n = len(vertices)
    
    matriz_costos = []
    
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(float("inf"))
        matriz_costos.append(fila)
        
    for i in vertices:
        matriz_costos[i][i] = 0
        for j in grafo[i]:
            matriz_costos[i][j] = grafo[i][j]
            
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if matriz_costos[i][k] + matriz_costos[k][j] < matriz_costos[i][j]:
                    matriz_costos[i][j] = matriz_costos[i][k] + matriz_costos[k][j]
                    
    fin_tiempo = time.time()
    
    tiempo_total = (fin_tiempo - inicio_tiempo) * 1000
    print(f"Tiempo total de ejecución: {tiempo_total:.6f} ms")
    
    return matriz_costos

# Ejecución de los Algoritmos

import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    algoritmo = sys.argv[1].lower()
    archivo = sys.argv[2]
    
    if algoritmo == "dijkstra":
        print("Algoritmo: Dijkstra")
        matriz_costos_dijkstra = matriz_costos_minimos_dijkstra(archivo)
        #print(matriz_costos_dijkstra)
        
    elif algoritmo == "bellman-ford" or algoritmo == "bellmanford":
        print("Algoritmo: Bellman-Ford")
        matriz_costos_bellmanford = matriz_costos_minimos_bellmanford(archivo)
        #print(matriz_costos_bellmanford)
        
    elif algoritmo == "floyd-warshall" or algoritmo == "floydwarshall":
        print("Algoritmo: Floyd-Warshall")
        matriz_costos_floydwarshall = matriz_costos_minimos_floydwarshall(archivo)
        #print(matriz_costos_floydwarshall)
        
    else:
        print("Algoritmo no reconocido. Usa uno de los siguientes:")
        print("- dijkstra")
        print("- bellman-ford")
        print("- floyd-warshall")
