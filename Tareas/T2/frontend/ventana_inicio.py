import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSignal
import parametros as p


class VentanaInicio(QDialog):
    
    senal_entrar_a_jugar = pyqtSignal()
    senal_ver_ranking = pyqtSignal()

    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi(p.RUTA_UI_VENTANA_INICIO, self)
        self.boton_jugar_inicio.clicked.connect(self.ir_a_jugar)
        self.boton_ver_rankings_inicio.clicked.connect(self.ir_a_ver_rankings)

    def ir_a_jugar(self):
        self.close()
        self.senal_entrar_a_jugar.emit()
        
    def ir_a_ver_rankings(self):
        self.close()
        self.senal_ver_ranking.emit()

    def mostrar_ventana_inicio(self):
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    ventana_inicio = VentanaInicio()
    sys.exit(app.exec_())


