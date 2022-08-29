from email.mime import base
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType("regg.ui")


class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        caja_nombre = self.lineEdit.text()
        caja_edad = self.lineEdit_2.text()
        caja_ciudad = self.lineEdit_3.text()
        caja_sexo = self.checkBox.text()

        print(f"Se ha registrado correctamente. Usted es {caja_nombre}.")
        print(f"Su edad es {caja_edad}")
        print(f"Proviene de {caja_ciudad}")
        print(f"Usted es {caja_sexo}")





if __name__ == "__main__":
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec())
