from abc import ABC, abstractmethod
from parametros import PROB_REVIVIR, PROB_CRITICO_GUERRERO, \
    PROB_CRITICO_MAGO, PROB_CRITICO_MAGO_GUERRERO
import math
from random import random


# Recuerda que es una clase abstracta
class Persona(ABC):

    def __init__(self, xp, stamina, **kwargs):
        # No modificar
        super().__init__(**kwargs)
        self.xp = xp
        self.stamina = stamina
        self.asignar_parametros()

    @property
    def stamina(self):
        # No modificar
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        # No modificar
        if value <= 0:
            if not self.revivir():
                print("F")
        else:
            self._stamina = value

    def revivir(self):
        # No modificar
        if PROB_REVIVIR > random():
            self.stamina += 3
            return True
        else:
            return False

    # ---------------
    # Completar los métodos abstractos aquí

    @abstractmethod
    def asignar_parametros(self):
        pass

    @abstractmethod
    def accion(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    # ---------------


# Recuerda completar la herencia
class Guerrero(Persona):

    def __init__(self, armado, **kwargs):
        # Completar
        self.armado = armado
        super().__init__(**kwargs)

        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_parametros(self):
        operacion = 5 * math.pi * self.xp * (1/2)
        operacion = round(operacion)

        if self.armado == True:
            self.ataque = operacion*2

        elif self.armado == False:
            self.ataque = operacion

    def accion(self):
        if random() < PROB_CRITICO_GUERRERO:
            return round(self.ataque*(1.5))

        elif random() >= PROB_CRITICO_GUERRERO:
            return self.ataque

    def __str__(self):

        if self.armado == True:
            return f"Guerrero Armado con {self.ataque} pts de ataque"

        elif self.armado == False:
            return f"Guerrero con {self.ataque} pts de ataque"
    # ---------------


# Recuerda completar la herencia
class Mago(Persona):

    def __init__(self, bendito, **kwargs):
        # Completar
        self.bendito = bendito
        super().__init__(**kwargs)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_parametros(self):
        operacion_curacion = 1.6180 * math.pi * self.xp * (1/2)
        operacion_curacion = round(operacion_curacion)

        if self.bendito == True:
            self.curacion = operacion_curacion*2

    def accion(self):
        if random() < PROB_CRITICO_MAGO:
            return round(self.curacion*(1.5))

        else:
            return self.curacion

    def __str__(self):

        if self.bendito == True:
            return f"Mago BENDITO con {self.curacion} pts de curación"

        elif self.bendito == False:
            return f"Mago con {self.curacion} pts de curación"
    # ---------------


# Recuerda completar la herencia
class MagoGuerrero(Mago, Guerrero):

    def __init__(self, **kwargs):
        # Completar
        super().__init__(**kwargs)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_parametros(self):
        Mago.asignar_parametros()
        Guerrero.asignar_parametros()

    def accion(self):

        if random() < PROB_CRITICO_MAGO_GUERRERO:
            self.curacion *= 2
            self.ataque *= 2

        return(self.curacion, self.ataque)
        

    # ---------------

    def __str__(self):
        # No modificar
        if self.armado and self.bendito:
            return f"MagoGuerrero BENDITO y ARMADO con {self.curacion}" \
                   + f" pts de curación y {self.ataque} pts de ataque."
        else:
            return f"MagoGuerrero con {self.curacion} pts de curación" \
                + f" y {self.ataque} pts de ataque."


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
