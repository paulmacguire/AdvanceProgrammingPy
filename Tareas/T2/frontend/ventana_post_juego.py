from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QDialog)

import parametros as p


class VentanaPostJuego(QDialog):

    def __init__(self):
        super(VentanaPostJuego, self).__init__()
        loadUi(p.RUTA_UI_VENTANA_POST_JUEGO, self)
        self.boton_salir_post_juego.clicked.connect(
            self.salir_del_juego_ventana_post_juego)

    def mostrar_ventana_post_juego(self, astronauta, balas_restantes, segundos_restantes, puntaje):
        self.label_balas_restantes.setText(str(balas_restantes))
        self.label_tiempo_restante.setText(str(segundos_restantes))
        self.label_puntaje_total.setText(str(puntaje))
        self.label_puntaje_obtenido_nivel.setText(str(puntaje))
        self.nombre_astronauta = astronauta
        self.puntaje_astronauta = str(puntaje)

        self.show()

    def salir_del_juego_ventana_post_juego(self):
        with open("puntajes.txt", encoding="utf-8") as puntajes:
            lista_de_elementos = []
            for lineas in puntajes:
                jugador = lineas.strip("\n").split(",")
                lista_de_elementos.append(jugador)

        with open("puntajes.txt", "w", encoding="utf-8") as puntajes_finales:

            lista_de_elementos[len(
                lista_de_elementos)-1] = [self.nombre_astronauta, str(self.puntaje_astronauta)]
            lista_escribir_archivo = lista_de_elementos
            index = 0
            for usuario in lista_escribir_archivo:
                if index == 0:
                    linea_final = ",".join(usuario)
                    puntajes_finales.write(linea_final)
                    index += 1
                else:
                    linea_final = "\n"+",".join(usuario)
                    puntajes_finales.write(linea_final)
        self.close()
