from PyQt5.QtCore import pyqtSignal, QObject

from frontend.ventana_de_inicio import VentanaInicio
from frontend.ventana_de_espera import VentanaEspera
from frontend.ventana_de_juego import VentanaJuego


class Interfaz(QObject):
    senal_abrir_ventana_inicio = pyqtSignal()
    senal_abrir_ventana_espera = pyqtSignal()
    senal_preparar_ventana_espera = pyqtSignal(str, list)
    senal_login_rechazado = pyqtSignal()

    
    def __init__(self, parent):    
        super().__init__()
        self.ventana_inicio = VentanaInicio()
        self.ventana_de_espera = VentanaEspera()
        self.ventana_de_juego = VentanaJuego()

    
        # ------------------------------------------------------------------ Señales

        # Señales ventana de inicio para validar el usuario
        self.ventana_inicio.senal_enviar_login.connect(parent.enviar_mensaje)

        # Señales

        self.ventana_de_espera.senal_abrir_ventana_de_juego.connect(self.mostrar_ventana_de_juego)
        
        
        # Señales interfaz
        self.senal_preparar_ventana_espera.connect(self.ventana_de_espera.preparar_ventana_espera)
        
        self.senal_abrir_ventana_espera.connect(self.abrir_ventana_de_espera)
        

        self.senal_login_rechazado.connect(self.ventana_inicio.mostrar_error)

    def mostrar_ventana_inicio(self):
        self.ventana_inicio.mostrar_ventana_inicio()

    def abrir_ventana_de_espera(self):
        self.ventana_inicio.cerrar_ventana_inicio()
        self.ventana_de_espera.mostrar_ventana_espera()

    def mostrar_ventana_de_juego(self,username,usuarios):
        self.ventana_de_espera.cerrar_ventana_espera()
        self.ventana_de_juego.mostrar_ventana_de_juego(username,usuarios)
    
    
    
    def manejar_mensaje(self, mensaje: dict):

        try:
            comando = mensaje["comando"]

        except KeyError:
            return {}

        if comando == "respuesta_validacion_login":
            if mensaje["estado"] == "aceptado":
                nombre_usuario = mensaje["nombre_usuario"]
                usuarios = mensaje["usuarios"].split(",")

                self.senal_preparar_ventana_espera.emit(nombre_usuario, usuarios)
                self.senal_abrir_ventana_espera.emit()
            else:
                self.senal_login_rechazado.emit()

        

