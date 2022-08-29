import sys

from PyQt5.QtWidgets import (QApplication)

from backend.logica_juego import Alien, LogicaJuego, MiraJuego
from backend.logica_principal import LogicaPrincipal
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post_juego import VentanaPostJuego
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_ver_rankings import VentanaRankings

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventanas

    ventana_de_inicio = VentanaInicio()
    ventana_de_principal = VentanaPrincipal()
    ventana_de_ranking = VentanaRankings()
    ventana_de_juego = VentanaJuego()
    ventana_post_juego = VentanaPostJuego()

    # Instanciación de lógica
    logica_de_principal = LogicaPrincipal()
    mira_del_juego = MiraJuego()
    mira_del_juego_disparo = MiraJuego()
    alien = Alien("1")
    alien2 = Alien("2")
    logica_del_juego = LogicaJuego(mira_del_juego, alien, alien2)

    # Conexiones de señales Ventana de inicio

    ventana_de_inicio.senal_entrar_a_jugar.connect(
        ventana_de_principal.mostrar_ventana_principal)

    ventana_de_inicio.senal_ver_ranking.connect(
        ventana_de_ranking.mostrar_ventana_ranking)

    ventana_de_ranking.senal_cerrar_ventana_ranking.connect(
        ventana_de_inicio.mostrar_ventana_inicio)

    # Conexiones de señales en Ventana principal
    ventana_de_principal.senal_enviar_info_usuario.connect(
        logica_de_principal.comprobar_usuario)

    ventana_de_principal.senal_cerrar_ventana_principal.connect(
        ventana_de_inicio.mostrar_ventana_inicio)

    ventana_de_principal.senal_obtener_escenario.connect(
        ventana_de_juego.ingresar_fondo_juego)

    logica_de_principal.senal_respuesta_validacion.connect(
        ventana_de_principal.recibir_validacion)

    ventana_de_principal.senal_iniciar_juego.connect(
        ventana_de_juego.mostrar_ventana_juego)

    ventana_de_juego.senal_salir_del_juego_boton.connect(
        ventana_de_principal.mostrar_ventana_principal)

    # Conexiones de señales en Ventana de juego

    ventana_de_juego.senal_iniciar_juego.connect(
        logica_del_juego.iniciar_juego)

    ventana_de_juego.senal_teclas.connect(logica_del_juego.mover_mira_logica)

    logica_del_juego.senal_mira.connect(
        ventana_de_juego.mover_mira_ventana_juego)

    ventana_de_juego.senal_pausar_juego.connect(logica_del_juego.pausar_juego)

    ventana_de_juego.senal_pausar_mira.connect(
        mira_del_juego.bloquear_teclas_juego)

    ventana_de_juego.senal_pausar_disparo.connect(
        mira_del_juego.bloqueo_disparo)

    # Conexiones de señales para instanciar los aliens dentro del juego
    ventana_de_principal.senal_mandar_coordenadas.connect(
        logica_del_juego.poner_foto_alien_logica)

    logica_del_juego.senal_alien_objeto.connect(
        ventana_de_juego.asignar_objeto_alien)

    ventana_de_principal.senal_mandar_coordenadas2.connect(
        logica_del_juego.poner_foto_alien_logica2)

    logica_del_juego.senal_alien_objeto2.connect(
        ventana_de_juego.asignar_objeto_alien2)

    ventana_de_juego.senal_iniciar_juego.connect(
        logica_del_juego.iniciar_juego)

    # Conexiones de señales para disparar y que se mueran los aliens

    ventana_de_juego.senal_disparar.connect(
        logica_del_juego.mandar_coordenadas_mira)

    logica_del_juego.senal_enviar_coordenadas_mira.connect(alien.matar_aliens)
    logica_del_juego.senal_enviar_coordenadas_mira.connect(alien2.matar_aliens)

    alien.senal_mata_alien.connect(logica_del_juego.disparar_mira_logica)
    alien2.senal_mata_alien.connect(logica_del_juego.disparar_mira_logica)

    mira_del_juego.senal_alien_muerto.connect(
        ventana_de_juego.animacion_aliens)

    ventana_de_juego.senal_mover_aliens_muertos.connect(
        alien.mover_aliens_muertos_abajo_menu)
    ventana_de_juego.senal_mover_aliens_muertos2.connect(
        alien2.mover_aliens_muertos_abajo_menu)

    alien.senal_alien_muerto.connect(
        ventana_de_juego.animacion_explosion_alien)
    alien2.senal_alien_muerto.connect(
        ventana_de_juego.animacion_explosion_alien)

    ventana_de_juego.senal_empezar_nuevamente.connect(
        logica_del_juego.iniciar_juego_nuevamente)

    # Señales ventana post-juego:

    ventana_de_juego.senal_ventana_post_juego.connect(
        ventana_post_juego.mostrar_ventana_post_juego)

    ventana_de_inicio.show()
    app.exec()
