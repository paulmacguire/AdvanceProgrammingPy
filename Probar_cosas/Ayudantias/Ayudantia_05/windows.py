import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QPlainTextEdit,
                             QLineEdit)
from PyQt5.QtCore import QCoreApplication, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap


class MailWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("DCCorreos")
        self.boton = QPushButton("Botón")
        self.line = QLineEdit("Emisor")
        self.logo = QLabel(self)
        self.logo.setFixedSize(800, 150)
        self.logo.setGeometry(50, 50, 100, 100)
        vbox_left = QVBoxLayout()
        vbox_left.addWidget(self.boton)
        vbox_left.addWidget(self.line)
        self.setLayout(vbox_left)
