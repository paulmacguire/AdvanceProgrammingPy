from parametros import PROBABILIDAD_EVENTO, PORCENTAJE_APUESTA_TACANO, BONIFICACION_TACANO,\
    MULTIPLICADOR_BONIFICACION_BEBEDOR, BONIFICACION_SUERTE_CASUAL, FRUSTRACION_PERDER, \
    CONFIANZA_PERDER, EGO_GANAR, CARISMA_GANAR, FRUSTRACION_GANAR, \
    MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE

from abc import ABC, abstractmethod
from random import randint, random
import funciones2


class Bebestibles(ABC):
    def __init__(self, nombre_bebestible, tipo, precio):
        self.nombre_bebestible = str(nombre_bebestible)
        self.tipo = str(tipo)
        self.precio = int(precio)

    @abstractmethod
    def consumir_bebestible(self):
        pass


class Jugo(Bebestibles):
    def __init__(self, nombre_bebestible, tipo, precio):
        super().__init__(nombre_bebestible, tipo, precio)

    # jugador corresponde a una instancia de Jugador
    def consumir_bebestible(self, jugador):
        if self.tipo == "Jugo":
            if len(self.nombre_bebestible) <= 4:
                jugador.ego += 4
                print("¡Su ego ha aumentado en 4!")

            elif 5 <= len(self.nombre_bebestible) <= 7:
                jugador.suerte += 7
                print("Al parecer has tenido bastante suerte... tu suerte aumentó en 7")

            elif len(self.nombre_bebestible) >= 8:
                jugador.frustracion -= 10
                jugador.ego += 11
                print("¡Jugando has disminuido tu frustración en 10!")
                print("¡Su ego ha aumentado en 11!")
        else:
            print("No está consumiendo jugo. Consuma otro bebestible.")


class Gaseosa(Bebestibles):
    def __init__(self, nombre_bebestible, tipo, precio):
        super().__init__(nombre_bebestible, tipo, precio)

    def consumir_bebestible(self, jugador):
        if self.tipo == "Gaseosa":
            if (jugador.personalidad == "Tacano") or (jugador.personalidad == "Ludopata"):
                jugador.frustracion -= 5
                jugador.ego += 6
                print(
                    "Debido a que usted presenta índices de tacaño o de ludópata, su frustración disminuyó en 5.")

            elif (jugador.personalidad == "Bebedor") or (jugador.personalidad == "Casual"):
                if jugador.personalidad == "Bebedor":
                    jugador.frustracion += 5*jugador.cliente_recurrente()
                    jugador.ego += 6
                    print(
                        "Debido a que usted es una persona bebedora y/o casual,\
                            su frustración ha aumentado en 7.5")
                else:
                    jugador.frustracion += 5
                    jugador.ego += 6
                    print(
                        "Debido a que usted es una persona bebedora y/o casual,\
                            su frustración ha aumentado en 5")

            jugador.energia += randint(MIN_ENERGIA_BEBESTIBLE,
                                       MAX_ENERGIA_BEBESTIBLE)
            print("Como usted toma bastante gaseosa, su ego ha aumentado en 6.")

        else:
            print("No está consumiendo gaseosa. Consuma otro bebestible.")


class BrebajeMagico(Bebestibles):
    def __init__(self, nombre_bebestible, tipo, precio):
        super().__init__(nombre_bebestible, tipo, precio)

    def consumir_bebestible(self, jugador):
        if self.tipo == "Brebaje mágico":
            if len(self.nombre_bebestible) <= 4:
                jugador.ego += 4
                print("¡Su ego ha aumentado en 4!")

            elif 5 <= len(self.nombre_bebestible) <= 7:
                jugador.suerte += 7
                print("Al parecer has tenido bastante suerte... tu suerte aumentó en 7")

            elif len(self.nombre_bebestible) >= 8:
                jugador.frustracion -= 10
                jugador.ego += 11
                print("¡Jugando has disminuido tu frustración en 10!")
                print("¡Su ego ha aumentado en 11!")

            if (jugador.personalidad == "Tacano") or (jugador.personalidad == "Ludopata"):
                jugador.frustracion -= 5
                print(
                    "Debido a que usted presenta índices de tacaño o de ludópata, su frustración disminuyó en 5.")

            elif (jugador.personalidad == "Bebedor") or (jugador.personalidad == "Casual"):
                if jugador.personalidad == "Bebedor":
                    jugador.frustracion += 5*jugador.cliente_recurrente()
                    print(
                        "Debido a que usted es una persona bebedora y/o casual, su frustración ha aumentado en 7.5.")
                else:
                    jugador.frustracion += 5
                    print(
                        "Debido a que usted es una persona bebedora y/o casual, su frustración ha aumentado en 5.")
            jugador.carisma += 5
            print(
                "Como usted toma bastante brebaje mágico, su carisma ha aumentado en 5.")

        else:
            print("No está consumiendo un Brebaje Mágico. Consuma otro bebestible.")
