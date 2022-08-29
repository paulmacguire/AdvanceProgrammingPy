import json
import socket
import threading
from logica import Logica
from utils import data_json as p


class Servidor:

    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = p("PORT")
        self.socket_servidor = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()

        self.logica = Logica(self)
        self.id_cliente = p("ID_CLIENTE")
        self.clientes_conectados = {}
        self.log(
            f"El host es: {self.host} y se está escuchando desde el puerto {self.port}")

        thread = threading.Thread(target=self.aceptar_clientes)
        thread.start()

    def aceptar_clientes(self):

        try:
            while True:

                socket_cliente, addr = self.socket_servidor.accept()
                self.clientes_conectados[str(socket_cliente)] = socket_cliente

                self.log(
                    f"Cliente {self.id_cliente} con dirección {addr} se ha conectado al servidor")

                thread_escucha_cliente = threading.Thread(
                    target=self.escuchar_cliente, args=(socket_cliente,), daemon=True)
                thread_escucha_cliente.start()

        except WindowsError:
            self.log(
                "Un usuario ha cerrado la ventana, por lo que el socket del servidor se cerrará")

    def escuchar_cliente(self, socket_cliente):
        self.log(f"Se comenzó a escuchar al Cliente {self.id_cliente}")
        self.id_cliente += 1
        try:
            while True:
                mensaje_cliente = self.recibir_mensaje(socket_cliente)
                respuesta = self.logica.procesar_mensaje(
                    mensaje_cliente, socket_cliente)
                estado_login = 'aceptado'

                if respuesta['estado'] == estado_login:
                    self.log("HA LLEGADO AL ENVIAR A TODOS DE ESCUCHAR CLIENTE")
                    self.enviar_todos(respuesta)
                    self.enviar_mensaje(respuesta, socket_cliente)

                else:
                    self.enviar_mensaje(respuesta, socket_cliente)
                self.log(f"Enviando respuesta: {respuesta}")
        except ConnectionResetError:
            self.log("Ha tenido un error de conexión con el cliente")
            self.socket_servidor.close()

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            bytes_mensaje = mensaje_json.encode('utf-8')
            return bytes_mensaje
        except json.JSONDecodeError:
            self.log('No se pudo codificar el mensaje')
            return b''

    def decodificar_mensaje(self, bytes_mensaje):
        print(bytes_mensaje)
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            self.log('No se pudo decodificar el mensaje')
            return ''

    def recibir_mensaje(self, socket_cliente):
        cantidad_de_chunks_bytes = socket_cliente.recv(4)
        cantidad_de_chunks = int.from_bytes(
            cantidad_de_chunks_bytes, byteorder="little")
        respuesta = bytearray()

        contador_de_bloques = 0
        for _ in range(cantidad_de_chunks):
            bytes_inutiles = socket_cliente.recv(6)
            bytes_utiles = socket_cliente.recv(20)
            respuesta.extend(bytes_utiles)

            contador_de_bloques += 1

        self.log(f"EL MENSAJE DEL CLIENTE ES {respuesta}")
        mensaje = self.decodificar_mensaje(respuesta)

        return mensaje

    def enviar_mensaje(self, mensaje, socket_cliente):
        bytes_mensaje = self.codificar_mensaje(mensaje)

        mensaje_codificado = bytearray()

        if (len(bytes_mensaje) % 20) == 0:
            cantidad_de_chunks = len(bytes_mensaje) // 20

        elif (len(bytes_mensaje) % 20) != 0:
            cantidad_de_chunks = (len(bytes_mensaje) // 20) + 1

        cantidad_de_chunks_bytes = cantidad_de_chunks.to_bytes(
            4, byteorder="little")
        mensaje_codificado.extend(cantidad_de_chunks_bytes)

        contador_de_bloques = p("CONTADOR_DE_BLOQUES")

        for i in range(0, len(bytes_mensaje), p("20_BYTES")):

            contador_de_bloques_bytes = contador_de_bloques.to_bytes(
                4, byteorder="big")
            mensaje_codificado.extend(contador_de_bloques_bytes)

            chunk_mensaje = bytearray(bytes_mensaje[i:i+20])
            if len(chunk_mensaje) == p("20_BYTES"):
                uno_byte = b"\x01"
                mensaje_codificado.extend(uno_byte)

            elif len(chunk_mensaje) != p("20_BYTES"):
                cero_byte = b"\x00"
                mensaje_codificado.extend(cero_byte)

            cantidad_de_bytes_ocupados = len(
                chunk_mensaje).to_bytes(1, byteorder="big")

            mensaje_codificado.extend(cantidad_de_bytes_ocupados)
            mensaje_codificado.extend(chunk_mensaje)

            contador_de_bloques += 1

        socket_cliente.sendall(mensaje_codificado)

    def enviar_todos(self, mensaje):
        for socket_cliente in self.clientes_conectados.values():
            bytes_mensaje = self.codificar_mensaje(mensaje)

            mensaje_codificado = bytearray()

            if (len(bytes_mensaje) % p("20_BYTES")) == 0:
                cantidad_de_chunks = len(bytes_mensaje) // 20

            elif (len(bytes_mensaje) % p("20_BYTES")) != 0:
                cantidad_de_chunks = (len(bytes_mensaje) // 20) + 1

            cantidad_de_chunks_bytes = cantidad_de_chunks.to_bytes(
                4, byteorder="little")
            mensaje_codificado.extend(cantidad_de_chunks_bytes)

            contador_de_bloques = 0

            for i in range(0, len(bytes_mensaje), p("20_BYTES")):

                contador_de_bloques_bytes = contador_de_bloques.to_bytes(
                    4, byteorder="big")
                mensaje_codificado.extend(contador_de_bloques_bytes)

                chunk_mensaje = bytearray(bytes_mensaje[i:i+20])
                if len(chunk_mensaje) == p("20_BYTES"):
                    uno_byte = b"\x01"
                    mensaje_codificado.extend(uno_byte)

                elif len(chunk_mensaje) != p("20_BYTES"):
                    cero_byte = b"\x00"
                    mensaje_codificado.extend(cero_byte)

                cantidad_de_bytes_ocupados = len(
                    chunk_mensaje).to_bytes(1, byteorder="big")

                mensaje_codificado.extend(cantidad_de_bytes_ocupados)
                mensaje_codificado.extend(chunk_mensaje)

                contador_de_bloques += 1

            socket_cliente.sendall(mensaje_codificado)

    # COMPLETAR

    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")


print("[EMPEZANDO] Server está empezando...")

