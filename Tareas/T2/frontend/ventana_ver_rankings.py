import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
import parametros as p



class VentanaRankings(QDialog):
    
    senal_cerrar_ventana_ranking = pyqtSignal()
    
    def __init__(self):
        super(VentanaRankings, self).__init__()
        loadUi(p.RUTA_UI_VENTANA_VER_RANKINGS, self)
        self.boton_volver_incio.clicked.connect(self.cerrar_ventana_ranking_volver)
        
        with open("puntajes.txt", encoding="utf-8") as puntajes:
            lista_de_elementos = []
            for lineas in puntajes:
                jugador = lineas.strip("\n").split(",")
                lista_de_elementos.append(jugador)

        lista_usuarios = []
        lista_puntajes = []

        for usuario in lista_de_elementos:
            lista_usuarios.append(usuario[0])
            lista_puntajes.append(int(usuario[1]))
            
        lista_top5 = []
        for _ in range(5):
            puntaje = max(lista_puntajes)
            indice = lista_puntajes.index(puntaje)
    
            jugador_pop = lista_usuarios.pop(indice)
            puntaje_pop = lista_puntajes.pop(indice)

            lista_top5.append([jugador_pop, puntaje_pop])

        self.primero_ranking.setText(lista_top5[0][0])
        self.segundo_ranking.setText(lista_top5[1][0])
        self.tercero_ranking.setText(lista_top5[2][0])
        self.cuarto_ranking.setText(lista_top5[3][0])
        self.quinto_ranking.setText(lista_top5[4][0])

        self.puntaje_primero_rank.setText(str(lista_top5[0][1]))
        self.puntaje_segundo_rank.setText(str(lista_top5[1][1]))
        self.puntaje_tercero_rank.setText(str(lista_top5[2][1]))
        self.puntaje_cuarto_rank.setText(str(lista_top5[3][1]))
        self.puntaje_quinto_rank.setText(str(lista_top5[4][1]))

    def mostrar_ventana_ranking(self):
        self.show()

    def cerrar_ventana_ranking_volver(self):
        self.close()
        self.senal_cerrar_ventana_ranking.emit()

        



