from parametros import PROBABILIDAD_EVENTO, PORCENTAJE_APUESTA_TACANO, BONIFICACION_TACANO,\
    MULTIPLICADOR_BONIFICACION_BEBEDOR, BONIFICACION_SUERTE_CASUAL, FRUSTRACION_PERDER, \
    CONFIANZA_PERDER, EGO_GANAR, CARISMA_GANAR, FRUSTRACION_GANAR, \
    MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE

from abc import ABC, abstractmethod
from random import randint, random
import funciones2


class Jugador:
    def __init__(self, n, e, s, d, f, eg, p, car, conf, jf):
        self.nombre = n
        self._energia = int(e)
        self._suerte = int(s)
        self._dinero = int(d)
        self._frustracion = int(f)
        self._ego = int(eg)
        self.personalidad = str(p)
        self.juegos_jugados = []
        self._carisma = int(car)
        self._confianza = int(conf)
        self.juego_favorito = jf

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if valor < 0:
            self._energia = 0
        elif valor > 100:
            self._energia = 100
        else:
            self._energia = valor

    @property
    def suerte(self):
        return self._suerte

    @suerte.setter
    def suerte(self, valor):
        if valor < 0:
            self._suerte = 0
        elif valor > 50:
            self._suerte = 50
        else:
            self._suerte = valor

    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, dinero_restante):
        if dinero_restante < 0:
            self._dinero = 0
        else:
            self._dinero = dinero_restante

    @property
    def frustracion(self):
        return self._frustracion

    @frustracion.setter
    def frustracion(self, valor):
        if valor < 0:
            self._frustracion = 0

        elif valor > 100:
            self._frustracion = 100

        else:
            self._frustracion = valor

    @property
    def ego(self):
        return self._ego

    @ego.setter
    def ego(self, valor):
        if valor < 0:
            self._ego = 0
        elif valor > 15:
            self._ego = 15
        else:
            self._ego = valor

    @property
    def carisma(self):
        return self._carisma

    @carisma.setter
    def carisma(self, valor):
        if valor < 0:
            self._carisma = 0

        elif valor > 50:
            self._carisma = 50

        else:
            self._carisma = valor

    @property
    def confianza(self):
        return self._confianza

    @confianza.setter
    def confianza(self, valor):
        if valor < 0:
            self._confianza = 0
        elif valor > 30:
            self._confianza = 30
        else:
            self._confianza = valor


    def comprar_bebestible(self, bebestible):

        if self.dinero >= bebestible.precio:
            self.dinero -= bebestible.precio
            print(
                f"Ha comprado {bebestible.nombre_bebestible} por {bebestible.precio}")
        else:
            print("No posee suficiente dinero para comprar el bebestible.")

    def apostar(self, apuesta, juego):  
        pass


class Ludopata(Jugador):
    def __init__(self, n, e, s, d, f, eg, p, car, conf, jf):
        super().__init__(n, e, s, d, f, eg, p, car, conf, jf)

    # ESTE INDICE CAMBIARÁ SI EL JUGADOR DECIDE APOSTAR. True si es que GANA. False si es que pierde.
    def ludopatia(self, resultado_final):
        if resultado_final == True:
            self.ego += 2
            self.suerte += 3
            print("¡Usted es un ludópata!. Su ego ha aumentado en 2.")
            print("¡Usted es un ludópata!. Su suerte ha aumentado en 3")

        elif resultado_final == False:
            self.frustracion += 5
            print("Parece que está un poco frustrado. Su frustación aumentó en 5")

    def apostar(self, apuesta, juego):

        energia_gastada = round((self.ego + self.frustracion)*0.15)
        self.energia -= energia_gastada
        self.juegos_jugados.append(juego.nombre_juego)

        if juego.probabilidad_de_ganar(self, apuesta) >= random():  
            self.dinero += apuesta*2
            resultado_final_juego = True
            print(
                f"Usted ha ganado. Ha terminado con {apuesta*2}$ extra de lo que tenía en el inicio.")
        elif juego.probabilidad_de_ganar(self, apuesta) <= random():  
            self.dinero -= apuesta
            resultado_final_juego = False
            print(f"Lo sentimos, usted ha perdido {apuesta}$")
        print(
            f"Debido a su esfuerzo durante el juego, ha gastado {energia_gastada} de su energía.")
        self.ludopatia(resultado_final_juego)


