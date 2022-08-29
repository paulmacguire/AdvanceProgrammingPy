from parametros import PROBABILIDAD_EVENTO, PORCENTAJE_APUESTA_TACANO, BONIFICACION_TACANO,\
    MULTIPLICADOR_BONIFICACION_BEBEDOR, BONIFICACION_SUERTE_CASUAL, FRUSTRACION_PERDER, \
    CONFIANZA_PERDER, EGO_GANAR, CARISMA_GANAR, FRUSTRACION_GANAR, \
    MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE

from abc import ABC, abstractmethod
from random import randint, random
import funciones2

class Casino:
    def __init__(self):
        pass

    def evento_especial(self):
        if randint(1, 10)/10 == PROBABILIDAD_EVENTO:
            print(f"*** ¡¡¡Evento especial!!! ***")
            lista_de_bebestibles = funciones2.abrir_archivo("bebestibles.csv")
            lista_bebestible_aleatorio = lista_de_bebestibles[randint(
                0, len(lista_de_bebestibles))]
            nombre_bebestible_aleatorio = lista_bebestible_aleatorio[0]
            tipo_bebestible_aleatorio = lista_bebestible_aleatorio[1]
            print(f"Ha ingerido {nombre_bebestible_aleatorio}")
            
            return nombre_bebestible_aleatorio, tipo_bebestible_aleatorio

        else:
            print(f"Lo siento, no hay evento especial para usted.")

    def jugar_casino(self):
        pass