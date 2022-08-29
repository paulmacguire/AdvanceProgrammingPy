"""
Tambien puedes heredar de QTimer para crear timers personalizados, igual que con QThreads.
En la clase de interfaces graficas 2 hay un ejemplo, en esta ayudantia queremos mostrar
su utilidad general.
"""

# Importacion de librerias para todas las celdas del ejemplo
import sys
from time import sleep
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class VentanaConTimer(QWidget):
    actualizar_label_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        # Crear botones y labels
        self.label_numero = QLabel("0", self)
        self.boton_numero = QPushButton("0", self)
        self.boton_loop = QPushButton("Iniciar Loop", self)
        self.layout_principal = QVBoxLayout(self)

        self.timer_epico = QTimer(self)

        self.init_gui()

    def init_gui(self):
        self.layout_principal.addWidget(self.label_numero)
        self.layout_principal.addStretch()
        self.layout_principal.addWidget(self.boton_numero)
        # Conectar las señales
        self.boton_numero.clicked.connect(self.iniciar_loop)
        self.boton_loop.clicked.connect(self.iniciar_loop)
        self.actualizar_label_signal.connect(self.actualizar_label)

        self.show()
        
    def actualizar_label(self):
        numero_actual =  int(self.label_numero.text())
        self.label_numero.setText(str(numero_actual + 1))
        
        if numero_actual == 10:
            self.timer_epico.stop()
        

    def actualizar_boton(self):
        numero_actual = int(self.boton_numero.text())
        self.boton_numero.setText(str(numero_actual + 1))
        
    def iniciar_loop(self):
        # Los timers emiten una senal cada vez que pasa una cantidad de tiempo especificada
        # la cual puedes acceder para conectarla utilizando el atributo timeout.
        self.timer_epico.timeout.connect(self.actualizar_label_signal)
        # Ojo: el tiempo se especifica en milisegundos!
        self.timer_epico.setInterval(1000)
        self.timer_epico.start()
    


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaConTimer()
    #ventana = VentanaConThread()
    #ventana = VentanaConTimer()
    sys.exit(app.exec_())