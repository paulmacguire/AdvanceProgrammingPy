from distutils.log import error
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap
import parametros as p
import os


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # CCOMPLETAR

        # Usuario
        self.label_nombre = QLabel("Usuario:")
        self.usuario_edit = QLineEdit("", self)

        caja_usuario = QHBoxLayout()
        caja_usuario.addStretch(5)
        caja_usuario.addWidget(self.label_nombre)
        caja_usuario.addWidget(self.usuario_edit)
        caja_usuario.addStretch(1)

        # Contraseña
        self.label_contrasena = QLabel("Contraseña:")
        self.contrasena_edit = QLineEdit("", self)
        self.contrasena_edit.setEchoMode(QLineEdit.Password)
        caja_contrasena = QHBoxLayout()
        caja_contrasena.addStretch(1)
        caja_contrasena.addWidget(self.label_contrasena)
        caja_contrasena.addWidget(self.contrasena_edit)
        caja_contrasena.addStretch(1)

        # Botones

        self.ingresar_boton = QPushButton("Ingresar")
        self.ingresar_boton.clicked.connect(self.enviar_login)
        caja_boton = QVBoxLayout()
        caja_boton.addStretch(5)
        caja_boton.addWidget(self.ingresar_boton)

        # Logo

        self.logo = QLabel(self)
        self.logo.setMaximumSize(300, 300)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setGeometry(80, 50, 500, 300)
        caja_logo = QHBoxLayout()
        caja_logo.addStretch(1)
        caja_logo.addWidget(self.logo)
        caja_logo.addStretch(1)

        # Layout definitivo

        vbox = QVBoxLayout()
        vbox.addStretch(5)

        vbox.addLayout(caja_usuario)
        vbox.addLayout(caja_contrasena)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addLayout(caja_boton)
        hbox.addStretch(1)
        self.setLayout(hbox)

        pass

    def enviar_login(self):
        # COMPLETAR
        usuario = self.usuario_edit.text()
        contrasena = self.contrasena_edit.text()
        tupla = (usuario, contrasena)
        self.senal_enviar_login.emit(tupla)

        pass

    def recibir_validacion(self, valid, errores):
        # COMPLETAR
        if valid:
            self.hide()
        
        else:
            if ("Usuario" in errores) and ("Contraseña" in errores):
                self.usuario_edit.setText("")
                self.usuario_edit.setPlaceholderText("Usuario inválido!")

                self.contrasena_edit.setText("")
                self.contrasena_edit.setPlaceholderText("Contraseña inválida")
            
            elif "Usuario" in errores:
                self.usuario_edit.setText("")
                self.usuario_edit.setPlaceholderText("Usuario inválido!")
            
            elif "Contraseña" in errores:
                self.contrasena_edit.setText("")
                self.contrasena_edit.setPlaceholderText("Contraseña inválida")

            

        
        pass


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.crear_elementos()
    ventana.show()
    sys.exit(app.exec_())
