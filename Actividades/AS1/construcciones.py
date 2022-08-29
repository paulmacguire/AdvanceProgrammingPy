from abc import ABC, abstractmethod
from random import randint, random, choice
from unidades import Guerrero, Mago, MagoGuerrero
from parametros import PROB_CRITICO_MURO, PROB_CRITICO_CATAPULTA, \
    HP_MUROCATAPULTA, PROB_CRITICO_MURO_CATAPULTA, \
    HP_BARRACAS, HP_MURO, HP_CATAPULTA


# Recuerda que es una clase abstracta
class Estructura(ABC):

    def __init__(self, edad, *args):
        # No modificar
        super().__init__(*args)
        self.edad = edad
        self.asignar_atributos_segun_edad()

    # ---------------
    # Completar los métodos abstractos aquí
    @abstractmethod
    def asignar_atributos_segun_edad(self):
        pass

    @abstractmethod
    def accion(self):
        pass

    def avanzar_edad(self):
        pass

    # ---------------


# Recuerda completar la herencia
class Barracas(Estructura):

    def __init__(self, *args):
        # Completar
        self.hp = HP_BARRACAS
        super().__init__(*args)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.unidades = ["Guerrero", "Mago"]

        elif self.edad == "Moderna":
            self.unidades = ["Guerrero", "Mago", "MagoGuerrero"]

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.unidades.append("MagoGuerrero")

    # ---------------

    def accion(self):
        # No modificar
        elegido = choice(self.unidades)
        suerte = choice((True, False))
        experiencia = choice([1, 2, 3, 4, 5, 6])
        energia = choice([1, 2, 3, 4, 5, 6])
        if elegido == "Guerrero":
            return elegido, Guerrero(suerte, xp=experiencia, stamina=energia)
        elif elegido == "Mago":
            return elegido, Mago(suerte, xp=experiencia, stamina=energia)
        elif elegido == "MagoGuerrero":
            atributos = {"bendito": suerte, "armado": suerte, "xp": experiencia,
                         "stamina": energia}
            return elegido, MagoGuerrero(**atributos)


# Recuerda completar la herencia
class Muro(Estructura):

    def __init__(self, *args, **kwargs):
        # Completar
        self.hp = HP_MURO
        super().__init__(*args, **kwargs)
        pass

    # ---------------
    # Completar los métodos aquí

    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.reparacion = [20, 80]

        elif self.edad == "Moderna":
            self.reparacion = [40, 100]

    def accion(self):
        if random() < PROB_CRITICO_MURO:
            valor_aleatorio = randint(
                self.reparacion[0], self.reparacion[1])
            return valor_aleatorio*2

        else:
            return valor_aleatorio

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.reparacion = [40, 100]
    # ---------------


# Recuerda completar la herencia
class Catapulta(Estructura):

    def __init__(self, *args):
        # Completar
        self.hp = HP_CATAPULTA
        super().__init__(*args)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.ataque = [40, 100]

        elif self.edad == "Moderna":
            self.ataque = [80, 100]

    def accion(self):
        if random() < PROB_CRITICO_CATAPULTA:
            valor_aleatorio = randint(self.ataque[0], self.ataque[1])
            return valor_aleatorio*2

        else:
            return valor_aleatorio

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.ataque = [80, 140]
    # ---------------


# Recuerda completar la herencia
class MuroCatapulta(Muro, Catapulta):

    def __init__(self, *args):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
