from PyQt5.QtCore import QObject, pyqtSignal,QRect, QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

import parametros as p
import random


class Alien(QObject):

    senal_mata_alien = pyqtSignal(str)
    senal_alien_muerto = pyqtSignal(int, int)

    def __init__(self, identificador):
        super().__init__()
        self.identificador = identificador

        self.posicion_alien_x = 0
        self.posicion_alien_y = 0

        self.valores_x = [-p.VELOCIDAD_ALIENS, p.VELOCIDAD_ALIENS]
        self.valores_y = [-p.VELOCIDAD_ALIENS, p.VELOCIDAD_ALIENS]

        self.aumento_x = random.choice(self.valores_x)
        self.aumento_y = random.choice(self.valores_y)
        self.tipo_escenario = None
        self.ponderador_escenario = 0

        self.label_alien1 = QLabel("")

        self.instanciar_timer()

        self.contador_timer = 0
        self.contador_timer_explosion = 0
        self.instanciar_timer_alien_muerto()
        self.contador = 0

    def ingresar_foto_alien_vivo(self, foto_alien_vivo, coordenadas_x, coordenadas_y):

        self.posicion_alien_x = coordenadas_x
        self.posicion_alien_y = coordenadas_y
        self.foto_alien_vivo = foto_alien_vivo
        self.pixeles_alien1 = QPixmap(self.foto_alien_vivo)

        self.label_alien1.setPixmap(self.pixeles_alien1)
        self.label_alien1.setScaledContents(True)
        self.label_alien1.setStyleSheet("background:transparent;")
        self.label_alien1.resize(p.ANCHO_ALIEN_1, p.ALTURA_ALIEN_1)
        self.label_alien1.move(coordenadas_x, coordenadas_y)

    def instanciar_timer(self):
        self.timer_mover_aliens = QTimer()
        self.timer_mover_aliens.setSingleShot(True)
        self.timer_mover_aliens.setInterval(100)
        self.timer_mover_aliens.timeout.connect(self.mover_aliens)

    def mover_aliens(self):
        
        if self.tipo_escenario == p.RUTA_ESCENARIO_TUTORIAL_LUNAR:
            self.ponderador_escenario = p.PONDERADOR_TUTORIAL

        elif self.tipo_escenario == p.RUTA_ESCENARIO_ENTRENAMIENTO_JUPITER:
            self.ponderador_escenario = p.PONDERADOR_ENTRENAMIENTO
        
        elif self.tipo_escenario == p.RUTA_ESCENARIO_INVASION_INTERGALACTICA:
            self.ponderador_escenario = p.PONDERADOR_INVASION

        
        self.posicion_alien_x += self.aumento_x/self.ponderador_escenario
        self.posicion_alien_y += self.aumento_y/self.ponderador_escenario

        self.label_alien1.move(self.posicion_alien_x, self.posicion_alien_y)

        if self.posicion_alien_x < p.LADO_DERECHO_VENTANA + 100:  # Ajustes de ventana
            self.aumento_x = self.aumento_x*(-1)

        if self.posicion_alien_x > p.LADO_IZQUIERDO_VENTANA + 40:  # Ajustes de ventana
            self.aumento_x = self.aumento_x*(-1)

        if self.posicion_alien_y < p.LADO_ABAJO_VENTANA + 90:  # Ajustes de ventana
            self.aumento_y = self.aumento_y*(-1)

        if self.posicion_alien_y > p.LADO_ARRIBA_VENTANA:  # Ajustes de ventana
            self.aumento_y = self.aumento_y*(-1)

        self.timer_mover_aliens.start()

    def star_timer_aliens(self):
        self.timer_mover_aliens.start()

    def instanciar_timer_alien_muerto(self):
        self.timer_mover_aliens_muertos = QTimer()
        self.timer_mover_aliens_muertos.setSingleShot(True)
        self.timer_mover_aliens_muertos.setInterval(50)
        self.timer_mover_aliens_muertos.timeout.connect(
            self.mover_aliens_muertos_abajo_menu)

    def mover_aliens_muertos_abajo_menu(self):
        self.posicion_alien_y += 5
        self.contador_timer += 1
        self.label_alien1.move(self.posicion_alien_x, self.posicion_alien_y)
        self.timer_mover_aliens_muertos.start()
        if self.contador_timer == 1:
            self.timer_mover_aliens.stop()
            self.senal_alien_muerto.emit(self.posicion_alien_x, self.posicion_alien_y)

    def matar_aliens(self, coordenadas_mira):

        if (self.label_alien1.geometry().x() - 11 <= coordenadas_mira.x() +
            65 <= self.label_alien1.geometry().x() + 11) and \
            (self.label_alien1.geometry().y() - 10 <= coordenadas_mira.y() +
             45 <= self.label_alien1.geometry().y() + 10):
            self.senal_mata_alien.emit(f"Alien muerto {self.identificador}")

        else:
            self.senal_mata_alien.emit(f"Alien vivo {self.identificador}")

            


