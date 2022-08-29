import socket
import json
import threading
from backend.interfaz import Interfaz
from utils import data_json as p

class Cliente:

    def __init__(self):

        self.host = socket.gethostbyname(socket.gethostname())
        self.port = p("PORT")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Interfaz(self)
        try:
            self.conectado = True
            self.socket_cliente.connect((self.host, self.port))
            thread = threading.Thread(target=self.escuchar_servidor, daemon=True)
            thread.start()
            """ self.recibir_input() """

        except:      
            print("ERROR CON EL CLIENTE")
            self.conectado = False


    """ def recibir_input(self):
        while self.conectado:
            mensaje = input("INGRESE EL INPUT ACA: ")
            print(f"Enviando mensaje: {mensaje}")
            self.enviar_mensaje(mensaje) """


    def escuchar_servidor(self):
        try:
            while self.conectado == True:
                mensaje = self.recibir_mensaje()
                respuesta = self.interfaz.manejar_mensaje(mensaje)                
                self.log(f"Mensaje recibido: {mensaje}")

        except ConnectionResetError:
            self.log("Ha tenido un error de conexión (cliente)")
        finally:
            self.conectado = False


    def recibir_mensaje(self):
        cantidad_de_chunks_bytes = self.socket_cliente.recv(4)
        cantidad_de_chunks = int.from_bytes(
            cantidad_de_chunks_bytes, byteorder="little")
        respuesta = bytearray()
        
        contador_de_bloques = p("CONTADOR_DE_BLOQUES")
        for _ in range(cantidad_de_chunks):
            bytes_inutiles = self.socket_cliente.recv(6)
            bytes_utiles = self.socket_cliente.recv(20)
            respuesta.extend(bytes_utiles)

            contador_de_bloques += 1

        mensaje = self.decodificar_mensaje(respuesta)

        self.log(f"El mensaje recibido es {mensaje}")

        return mensaje

    def enviar_mensaje(self, mensaje):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        self.log(f"Llego a función enviar mensaje y el mensaje en bytes es {bytes_mensaje}")
        mensaje_codificado = bytearray()

        if (len(bytes_mensaje) % 20) == 0:
            self.log("CANTIDAD DE CHUNKS JUSTOS")
            cantidad_de_chunks = len(bytes_mensaje) // 20

        elif (len(bytes_mensaje) % 20) != 0:
            self.log("CANTIDAD DE CHUNKS NOOOO JUSTOS")
            cantidad_de_chunks = (len(bytes_mensaje) // 20) + 1

        cantidad_de_chunks_bytes = cantidad_de_chunks.to_bytes(4, byteorder= "little")
        mensaje_codificado.extend(cantidad_de_chunks_bytes)

        contador_de_bloques = p("CONTADOR_DE_BLOQUES")

        self.log("LLEGUE A PUNTO ANTES DEL FOR DE ENVIAR")
        for i in range(0, len(bytes_mensaje), p("20_BYTES")):

            contador_de_bloques_bytes = contador_de_bloques.to_bytes(4, byteorder= "big")
            mensaje_codificado.extend(contador_de_bloques_bytes)

            chunk_mensaje = bytearray(bytes_mensaje[i:i+p("20_BYTES")])
            if len(chunk_mensaje) == p("20_BYTES"):
                uno_byte = b"\x01"
                mensaje_codificado.extend(uno_byte)
            
            elif len(chunk_mensaje) != p("20_BYTES"):
                cero_byte = b"\x00"
                mensaje_codificado.extend(cero_byte)

            cantidad_de_bytes_ocupados = len(chunk_mensaje).to_bytes(1, byteorder= "big")

            mensaje_codificado.extend(cantidad_de_bytes_ocupados)
            
            mensaje_codificado.extend(chunk_mensaje)

            contador_de_bloques += 1

        self.log(f"El mensaje codificado para mandar es {mensaje_codificado}")

        self.socket_cliente.sendall(mensaje_codificado)

        

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            bytes_mensaje = mensaje_json.encode('utf-8')
            return bytes_mensaje
        except json.JSONDecodeError:
            self.log('No se pudo codificar el mensaje')
            return b''

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            self.log('No se pudo decodificar el mensaje')
            return ''


    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")


""" if __name__ == "__main__":
    cliente = Cliente() """