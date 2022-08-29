"""
Modulo contiene funciones auxiliares
"""
import json
import os


def data_json(llave):
    """
    Lee parametros.json y retorna el valor del dato con la key correspondiente
    """
    ruta = os.path.join("cliente","parametros.json")
    with open(ruta, "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    valor = diccionario_data[llave]
    return valor


def guardar_archivo(bytes_, ruta):
    with open(ruta, "wb") as archivo:
        archivo.write(bytes_)
    return True
