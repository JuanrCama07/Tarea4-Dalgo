def encontrar(padre, vertice):
    
    if padre[vertice] != vertice:
        padre[vertice] = encontrar(padre, padre[vertice])

    return padre[vertice]

def unir(padre, rango, vertice_1, vertice_2):
    raiz_vertice_1 = encontrar(padre, vertice_1)
    raiz_vertice_2 = encontrar(padre, vertice_2)
    
    if raiz_vertice_1 == raiz_vertice_2:
        return False
    
    if rango[raiz_vertice_1] < rango[raiz_vertice_2]:
        padre[raiz_vertice_1] = raiz_vertice_2
    elif rango[raiz_vertice_1] > rango[raiz_vertice_2]:
        padre[raiz_vertice_2] = raiz_vertice_1
    else: 
        padre[raiz_vertice_2] = raiz_vertice_1
        rango[raiz_vertice_1] += 1
    
    return True

def convertir_rutas(grafo, costos):
    
    vertices = list(grafo.keys())
    n = len(vertices)
    
    padre = []
    for i in range (n):
        padre.append(i)
        
    rango = []
    for _ in range (n):
        rango.append(0)
        
    aristas = []
    for arista, vecinos in grafo.items():
        for vecino in vecinos:
            if (arista, vecino) in costos:
                aristas.append((costos[(arista, vecino)], arista, vecino))
                
    aristas.sort(key=lambda c: c[0])
    
    vias_seleccionadas = []
    costo_total = 0
    
    for costo, arista, vecino in aristas:
        if unir(padre, rango, arista, vecino):
            vias_seleccionadas.append((arista, vecino, costo))
            costo_total += costo
            
    print("Vías que deben convertirse en doble vía:")
    for arista, vecino, costo in vias_seleccionadas:
        print(f"   {arista} - {vecino}  (costo {costo})")

    print(f"Costo total mínimo: {costo_total}")
    
    return vias_seleccionadas

# Ejecución del Algoritmo

import ast
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    try:
        grafo = ast.literal_eval(sys.argv[1])
        costos = ast.literal_eval(sys.argv[2])
    except Exception as e:
        print("Error")
        sys.exit(1)
        
    convertir_rutas(grafo, costos)
        
'''
Ejemplo de entrada: 

    Si grafo = {0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [4], 4: []}
    y si costos = {(0, 1): 4, (0, 2): 3, (1, 2): 2, (1, 3): 6, (2, 3): 5, (2, 4): 7, (3, 4): 4}

    python convertir_vias_KRUSKAL.py "{0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [4], 4: []}" "{(0, 1): 4, (0, 2): 3, (1, 2): 2, (1, 3): 6, (2, 3): 5, (2, 4): 7, (3, 4): 4}"
'''
