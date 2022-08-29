# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
from collections import namedtuple


def cargar_platos(ruta_archivo: str) -> list:
    lista_de_platos = []
    Platos = namedtuple("Plato_type", "nombre", "categoria",
                        "tiempo", "precio", "ingredientes")
    with open(ruta_archivo, "r") as platos:
        lineas = platos.readlines()
    for preparacion in lineas:
        cada_plato = preparacion.split(",")
        for i in cada_plato:
            
            tupla = Platos()
            lista_de_platos.append(tupla)


pass


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    pass