class MiraJuego(QObject):

    senal_alien_muerto = pyqtSignal(Alien)

    def __init__(self, posicion_mira=QRect(*p.POSICION_DE_LA_MIRA)):
        super().__init__()
        self.posicion_mira = posicion_mira
        self.bloqueo_teclado_moverse = False
        self.bloqueo_teclado_disparar = False
        self.label_mira = QLabel("")
        self.pixeles_mira = QPixmap(p.RUTA_MIRA_NEGRA)
        self.label_mira.setPixmap(self.pixeles_mira)
        self.label_mira.setScaledContents(True)
        self.label_mira.setStyleSheet("background:transparent;")
        self.label_mira.resize(p.ANCHO_DE_LA_MIRA, p.ALTURA_DE_LA_MIRA)
        self.label_mira.move(self.posicion_mira.x(), self.posicion_mira.y())

        self.timer_mira = QTimer()
        self.timer_mira.setInterval(1000)
        self.timer_mira.setSingleShot(True)
        self.timer_mira.timeout.connect(self.volver_mirar_negro)

    def mover_mira(self, direccion):
        if self.bloqueo_teclado_moverse == False:
            if direccion == "arriba":

                if self.posicion_mira.y() < p.LADO_ARRIBA_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x(), self.posicion_mira.y())

                if self.posicion_mira.y() > p.LADO_ARRIBA_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x(), self.posicion_mira.y() - p.VELOCIDAD_DE_LA_MIRA)

            if direccion == "abajo":

                if self.posicion_mira.y() > p.LADO_ABAJO_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x(), self.posicion_mira.y())

                if self.posicion_mira.y() < p.LADO_ABAJO_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x(), self.posicion_mira.y() + p.VELOCIDAD_DE_LA_MIRA)

            if direccion == "izquierda":

                if self.posicion_mira.x() < p.LADO_IZQUIERDO_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x(), self.posicion_mira.y())

                if self.posicion_mira.x() > p.LADO_IZQUIERDO_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x() - p.VELOCIDAD_DE_LA_MIRA, self.posicion_mira.y())

            if direccion == "derecha":

                if self.posicion_mira.x() > p.LADO_DERECHO_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x(), self.posicion_mira.y())

                if self.posicion_mira.x() < p.LADO_DERECHO_VENTANA:
                    self.posicion_mira.moveTo(
                        self.posicion_mira.x() + p.VELOCIDAD_DE_LA_MIRA, self.posicion_mira.y())

    def bloquear_teclas_juego(self,bloqueo):
        self.bloqueo_teclado_moverse = bloqueo

    def volver_mirar_negro(self):
        self.pixeles_mira = QPixmap(p.RUTA_MIRA_NEGRA)
        self.label_mira.setPixmap(self.pixeles_mira)
        self.label_mira.setScaledContents(True)

    def disparar_mira(self, alien, alien2, alien_vivo_o_muerto):
        if self.bloqueo_teclado_disparar == False:
            self.pixeles_mira = QPixmap(p.RUTA_MIRA_ROJA)
            self.label_mira.setPixmap(self.pixeles_mira)
            self.label_mira.setScaledContents(True)
            self.timer_mira.start()
            self.sonido_disparo()
        

            if alien_vivo_o_muerto == "Alien muerto 1":
                self.senal_alien_muerto.emit(alien)

            if alien_vivo_o_muerto == "Alien muerto 2":
                self.senal_alien_muerto.emit(alien2)

    def bloqueo_disparo(self, bloqueo_disparo):
        self.bloqueo_teclado_disparar = bloqueo_disparo

    def sonido_disparo(self):
        self.player = QMediaPlayer()

        self.ruta_sonido_disparo = QUrl.fromLocalFile(p.RUTA_DISPARO)
        self.audio_sonido_disparo = QMediaContent(self.ruta_sonido_disparo)
        self.player.setMedia(self.audio_sonido_disparo)
        self.player.play()

    def reset(self):
        self.posicion_mira.moveTo(
            p.POSICION_DE_LA_MIRA[0], p.POSICION_DE_LA_MIRA[1])


