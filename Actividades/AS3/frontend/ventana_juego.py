from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

import parametros as p


# Recuerda que estamos usando QT Designer :eyes:
# CARGAR ARCHIVO AQUÍ

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)

# COMPLETAR:
class VentanaJuego(window_name, base_class):  # pylint: disable=E0602

    senal_iniciar_juego = pyqtSignal()
    senal_tecla = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # COMPLETAR
        self.setupUi(self)
        self.init_gui()

    def mostrar_ventana(self, usuario):
        # COMPLETAR
        self.show()
        self.casilla_nombre.setText(usuario)
        self.casilla_puntaje.setText(p.PUNTAJE_INICIAL) 
        self.casilla_tiempo.setText(p.TIEMPO_JUEGO)
        self.senal_iniciar_juego.emit()
        pass

    def keyPressEvent(self, event):
        # COMPLETAR
        tecla_apretada = event.text()
        if p.TECLA_ARRIBA == tecla_apretada:
            self.senal_tecla.emit("U")
        elif p.TECLA_ABAJO == tecla_apretada:
            self.senal_tecla.emit("D")
        elif p.TECLA_DERECHA == tecla_apretada:
            self.senal_tecla.emit("R")
        elif p.TECLA_IZQUIERDA == tecla_apretada:
            self.senal_tecla.emit("L")
        
        pass

    def init_gui(self):
        self.setWindowTitle("Ventana de Juego")
        self.boton_salir.clicked.connect(self.salir)

    def actualizar_topos(self, topos):
        for topo in topos:
            topo.topo_label.setParent(self)
            topo.topo_label.setVisible(True)
            topo.topo_label.move(topo.pos_topo.x(), topo.pos_topo.y())

    def mover_martillo(self, martillo):
        martillo.martillo_label.setParent(self)
        martillo.martillo_label.setVisible(True)
        martillo.martillo_label.move(martillo.pos_martillo.x(),
                                     martillo.pos_martillo.y())

    def actualizar_datos(self, tiempo, puntaje):
        self.casilla_tiempo.setText(tiempo)
        self.casilla_tiempo.repaint()

        self.casilla_puntaje.setText(puntaje)
        self.casilla_puntaje.repaint()

    def salir(self):
        self.close()
