# Importacion de librerias para todas las celdas del ejemplo
import sys
from time import sleep
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class VentanaSinThread(QWidget):
    actualizar_label_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        # Crear botones y labels
        self.label_numero = QLabel("0", self)
        self.boton_numero = QPushButton("0", self)
        self.boton_loop = QPushButton("Iniciar Loop", self)
        self.layout_principal = QVBoxLayout(self)

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
       

    def actualizar_boton(self):
        numero_actual = int(self.boton_numero.text())
        self.boton_numero.setText(str(numero_actual + 1))
        
    def iniciar_loop(self):
        pass
        # Emitimos la senal 10 veces, con 0.5 segundos de espera entre emisiones.
        for _ in range(10):
            self.actualizar_label_signal.emit()
            sleep(0.5)
        

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaSinThread()
    #ventana = VentanaConThread()
    #ventana = VentanaConTimer()
    sys.exit(app.exec_())