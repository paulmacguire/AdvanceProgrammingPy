import sys
from urllib.parse import quote_plus
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap


class MiVentana(QWidget):

    def __init__(self, *args, **kwargs):
        """
        Este método inicializa la ventana.
        """
        super().__init__(*args, **kwargs)

        # Llamamos a un método propio que inicializa los elementos de la ventana
        self.init_gui()

    def init_gui(self):
        """
        Este método configura la interfaz y todos sus widgets,
        posterior a __init__().
        """
        # Ajustamos la geometría de la ventana y su título
        self.setGeometry(200, 100, 500, 500)
        self.setWindowTitle('Buenas')

        self.label1 = QLabel('Texto:', self)
        self.label1.move(10, 15)

        self.label2 = QLabel('Esta etiqueta es variable:', self)
        self.label2.move(10, 50)

        self.edit = QLineEdit('', self) #Con este método hacemos un cuadro de texto
        self.edit.setGeometry(45, 15, 100, 20)

        self.edit2 = QLineEdit("", self)
        self.edit2.setGeometry(135, 50, 100, 20)

        pixeles = QPixmap("menu_cocina.jpg")

        self.label_imagen = QLabel(self)
        self.label_imagen.setGeometry(10, 70, 100, 100)

        self.label_imagen.setPixmap(pixeles)
        self.label_imagen.setScaledContents(True)

        # Se ocupa QPushButton para agregar un botón.

        self.boton1 = QPushButton("Botón culiao", self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(10,180)

        self.show()


if __name__ == '__main__':
    """
    Recordar que en el programa principal debe existir una instancia de
    QApplication ANTES de crear los demas widgets, incluida la ventana
    principal.
    Si la aplicación no recibe parámetros desde la línea de comandos,
    QApplication recibe una lista vacia como QApplication([]).
    """

    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
