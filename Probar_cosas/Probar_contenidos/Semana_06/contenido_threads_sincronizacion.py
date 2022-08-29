import threading


class Contador: 
    def __init__(self):
        self.valor = 0

        
import time

def sumador(contador):
    nombre = threading.current_thread().name
    for _ in range(10):
        valor = contador.valor
        print(f"{nombre}: lee {valor}")
        nuevo_valor = valor + 1
        print(f"{nombre}: suma 1 => {nuevo_valor}")
        contador.valor = nuevo_valor
        print(f"{nombre}: guarda {nuevo_valor}")
        time.sleep(1)

contador = Contador()        
t1 = threading.Thread(name="T1", target=sumador, args=(contador,))
t2 = threading.Thread(name="T2", target=sumador, args=(contador,))

t1.start()
t2.start()
t1.join()
t2.join()

print("Listo, nuestro contador vale", contador.valor)