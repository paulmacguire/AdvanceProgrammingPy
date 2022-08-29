# Tarea 3: DCCasillas :school_satchel:


## Consideraciones generales :octocat:

En primer lugar, para poder corregir esta tarea de manera adecuada, se debe poner la carpeta **Sprites** dentro de la carpeta **frontend** a la misma altura que las carpetas **archivos_ui**, **ventana_de_juego.py**, **ventana_de_inicio.py**.....

No logré terminar la tarea , pero traté de hacer lo que más pude y salvar puntos de donde pueda. En mi caso, no puedo hacer que el juego funcione, sin embargo lo que pude hacer es que los clientes puedan entrar a la sala de espera y que estos vean las conexiones de los clientes entre ellos mismos. Lo que tomé como consideración fué que si se inicia el **main.py** del cliente, este debe ingresar usuario y luego pasa a la lista de espera, y después al estar el cliente 0 (por ejemplo) en la lista de espera recién el cliente 1 puede abrir el archivo **main.py**. Esto se hace así ya que si es que se abren 4 achivos **main.py** de cliente y todos al mismo tiempo ingresan el nombre de usuario, los clientes no podrán verse entre sí en la sala de espera.

El color verde siempre será para el Cliente 0, el color amarillo para el Cliente 1, el color rojo para el Cliente 2, y el color azul para el Cliente 3.

Se logra pasar a la ventana de juego, sí y solo sí hay 4 clientes en la sala de espera. No pude hacer el caso para 2 y 3 clientes.

La ventana de juego se visualiza de manera correcta con los nombres de los clientes, sin embargo, no logro hacer que se cierre la ventana de espera cuando se abre la ventana de juego. Por lo que cuando hay 4 clientes que quieren jugar, cuando se pase a la ventana de juego van a haber 8 ventanas abiertas en vez de 4.

También no pude llevar a cabo la encriptación y desincriptación de los mensajes. No obstante, pude mandar los mensajes en bloques tal cual como pidieron en el enunciado y funciona de manera adecuada.

Por último, para esta tarea me basé CASI AL 90% DE LA **AF3** Y LA **AYUDANTÍA 8**, para que lo tengan en consideración por cualquier caso de "sospecha de código".

## Explicación de las clases

- **Server**: La clase Server posee todos los atributos/métodos que son propios del servidor. De esta clase se inicia el servidor y se escucha a los clientes, con un **Host** determinado y en el puerto **5050**.

- **Cliente**: La clase Cliente posee todos los atributos/métodos que son propios del cliente. De esta clase se empieza a escuchar al servidor y también se intancia un atributo que es un objeto de la clase **Interfaz** que se explicará a continuación.

- **Interfaz**: La clase Interfaz posee todos los atributos/métodos que son propios de la interfaz. Esta clase está encargada de hacer las conexiones entre ventanas e instanciarlas, también es encargada de ejecutar ciertos métodos de las ventanas para que estas se abran y se cierren.

- **Logica**: La clase Logica posee todos los atributos/métodos que son propios de la lógica de los mensajes entre cliente y servidor.



### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Networking: 23 pts (18%)
##### ✅ Protocolo: Creo que implementé el protocolo de manera correcta entre el servidor y el cliente.
##### ✅ Correcto uso de sockets: Implementé los sockets y el uso de IPV4 para conectarlos a los determinados puertos. También ocupé los sockets para mandar información de cliente a servidor y de servidor a cliente.
##### 🟠 Conexión: Como bien expliqué antes, si bien los clientes se conectan de manera adecuada y se ven entre ellos, esto se debe hacer sí y solo sí un cliente entra a la sala de espera y luego se abre el main.py para el cliente siguiente, ya que si se abren "al mismo tiempo" e ingresan a la sala de espera "al mismo tiempo" los clientes no se podrán ver entre sí.
##### 🟠 Manejo de clientes: Si bien los clientes están instanciados de manera "correcta", no logré que los clientes se manden información entre sí. Sin embargo, pude hacer que los clientes le manden información al servidor y que el servidor les mande información a cada uno de los clientes.
#### Arquitectura Cliente - Servidor: 31 pts (25%)
##### 🟠 Roles: Creo que separé de manera adecuada el servidor y el cliente, pero igual me deja la duda al respecto.
##### 🟠 Consistencia <explicacion\>: Igual que antes, creo que fui consistente con las responsabilidades que tiene el servidor y el cliente respectivamente, pero igual quedo con la duda.
##### ✅ Logs: Cuando se lleva a cabo alguna acción, se imprime en la consola mediante el uso de **logs**.
#### Manejo de Bytes: 26 pts (21%)
##### ✅ Codificación: Implementé la codificación de manera correcta, separé el mensaje en bloques de 20 bytes y le sumé los 2 bytes respectivos.
##### ❌✅🟠 Decodificación: Cada vez que se mandan mensajes, los decodifico recibiendo el mensaje en bloques y filtrandolo para poder leer el mensaje que me está mandando el cliente.
##### ❌ Encriptación: No pude implementar la encriptación.
##### ❌ Desencriptación: No pude implementar la desencriptación.
##### 🟠 Integración: Creo que implementé el buen uso de envío de mensajes, pero quedo con la duda.
#### Interfaz: 23 pts (18%)
##### ✅ Ventana inicio: Implementé todos los elementos que se pedían en el enunciado. Se revisa que el usuario tenga un formato correcto para que pueda pasar a la Sala de Espera.
##### ✅ Sala de Espera: Implementé todos los elementos que se pedían en el enunciado. Se logran ver los clientes que están conectados y cómo estos se pueden ver entre sí.
##### 🟠 Sala de juego: Implementé todos los elementos que se pedían en el enunciado. No obstante, no logro hacer que se vea el turno de algún cliente en específico, ni tampoco el valor del Turno, Fichas en base, Fichas en color, y Fichas en victoria.
##### ❌ Ventana final: No pude implementar la ventana final.
#### Reglas de DCCasillas: 18 pts (14%)
##### ❌ Inicio del juego: No pude hacer el juego
##### ❌ Ronda: No pude hacer el juego
##### ❌ Termino del juego: No pude hacer el juego
#### General: 4 pts (3%)
##### 🟠 Parámetros (JSON): Creo que de parametros JSON pude implementarlo bien, solo que no ocupé tantos valores que son constantes por lo que no son tantos los elementos que hay en los archivos parametros.json .


#### Bonus: 5 décimas máximo
##### ❌ Cheatcode: No pude hacer el juego
##### ❌ Turnos con tiempo: No pude hacer el juego
##### ❌ Rebote: No pude hacer el juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` para el Servidor, ```main.py```  para el Cliente (cada uno con su main.py respectivo). 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5.uic```: ```loadUi```
2. ```PyQt5.QtWidgets```: ```QDialog```,```QLabel```  
3. ```PyQt5.QtGui```: ```QPixmap```,```QFont```
4. ```PyQt5.QtCore```: ```pyqtSignal```, ```Qt```
5. ```threading```: ```Thread```
6. ```json```: ```dumps```, ```loads```
7. ```socket```: ```socket```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ventana_de_inicio.py```: Contiene a ```VentanaInicio``` que es la clase de la ventana del inicio.
2. ```ventana_de_espera.py```: Contiene a ```VentanaEspera``` que es la clase de la ventana de espera.
3. ```ventana_de_juego.py```: Contiene a ```VentajaJuego``` que es la clase de la ventana de juego.
4.  ```cliente.py```: Contiene a ```Cliente``` que es la clase encargada de todas las funciones del cliente.
5. ```interfaz.py```: Contiene a ```Interfaz``` que es la clase de la ventana de juego.
6. ```servidor_archivo.py```: Contiene a ```Server``` que es la clase del servidor, y está encargada de todas las funciones que debe tener el servidor.
7. ```logica.py```: Contiene a ```Logica``` que es la clase encargada del formato de los mensajes.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://github.com/IIC2233/Syllabus/tree/main/Ayudant%C3%ADas/AY8 : Esto lo implementé para el código del cliente y servidor. Me basé muchisimo en la ayudantía 8.

2. https://github.com/IIC2233/paulmacguire-iic2233-2022-1/tree/main/Actividades/AF3 : Esto lo implementé para el código del cliente y servidor. Me basé muchísimo en la AF3.



