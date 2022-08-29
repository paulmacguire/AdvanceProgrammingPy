from datetime import datetime
from prettytable import PrettyTable
import funciones as funciones
import funciones_2 as funciones_2
import parametros as par

def menu_de_inicio():
    print(f"---- Bienvenid@ a DCCorreos de Chile ----\n")
    print(f" ** Menú de inicio **\n")
    print(f"Seleccione una de las siguientes opciones:\n")

    print("[1] Iniciar sesión como usuario")
    print("[2] Registrarse como usuario")
    print("[3] Iniciar sesión como administrador")
    print("[4] Salir del programa")
menu_de_inicio()
opcion = int(input("\nIndique la opción elegida: "))
while opcion != 4:
    if opcion == 1: # Iniciar sesión como usuario
        lista_de_encomiendas_realizadas = []
        # Lista que sea vacía cada vez que un usuario nuevo inicia sesión.
        iniciar_sesion_usuario = str(input("Ingrese su nombre de usuario: "))
        iniciar_sesion_contrasena = str(input("Ingrese su contraseña: "))
        if (iniciar_sesion_usuario in funciones.diccionario_de_cuentas) == True:
            if iniciar_sesion_contrasena != \
                    funciones.diccionario_de_cuentas[iniciar_sesion_usuario]:
                while True:
                    print("Contraseña incorrecta. Porfavor, intente nuevamente.")
                    iniciar_sesion_contrasena = str(
                        input("Ingrese su contraseña: "))

                    if iniciar_sesion_contrasena == funciones.diccionario_de_cuentas[iniciar_sesion_usuario]:
                        break

        if (iniciar_sesion_usuario in funciones.diccionario_de_cuentas) == False:
            print(
                "Usted no se encuentra registrado en el sistema. Debe crearse una cuenta.")

        else:
            print("\n")
            lista_de_encomiendas_realizadas = []

            def menu_de_usuario():
                print()
                print(f"* Menú de usuario *")
                print(f"[1] Hacer Encomienda")
                print(f"[2] Revisar estado de encomiendas realizadas")
                print(f"[3] Realizar reclamos ")
                print(f"[4] Ver el estado de los pedidos personales")
                print(f"[5] Cerrar sesión")

                opcion_menu_de_usuario = int(
                    input("\nIndique qué opción desea realizar: "))
                # Con este while hace que se pueda volver al menú
                while opcion_menu_de_usuario != 5:
                    # [1] Ingresar Encomienda
                    while opcion_menu_de_usuario == 1:
                        with open("encomiendas.csv", encoding="UTF-8") as encomiendas:
                            lista_encomiendas = []
                            # Con este for lo que se hará es recorrer las lineas del encomiendas.csv
                            # y agregar cada fila filtrada a una lista_encomiendas
                            # la cual contendrá todas las encomiendas registradas.
                            for linea in encomiendas:
                                encomienda_solicitada = linea.strip(
                                    "\n").split(",")
                                lista_encomiendas.append(
                                    encomienda_solicitada)

                        print(
                            f"* Ingresa los datos de tu encomienda a continuación *")

                        nombre_articulo = str(
                            input("Ingrese el nombre del artículo: "))

                        nombre_destinatario = str(
                            input("Ingrese el nombre del destinatario: "))

                        peso_articulo = float(
                            input("Ingrese el peso del artículo en kilogramos (kg): "))

                        destino_articulo = str(
                            input("Ingrese el destino del artículo: "))

                        # Nombre del artículo no debe contener ","
                        # El destinatario debe estar registrado en el DCCorreos de
                        # Chile en el archivo usuarios.csv
                        # #El peso máximo de los articulos deben ser MAX_PESO
                        while True:
                            if (nombre_articulo.count(",")) == 0 and \
                                ((nombre_destinatario in funciones.diccionario_de_cuentas) == True)\
                                    and (peso_articulo <= par.MAX_PESO):
                                with open("encomiendas.csv", "a", encoding="UTF-8") as encomiendas:
                                    data = datetime.now()
                                    fecha_y_hora_actual = data.strftime(
                                        "%Y/%m/%d %H:%M:%S")
                                    concatenacion_palabras_encomienda = nombre_articulo + "," + \
                                        nombre_destinatario + "," + \
                                        str(peso_articulo) + "," + destino_articulo + \
                                        "," + fecha_y_hora_actual + ",Emitida\n"
                                    encomiendas.write(
                                        concatenacion_palabras_encomienda)
                                    lista_de_encomiendas_realizadas.append(
                                        [nombre_articulo, "Emitida"])

                                return menu_de_usuario()

                            while (nombre_articulo.count(",") != 0) or \
                                ((nombre_destinatario in funciones.diccionario_de_cuentas) == False) or \
                                    (peso_articulo > par.MAX_PESO):
                                print(
                                    "Los datos ingresados no cumplen con  el formato en cuestión.")
                                print("\nLos datos con formato erróneo son: ")
                                if nombre_articulo.count(",") != 0:
                                    print(
                                        "El nombre del artículo contiene comas.")
                                if (nombre_destinatario in funciones.diccionario_de_cuentas) == False:
                                    print(
                                        "El nombre del destinatario no se encuentra registrado en el sistema.")
                                if peso_articulo > par.MAX_PESO:
                                    print(
                                        "El artículo no cumple con los estándares de pesaje")

                                print("¿Qué es lo que desea hacer?")
                                print("[1] Continuar")
                                print("[2] Cancelar encomienda")

                                opcion_que_desea_hacer = int(
                                    input("Ingrese el número de la función que desea hacer: "))
                                if opcion_que_desea_hacer == 1:
                                    nombre_articulo = str(
                                        input("Ingrese el nombre del artículo: "))
                                    nombre_destinatario = str(
                                        input("Ingrese el nombre del destinatario: "))
                                    peso_articulo = float(
                                        input("Ingrese el peso del artículo en kilogramos (kg): "))
                                    destino_articulo = str(
                                        input("Ingrese el destino del artículo: "))

                                elif opcion_que_desea_hacer == 2:
                                    return menu_de_usuario()

                    # [2] Revisar el estado de encomiendas realizadas
                    while opcion_menu_de_usuario == 2:
                        print(lista_de_encomiendas_realizadas)

                        return menu_de_usuario()

                    # [3] Realizar reclamos
                    while opcion_menu_de_usuario == 3:
                        print("Este es el buzón de reclamos.")

                        titulo_reclamo = str(
                            input("Porfavor ingrese el título de su reclamo (no debe contener comas): "))
                        titulo_reclamo = titulo_reclamo.replace(",", " ")

                        descripcion_reclamo = str(
                            input("Inserte el texto aquí explicando su reclamo: "))
                        descripcion_reclamo = descripcion_reclamo.replace(
                            ",", " ")
                        with open("reclamos.csv", "a", encoding="UTF-8") as reclamos:
                            reclamos.write(
                                iniciar_sesion_usuario+","+titulo_reclamo + ","+descripcion_reclamo)

                        return menu_de_usuario()

                    # [4] Ver el estado de los pedidos personales
                    while opcion_menu_de_usuario == 4:
                        with open("encomiendas.csv", encoding="UTF-8") as encomiendas:
                            lista_encomiendas = []
                            # Con este for lo que se hará es recorrer las lineas del encomiendas.csv
                            # y agregar cada fila filtrada a una lista_encomiendas
                            # la cual contendrá todas las encomiendas registradas.
                            for linea in encomiendas:
                                encomienda_solicitada = linea.strip(
                                    "\n").split(",")
                                lista_encomiendas.append(encomienda_solicitada)
                            lista_encomiendas_del_usuario = []
                            for cada_encomienda_del_usuario in lista_encomiendas:
                                if cada_encomienda_del_usuario[1] == iniciar_sesion_usuario:
                                    lista_encomiendas_del_usuario.append(
                                        cada_encomienda_del_usuario)

                        print("Sus pedidos personales son los siguientes: ")
                        numero_de_pedido = 1
                        for pedido_personal in lista_encomiendas_del_usuario:
                            print(
                                f"Su pedido N°{numero_de_pedido} es el siguiente:")
                            print(f"Artículo: {pedido_personal[0]}")
                            print(f"Nombre: {pedido_personal[1]}")
                            print(f"Peso: {pedido_personal[2]}")
                            print(f"Destino: {pedido_personal[3]}")
                            print(f"Fecha y Hora: {pedido_personal[4]}")
                            print(f"Estado del pedido: {pedido_personal[5]}\n")
                            numero_de_pedido += 1
                        return menu_de_usuario()

                    # [5] Cerrar sesion
                    while opcion_menu_de_usuario == 5:
                        return menu_de_inicio()
                    while opcion_menu_de_usuario > 5 or opcion_menu_de_usuario < 1:
                        print(
                            "\nHa ocurrido un error, intente nuevamente ingresando otro número.")
                        print()
                        return menu_de_usuario()

                print("Ha cerrado sesión.")
            menu_de_usuario()

    elif opcion == 2:
        # Registrarse como usuario
        def menu_registrarse_como_usuario():
            print("** Bienvenido al menú de registro **\n")
            print("** Ingrese el nombre de usuario con el que se quiere registrar **\n")

            usuario_nuevo_registrado = str(
                input("Ingrese aquí el nombre de usuario (no debe incluir comas \
ni caracteres especiales y debe ser alfabético): "))
            contrasena_usuario_nuevo_registrado = str(
                input("Ingrese su contraseña aquí (debe incluir mínimo 5 \
caracteres y debe ser alfanumérico): "))

            while (usuario_nuevo_registrado in funciones.diccionario_de_cuentas) or \
                (funciones_2.contador_caracteres_especiales(usuario_nuevo_registrado) >= 1) or \
                (funciones_2.contador_caracteres_numericos(usuario_nuevo_registrado) >= 1)\
                or (funciones_2.contador_de_caracteres_alfabeticos(usuario_nuevo_registrado) < par.MIN_CARACTERES)\
                or (funciones_2.contador_caracteres_especiales(contrasena_usuario_nuevo_registrado) >= 1)\
                    or (len(contrasena_usuario_nuevo_registrado) < par.LARGO_CONTRASENA):
                print()
                if (usuario_nuevo_registrado in funciones.diccionario_de_cuentas):
                    print(
                        "Este nombre de usuario ya existe. Porfavor, intente con uno nuevo.")
                if (funciones_2.contador_caracteres_numericos(usuario_nuevo_registrado) >= 1):
                    print(
                        "Este nombre de usuario contiene números. Porfavor, intente con uno nuevo.")
                if (funciones_2.contador_de_caracteres_alfabeticos(usuario_nuevo_registrado) < par.MIN_CARACTERES):
                    print(
                        "El nombre de usuario no contiene como mínimo\
 5 caracteres alfabéticas. Porfavor, ingrese otro usuario. ")
                if (len(contrasena_usuario_nuevo_registrado) < par.LARGO_CONTRASENA):
                    print(
                        "La contraseña ingresada no cumple con el\
 mínimo de caracteres que son 6. Porfavor, ingrese otra contraseña. ")
                if (funciones_2.contador_caracteres_especiales(usuario_nuevo_registrado) >= 1):
                    print(
                        "El nombre de usuario no puede contener caracteres especiales, solo letras. ")
                if (funciones_2.contador_caracteres_especiales(contrasena_usuario_nuevo_registrado) >= 1):
                    print(
                        "La contraseña no puede contener caracteres especiales. Porfavor, intente nuevamente")
                return

            concatenacion_usuario_contrasena_registrada = usuario_nuevo_registrado + \
                ","+contrasena_usuario_nuevo_registrado+"\n"
            with open("usuarios.csv", "a", encoding="UTF-8") as us:
                us.write(concatenacion_usuario_contrasena_registrada)
            print(
                "\n¡Su registro fue un exito!. Volverá al menú de inicio para que inicie sesión. ")
        menu_de_inicio()
        menu_registrarse_como_usuario()

    elif opcion == 3:  # Iniciar sesión como administrador
        def menu_de_administrador():
            print("\n** Menú de administrador **\n")

            contrasena_administrador = str(
                input("Ingrese la contraseña del administrador: "))
            if contrasena_administrador != par.CONTRASENA_ADMIN:
                print("Contraseña invalida. Porfavor, intente nuevamente.")
                print("\n")
                print(
                    "¿Qué desea realizar?\n\nInserte [0] si quiere volver a introducir\
 la contraseña\nInserte [1] si quiere volver al menú de inicio.")
                opcion_contrasena_invalida = int(input("Ingrese el número: "))
                if opcion_contrasena_invalida == 0:
                    return menu_de_administrador()
                elif opcion_contrasena_invalida == 1:
                    return menu_de_inicio()
                else:
                    print(
                        "El número que ha ingresado es inválido. Volverá al menú de inicio.")
                    return menu_de_inicio()

            print(
                "[1] Actualizar encomiendas\n[2] Revisar reclamos\n[3] Cerrar sesión")
            opcion_elegida_administrador = int(
                input("Indique la opción elegida (administrador): "))

            # [1] Actualizar encomiendas
            while opcion_elegida_administrador == 1:
                with open("encomiendas.csv", encoding="UTF-8") as encomiendas:
                    tabla = PrettyTable([" Indice ", "   Nombre artículo   ", "   Receptor   ",
                                        "  Peso  ", "   Destino   ", "   Fecha y Hora   ", "   Estado   "])
                    lista_encomiendas = []
                    # Con este for lo que se hará es recorrer las lineas del encomiendas.csv
                    # y agregar cada fila filtrada a una lista_encomiendas
                    # la cual contendrá todas las encomiendas.
                    indice = -1
                    for linea in encomiendas:
                        linea = linea.strip("\n").split(",")
                        indice_con_corchetes = [indice]
                        linea.insert(0, indice_con_corchetes)
                        lista_encomiendas.append(linea)
                        indice += 1

                    lista_encomiendas.pop(0) # Con este pop se saca nombre_articulo,receptor,peso,destino,fecha,estado
                    for encomiendas_en_particular in lista_encomiendas:
                        tabla.add_row(encomiendas_en_particular)
                    print(tabla)
                encomienda_que_quiere_ver_administrador = int(
                    input("Inserte el índice de la encomienda que desea actualizar: "))
                for encomienda_que_esta_viendo_el_administrador in lista_encomiendas:
                    if encomienda_que_esta_viendo_el_administrador[0] == [encomienda_que_quiere_ver_administrador]:
                        actualizacion = funciones_2.actualizar_encomiendas(
                            encomienda_que_esta_viendo_el_administrador)
                        lista_encomiendas[encomienda_que_quiere_ver_administrador] = actualizacion

                tabla2 = PrettyTable([" Indice ", "   Nombre artículo   ", "   Receptor   ",
                                     "  Peso  ", "   Destino   ", "   Fecha y Hora   ", "   Estado   "])

                for encomiendas_en_particular_actualizada in lista_encomiendas:
                    tabla2.add_row(encomiendas_en_particular_actualizada)
                print(tabla2)

                with open("encomiendas.csv", "w", encoding="UTF-8") as enco:
                    lista_nueva_encomiendas_write = lista_encomiendas
                    enco.write(
                        "nombre_articulo,receptor,peso,destino,fecha,estado\n")
                    for encomienda in lista_nueva_encomiendas_write:
                        encomienda.pop(0)
                        encomienda_final = ",".join(encomienda) + "\n"
                        enco.write(encomienda_final)

                opcion_volver_menu_anterior = int(
                    input("Inserte [1] para volver al menú anterior: "))
                while opcion_volver_menu_anterior != 1:
                    print(
                        "El número ingresado es inválido. Porfavor, intente nuevamente")
                    opcion_volver_menu_anterior = int(
                        input("Inserte [1] para volver al menú anterior: "))
                return menu_de_administrador()

            # [2] Revisar reclamos
            while opcion_elegida_administrador == 2:
                with open("reclamos.csv", encoding="UTF-8") as reclamos:
                    lista_reclamos = []
                    lista_reclamos_indexada = []
                    indice = -1
                    for linea in reclamos:
                        linea = linea.strip("\n").split(",")
                        lista_reclamos.append(linea)
                        lista_reclamos_indexada.append([indice, linea[1]])
                        indice += 1
                    lista_nueva_reclamos_indexada = lista_reclamos_indexada
                    lista_nueva_reclamos_indexada.pop(0)
                    lista_reclamos.pop(0)
                    for reclamos_indexados in lista_nueva_reclamos_indexada:
                        print(
                            f"\n[{reclamos_indexados[0]}] {reclamos_indexados[1]}")

                    print("¿Qué reclamo desea visualizar?")
                    reclamo_que_desea_visualizar = int(
                        input("Ingrese el índice del reclamo que desea visualizar: "))
                    while 0 <= reclamo_que_desea_visualizar <= len(lista_nueva_reclamos_indexada):
                        for indice_reclamo in range(0, len(lista_reclamos)):
                            if indice_reclamo == reclamo_que_desea_visualizar:
                                print(
                                    f"Usuario: {lista_reclamos[indice_reclamo][0]}")
                                print(
                                    f"Título del reclamo: {lista_reclamos[indice_reclamo][1]}")
                                print(
                                    f"Descripción del reclamo: {lista_reclamos[indice_reclamo][2]}")

                        numero_para_salir = int(input(
                            "Ingrese [1] si desea volver al menú de administrador.\nIngrese cualquier\
 otro número que no sea 1 para volver a ver los reclamos: "))
                        if numero_para_salir == 1:
                            return menu_de_administrador()
                        else:
                            reclamo_que_desea_visualizar = int(
                                input("Ingrese el índice del reclamo que desea visualizar: "))
                    return menu_de_administrador()

            # [3] Cerrar cesión
            while opcion_elegida_administrador == 3:
                return menu_de_inicio()

            while opcion_elegida_administrador > 3 or opcion_elegida_administrador < 1:
                print("La opción escogida es inválida, intente nuevamente.")
                return menu_de_administrador()
            # Acá tengo un problema, resulta que cada vez que quiero cerrar sesión como administrador,
            # se printea 2 veces el menú de inicio pero funciona bien. Es algo visual mas que nada.
        menu_de_administrador()
    else:
        print("\nHa ocurrido un error, intente nuevamente ingresando otro número.")
        print()
    menu_de_inicio()
    opcion = int(input("Indique la opción elegida: "))
print("Ha salido del programa.")
