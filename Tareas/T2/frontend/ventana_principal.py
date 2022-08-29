import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QDialog)
from PyQt5.QtCore import pyqtSignal
import parametros as p
import random


class VentanaPrincipal(QDialog):
    senal_iniciar_ventana_principal = pyqtSignal()
    senal_enviar_info_usuario = pyqtSignal(str, int)
    senal_cerrar_ventana_principal = pyqtSignal()
    senal_ir_a_cazar_juego = pyqtSignal()
    senal_iniciar_juego = pyqtSignal(str, str)
    senal_obtener_escenario = pyqtSignal(str)
    senal_mandar_foto_alien_vivo = pyqtSignal(str)
    senal_mandar_foto_alien_muerto = pyqtSignal(str)
    senal_mandar_coordenadas = pyqtSignal(str, int, int)
    senal_mandar_coordenadas2 = pyqtSignal(str, int, int)

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi(p.RUTA_UI_VENTANA_PRINCIPAL, self)
        self.boton_cazar_ventana_principal.clicked.connect(
            self.ingresar_usuario)
        self.boton_volver_al_menu_de_inicio.clicked.connect(
            self.ocultar_ventana_principal_volver)
        self.boton_opcion_tutorial_lunar.clicked.connect(
            self.obtener_escenario_lunar)
        self.boton_opcion_entrenamiento.clicked.connect(
            self.obtener_escenario_entrenamiento)
        self.boton_opcion_invasion.clicked.connect(
            self.obtener_escenario_invasion)
        self.contador_escenario = 0

    def ingresar_usuario(self):
        astronauta = self.line_edit_nombre_astronauta.text()
        self.senal_enviar_info_usuario.emit(
            astronauta, self.contador_escenario)


    """ Lo que hace este metodo es recibir el nombre ingresado en el line edit e ingresarlo en el 
    archivo puntajes.txt con el formato nombre,0 ya que posteriormente se cambiará el puntaje de la
    persona una vez que termine el juego """

    def recibir_validacion(self, nombre, valid, errores, contador):

        if valid and contador != 0:
            with open("puntajes.txt", encoding="utf-8") as puntajes:
                lista_de_elementos = []
                for lineas in puntajes:
                    jugador = lineas.strip("\n").split(",")
                    lista_de_elementos.append(jugador)

            with open("puntajes.txt", "w", encoding="utf-8") as puntajes_finales:
                lista_de_elementos.append([nombre, "0"])
                lista_escribir_archivo = lista_de_elementos
                index = 0
                for usuario in lista_escribir_archivo:
                    if index == 0:
                        linea_final = ",".join(usuario)
                        puntajes_finales.write(linea_final)
                        index += 1
                    else:
                        linea_final = "\n"+",".join(usuario)
                        puntajes_finales.write(linea_final)

            astronauta = self.line_edit_nombre_astronauta.text()
            self.senal_iniciar_juego.emit(nombre, astronauta)
            self.close()

        else:
            if ("Alfanumérico" in errores) and ("Largo" in errores):
                self.label_error.setText("El nombre debe tener mínimo 1 caracter y \
debe ser alfanumérico.")

            elif "Alfanumérico" in errores:
                self.label_error.setText(
                    "El nombre de usuario no es alfanumérico.")

            self.label_error_escenario.setText(
                "Porfavor, ingrese un escenario.")

    def obtener_escenario_lunar(self):
        self.contador_escenario += 1
        self.senal_obtener_escenario.emit(p.RUTA_ESCENARIO_TUTORIAL_LUNAR)

        """ self.senal_mandar_foto_alien_vivo.emit(
            p.RUTA_ALIEN_LUNAR_VIVO)
        self.senal_mandar_foto_alien_muerto.emit(p.RUTA_ALIEN_LUNAR_MUERTO) """
        posicion_x = self.obtener_coordenadas_random()[0]
        posicion_y = self.obtener_coordenadas_random()[1]

        posicion_x2 = self.obtener_coordenadas_random()[0]
        posicion_y2 = self.obtener_coordenadas_random()[1]

        self.senal_mandar_coordenadas.emit(
            p.RUTA_ALIEN_LUNAR_VIVO, posicion_x, posicion_y)
        self.senal_mandar_coordenadas2.emit(
            p.RUTA_ALIEN_LUNAR_VIVO, posicion_x2, posicion_y2)

    def obtener_escenario_entrenamiento(self):
        self.contador_escenario += 1
        self.senal_obtener_escenario.emit(
            p.RUTA_ESCENARIO_ENTRENAMIENTO_JUPITER)
        """ self.senal_mandar_foto_alien_vivo.emit(
            p.RUTA_ALIEN_JUPITER_VIVO)
        self.senal_mandar_foto_alien_muerto.emit(p.RUTA_ALIEN_JUPITER_MUERTO) """
        posicion_x = self.obtener_coordenadas_random()[0]
        posicion_y = self.obtener_coordenadas_random()[1]

        posicion_x2 = self.obtener_coordenadas_random()[0]
        posicion_y2 = self.obtener_coordenadas_random()[1]

        self.senal_mandar_coordenadas.emit(
            p.RUTA_ALIEN_JUPITER_VIVO, posicion_x, posicion_y)
        self.senal_mandar_coordenadas2.emit(
            p.RUTA_ALIEN_JUPITER_VIVO, posicion_x2, posicion_y2)

    def obtener_escenario_invasion(self):
        self.contador_escenario += 1
        self.senal_obtener_escenario.emit(
            p.RUTA_ESCENARIO_INVASION_INTERGALACTICA)
        posicion_x = self.obtener_coordenadas_random()[0]
        posicion_y = self.obtener_coordenadas_random()[1]

        posicion_x2 = self.obtener_coordenadas_random()[0]
        posicion_y2 = self.obtener_coordenadas_random()[1]

        self.senal_mandar_coordenadas.emit(
            p.RUTA_ALIEN_INTERGALACTICO_VIVO, posicion_x, posicion_y)
        self.senal_mandar_coordenadas2.emit(
            p.RUTA_ALIEN_INTERGALACTICO_VIVO, posicion_x2, posicion_y2)


    def mostrar_ventana_principal(self):
        self.show()

    def ocultar_ventana_principal_volver(self):
        self.close()
        self.senal_cerrar_ventana_principal.emit()

    def obtener_coordenadas_random(self):
        posicion_x = random.randint(30, 705)
        posicion_y = random.randint(20, 270)

        return posicion_x, posicion_y
