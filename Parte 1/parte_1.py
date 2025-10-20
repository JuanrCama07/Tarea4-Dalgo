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
def hallar_costos_minimos_dijkstra(grafo, inicio):
    
    costos_minimos = {}
    
    for vertice in grafo:
        costos_minimos[vertice] = 999999
    
    costos_minimos[inicio] = 0
    
    cola = []
    heapq.heappush(cola, (inicio, 0))
    
    while len(cola) > 0:
        vertice_actual, costo_actual = heapq.heappop(cola)
        
        if costo_actual > costos_minimos[vertice_actual]:
            pass
        
        for vecino in grafo[vertice_actual]:
            peso_vecino = grafo[vertice_actual][vecino]
            nuevo_costo = costo_actual + peso_vecino
            
            if nuevo_costo < costos_minimos[vecino]:
                costos_minimos[vecino] = nuevo_costo
                
                heapq.heappush(cola, (vecino, nuevo_costo))
            
    return costos_minimos

'''
Param: Recibe el archivo de conexiones.txt
Return: Retorna la matriz de costos mínimos entre todo par de vértices del grafo.
'''

def matriz_costos_minimos_dijkstra (archivo):
    
    inicio_tiempo = time.time()
    
    grafo = construir_grafo_desde_archivo(archivo)
    
    vertices = list(grafo.keys())
    
    n = len(vertices)
    
    matriz = []
    
    for i in range (n):
        fila = []
        for j in range(n):
            fila.append(0)
        matriz.append(fila)
        
    for i in vertices:
        costos_minimos = hallar_costos_minimos_dijkstra(grafo, i)
        
        for j in vertices:
            matriz[i][j] = costos_minimos[j]
            
    fin_tiempo = time.time()
    
    tiempo_total = (fin_tiempo - inicio_tiempo) * 1000
    print(f"⏱️ Tiempo total de ejecución: {tiempo_total:.6f} ms")
            
    return matriz

#---------------------------------------------------------------------------------------------------
# BELLMAN-FORD
#---------------------------------------------------------------------------------------------------

def matriz_costos_minimos_bellmanford(archivo):
    
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
        
    aristas = []
    for arista in grafo:
        for vertice, peso in grafo[arista].items():
            aristas.append((arista, vertice, peso))
            
    for vertice_actual in vertices:
        distancias = [float("inf")] * n
        distancias[vertice_actual] = 0
        
        for i in range(n-1):
            for arista, vertice, peso in aristas:
                if distancias[arista] + peso < distancias[vertice]:
                    distancias[vertice] = distancias[arista] + peso
                    
        matriz_costos[vertice_actual] = distancias
        
    fin_tiempo = time.time()
    
    tiempo_total = (fin_tiempo - inicio_tiempo) * 1000
    print(f"⏱️ Tiempo total de ejecución: {tiempo_total:.6f} ms")
    
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
    print(f"⏱️ Tiempo total de ejecución: {tiempo_total:.6f} ms")
    
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
        print(matriz_costos_dijkstra)
        
    elif algoritmo == "bellman-ford" or algoritmo == "bellmanford":
        print("Algoritmo: Bellman-Ford")
        matriz_costos_bellmanford = matriz_costos_minimos_bellmanford(archivo)
        print(matriz_costos_bellmanford)
        
    elif algoritmo == "floyd-warshall" or algoritmo == "floydwarshall":
        print("Algoritmo: Floyd-Warshall")
        matriz_costos_floydwarshall = matriz_costos_minimos_floydwarshall(archivo)
        print(matriz_costos_floydwarshall)
        
    else:
        print("Algoritmo no reconocido. Usa uno de los siguientes:")
        print("- dijkstra")
        print("- bellman-ford")
        print("- floyd-warshall")
