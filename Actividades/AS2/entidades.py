from abc import ABC, abstractmethod
from random import randint
from threading import Thread, Lock, Event, Timer
from time import sleep



class Persona(ABC, Thread):

    # Completar

    lock_bodega = Lock()
    lock_cola_pedidos = Lock()
    lock_cola_pedidos_listos = Lock()

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.disponible = True
        self.trabajando = True
        self.daemon = True
     # REVISAR LOS LOCKS

    @abstractmethod
    def run(self):
        pass


class Cocinero(Persona):

    def __init__(self, nombre, cocina):
        super().__init__(nombre)
        self.lugar_trabajo = cocina
        # Completar
        self.evento_plato_asignado = Event()

    def run(self):
        # Completar
        while self.trabajando:
            if self.disponible:
                self.evento_plato_asignado.wait()
                sleep(randint(1, 3))
                self.cocinar()
        pass

    def cocinar(self):
        # Completar
        self.disponible = False
        plato = self.sacar_plato()
        if plato != None:

            print(f"El cocinero {self.nombre} está cocinando plato {plato[1]}")
            self.buscar_ingredientes(plato, self.lugar_trabajo.bodega, self.lugar_trabajo.recetas)
            print(f"Buscando ingredientes...") ######## RELLENAR!!!!!
            sleep(randint(1,3))
            self.agregar_plato(plato)
            self.evento_plato_asignado.clear()
            self.disponible = True
            pass

    def sacar_plato(self):
        # Completar
        with self.lock_cola_pedidos:
            lista_pedidos = self.lugar_trabajo.cola_pedidos
            if len(lista_pedidos) >= 1:

                plato_sacado = lista_pedidos.popleft()
                return plato_sacado

    def buscar_ingredientes(self, plato, bodega, recetas):
        # Formato de los dicts entregados:
        # bodega = {
        #     "alimento_1": int cantidad_alimento_1,
        #     "alimento_2": int cantidad_alimento_2,
        # }
        # recetas = {
        #     "nombre_plato_1": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")],
        #     "nombre_plato_2": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")]
        # }

        # Completar
        print(
                f"El cocinero {self.nombre} está buscando ingredientes \
en la bodega para el plato {plato[1]}")
        
        with self.lock_bodega:
            
            for ingredientes_plato in recetas[plato[1]]:
                bodega[ingredientes_plato[0]] = bodega[ingredientes_plato[0]] - int(ingredientes_plato[1])
            
            pass

    def agregar_plato(self, plato):
        # Completar
        with self.lock_cola_pedidos_listos:
            self.lugar_trabajo.cola_pedidos_listos.append(plato)
        
        pass


class Mesero(Persona):

    evento_manejar_pedido = Event()
    def __init__(self, nombre):
        super().__init__(nombre)
        # Completar

    def run(self):
        # Completar
        while self.trabajando:
            if self.disponible:
                self.evento_manejar_pedido.set()
        
        pass

    def agregar_pedido(self, pedido, cocina):
        # Completar
        with self.lock_cola_pedidos:
            self.evento_manejar_pedido.clear()

            sleep(randint(1,2))
            cocina.cola_pedidos.append(pedido)
            self.evento_manejar_pedido.set()
        
        pass

    def entregar_pedido(self, cocina):
        # Completar
        with self.lock_cola_pedidos_listos:
            self.evento_manejar_pedido.clear()

            sleep(randint(1,3))
            if len(cocina.cola_pedidos_listos) >= 1:

                tupla_plato_entregado = cocina.cola_pedidos_listos.popleft()
                self.pedido_entregado(tupla_plato_entregado)
                print(f"El mesero {self.nombre} está entregando el pedido a la mesa {tupla_plato_entregado[0]} ")
                pass

    def pedido_entregado(self, pedido):
        # Completar
        print(f"El plato {pedido[1]} fue entregado a la mesa {pedido[0]}")
        self.evento_manejar_pedido.set()
        pass


