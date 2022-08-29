import threading


class Contador: 
    def __init__(self):
        self.valor = 0
""" 
## El mismo lock para todos los threads
lock_global = threading.Lock()

def sumador_con_seccion_critica(contador, lock):
    thread_actual = threading.current_thread()
    for _ in range(20):
        # Pedimos el lock antes de entrar a la sección crítica.
        lock.acquire()
        # --- Sección crítica ---. 
        # Está garantizado que en estas líneas sólo habrá un thread a la vez.
        contador.valor += 1
        # --- Fin de la sección crítica ---.
        # Liberamos el lock luego de salir de la sección crítica.
        lock.release()
        print(f"{thread_actual.name}")

contador = Contador()        
t1 = threading.Thread(name= "Thread 1", target=sumador_con_seccion_critica, args=(contador,lock_global))
t2 = threading.Thread(name= "Thread 2", target=sumador_con_seccion_critica, args=(contador,lock_global))

# Esto podría tomar algunos segundos...
t1.start()
t2.start()
t1.join()
t2.join()

print("Listo, nuestro contador vale", contador.valor) """


###### Lo mismo pero con el comando with lock

import time


lock_global = threading.Lock()

def sumador(contador, lock):
    nombre = threading.current_thread().name
    contador_numero = 0
    for _ in range(10):
        with lock:
            
            print(f"Este es el contador del for: {contador_numero}")
            contador_numero += 1
            # --- Sección crítica ---. 
            # Está garantizado que en estas líneas sólo habrá un thread a la vez.
            valor = contador.valor
            print(f"{nombre}: lee {valor}")
            nuevo_valor = valor + 1
            print(f"{nombre}: suma 1 => {nuevo_valor}")
            contador.valor = nuevo_valor
            print(f"{nombre}: guarda {nuevo_valor}")
            time.sleep(1)
            # --- Fin de la sección crítica ---.

contador = Contador()        
t1 = threading.Thread(name="T1", target=sumador, args=(contador,lock_global))
t2 = threading.Thread(name="T2", target=sumador, args=(contador,lock_global))

t1.start()
t2.start()
t1.join()
t2.join()