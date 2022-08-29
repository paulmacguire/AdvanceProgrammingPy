"""
Modulo contiene la implementación principal del servidor
"""
from http import client
import json
import socket
import threading
from logica import Logica


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.conectado = False
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.iniciar_servidor()

    def iniciar_servidor(self):
        """
        Crea el socket, lo enlaza y comienza a escuchar
        """
        # TODO: Completado por estudiante
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.conectado = True
        self.log(f"Este es el host: {self.host} y se esta escuchando desde el puerto {self.port}")
        self.comenzar_a_aceptar()

        pass
        

    def comenzar_a_aceptar(self):
        """
        Crea y comienza el thread encargado de aceptar clientes
        """
        # TODO: Completado por estudiante
        
        thread = threading.Thread(target = self.aceptar_clientes)
        thread.start()
        
        pass
        

    def aceptar_clientes(self):
        """
        Es arrancado como thread para de aceptar clientes, este se ejecuta
        siempre que se este conectado y acepta el socket del servidor. Luego
        se crea y comienza a escuchar al cliente. para finalmente aumentar en 1
        el id_cliente.
        """
        while self.conectado:
        # TODO: Completado por estudiante
            try:
                client_socket, _ = self.socket_servidor.accept()
                thread_que_se_escucha = threading.Thread(target =  self.escuchar_cliente, args = (self.id_cliente, client_socket), daemon=True)
                thread_que_se_escucha.start()
                self.id_cliente += 1
                pass
            except ConnectionError as error:
                print("Usted ha fallado conectando.")
                thread_que_se_escucha.close()
                pass


    def escuchar_cliente(self, id_cliente, socket_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        # TODO: Completado por estudiante
        try:
            while self.conectado:
                mensaje_que_se_recibe = self.recibir_mensaje(socket_cliente)

                if mensaje_que_se_recibe != {}:
                    mensaje_procesado = self.logica.procesar_mensaje(mensaje_que_se_recibe, socket_cliente)
                    if mensaje_procesado != "":
                        self.enviar_mensaje(mensaje_procesado, socket_cliente)

                    """ else:
                        print("Lamentablemente hay error de conexión")
                        self.eliminar_cliente(self.id_cliente, self.socket_servidor) """
                    pass
            
                else:
                    print("Lamentablemente el mensaje está vacío.")
                    self.eliminar_cliente(self.id_cliente,self.socket_servidor)


        except ConnectionResetError:
            print("Lamentablemente no logró la conexion cpn el cliente.")
            self.eliminar_cliente(self.id_cliente,self.socket_servidor)
            pass


    def recibir_mensaje(self, socket_cliente):
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        # TODO: Completado por estudiante
        largo_de_la_respuesta = socket_cliente.recv(4)
        respuesta_largo = int.from_bytes(largo_de_la_respuesta, byteorder= "little")
        respuesta = bytearray()

        while len(respuesta) < largo_de_la_respuesta:
            leer_largo = min(64, respuesta_largo - len(respuesta))
            respuesta.extend(socket_cliente.recv(leer_largo))

        decodificado = self.decodificar_mensaje(respuesta)
        return decodificado
        


    def enviar_mensaje(self, mensaje, socket_cliente):
        """
        Recibe una instruccion,
        lo CODIFICA usando el protocolo establecido y lo envía al cliente
        """
        # TODO: Completado por estudiante
        codificacion = self.codificar_mensaje(mensaje)
        largo_codificado = len(codificacion).to_bytes(4, byteorder="little")
        socket_cliente.send(largo_codificado + codificacion)
        
        pass

    def enviar_archivo(self, socket_cliente, ruta):
        """
        Recibe una ruta a un archivo a enviar y los separa en chunks de 8 kb
        """
        with open(ruta, "rb") as archivo:
            chunk = archivo.read(8000)
            largo = len(chunk)
            while largo > 0:
                chunk = chunk.ljust(8000, b"\0")  # Padding
                msg = {
                    "comando": "chunk",
                    "argumentos": {"largo": largo, "contenido": chunk.hex()},
                    "ruta": ruta,
                }
                self.enviar_mensaje(msg, socket_cliente)
                chunk = archivo.read(8000)
                largo = len(chunk)

    def eliminar_cliente(self, id_cliente, socket_cliente):
        """
        Elimina un cliente del diccionario de clientes conectados
        """
        try:
            # Cerramos el socket
            self.log(f"Borrando socket del cliente {id_cliente}.")
            socket_cliente.close()
            # Desconectamos el usuario de la lista de jugadores
            self.logica.procesar_mensaje(
                {"comando": "desconectar", "id": id_cliente}, socket_cliente
            )

        except KeyError as e:
            self.log(f"ERROR: {e}")

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_formato_json = json.dumps(mensaje)
            mensaje_formato_bytes = mensaje_formato_json.encode()
            return mensaje_formato_bytes

        except json.JSONDecodeError:
            print("Lamentablemente no se pudo codificar este mensaje recibido")
        
        pass


    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje_json = json.loads(mensaje_bytes)
            return mensaje_json

        except json.JSONDecodeError:
            print("Lamentablemente no se pudo decodificar este mensaje recibido")
        
        pass

    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")
