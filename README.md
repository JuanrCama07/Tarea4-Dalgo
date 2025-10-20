# Instrucciones de Ejecución de cada parte de la tarea:

    Parte 1: Esta parte consta de 3 algoritmos que implementan una solución al mismo problema. 
    
        A tener en cuenta: Todos los archivos de entrada .txt deben estar en la misma carpeta que el archivo .py en cuestión

        1. Ubicarse en la carpeta /Parte 1:
        2. Ejecutar el siguiente comando: 

            python parte_1.py <algoritmo> <archivo.txt>

            <algoritmo> = dijkstra | bellman-ford | floyd-warshall
            <archivo.txt> = distances5.txt | distances100.txt | distances1000.txt

        3. El resultado de la ejecución se imprimirá directamente en consola acompañado del tiempo de ejecución.

# ---------------------------------------------------------------------------------------------------------------------------

    Parte 2: 

        A tener en cuenta: Todos los archivos de entrada .txt deben estar en la misma carpeta que el archivo .py en cuestión

        1. Ubicarse en la carpeta /Parte 2:
        2. Ejecutar el siguiente comando: 

            python particiones_BFS.py <archivo.txt>

# ---------------------------------------------------------------------------------------------------------------------------

    Parte 3:

        A tener en cuenta: Este programa no recibe archivos.txt, recibe datos directamente:

        1. Ubicarse en la carpeta /Parte 3:
        2. Ejecutar el siguiente comando:

            python convertir_vias_KRUSKAL.py "<grafo>" "<costos>"

            donde:

                grafo = {0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [4], 4: []}
                costos = {(0, 1): 4, (0, 2): 3, (1, 2): 2, (1, 3): 6, (2, 3): 5, (2, 4): 7, (3, 4): 4}

            Importante: Poner tanto la estructura de "grafo" como "costos" entre comillas.

# ---------------------------------------------------------------------------------------------------------------------------

    Parte 4:

        A tener en cuenta: Este programa no recibe archivos.txt, recibe datos directamente:

        1. Ubicarse en la carpeta /Parte 4:
        2. Ejecutar el siguiente comando:

            python flujo_maximo_libros.py "<grafo>" "<fuente>" "<sumidero>"

            donde:

                grafo = {'A': {'B': 10, 'C': 5}, 'B': {'E': 10, 'F': 5}, 'C': {'F': 10}, 'D': {'B': 15}, 'E': {}, 'F': {}}
                fuente = A
                sumidero = F

            Importante: Poner tanto la estructura de "grafo" como los valores de "fuente" y "sumidero" entre comillas.