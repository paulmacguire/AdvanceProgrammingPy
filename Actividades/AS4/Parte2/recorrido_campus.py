from Parte2.campus import Lugar
from collections import deque

def comprobar_chismoso(lugar: Lugar):
    # NO MODIFICAR
    for ayudante in lugar.ayudantes:
        if "Croak" in ayudante.frase:
            return True
    return False


def bfs_iterativo(inicio: Lugar, final: Lugar):
    # Completar
    # Contenidos Semana 12 3-recorrido Ejemplo BFS

    visitados = []
    trayecto_de_la_persona = []
    cola_de_destinos = deque([inicio])
    

    while len(cola_de_destinos) > 0:
        vertice = cola_de_destinos.popleft()

        if vertice in visitados:
            continue

        print(vertice)
        visitados.append(vertice)

    # Todo esto como dije antes lo saqué de los contenidos de la semana 12
        for lugares_vecinos in vertice.vecinos:
            if comprobar_chismoso(lugares_vecinos) == False:
                trayecto_de_la_persona.append(lugares_vecinos)
                cola_de_destinos.append(lugares_vecinos)

                if lugares_vecinos == final:
                    return True

    return False


def dfs_iterativo(inicio: Lugar, final: Lugar):
    # Completar
    pass

def bfs_iterativo_largo(inicio: Lugar, final: Lugar):
    # Completar 
    # Contenidos Semana 12 3-recorrido Ejemplo BFS

    visitados = []
    trayecto_de_la_persona = []
    cola_de_destinos = deque([inicio])
    contador = 0
    

    while len(cola_de_destinos) > 0:
        vertice = cola_de_destinos.popleft()

        if vertice in visitados:
            continue

        print(vertice)
        visitados.append(vertice)

    # Todo esto como dije antes lo saqué de los contenidos de la semana 12
        for lugares_vecinos in vertice.vecinos:
            if comprobar_chismoso(lugares_vecinos) == False:
                trayecto_de_la_persona.append(lugares_vecinos)
                cola_de_destinos.append(lugares_vecinos)


                if lugares_vecinos == final:
                    return len(visitados)  
    
    pass


def dfs_iterativo_largo(inicio: Lugar, final: Lugar):
    # Completar 
    pass


def bfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    

def dfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    
    
def creador_camino(diccionario_padres, final):
    # NO MODIFICAR
    camino = []
    camino.append(final)
    while diccionario_padres[final] is not None:
        camino.append(diccionario_padres[final])
        final = diccionario_padres[final]
    camino.reverse()
    return camino


def imprimir_camino(camino):
    # NO MODIFICAR
    recorrido = ""
    largo = len(camino)
    contador = 1
    for lugar in camino:
        if contador < largo:
            recorrido = recorrido + f"[{lugar.nombre}] -> "
        else:
            recorrido = recorrido + f"[{lugar.nombre}]."
        contador += 1
    print(recorrido)

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
