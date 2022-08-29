""" import threading

def contar_diez_ovejas():
    print("Tengo sueño...")
    for numero in range(1, 11):
        print(f"({numero} oveja{'s' if numero > 1 else ''})")
    print("A dormir...")


mi_hilo = threading.Thread(target=contar_diez_ovejas)


def saludar():
    thread_actual = threading.current_thread()
    print(f"Hola desde {thread_actual.name}")


hilo_1 = threading.Thread(name="Mi thread 1", target=saludar)
hilo_2 = threading.Thread(name="Mi thread 2", target=saludar)

# Llamaremos a saludar() desde los threads nombrados
hilo_1.start()
hilo_2.start()

saludar() """


#### Ejemplo 2

""" import threading
import time


def trabajador_rapido():
    # Función rápida, que toma 2 segundos
    thread_actual = threading.current_thread()
    print(f"{thread_actual.name} partiendo...")
    # Pondremos a dormir el thread por 2 segundos simulando 
    # que ocurre algun proceso dentro de la función
    time.sleep(2) 
    print(f"{thread_actual.name} terminando...")


def trabajador_lento():
    # Función lenta, que toma 6 segundos
    thread_actual = threading.current_thread()
    print(f"{thread_actual.name} partiendo...")
    # Ponemos a dormir el thread por 6 segundos simulando
    # un proceso más largo que el anterior dentro de la función
    time.sleep(6) 
    print(f"{thread_actual.name} terminando...")

# Creamos los threads usando la clase Thread
hilo_lento = threading.Thread(name="Hilo lento (6s)", target=trabajador_lento)
hilo_rapido_1 = threading.Thread(name="Hilo rápido (2s)", target=trabajador_rapido)
hilo_rapido_2 = threading.Thread(target=trabajador_rapido)  # Usa el nombre asignado por defecto


# Se inicializan los threads creados
hilo_rapido_1.start() # Dormirá por 2 segundos
hilo_rapido_2.start() # Dormirá por 2 segundos
hilo_lento.start() # Dormirá por 6 segundos
print("Thread principal: Fueron iniciados 3 threads")
# Todas estas líneas serán ejecutadas mientras los threads
# se ejecutan independientemente del programa principal

print()
# El thread principal ejecutará lo que queda de código
# mientras los otros 3 threads hacen lo suyo

for i in range(10):
    print(f"Thread principal: Segundo actual: {i}")
    time.sleep(1) """


### Ejemplo 3

""" import threading
import time


def contar_ovejas_hasta(max_ovejas):
    thread_actual = threading.current_thread()
    print(f"{thread_actual.name} tiene sueño...")
    for numero in range(1, max_ovejas + 1):
        time.sleep(1)
        print(f"({thread_actual.name}: {numero} oveja{'s' if numero > 1 else ''})")
    print(f"{thread_actual.name} a dormir...")


# Se crean los threads usando la clase Thread, asociada a la función objetivo para 
# ser ejecutada por el thread, y los atributos de la función son ingresados en 
# args o kwargs

t1 = threading.Thread(name="Thread 1", target=contar_ovejas_hasta, args=(10,))
t2 = threading.Thread(name="Thread 2", target=contar_ovejas_hasta, kwargs={"max_ovejas": 15})
t1.start()
t2.start() """


### Ejemplo 4

import threading
import time


class CuentaOvejas(threading.Thread): # Hereda de Thread
    """Este será nuestro nuevo Cuenta Ovejas basado en Thread"""
    def __init__(self, nombre, max_ovejas):
        # En el caso de los threads, lo primero es invocar al init original. SIEMPRE.
        super().__init__(name=nombre)
        self.max_ovejas = max_ovejas # Se agrega un atributo de instancia extra
    
    def run(self):
        # Este metodo define las instrucciones a ejecutar de este thread
        # cuando ejecutamos el metodo start()
        print(f"{self.name} tiene sueño...")
        tiempo_partida = time.time()
        for numero in range(1, self.max_ovejas + 1):
            time.sleep(1)
            print(f"({self.name}: {numero} oveja{'s' if numero > 1 else ''})")
        print(f"{self.name} a dormir...")
        print(f"{self.name} se durmió después de {time.time() - tiempo_partida} seg.")

        
class CuentaLiebres(threading.Thread): # Hereda de Thread
    """
    Este será un nuevo Cuenta Liebres basado en Thread
    Las liebres son más rápidas, así que cuenta dos por segundo
    """
    def __init__(self, nombre, max_liebres):
        super().__init__(name=nombre)
        self.max_liebres = max_liebres
    
    def run(self):
        print(f"{self.name} tiene sueño...")
        tiempo_partida = time.time()   # Lo que hace el metodo time() es entregar el tiempo actual
        for numero in range(1, self.max_liebres + 1):
            if numero % 2 == 1:
                time.sleep(1)
            print(f"({self.name}: {numero} liebre{'s' if numero > 1 else ''})")
        print(f"{self.name} a dormir...")
        print(f"{self.name} se durmió después de {time.time() - tiempo_partida} seg.")
        

""" # Se crean los threads
cuenta_ovejas = CuentaOvejas("Cristian", 10)
cuenta_liebres = CuentaLiebres("Nico", 10)
print("Thread principal: Fueron creados 2 threads")


# Se inicializan los threads creados
cuenta_ovejas.start()
cuenta_liebres.start()
print("Thread principal: Fueron iniciados 2 threads")
# Todas estas líneas serán ejecutadas mientras los threads se ejecutan
# independientemente del programa principal


print() 
# El thread principal ejecutará lo que queda código
# mientras los otros 2 threads hacen lo suyo
for i in range(10):
    print(f"Thread principal: Segundo actual: {i}")
    time.sleep(1) """