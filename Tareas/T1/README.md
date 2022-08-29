# Tarea 1: DCCasino


## Consideraciones generales 
1) Esta tarea consta de un Menú de inicio, el cual contiene 2 opciones principales: [1] que corresponde a iniciar partida el cual la "persona" entra al casino. 

2) Se consideró que los parámetros de cada archivo .csv están ordenados de una forma en específica. Esto quiere decir que si por ejemplo se cambia de lugar "personalidad" en el archivo jugadores.csv, el código correrá mal. No se tuvo en cuenta el desorden de esto.

3) No consideré el dinero faltante para pagar la deuda del jugador, sino que consideré que cuando este quiere "salir" del Casino es porque ya está listo con la cantidad de dinero que ganó para poder pagarle la deuda a la otra persona.

4) Se consideró que la clase Casino no tenga parámetros y que se juegue todo en el archivo main.py

5) Se consideró que cuando una persona juega más de una vez un juego en particular, este no se agregará más de una vez a la lista de juegos jugados del jugador.

6) Se considera que la persona no utilizará caracteres especiales a la hora de ingresar los inputs.

7) Se creó cada clase en archivos diferentes y luego se importaron esos archivos al archivo main.py. Luego, dentro del archivo main.py se instanciaron todas los objetos de las clases correspondientes.


#### Programación Orientada a Objetos: 38 pts (28%)
##### ❌ Diagrama: No pude realizar el diagrama ya que pensé que se entregaba a la misma hora del README.
##### 🟠 Definición de clases, atributos, métodos y properties : Definí todas las clases y métodos que se solicitaban, sin embargo no se realizó de manera adecuada la clase Casino. Se hizo el método evento_especial y nada más.
##### ✅ Relaciones entre clases: Se crearon las clases y se heredaron algunas de otras, como en el caso de Bebestibles que heredó a Jugo, Gaseosa,y Brebaje mágico. También la clase Jugador heredó a Ludópata, Bebedor, Tacaño, y Casual.

#### Simulaciones: 10 pts (7%)
##### 🟠 Crear partida: La partida se crea de manera adecuada, sin embargo como expliqué antes no se ejecutó el programa en la clase Casino, sino que se ejecutó todo en el archivo main.py y luego se fueron instanciando las clases.

#### Acciones: 35 pts (26%)
##### ✅ Jugador: Se realizaron todos los métodos que se solicitaron para jugador, todos los métodos para cada subclase de jugador.
##### ✅ Juego: Se realizaron todos los métodos que se solicitaron para juego.
##### ✅ Bebestible: Se realizaron todos los métodos
##### 🟠 Casino: Como se explicó anteriormente, solo se creó 1 método de la clase Casino. También la clase Casino no tenía atributos, solo eran métodos.

#### Consola: 41 pts (30%)
##### ✅ Menú de Inicio: El código del menú de inicio corre de forma fluida.
##### ✅ Opciones de jugador: El código de opciones de jugador corre de forma fluida.
##### ✅ Menú principal: El código del menú principal corre de forma fluida.
##### ✅ Opciones de juegos: El código de opciones de juegos corre de forma fluida. <explicacion>
##### ✅ Carta de bebestibles: El código de carta de bebestibles corre de forma fluida.
##### ✅ Ver estado del Jugador: Se printean todos los cambios realizados a los atributos del objeto jugador de la clase Jugador. Funciona de forma fluida el programa.
##### 🟠 Robustez: Es posible que el código en general (la mezcla de todos los archivos) se pueda hacer más corto, preciso, y prolijo. Sin embargo, el flujo del programa es adecuado.

#### Manejo de archivos: 13 pts (9%)
##### 🟠 Archivos CSV: Como expliqué anteriormente, si bien ocupé todos los archivos.csv, no consideré que estos pueden estar en desorden a la hora de ejecutar el código. Es por ello que puedan tener en consideración eso a la hora de correr el programa. Que esté con la misma sintaxis de como se entregó cuando recién se publicó la tarea.
##### 🟠 parametros.py: Se crearon y utilizaron casi todos los parámetros. Los parámetros que faltaron fueron los límites de los setter de la clase Jugador, que esos los consideré tal cual como salía en el enunciado.

#### Bonus: 3 décimas máximo
##### ❌ Ver Show: No realicé el show

#### Ejecución 💻
1. El archivo principal de la tarea es ```main.py```. Luego se tienen los archivos ```clase_bebestible.py```, ```clase_casino.py```, ```clase_juego.py```, ```clase_jugador.py```, ```funciones_menus.py```, ```funciones2.py```, y finalmente ```parametros.py```. Todo el programa se trabajó en la carpeta ```T1``

#### Librerías 📚

La lista de librerías externas que utilicé fue la siguiente:

1. ```prettytable```: ```PrettyTable()```, ```add_row() ``` (DEBE INSTALARSE)
Por otro lado, los módulos que fueron creados fueron los siguientes:

##### clase_jugador: Contiene la clase Jugador, y ciertas subclases como Ludopata, Tacano, Bebedor, y Casual. Todas estas subclases son heredadas de Jugador.

##### clase_bebestible: Contiene la clase Bebestibles, y ciertas subclases como Jugo, Gaseosa, y BrebajeMagico.

##### clase_juego: Contiene la clase Juego, en la cual contiene todos los métodos que utilizaron para raelizar los juegos.

##### clase_casino: Contiene la clase Casino, en la cual contiene a 2 acciones (métodos) que puede realizar Casino.

##### funciones_menus: Contiene todas las funciones para poder printear los menús de manera adecuada.

##### funciones2: Contiene una función que permite abrir archivos y sacarle la primera linea de archivo que siempre indica el orden de como están escrito los datos dentro del código.

##### parametros: Contiene todos los parámetros que se utilizaron en la ejecución del programa.

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://pypi.org/project/prettytable/ : este permite crear la tabla (prettytable) para la parte de revisar las encomiendas por parte del administrador. Esta librería se implementa en el archivo funciones_menus, la cual es utilizada en la función menu_principal_comprar_bebestible() y opciones_de_juego().
