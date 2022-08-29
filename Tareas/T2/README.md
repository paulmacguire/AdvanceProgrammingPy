# Tarea 2: DCComando espacial

## Consideraciones generales :octocat:

En primer lugar, para poder corregir esta tarea de manera adecuada, se debe crear una carpeta **assets** y dentro de esa carpeta poner la carpeta de **Sprites**. Todo esto debe estar dentro de la carpeta **frontend**. Y la carpeta **Sonidos** debe colocarse dentro de la carpeta frontend, nada más. También el archivp **puntajes.txt** debe estar a la misma altura que los archivos **main.py**, **frontend**, **backend**, **parametros.py**....

No logré terminar la tarea, pero traté de hacer lo más que pude y salvar puntos de donde pueda. En mi caso, no pude hacer que se vuelvan a instanciar 2 aliens una vez que muere la pareja, por lo que mi juego tecnicamente es 1 nivel y finaliza. Es por ello que la ventana post-juego hay un botón de salir y otro de siguiente nivel pero el botón de siguiente nivel no sirve por lo que comenté anteriormente.

También otro supuesto que tomé es que al disparar al alien, hay veces que no acierta debido a lo "reducido" que és el hitbox del alien. Es por ello que hay que ser precisos con el disparo (tratar de dispararle justo al medio al alien para que así muera)

Se está tomando como supuesto que el archivo **puntajes.txt** siempre vendrá con el formato nombre,puntaje\n.

Se está considerando que el boton de **Salir** en la ventana de juego te regresa a la ventana principal y no a la de inicio.

**Algunas consideraciones que tomé:**

- La ventana no se puede agrandar ni achicar al gusto que uno quiera. Es por ello que le puse un tamaño por defecto, y se asumirá que la persona que lo corrija tenga una pantalla con el tamaño asignado a la ventana.

- El jugador cuando apreta el botón de ir a cazar en la ventana principal se registra en el archivo **puntajes.txt** con su nombre y seguido de su puntaje que es 0. Es por esto que si el jugador entra a jugar y simplemente apreta el botón salir este tendrá un puntaje de 0.

- El label de la mira se mostrará en pantalla cuando el jugador decida mover por primera vez la mira, y ahí se mantendrá el label en la pantalla.

- Si el jugador decide ponerse balas infinitas mediante el cheatcode, el puntaje se calculará con una cantidad de balas sumamente grande que es 10000.

- Si el jugador decide ocupar el cheatcode de pasar nivel, lo mandará automáticamente a la **ventana post-juego**.

- El botón pausa (P) la única función que tiene es referenciar a la persona en como pausar el juego y mediante qué tecla (que en este caso es la tecla P).

- Si la persona pausa el juego una vez que sale la animación de la explosión del alien, la explosión continuará. También la mira seguirá estando en pantalla.

## Explicación de las clases

- **Alien** : La clase Alien posee todos los atributos que son propios del alien. De esta clase se hacen 2 objetos provenientes de la clase alien y cada objeto recibe como parámetro un identificador que representa qué alien es en particular (es como una especie de RUT)

- **MiraJuego** : La clase MiraJuego posee todos los atributos que son propios de la mira del juego. Acá está implementado el movimiento de la mira, el disparo, etc.