class Tacano(Jugador):
    def __init__(self, n, e, s, d, f, eg, p, car, conf, jf):
        super().__init__(n, e, s, d, f, eg, p, car, conf, jf)

    # ESTE INDICE CAMBIARÁ SI EL JUGADOR DECIDE APOSTAR. True si es que GANA. False si es que pierde.
    def tacano_extremo(self, apuesta, resultado_final):
        if apuesta <= PORCENTAJE_APUESTA_TACANO*self.dinero:
            if resultado_final == True:
                self.dinero += BONIFICACION_TACANO
                print("¡Ha recibido una bonificación por ser un verdadero tacaño!")
            elif resultado_final == False:
                print("Lo siento, no puede recibir su bonificación ya que perdió.")

        else:
            print("Parece que hoy no anda tan tacaño. ")

    def apostar(self, apuesta, juego):

        energia_gastada = round((self.ego + self.frustracion)*0.15)
        self.energia -= energia_gastada
        self.juegos_jugados.append(juego.nombre_juego)

        if juego.probabilidad_de_ganar(self, apuesta) >= random():  
            self.dinero += apuesta*2
            resultado_final_juego = True
            print(
                f"Usted ha ganado. Ha terminado con {apuesta*2}$ extra de lo que tenía en el inicio.")
            self.tacano_extremo(apuesta, resultado_final_juego)

        elif juego.probabilidad_de_ganar(self, apuesta) <= random():  
            self.dinero -= apuesta
            resultado_final_juego = False
            print(f"Lo sentimos, usted ha perdido {apuesta*2}$")
            print(
                f"Debido a su esfuerzo durante el juego, ha gastado {energia_gastada} de su energía.")
            self.tacano_extremo(apuesta, resultado_final_juego)


class Bebedor(Jugador):
    def __init__(self, n, e, s, d, f, eg, p, car, conf, jf):
        super().__init__(n, e, s, d, f, eg, p, car, conf, jf)

    def cliente_recurrente(self):
        return MULTIPLICADOR_BONIFICACION_BEBEDOR

    def apostar(self, apuesta, juego):

        
        energia_gastada = round((self.ego + self.frustracion)*0.15)
        self.energia -= energia_gastada
        self.juegos_jugados.append(juego.nombre_juego)

        if juego.probabilidad_de_ganar(self, apuesta) >= random():  
            self.dinero += apuesta*2
            resultado_final_juego = True
            print(
                f"Usted ha ganado. Ha terminado con {apuesta*2}$ extra de lo que tenía en el inicio.")
        elif juego.probabilidad_de_ganar(self, apuesta) <= random():  
            self.dinero -= apuesta
            resultado_final_juego = False
            print(f"Lo sentimos, usted ha perdido {apuesta}$")
        print(
            f"Debido a su esfuerzo durante el juego, ha gastado {energia_gastada} de su energía.")


class Casual(Jugador):
    def __init__(self, n, e, s, d, f, eg, p, car, conf, jf):
        self.numero_juegos_jugados = 0
        super().__init__(n, e, s, d, f, eg, p, car, conf, jf)

    def suerte_principante(self):
        return BONIFICACION_SUERTE_CASUAL
    
    def apostar(self, apuesta, juego):  

        
        energia_gastada = round((self.ego + self.frustracion)*0.15)
        self.energia -= energia_gastada
        self.juegos_jugados.append(juego.nombre_juego)
        
        if self.numero_juegos_jugados == 0:

            if juego.probabilidad_de_ganar_casual(self, apuesta)>= random():  
                self.dinero += apuesta*2
                print(
                    f"Usted ha ganado. Ha terminado con {apuesta*2}$ extra de lo que tenía en el inicio.")
                self.numero_juegos_jugados += 1

            elif juego.probabilidad_de_ganar_casual(self, apuesta) <= random():  
                self.dinero -= apuesta
                print(f"Lo sentimos, usted ha perdido {apuesta}$")
                self.numero_juegos_jugados += 1
            print(f"Debido a su esfuerzo durante el juego, ha gastado {energia_gastada} de su energía.")

        else:
            if juego.probabilidad_de_ganar_casual(self, apuesta)>= random():
                self.dinero += apuesta*2
                print(
                    f"Usted ha ganado. Ha terminado con {apuesta*2}$ extra de lo que tenía en el inicio.")

            elif juego.probabilidad_de_ganar_casual(self, apuesta) <= random():
                self.dinero -= apuesta
                print(f"Lo sentimos, usted ha perdido {apuesta}$")
            print(f"Debido a su esfuerzo durante el juego, ha gastado {energia_gastada} de su energía.")
    
