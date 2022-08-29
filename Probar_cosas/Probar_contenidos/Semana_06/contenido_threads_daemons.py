import threading
import time


def dormilon():
    print(f"{threading.current_thread().name} tiene sueño...")
    time.sleep(2)
    print(f"{threading.current_thread().name} se durmió.")

    
def con_insonmio():
    print(f"{threading.current_thread().name} tiene sueño...")
    time.sleep(10)
    print(f"{threading.current_thread().name} se durmió.")


# Forma 1 de hacer un thread daemon
dormilon = threading.Thread(name="Dormilón", target=dormilon, daemon=True)
# Forma 2 de hacer un thread daemon
con_insomnio = threading.Thread(name="Con insonmio", target=con_insonmio)
con_insomnio.daemon = True

# Se inicializan los threads
dormilon.start()
con_insomnio.start()


#### También podemos hacer que los threads daemons esperen una cierta cantidad de tiempo.

# Esperamos los threads.
# Lo esperamos por una cantidad indefinida de tiempo
dormilon.join()
# Esperamos sólo 5 segundos
con_insomnio.join(5)

## IMPORTANTE!!!! UN thread no puede cambiar desde daemon a no-daemon, o vicecersa.


class Daemon(threading.Thread):
    
    def __init__(self):
        super().__init__()
        # Cuando inicializamos el thread lo declaramos como daemon
        self.daemon = True
    
    def run(self):
        print("Daemon thread: Empezando...")
        time.sleep(2)
        print("Daemon thread: Terminando...")

daemon = Daemon()
daemon.start()
daemon.join()