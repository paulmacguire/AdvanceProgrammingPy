import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSignal


class VentanaInicio(QDialog):

    senal_enviar_login = pyqtSignal(dict)
    """ senal_enviar_login_todos = pyqtSignal(dict) """

    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi(os.path.join("cliente", "frontend",
               "archivos_ui", "ventana_de_inicio.ui"), self)
        self.boton_jugar_ventana_inicio.clicked.connect(self.enviar_login)

        self.mostrar_ventana_inicio()

    def mostrar_ventana_inicio(self):
        self.show()

    def cerrar_ventana_inicio(self):
        self.close()

    def enviar_login(self):
        nombre_usuario = self.line_edit_nombre_usuario.text()
        diccionario = {
            "comando": "validar_login",
            "nombre usuario": nombre_usuario,
        }
        self.senal_enviar_login.emit(diccionario)
        """ self.senal_enviar_login_todos.emit(diccionario) """

    def mostrar_error(self):
        self.label_error_ingresar_usuario.setText(
            "No cumple con el formato deseado, intente nuevamente.")
