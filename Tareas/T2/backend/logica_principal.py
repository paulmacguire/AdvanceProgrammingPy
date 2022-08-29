from PyQt5.QtCore import QObject, pyqtSignal
import os


RUTA_UI_VENTANA_PRINCIPAL = os.path.join(
    "frontend", "assets", "ventana_principal.ui")


class LogicaPrincipal(QObject):

    senal_respuesta_validacion = pyqtSignal(str, bool, list, int)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario, contador):
        nombre = usuario
        estado = False
        lista = []

        if nombre.isalnum() and len(nombre) != 0:
            estado = True
            self.senal_respuesta_validacion.emit(nombre, estado, lista, contador)

        else:
            if len(nombre) == 0:

                estado = False
                lista.append("Alfanumérico")
                lista.append("Largo")
                self.senal_respuesta_validacion.emit(nombre, estado, lista, contador)

            elif not nombre.isalnum():
                estado = False

                lista.append("Alfanumérico")
                self.senal_respuesta_validacion.emit(nombre, estado, lista, contador)

