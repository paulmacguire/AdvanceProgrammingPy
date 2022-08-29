""" import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QGridLayout, QVBoxLayout)


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):

        # Creamos una etiqueta para status. Recordar que los widgets simples
        # no tienen StatusBar.
        self.label = QLabel('Status:', self)

        # Creamos la grilla para ubicar los widgets de manera matricial
        self.grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '0', 'CE', 'C']

        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada botón guardados en la lista valores
        posiciones = [(i, j) for i in range(4) for j in range(3)]
        
        for posicion, valor in zip(posiciones, valores):
            boton = QPushButton(valor, self)
            self.grilla.addWidget(boton, *posicion)

        # Creamos un layout vertical
        vbox = QVBoxLayout()

        # Agregamos el label al layout con addWidget
        vbox.addWidget(self.label)

        # Agregamos el layout de la grilla al layout vertical con addLayout
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Calculator')


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_()) """

""" import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)


class MiBoton(QPushButton):
    
    # Recibe dos argumentos extra además de los regulares de QPushButton
    # Un nombre para identificar el botón
    # Una posición para ubicarse en la ventana
    def __init__(self, nombre, pos, *args, **kwargs):
        # Llama al constructor de la clase madre
        super().__init__(*args, **kwargs)
        
        # Asigna el nombre a la instancia
        self.nombre = nombre
        
        # Crea un contador de instancia inicialmente en 0
        self.contador = 0
        
        # Fija su propia geometría
        self.resize(self.sizeHint())
        self.move(*pos)
        
        # La siguiente línea conecta un clic con el método contar
        # Entenderemos mejor esta línea en el siguiente notebook
        self.clicked.connect(self.contar)
        
    # Agregamos comportamiento al botón, aumenta el contador en cada clic
    def contar(self):
        self.contador += 1
        print(f'{self.nombre} apretado {self.contador} veces.')


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        # Fija la geometría de la ventana principal
        self.setGeometry(200, 200, 100, 100)
        self.setMaximumHeight(100)
        self.setMaximumWidth(100)
        
        # Instancia dos botones de nuestra clase, con atributos extra
        # de los que QPushButton está acostumbrado: nombre y posición
        self.boton_1 = MiBoton('Botón 1', (0, 20), 'Aprétame', self)
        self.boton_2 = MiBoton('Botón 2', (0, 60), 'Aprétame', self)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_()) """



import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout, QLineEdit)


class CampoFormulario(QHBoxLayout):
    # Heredamos de Layout Horizontal para colocar cada campo.

    def __init__(self, texto, *args, **kwargs):
        # Llama al constructor de la clase madre
        super().__init__(*args, **kwargs)
        
        # Crea la etiqueta y cuadro correspondientes
        label = QLabel(f"{texto}: ")
        campo = QLineEdit("")
        
        # Los coloca dentro del Layout
        self.addStretch(1)
        self.addWidget(label)
        self.addWidget(campo)
        self.addStretch(1)

class Formulario(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fija datos de ventana
        self.setWindowTitle("Formulario")
        self.setGeometry(200, 200, 400, 400)
        
        # Crea contenedor vertical para colocar los campos
        contenedor = QVBoxLayout()
        
        # Coloca cada campo que creamos
        contenedor.addLayout(CampoFormulario("Nombre"))
        contenedor.addLayout(CampoFormulario("Apellido"))
        contenedor.addLayout(CampoFormulario("Dirección"))
        contenedor.addLayout(CampoFormulario("Correo"))
        contenedor.addLayout(CampoFormulario("Usuario"))
        contenedor.addLayout(CampoFormulario("Contraseña"))
        
        # Fijamos el Layout completo
        self.setLayout(contenedor)
        
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    formulario = Formulario()
    sys.exit(app.exec())
    