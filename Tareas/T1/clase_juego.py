from parametros import PROBABILIDAD_EVENTO, PORCENTAJE_APUESTA_TACANO, BONIFICACION_TACANO,\
    MULTIPLICADOR_BONIFICACION_BEBEDOR, BONIFICACION_SUERTE_CASUAL, FRUSTRACION_PERDER, \
    CONFIANZA_PERDER, EGO_GANAR, CARISMA_GANAR, FRUSTRACION_GANAR, \
    MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE

from abc import ABC, abstractmethod
from random import randint, random
import funciones2


class Juego:
    def __init__(self, nombre_juego, esperanza_juego, apuesta_minima_juego, apuesta_maxima_juego):
        self.nombre_juego = nombre_juego
        self.esperanza_juego = int(esperanza_juego)
        self.apuesta_minima = int(apuesta_minima_juego)
        self.apuesta_maxima = int(apuesta_maxima_juego)

    # Resultado_final = True, si gana. Resultado_final = False, si pierde
    def entregar_resultados(self, jugador, resultado_final):
        if resultado_final == False:
            jugador.frustracion += FRUSTRACION_PERDER
            jugador.confianza -= CONFIANZA_PERDER
        
        elif resultado_final == True:
            jugador.ego += EGO_GANAR
            jugador.carisma += CARISMA_GANAR
            jugador.frustracion -= FRUSTRACION_GANAR

    def probabilidad_de_ganar(self, jugador, apuesta):
        if self.nombre_juego == jugador.juego_favorito:
            probabilidad_ganar_jugador = min(
                1, max(0, (jugador.suerte*15 - apuesta*0.4 + jugador.confianza*3*1+jugador.carisma*2)/1000))
            probabilidad_ganar_final = min(
                1, probabilidad_ganar_jugador - ((apuesta-(1*50)-(self.esperanza_juego*30))/10000))  # VER VALOR DE FAVORITO

        elif self.nombre_juego != jugador.juego_favorito:
            probabilidad_ganar_jugador = min(
                1, max(0, (jugador.suerte*15 - apuesta*0.4 + jugador.confianza*3*0+jugador.carisma*2)/1000))
            probabilidad_ganar_final = min(
                1, probabilidad_ganar_jugador - ((apuesta-(0*50)-(self.esperanza_juego*30))/10000))  # VER VALOR DE FAVORITO

        return probabilidad_ganar_final


def probabilidad_de_ganar_casual(self, jugador, apuesta):
    if self.nombre_juego == jugador.juego_favorito:
        probabilidad_ganar_jugador = min(
            1, max(0, (jugador.suerte*15 - apuesta*0.4 + jugador.confianza*3*1+jugador.carisma*2)/1000))
        probabilidad_ganar_final = min(
            1, (probabilidad_ganar_jugador + jugador.suerte_principiante() - ((apuesta-(1*50)-(self.esperanza_juego*30))/10000)))  # VER VALOR DE FAVORITO

    elif self.nombre_juego != jugador.juego_favorito:
        probabilidad_ganar_jugador = min(
            1, max(0, (jugador.suerte*15 - apuesta*0.4 + jugador.confianza*3*0+jugador.carisma*2)/1000))
        probabilidad_ganar_final = min(
            1, (probabilidad_ganar_jugador + jugador.suerte_principiante() - ((apuesta-(0*50)-(self.esperanza_juego*30))/10000)))  # VER VALOR DE FAVORITO

    return probabilidad_ganar_final