- **Logica(Algo)** : La clase Logica(Algo) representa la lógica de esa ventana "algo". Por ejemplo, LogicaJuego, LogicaPrincipal.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Ventana de Inicio: 4 pts (4%)
#### Ventana de Ranking: 5 pts (5%)
#### Ventana principal: 7 pts (7%)
#### Ventana de juego: 14 pts (13%)
#### Ventana de post-nivel: 5 pts (5%)
#### Mecánicas de juego: 47 pts (45%)
##### 🟠 Arma: Cumplí con casi todo, sin embargo como bien dije antes, no pude hacer que se instancien denuevo 2 aliens una vez que se mata a la pareja inicial, es por ello que no pude hacer tecnicamente el método que reincie las coordenadas de la mira y las ponga en el centro de la pantalla nuevamente.
##### 🟠 Aliens y Escenario de Juego: Cumplí con los escenarios del juego, pero no todo con los aliens. No supe como volver a instanciar 2 aliens en la pantalla, pero lo demás que se pedía para los aliens creo que cumplí con todo.
##### ✅ Fin de Nivel: El nivel termina cuando se te acaban las balas y/o cuando se te acaba el tiempo.
##### 🟠 Fin del juego: Está directamente relacionado con el fin de nivel ya que tecnicamente mi juego solo tiene 1 nivel.
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa: El juego se pausa con la tecla P y se pausa todos los moviemientos del juego, incluido aliens y mira.
##### ✅ O + V+ N + I: Se otorgan balas infinitas (10000 exactamente) una vez ingresadas las teclas O V N I.
##### ✅ C + I + A: Se termina el nivel una vez ingresadas las teclas C I A.
#### General: 14 pts (13%)
##### ✅ Modularización: Separé varias ventanas entre un backend y un frontend, lo que me generaría un mejor uso de código.
##### 🟠 Modelación: Si bien separé las ventanas entre un backend y un frontend, por temas de cohesión de código tuve que poner algunos labels en algunos backend.
##### ✅ Archivos
##### ✅ Parametros.py: Gran parte de los valores constantes son incluidos en este archivo por temas de practicidad.
#### Bonus: 10 décimas máximo
##### ✅ Risa Dog: La risa suena una vez consigues ganar el nivel.
##### ❌ Estrella 
##### ❌ Disparos extra
##### ❌ Bomba

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además, como bien comenté antes se debe crear el siguente directorio:
1. ```assets``` en ```frontend```

Como bien expliqué antes, es de suma importancia que la carpeta **assets** esté dentro de la carpeta **frontend** y que dentro de la carpeta **assets** esté la carpeta **Sprites**. También es muy relevante que la carpeta **Sonidos** esté dentro de la carpeta **frontend**


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5.uic```: ```loadUi```
2. ```PyQt5.QtMultimedia```: ```QMediaPlayer```,```QMediaContent```  (debe instalarse)
3. ```PyQt5.QtWidgets```: ```QDialog```,```QLabel```  
4. ```PyQt5.QtGui```: ```QPixmap```,```QFont```
5. ```PyQt5.QtCore```: ```pyqtSignal```, ```QTimer```, ```Qt```, ```QUrl```, ```QRect```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ventana_inicio.py```: Contiene a ```VentanaInicio``` que es la clase de la ventana del inicio.
2. ```ventana_principal.py```: Contiene a ```VentanaPrincipal``` que es la clase de la ventana principal
3. ```ventana_ver_rankings.py```: Contiene a ```VentanaRankings``` que es la clase de la ventana de rankings
4. ```ventana_juego.py```: Contiene a ```VentanaJuego``` que es la clase de la ventana de juego
5. ```ventana_post_juego.py```: Contiene a ```VentanaPostJuego``` que es la clase de la ventana del post juego
6. ```logica_juego.py```: Contiene a ```LogicaJuego``` que es la clase de la logica de todo el juego, también contiene a ```Alien``` que es la clase de los aliens, y finalmente a ```MiraJuego``` que es la clase del arma.
7. ```logica_principal.py```: Contiene a ```LogicaPrincipal``` que es la clase de la logica de la ventana principal.



## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://www.youtube.com/watch?v=Ciz3slS1xt0 : este hace que pueda instanciar la risa del **terminator-dog** y luego reproducirla,  y está implementado en el archivo **logica_juego.py** en las líneas **213** y también en **ventana_juego.py** en la linea **365**

2. https://stackoverflow.com/questions/38507011/implementing-keypressevent-in-qwidget : este hace que las teclas del teclado tengan funciones específicas, y está implementado en el archivo **ventana_juego.py** en las lineas **133**
