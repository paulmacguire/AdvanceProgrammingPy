"""
Módulo principal del cliente.
"""
import sys
from os.path import join
from PyQt5.QtWidgets import QApplication
from backend.cliente import Cliente

if __name__ == "__main__":
    # =========> Instanciamos la APP <==========
    
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon(RUTA_ICONO))

    # =========> Iniciamos el cliente <==========
    cliente = Cliente()

    app.exec_()
    


######################### ACORDARME DE BORRAR EL OBJETO CLIENTE EN EL CLIENTE.PY