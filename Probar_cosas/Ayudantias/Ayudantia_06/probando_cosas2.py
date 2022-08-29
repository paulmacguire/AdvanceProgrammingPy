import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.init_gui()

    def init_gui(self):
        # Método que configura todos los widgets de la ventana.
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Página con título")
        self.label1 = QLabel("Ingrese el texto:",self)
        self.edit1 = QLineEdit("",self)
        """ self.edit1.resize(100,20) """
        self.boton1 = QPushButton("&Calcular", self)
        """ self.boton1.resize(self.boton1.sizeHint()) """


        self.label2 = QLabel("Hola:",self)
        self.edit2 = QLineEdit("",self)
        """ self.edit2.resize(200,20) """
        self.boton2 = QPushButton("&Proceso", self)
        """ self.boton2.resize(self.boton1.sizeHint()) """


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.edit1)
        hbox.addWidget(self.boton1)
        hbox.addStretch()
        hbox.addWidget(self.label2)
        hbox.addWidget(self.edit2)
        hbox.addWidget(self.boton2)

        self.setLayout(hbox)
        

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.edit1)
        vbox.addWidget(self.boton1)
        vbox.addStretch()
        vbox.addWidget(self.label2)
        vbox.addWidget(self.edit2)
        vbox.addWidget(self.boton2)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())
