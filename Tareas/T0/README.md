# Tarea 0: DCCorreos

## Consideraciones generales 
1) Esta tarea consta de un Menú de inicio, el cual contiene 4 opciones para poder realizar. Cada opción tiene ciertas características que posteriormente serán explicadas, como funciones, variables, etc.

2) Se considera que una persona cuando ingresa a la opción "Iniciar sesión como usuario" su usuario es distinto a usuario + " " (usuario + espacio) ya que contiene un caracter más que hace que el usuario no esté registrado en el sistema.

3) Cuandos se ingresa al Menú de administrador, al realizar alguna de las primeras 2 acciones luego para cerrar sesión se printea 2 veces el Menú de inicio, esto es un error visual más que nada ya que el código sigue funcionando de manera fluida sin pedir más de 1 input por cada acción.

4) Cuando se hace cierta acción dentro del Menú de administrador, luego al volver al Menú de administrador pide nuevamente la clave del usuario administrador. Decidí hacer esto ya que es algo más realista, debido que cuando una persona en la vida real quiere hacer algún cambio que requiera permiso del administrador del computador requiere ingresar la contraseña del administrador para poder efectuar el cambio en el sistema.

5) Estoy considerando que las personas cuando ingresen reclamos al sistema, las comas se remplacen por espacios para facilitar el filtrado para la persona que esté trabajando con el archivo en cuestión (reclamos.csv). Esto lo hice tanto para los títulos como para las descripciones

6) Cada vez que una persona se quiera registrar en el sistema (Registrarse como usuario), si es que esta se llega a equivocar en el formato, el aviso de en qué se equivocó se printeará después de haber puesto tanto el nombre de usuario como la contraseña.

7) Cuando se está ingresando una encomienda, si es que la persona se equivoca en el formato de esta, saltarán los errores de formato luego de haber ingresado todos los datos. Se indicarán cuales fueron los errores de formato, cosa de que la persona no se vuelva a equivocar.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

#### Menú de Inicio (18pts) (18%)
##### ✅ Requisitos: Se cumplieron todos los requisitos.
##### ✅ Iniciar sesión: Se cumplió con todos las funciones de iniciar sesión.
##### ✅ Ingresar como administrador: Se cumple con que la contraseña ingresada debe ser igual a la contrasena_admin que se encuentra en parametros.py .
##### ✅ Registrar usuario: Se cumplió con todas las restricciones que deben cumplir las personas a la hora de querer registrarse.
##### ✅ Salir: Al ingresar el índice de salir del programa, el programa deja de ejecutarse.
#### Flujo del programa (31pts) (31%) 
##### ✅ Menú de Usuario: El menú de usuario cumple con todas las funciones que debe realizar (5 funciones) .
##### 🟠 Menú de Administrador: El único error que puede tener esto es lo que expliqué anteriormente con respecto al menú de administrador (REVISAR 3) ).
#### Entidades 15pts (15%)
##### ✅ Usuarios: Los usuarios contenidos en el archivo usuarios.csv se actualizan si es que una persona se registra>
##### ✅ Encomiendas: Las encomiendas contenidas en el archivo encomiendas.csv se actualizan si es que una persona ingresa una encomienda. Además, si es que el administrador decide actualizar el estado de una encomienda, también se actualiza en el archivo encomiendas.csv.
##### 🟠 Reclamos: Se cumple con que los reclamos se actualizan si es que el usuario decide ingresar un reclamo. Sin embargo, a la hora de querer filtrar el archivo y mostrarlo en la parte de Revisar reclamos (menú de administrador) se corta la descripción del reclamo luego de la primera coma. Esto sucede ya que pensaba que las descripciones no podían tener comas. Sin embargo, solo sucede con los reclamos que ya existían en el archivo reclamos.csv ya que me encargué de que los reclamos ingresados posteriores al último que estaba en el archivo original no contengan comas, tanto el título como la descripción.
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos: Se abrieron los archivos de manera correcta con UTF-8.
#### General: 21 pts (21%)
##### ✅ Menús: Funcionan de manera fluida y sin múltiples inputs.
##### ✅ Parámetros: Se trabajó con todos los parámetros que se encontraban en el archivo parametros.py.
##### ✅ Módulos: Se trabajó con módulos distintos para ciertas funciones que se querían implementar al código para hacerlo de manera más eficiente.
##### ✅ PEP8: Se cumplió con la extensión de lineas de código (400 lineas) y se cumplió con la cantidad de caracteres por linea que eran máximo 100.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```menu_inicio.py```. Luego se tienen los archivos ```funciones.py``` y ```funciones_2.py``` que se modularizaron en el programa. Todo el programa se trabajó en la carpeta ```T0```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```strftime()```
2. ```prettytable```: ```PrettyTable()```, ```add_row() ``` (DEBE INSTALARSE)

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Cuando los inputs piden números, se hace el supuesto de que la persona no va a ingresar una palabra ya que si lo hace, el programa tirará un error de código por lo que el programa automáticamente se cae.

2. Cuando el usuario/administrador quiere realizar una acción, no se va a retractar de hacerla. Es decir, cuando por ejemplo un usuario quiere ingresar una encomienda, a mitad estar rellenando los datos no se va a arrepentir de subir la encomienda. Otro ejemplo es cuando el administrador quiere revisar un reclamo, efectivamente va a querer visualizar un reclamo, no se va a arrepentir de querer ver un reclamo. Lo mismo pasa para todas las funciones, exceptuando cuando ya termina de ingresar ciertos inputs. En el caso de "ingresar una encomienda" si es que la persona no cumple con el formato ingresado se le avisará que no cumple y se le dará la opción de regresar al menú anterior o reingresar nuevamente la encomienda que desea. 

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://pypi.org/project/prettytable/ : este permite crear la tabla (prettytable) para la parte de revisar las encomiendas por parte del administrador. Esta librería se implementa entre las líneas 289-331.


