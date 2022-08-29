from utils import data_json
from os.path import join

class Logica:

    def __init__(self, parent):
        
        self.parent = parent
        self.usuarios = {}

    def validar_login(self, nombre, socket_cliente):
        if (nombre not in self.usuarios.values()) and (10 >= len(nombre)>= 1) and nombre.isalnum() :
            temp = self.usuarios.values()  # Para que no se vea a si mismo
            self.usuarios[self.parent.id_cliente - 1] = nombre

            """ for ruta in self.rutas_caratulas:
                self.parent.enviar_archivo(socket_cliente, join(*ruta.split(";"))) """
            
            return {
                "comando": "respuesta_validacion_login",
                "estado": "aceptado",
                "nombre_usuario": nombre,
                "usuarios": ",".join(temp),
            }
        
        return {
            "comando": "respuesta_validacion_login",
            "estado": "rechazado",
            "error": "datos invalidos",
        }


    def procesar_mensaje(self, mensaje, socket_cliente):
        """
        Procesa un mensaje recibido desde el cliente
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "validar_login":
            respuesta = self.validar_login(
                mensaje["nombre usuario"], socket_cliente
            )
        if comando == "desconectar":
            self.eliminar_nombre(mensaje["id"])
            return None
        return respuesta


    def eliminar_nombre(self,id):
        """
        Elimina el nombre del usuario del diccionario
        """
        self.usuarios.pop(id, None)
        