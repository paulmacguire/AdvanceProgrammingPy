from PyQt5.uic import loadUi

from PyQt5.QtWidgets import (QDialog, QLabel)

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import parametros as p


class VentanaJuego(QDialog):

    senal_salir_del_juego = pyqtSignal()
    senal_pausar_juego = pyqtSignal(int)
    senal_pausar_mira = pyqtSignal(bool)
    senal_pausar_disparo = pyqtSignal(bool)
    senal_teclas = pyqtSignal(str)
    senal_coordenadas_jugador = pyqtSignal(dict)
    senal_enviar_nombre = pyqtSignal(str)
    senal_iniciar_juego = pyqtSignal()
    senal_disparar = pyqtSignal()
    senal_mover_aliens_muertos = pyqtSignal()
    senal_mover_aliens_muertos2 = pyqtSignal()
    senal_empezar_nuevamente = pyqtSignal(bool)
    senal_ventana_post_juego = pyqtSignal(str, int, int, int)
    senal_salir_del_juego_boton = pyqtSignal()

    def __init__(self):
        super(VentanaJuego, self).__init__()
        loadUi(p.RUTA_UI_VENTANA_JUEGO, self)
        self.boton_salir_del_juego.clicked.connect(self.salir_del_juego)
        self.boton_pausa_ventana_juego.clicked.connect(self.pausar_el_juego)
        self.aliens_explotados = 0
        self.contador_pausa = 0
        self._balas_iniciales = 4
        self._contador_segundos = 0
        self.bloquear_boton_pausa = False
        self.bloqueo_boton_disparo = False
        self.bloqueo_contador_segundos = False
        self.balas_infinitas = False
        self.ya_perdiste = False
        self.lista_teclas_que_se_apretan = []

        self.label_balas.setText(str(self.balas_iniciales))
        self.pixeles_perro = QPixmap(p.RUTA_PERRO)

        self.label_perro_juego.setPixmap(self.pixeles_perro)
        self.label_perro_juego.setScaledContents(True)

    @property
    def balas_iniciales(self):
        return self._balas_iniciales

    @balas_iniciales.setter
    def balas_iniciales(self, valor):
        if valor < 0:
            self._balas_iniciales = 0
        else:
            self._balas_iniciales = valor

    @property
    def contador_segundos(self):
        return self._contador_segundos

    @contador_segundos.setter
    def contador_segundos(self, valor):
        if valor < 0:
            self._contador_segundos = 0
        else:
            self._contador_segundos = valor

    def ingresar_fondo_juego(self, fondo):
        self.label_fondo_juego.setPixmap(QPixmap(fondo))
        self.label_fondo_juego.setScaledContents(True)
        self.timer_nivel = QTimer()
        self.timer_nivel.setInterval(1000)
        self.timer_nivel.setSingleShot(True)
        self.timer_nivel.timeout.connect(self.contador_timer_segundos)
        self.timer_nivel.start()

        if fondo == p.RUTA_ESCENARIO_TUTORIAL_LUNAR:
            self.contador_segundos = p.DURACION_ESCENARIO_LUNAR
            self.ponderador = p.PONDERADOR_TUTORIAL

        if fondo == p.RUTA_ESCENARIO_ENTRENAMIENTO_JUPITER:
            self.contador_segundos = p.DURACION_ESCENARIO_JUPITER
            self.ponderador = p.PONDERADOR_ENTRENAMIENTO

        if fondo == p.RUTA_ESCENARIO_INVASION_INTERGALACTICA:
            self.contador_segundos = p.DURACION_ESCENARIO_INTERGALACTICO
            self.ponderador = p.PONDERADOR_INVASION

    def contador_timer_segundos(self):
        self.timer_nivel.start()
        self.contador_segundos -= 1
        self.label_tiempo.setText(str(self.contador_segundos))
        if not self.bloqueo_contador_segundos:
            self.puntaje = int(((2*100 + (self.contador_segundos *
                                          30 + self.balas_iniciales*70)*1)/self.ponderador)//1)
            self.label_puntaje.setText(str(self.puntaje))
        if self.contador_segundos <= 0 and not self.bloqueo_contador_segundos:
            self.bloqueo_contador_segundos = True
            self.label_nivel_superado_o_no_3.setText(
                "¡Te has quedado sin tiempo!.")
            self.timer_fin = QTimer()
            self.timer_fin.setInterval(5000)
            self.ya_perdiste = True
            self.bloquear_boton_pausa = True
            self.bloqueo_boton_disparo = True
            self.senal_pausar_mira.emit(True)
            self.senal_pausar_disparo.emit(True)
            self.contador_pausa = 1
            self.senal_pausar_juego.emit(self.contador_pausa)

            self.timer_finalizado = QTimer()
            self.timer_finalizado.setInterval(5000)
            self.timer_finalizado.timeout.connect(
                self.cerrar_ventana_juego_sin_boton)
            self.timer_finalizado.start()

    def mostrar_ventana_juego(self, nombre, astronauta):
        self.nombre_astronauta = astronauta
        self.senal_enviar_nombre.emit(nombre)
        self.show()
        self.senal_iniciar_juego.emit()

    def salir_del_juego(self):
        self.senal_salir_del_juego_boton.emit()
        self.close()

    def pausar_el_juego(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:

            self.senal_teclas.emit("arriba")
        if event.key() == Qt.Key_S:

            self.senal_teclas.emit("abajo")
        if event.key() == Qt.Key_A:

            self.senal_teclas.emit("izquierda")
        if event.key() == Qt.Key_D:

            self.senal_teclas.emit("derecha")

        if self.bloqueo_boton_disparo == False:
            if event.key() == Qt.Key_K:  # Disparar con K

                self.senal_disparar.emit()
                if not self.balas_infinitas:
                    self.balas_iniciales -= 1
                    self.label_balas.setText(str(self.balas_iniciales))
                if self.balas_iniciales == 0 and not self.ya_perdiste:
                    self.ya_perdiste = True
                    if self.ya_perdiste and self.aliens_explotados <= 1:
                        self.label_nivel_superado_o_no_3.setText(
                            "¡Lo siento, has perdido!. Te has quedado sin balas.\
 Volviendo al menú de inicio...")
                        font = QFont()
                        font.setFamily("Copperplate Gothic Bold")
                        font.setPointSize(12)
                        font.setBold(False)
                        font.setWeight(50)
                        self.label_nivel_superado_o_no_3.setFont(font)
                        self.label_nivel_superado_o_no_3.setStyleSheet("color:white;\n"
                                                                       "background:transparent;\n"
                                                                       "")
                        self.senal_pausar_mira.emit(True)
                        self.senal_pausar_disparo.emit(True)
                        self.contador_pausa = 1
                        self.bloquear_boton_pausa = True
                        self.senal_pausar_juego.emit(self.contador_pausa)
                        self.timer_fin = QTimer()
                        self.timer_fin.setInterval(5000)
                        self.timer_fin.start()
                        self.timer_fin.timeout.connect(
                            self.cerrar_ventana_juego_sin_boton)

        if self.bloquear_boton_pausa == False:
            if event.key() == Qt.Key_P:
                self.contador_pausa += 1
                self.senal_pausar_juego.emit(self.contador_pausa)

                if self.contador_pausa % 2 == 1:
                    self.label_nivel_superado_o_no_2.setText("PAUSADO")
                    font = QFont()
                    font.setFamily("Copperplate Gothic Bold")
                    font.setPointSize(24)
                    font.setBold(False)
                    font.setWeight(50)
                    self.label_nivel_superado_o_no_2.setFont(font)
                    self.label_nivel_superado_o_no_2.setStyleSheet("color:white;\n"
                                                                   "background:transparent;\n"
                                                                   "")
                    self.senal_pausar_mira.emit(True)
                    self.senal_pausar_disparo.emit(True)

                if self.contador_pausa % 2 == 0:
                    self.label_nivel_superado_o_no_2.setText("")
                    self.senal_pausar_mira.emit(False)
                    self.senal_pausar_disparo.emit(False)

        self.lista_teclas_que_se_apretan.append(event.key())

        try:
            if self.lista_teclas_que_se_apretan[-4] == Qt.Key_O and\
                    self.lista_teclas_que_se_apretan[-3] == Qt.Key_V and\
                    self.lista_teclas_que_se_apretan[-2] == Qt.Key_N and\
                    self.lista_teclas_que_se_apretan[-1] == Qt.Key_I:
                self.balas_infinitas = True
                self.balas_iniciales = 10000
                self.label_balas.setText(str("Balas Infinitas"))

            if self.lista_teclas_que_se_apretan[-3] == Qt.Key_C and\
                    self.lista_teclas_que_se_apretan[-2] == Qt.Key_I and\
                    self.lista_teclas_que_se_apretan[-1] == Qt.Key_A:
                self.close()
                self.senal_ventana_post_juego.emit(
                    self.nombre_astronauta, self.balas_iniciales, \
                        self.contador_segundos, self.puntaje)

        except IndexError:
            pass

    def cerrar_ventana_juego_sin_boton(self):
        self.senal_ventana_post_juego.emit(
            self.nombre_astronauta, self.balas_iniciales, self.contador_segundos, self.puntaje) 
        self.close()

    def mover_mira_ventana_juego(self, mira):
        mira.label_mira.setParent(self)
        mira.label_mira.setVisible(True)
        mira.label_mira.move(mira.posicion_mira.x(), mira.posicion_mira.y())

    def asignar_objeto_alien(self, alien):
        alien.label_alien1.setParent(self)
        alien.label_alien1.setVisible(True)
        alien.label_alien1.move(alien.posicion_alien_x, alien.posicion_alien_y)

    def asignar_objeto_alien2(self, alien):
        alien.label_alien1.setParent(self)
        alien.label_alien1.setVisible(True)
        alien.label_alien1.move(alien.posicion_alien_x, alien.posicion_alien_y)

    def animacion_aliens(self, alien):

        nombre_archivo = alien.foto_alien_vivo[31:41]

        if nombre_archivo == "Alien1.png":
            self.tipo_alien = "Alien1.png"
            ruta_alien_muerto = p.RUTA_ALIEN_LUNAR_MUERTO

        if nombre_archivo == "Alien2.png":
            self.tipo_alien = "Alien2.png"
            ruta_alien_muerto = p.RUTA_ALIEN_JUPITER_MUERTO

        if nombre_archivo == "Alien3.png":
            self.tipo_alien = "Alien3.png"
            ruta_alien_muerto = p.RUTA_ALIEN_INTERGALACTICO_MUERTO

        alien.pixeles_alien1 = QPixmap(ruta_alien_muerto)
        alien.label_alien1.setPixmap(alien.pixeles_alien1)
        alien.label_alien1.setScaledContents(True)
        alien.label_alien1.setStyleSheet("background:transparent;")
        alien.label_alien1.resize(p.ANCHO_ALIEN_1, p.ALTURA_ALIEN_1)
        alien.label_alien1.setParent(self)
        alien.label_alien1.setVisible(True)

        if alien.identificador == "1":
            self.senal_mover_aliens_muertos.emit()

        if alien.identificador == "2":
            self.senal_mover_aliens_muertos2.emit()

    def instanciar_timer_explosion_juego(self):
        self.timer_animacion = QTimer()
        self.timer_animacion.setInterval(500)

    def animacion_explosion_alien(self, alien_coordenada_x, alien_coordenada_y):

        self.aliens_explotados += 1
        self.instanciar_timer_explosion_juego()
        self.timer_animacion.start()
        self.alien_coordenada_x = alien_coordenada_x
        self.alien_coordenada_y = alien_coordenada_y

        self.label_explosion = QLabel("")
        self.label_explosion.move(alien_coordenada_x, alien_coordenada_y)

        pixeles_explosion1 = QPixmap(p.RUTA_EXPLOSION_1)
        self.label_explosion.setPixmap(pixeles_explosion1)
        self.label_explosion.setScaledContents(True)
        self.label_explosion.setStyleSheet("background:transparent;")
        self.label_explosion.resize(p.ANCHO_ALIEN_1, p.ALTURA_ALIEN_1)
        self.label_explosion.setParent(self)
        self.label_explosion.setVisible(True)
        self.timer_animacion.timeout.connect(self.animacion_explosion_alien2)

    def animacion_explosion_alien2(self):

        pixeles_explosion2 = QPixmap(p.RUTA_EXPLOSION_2)
        self.label_explosion.setPixmap(pixeles_explosion2)
        self.label_explosion.setScaledContents(True)
        self.label_explosion.setStyleSheet("background:transparent;")
        self.label_explosion.resize(p.ANCHO_ALIEN_1, p.ALTURA_ALIEN_1)
        self.label_explosion.setParent(self)
        self.label_explosion.setVisible(True)
        self.timer_animacion.timeout.connect(self.animacion_explosion_alien3)

    def animacion_explosion_alien3(self):
        pixeles_explosion3 = QPixmap(p.RUTA_EXPLOSION_3)
        self.label_explosion.setPixmap(pixeles_explosion3)
        self.label_explosion.setScaledContents(True)
        self.label_explosion.setStyleSheet("background:transparent;")
        self.label_explosion.resize(p.ANCHO_ALIEN_1, p.ALTURA_ALIEN_1)
        self.label_explosion.setParent(self)
        self.label_explosion.setVisible(True)
        self.timer_animacion.timeout.connect(
            self.animacion_explosion_alien_final)

    def animacion_explosion_alien_final(self):

        pixeles_explosion4 = QPixmap("")
        self.label_explosion.setPixmap(pixeles_explosion4)
        self.label_explosion.setScaledContents(True)
        self.label_explosion.setStyleSheet("background:transparent;")
        self.label_explosion.resize(p.ANCHO_ALIEN_1, p.ALTURA_ALIEN_1)
        self.label_explosion.setParent(self)
        self.label_explosion.setVisible(True)
        self.timer_animacion.stop()
        if self.aliens_explotados % 2 == 0:
            self.label_nivel_superado_o_no.setText("¡Nivel superado!")
            font = QFont()
            font.setFamily("Copperplate Gothic Bold")
            font.setPointSize(18)
            font.setBold(False)
            font.setWeight(50)
            self.label_nivel_superado_o_no.setFont(font)
            self.label_nivel_superado_o_no.setStyleSheet("color:white;\n"
                                                         "background:transparent;\n"
                                                         "")
            if self.tipo_alien == "Alien1.png":
                pixeles_perro_nivel_superado = QPixmap(p.RUTA_ALIEN_PERRO_1)
            elif self.tipo_alien == "Alien2.png":
                pixeles_perro_nivel_superado = QPixmap(p.RUTA_ALIEN_PERRO_2)
            elif self.tipo_alien == "Alien3.png":
                pixeles_perro_nivel_superado = QPixmap(p.RUTA_ALIEN_PERRO_3)

            self.label_perro_juego.setPixmap(pixeles_perro_nivel_superado)
            self.label_perro_juego.setScaledContents(True)
            self.label_perro_juego.move(170, 290)
            self.timer_nivel.stop()
            self.senal_pausar_mira.emit(True)
            self.senal_pausar_disparo.emit(True)
            self.bloqueo_boton_disparo = True

            self.sonido_risa_perro()

            self.timer_fin = QTimer()
            self.timer_fin.setInterval(5000)
            self.timer_fin.start()
            self.timer_fin.timeout.connect(self.cerrar_ventana_juego_sin_boton)

    def sonido_risa_perro(self):
        self.player = QMediaPlayer()
        self.ruta_sonido_risa = QUrl.fromLocalFile(p.RUTA_RISA_PERRO)
        self.audio_sonido_risa = QMediaContent(self.ruta_sonido_risa)
        self.player.setMedia(self.audio_sonido_risa)
        self.player.play()
