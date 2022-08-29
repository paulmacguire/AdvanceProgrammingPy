from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_RAP,
                        AFINIDAD_STAFF_RAP, AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_RAP,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    
    @property
    def afinidad_con_publico(self):
        return self._afinidad_con_publico

    @afinidad_con_publico.setter
    def afinidad_con_publico(self,valor):
        if valor > 100:
            self._afinidad_con_publico = 100
        elif valor < 0:
            self._afinidad_con_publico = 0

    @property
    def afinidad_con_staff(self):
        return self._afinidad_con_staff

    @afinidad_con_staff.setter
    def afinidad_con_staff(self,valor):
        if valor > 100:
            self._afinidad_con_staff = 100
        elif valor < 0:
            self._afinidad_con_staff = 0
    
    @property
    def animo(self):
        return self.afinidad_con_publico*0.5 + self.afinidad_con_staff*0.5        

    def recibir_suministros(self, suministro):
        if suministro.valor_de_satisfaccion > 0:
            self.afinidad_con_staff += suministro.valor_de_satisfaccion
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones.")
            if self.afinidad_con_staff > 100:
                self.afinidad_con_staff = 100

        elif suministro.valor_de_satisfaccion < 0:
            self.afinidad_con_staff += suministro.valor_de_satisfaccion
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")
            if self.afinidad_con_staff < 0:
                self.afinidad_con_staff = 0 
            
        return self.afinidad_con_staff

    def cantar_hit(self):
        # COMPLETAR
        pass

    def __str__(self):
        # COMPLETAR
        pass


class ArtistaPop:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaRock:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaRap:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaReggaeton:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass
