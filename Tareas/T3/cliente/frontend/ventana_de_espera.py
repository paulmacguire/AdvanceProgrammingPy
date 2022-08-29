import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSignal

class VentanaEspera(QDialog):

    senal_abrir_ventana_de_juego = pyqtSignal(str, list)

    def __init__(self):
        super(VentanaEspera, self).__init__()
        loadUi(os.path.join("cliente","frontend","archivos_ui","ventana_de_espera.ui"), self)

    def mostrar_ventana_espera(self):
        self.show()

    def cerrar_ventana_espera(self):
        self.close()

    def preparar_ventana_espera(self, username, usuarios):
        
        if len(usuarios) == 1:
            self.label_jugador1.setText(usuarios[0])

        if len(usuarios) == 2:
            self.label_jugador1.setText(usuarios[0])
            self.label_jugador2.setText(usuarios[1])

        if len(usuarios) == 3:
            self.label_jugador1.setText(usuarios[0])
            self.label_jugador2.setText(usuarios[1])
            self.label_jugador3.setText(usuarios[2])

        if len(usuarios) == 4:
            self.label_jugador1.setText(usuarios[0])
            self.label_jugador2.setText(usuarios[1])
            self.label_jugador3.setText(usuarios[2])
            self.label_jugador4.setText(usuarios[3])

            """ self.cerrar_ventana_espera() """
            self.senal_abrir_ventana_de_juego.emit(username, usuarios)
            
            