from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        # COMPLETAR
        usuario = tupla_respuesta(0)
        contrasena = tupla_respuesta(1)
        lista_errores = []

        if ((not usuario.isalnum()) or (len(usuario) > p.MAX_CARACTERES)) and\
             (contrasena != p.PASSWORD):
            lista_errores.append("Usuario")
            lista_errores.append("Contraseña")
            self.senal_respuesta_validacion.emit(False, lista_errores)
            
        elif (not usuario.isalnum()) or (len(usuario) > p.MAX_CARACTERES):
            lista_errores.append("Usuario")
            self.senal_respuesta_validacion.emit(False, lista_errores)
            

        elif contrasena != p.PASSWORD:
            lista_errores.append("Contraseña")
            self.senal_respuesta_validacion.emit(False, lista_errores)
            
        else:
            self.senal_abrir_juego.emit(usuario)
            self.senal_respuesta_validacion.emit(True,lista_errores)
        


        pass
