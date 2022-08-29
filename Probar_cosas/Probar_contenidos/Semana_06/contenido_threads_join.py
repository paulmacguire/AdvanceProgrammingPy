import threading
import time

from contenido_threading import CuentaLiebres, CuentaOvejas

""" # Usamos la definicion de los Thread declarados en el ejemplo anterior
# Se crean los threads usando la clase Thread.
cristian = CuentaOvejas("Cristian", 5)
nico = CuentaOvejas("Nico", 7)
lesly = CuentaLiebres("Lesly", 5)
joaquin = CuentaLiebres("Joaquín", 20)

# Se inicializan los threads creados
cristian.start()
nico.start()
lesly.start()
joaquin.start()
print("Ayudantes: Los profes se fueron a dormir...")

# Aquí incorporamos el método join() para bloquear el programa principal
nico.join()  # Esperaremos lo que sea necesario.
print("Ayudantes: ¡NICO SE DURMIÓ!")
cristian.join() # No especificamos timeout, esperará lo que sea necesario
print("Ayudantes: ¡CRISTIAN SE DURMIÓ!")
lesly.join() # Esperaremos lo que sea necesario.
print("Ayudantes: ¡LESLY SE DURMIÓ!")
joaquin.join(1)  # Esperaremos máximo 1 segundo después del último dormido, ya es muy tarde
print("Ayudantes: ¡(casi todos) los profes se durmieron! ¡A festejar!")

# En este punto, el programa ha esperado por los cuatro threads que creamos
# Estas líneas serán ejecutadas después de que los threads hayan terminado
for _ in range(10):
    print("Ayudantes: 🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶")
    time.sleep(1)
print("Ayudantes: Ojalá no nos hayan escuchado...")
 """

import threading
import time


### Ejemplo 2, con is_alive()

# Usamos la definicion de los Thread declarados en el ejemplo anterior
# Se crean los threads usando la clase Thread.
cristian = CuentaOvejas("Cristian", 3)
nico = CuentaOvejas("Nico", 6)
lesly = CuentaLiebres("Lesly", 3)
joaquin = CuentaLiebres("Joaquin", 15)

# Se inicializan los threads creados
cristian.start()
nico.start()
lesly.start()
joaquin.start()
print("Ayudantes: Los profes se fueron a la cama...")

nico.join()  # Esperaremos lo que sea necesario.
print("Ayudantes: ¡NICO SE DURMIÓ!")
cristian.join() # No especificamos timeout, esperará lo que sea necesario
print("Ayudantes: ¡CRISTIAN SE DURMIÓ!")
lesly.join() # Esperaremos lo que sea necesario.
print("Ayudantes: ¡LESLY SE DURMIÓ!")
joaquin.join(1)  # Esperaremos máximo 1 segundos después del último dormido, ya es muy tarde

if joaquin.is_alive():
    print("Ayudantes: Joaquín sigue despierto 😞. A la casa cabros.")
else:
    print("Ayudantes: ¡Todos los profes se durmieron! ¡A festejar!")
    for i in range(10):
        print("Ayudantes: 🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶")
        time.sleep(1)


print("(Ayudantes vuelven)")
print("Ayudantes: Esperemos un poco más cabros...")
time.sleep(2)
for profe in [cristian, nico, lesly, joaquin]:
    if profe.is_alive():
        print(f"Ayudantes: {profe.name} aún está despierto 😞")
    else:
        print(f"Ayudantes: ¡{profe.name} se quedó dormido!")