class LogicaJuego(QObject):

    senal_mira = pyqtSignal(MiraJuego)
    senal_mira_disparar = pyqtSignal(MiraJuego)
    senal_enviar_coordenadas_mira = pyqtSignal(QRect)
    senal_alien_objeto = pyqtSignal(Alien)
    senal_alien_objeto2 = pyqtSignal(Alien)
    senal_iniciar_juego_logica = pyqtSignal()


    def __init__(self, mira, alien, alien2):
        super().__init__()
        self._puntaje = 0
        self.timers = []
        self.aliens = []
        self.mira = mira
        self.alien = alien
        self.alien2 = alien2
        self.juego_ya_empezo = False


    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self, valor):
        if valor <= 0:
            self._puntaje = 0

        else:
            self._puntaje = valor

    def instanciar_timer(self):
        """ self.timer_mira = QTimer() """
        pass

    def iniciar_juego_nuevamente(self, juego_ya_empezo):
        if juego_ya_empezo == True:
            self.alien = Alien("1")
            self.alien2 = Alien("2")
            
            self.iniciar_juego()


    def mover_mira_logica(self, direccion):
        self.mira.mover_mira(direccion)
        self.senal_mira.emit(self.mira)

    def disparar_mira_logica(self, alien_vivo_o_muerto_logica):
        self.mira.disparar_mira(self.alien, self.alien2,
                                alien_vivo_o_muerto_logica)

    def poner_foto_alien_logica(self, foto_alien_vivo_senal, coordenadas_x_senal,
                                coordenadas_y_senal):
        if foto_alien_vivo_senal == p.RUTA_ALIEN_LUNAR_VIVO:
            self.alien.tipo_escenario = p.RUTA_ESCENARIO_TUTORIAL_LUNAR
        
        elif foto_alien_vivo_senal == p.RUTA_ALIEN_JUPITER_VIVO:
            self.alien.tipo_escenario = p.RUTA_ESCENARIO_ENTRENAMIENTO_JUPITER
        
        elif foto_alien_vivo_senal == p.RUTA_ALIEN_INTERGALACTICO_VIVO:
            self.alien.tipo_escenario = p.RUTA_ESCENARIO_INVASION_INTERGALACTICA
        
        self.alien.ingresar_foto_alien_vivo(
            foto_alien_vivo_senal, coordenadas_x_senal, coordenadas_y_senal)
        self.senal_alien_objeto.emit(self.alien)

    def poner_foto_alien_logica2(self, foto_alien_vivo_senal2, coordenadas_x_senal2,
                                 coordenadas_y_senal2):
        if foto_alien_vivo_senal2 == p.RUTA_ALIEN_LUNAR_VIVO:
            self.alien2.tipo_escenario = p.RUTA_ESCENARIO_TUTORIAL_LUNAR
        
        elif foto_alien_vivo_senal2 == p.RUTA_ALIEN_JUPITER_VIVO:
            self.alien2.tipo_escenario = p.RUTA_ESCENARIO_ENTRENAMIENTO_JUPITER
        
        elif foto_alien_vivo_senal2 == p.RUTA_ALIEN_INTERGALACTICO_VIVO:
            self.alien2.tipo_escenario = p.RUTA_ESCENARIO_INVASION_INTERGALACTICA
        
        self.alien2.ingresar_foto_alien_vivo(
            foto_alien_vivo_senal2, coordenadas_x_senal2, coordenadas_y_senal2)
        self.senal_alien_objeto2.emit(self.alien2)

    def mandar_coordenadas_mira(self):
        self.senal_enviar_coordenadas_mira.emit(self.mira.posicion_mira)


    def iniciar_juego(self):
        self.puntaje = 0
        
        self.alien.star_timer_aliens()
        self.alien2.star_timer_aliens()

    def pausar_juego(self, veces_presionado_pausa):
        if veces_presionado_pausa % 2 == 1:
            
            self.alien.timer_mover_aliens.stop()
            self.alien2.timer_mover_aliens.stop()
        if veces_presionado_pausa % 2 == 0:
            
            self.alien.timer_mover_aliens.start()
            self.alien2.timer_mover_aliens.start()

    def reset_mira(self):
        self.mira.reset()
        self.senal_mira.emit(self.mira)
