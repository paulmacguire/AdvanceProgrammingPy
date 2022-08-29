import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSignal

class VentanaJuego(QDialog):


    def __init__(self):
        super(VentanaJuego, self).__init__()
        loadUi(os.path.join("cliente","frontend","archivos_ui","ventana_de_juego.ui"), self)

    def mostrar_ventana_de_juego(self,username,usuarios):
        self.show()
        self.preparar_ventana_de_juego(username,usuarios)

    def preparar_ventana_de_juego(self, username, usuarios):
        self.label_turno_jugador_username.setText(username)
        
        self.label_jugador1.setText(usuarios[0])
        self.label_jugador2.setText(usuarios[1])
        self.label_jugador3.setText(usuarios[2])
        self.label_jugador4.setText(usuarios[3])

