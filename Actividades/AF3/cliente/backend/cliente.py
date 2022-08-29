"""
Modulo contiene implementación principal del cliente
"""
from cmath import log
import socket
import json
from threading import Thread
import threading
from backend.interfaz import Interfaz


class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Interfaz(self)
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """

        # TODO: Completado por estudiante
        self.conectado = True ###### ME LO DIJO EL AYUDANTE!
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.comenzar_a_escuchar()
            self.interfaz.mostrar_ventana_carga()

        except ConnectionError:
            log("Ha ocurrido un error con la conexión del cliente")
            self.conectado = False   ###### ME LO DIJO EL AYUDANTE!
        pass

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        # TODO: Completado por estudiante
        
        thread = threading.Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()
        
        pass

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        # TODO: Completado por estudiante

        try:
            while self.conectado:
                mensaje_recbido = self.recibir()
                if mensaje_recbido != "":
                    self.interfaz.manejar_mensaje(mensaje_recbido)

        except ConnectionError:
            print("Se ha producido un error de conexión")
        
        pass

    def recibir(self):
        """
        Se encarga de recibir lis mensajes del servidor.
        """
        # TODO: Completado por estudiante
        largo_mensaje = self.socket_cliente.recv(4)
        largo_respuesta = int.from_bytes(largo_mensaje, byteorder= "little")
        respuesta = bytearray()

        while len(respuesta) < largo_respuesta:
            largo_leer = min(64, largo_respuesta - len(respuesta))
            respuesta.extend(self.socket_cliente.recv(largo_leer))

        decodificacion_mensaje = self.decodificar_mensaje(respuesta)
        return decodificacion_mensaje
        

    def enviar(self, mensaje):
        """
        Envía un mensaje a un cliente.
        """
        # TODO: Completado por estudiante

        mensaje_codificado = self.codificar_mensaje(mensaje)
        largo_mensaje = len(mensaje_codificado).to_bytes(4, byteorder="little")
        self.socket_cliente.sendall(largo_mensaje + mensaje_codificado)
        pass

    def codificar_mensaje(self, mensaje):
        """
        Codifica el mensaje a enviar
        """
        try:
            # TODO: Completado por estudiante
            mensaje_formato_json = json.dumps(mensaje)
            mensaje_formato_bytes = mensaje_formato_json.encode()
            return mensaje_formato_bytes
            
        except json.JSONDecodeError:
            print("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        """
        Decodifica el mensaje del servidor
        """
        try:
            # TODO: Completado por estudiante
            mensaje_formato_json = json.loads(mensaje_bytes)
            return mensaje_formato_json
            pass
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}

    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")
