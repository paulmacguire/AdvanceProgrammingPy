import clase_jugador
import clase_juego
import clase_bebestible
import clase_casino
import funciones_menus
import funciones2
from prettytable import PrettyTable

finalizar_programa = False

while not finalizar_programa:
    funciones_menus.menu_de_inicio()
    ingresar_input = str(
        input("Ingrese el índice de la opción que desee realizar: "))

    if ingresar_input != "1" and ingresar_input != "X":
        print("El índice ingresado es inválido. Porfavor, intente nuevamente.")

    elif ingresar_input == "1":

        finalizar_opciones_de_jugador = False
        while not finalizar_opciones_de_jugador:
            funciones_menus.opciones_de_jugador()
            opcion_de_jugador_input = input(
                "Ingrese el índice de la opción que desee realizar (Opcion de Jugador): ")
            diccionario_jugadores = funciones_menus.funcion_diccionario_opciones_de_jugador()[
                0]
            # if int(opcion_de_jugador_input) > 0:
            if not (opcion_de_jugador_input == "X" or opcion_de_jugador_input == "0"):
                nombre_jugador = diccionario_jugadores[int(
                    opcion_de_jugador_input)]

                # Acá se instanciará el objeto que es de la clase Jugador

                lista_jugadores = funciones_menus.funcion_diccionario_opciones_de_jugador()[
                    1]
                for jugadores in lista_jugadores:
                    if jugadores[0] == nombre_jugador:
                        nombre_jugador_todo_lista = jugadores
                if nombre_jugador_todo_lista[1] == "Ludopata":
                    jugador = clase_jugador.Ludopata(nombre_jugador_todo_lista[0],
                                                     nombre_jugador_todo_lista[2], nombre_jugador_todo_lista[3],
                                                     nombre_jugador_todo_lista[4], nombre_jugador_todo_lista[5],
                                                     nombre_jugador_todo_lista[6], nombre_jugador_todo_lista[1],
                                                     nombre_jugador_todo_lista[7], nombre_jugador_todo_lista[8],
                                                     nombre_jugador_todo_lista[9])

                elif nombre_jugador_todo_lista[1] == "Tacano":
                    jugador = clase_jugador.Tacano(nombre_jugador_todo_lista[0],
                                                   nombre_jugador_todo_lista[2], nombre_jugador_todo_lista[3],
                                                   nombre_jugador_todo_lista[4], nombre_jugador_todo_lista[5],
                                                   nombre_jugador_todo_lista[6], nombre_jugador_todo_lista[1],
                                                   nombre_jugador_todo_lista[7], nombre_jugador_todo_lista[8],
                                                   nombre_jugador_todo_lista[9])

                elif nombre_jugador_todo_lista[1] == "Bebedor":
                    jugador = clase_jugador.Bebedor(nombre_jugador_todo_lista[0],
                                                    nombre_jugador_todo_lista[2], nombre_jugador_todo_lista[3],
                                                    nombre_jugador_todo_lista[4], nombre_jugador_todo_lista[5],
                                                    nombre_jugador_todo_lista[6], nombre_jugador_todo_lista[1],
                                                    nombre_jugador_todo_lista[7], nombre_jugador_todo_lista[8],
                                                    nombre_jugador_todo_lista[9])

                elif nombre_jugador_todo_lista[1] == "Casual":
                    jugador = clase_jugador.Casual(nombre_jugador_todo_lista[0],
                                                   nombre_jugador_todo_lista[2], nombre_jugador_todo_lista[3],
                                                   nombre_jugador_todo_lista[4], nombre_jugador_todo_lista[5],
                                                   nombre_jugador_todo_lista[6], nombre_jugador_todo_lista[1],
                                                   nombre_jugador_todo_lista[7], nombre_jugador_todo_lista[8],
                                                   nombre_jugador_todo_lista[9])

            if str(opcion_de_jugador_input) == "0":
                finalizar_opciones_de_jugador = True

            elif opcion_de_jugador_input == "X":
                finalizar_opciones_de_jugador = True
                finalizar_programa = True

            else:
                finalizar_menu_principal = False
                while not finalizar_menu_principal:
                    funciones_menus.menu_principal()
                    opcion_menu_principal = input(
                        "Ingrese el índice de la opción que desee realizar (Menú principal): ")

                    if str(opcion_menu_principal) == "1":

                        finalizar_opciones_de_juegos = False
                        while not finalizar_opciones_de_juegos:
                            funciones_menus.opciones_de_juegos()
                            opcion_opciones_de_juegos = input(
                                "Ingrese el índice del juego que desee jugar (Opciones de juegos): ")

                            lista_de_juegos = funciones2.abrir_archivo(
                                "juegos.csv")

                            if str(opcion_opciones_de_juegos) == "0":
                                finalizar_opciones_de_juegos = True

                            elif opcion_opciones_de_juegos == "X":
                                finalizar_opciones_de_juegos = True
                                finalizar_menu_principal = True
                                finalizar_opciones_de_jugador = True
                                finalizar_programa = True

                            else:
                                # Acá se instanciará el juego que pertenece a la clase Juego
                                juego = clase_juego.Juego(lista_de_juegos[int(opcion_opciones_de_juegos)-1][0],
                                                          lista_de_juegos[int(
                                                              opcion_opciones_de_juegos)-1][1],
                                                          lista_de_juegos[int(
                                                              opcion_opciones_de_juegos)-1][2],
                                                          lista_de_juegos[int(opcion_opciones_de_juegos)-1][3])

                                apuesta = int(
                                    input("Ingrese la cantidad de dinero que desee apostar: "))

                                if int(lista_de_juegos[int(opcion_opciones_de_juegos)-1][2]) > apuesta:
                                    print(
                                        "Usted no posee suficiente dinero para apostar. Intente con otro juego.")
                                elif int(lista_de_juegos[int(opcion_opciones_de_juegos)-1][2]) <= apuesta \
                                    <= int(lista_de_juegos[int(opcion_opciones_de_juegos)-1][3]):
                                    jugador.apostar(apuesta, juego)
                                    finalizar_opciones_de_juegos = True
                                    #nombre_bebestible_aleatorio, tipo_bebestible_aleatorio = clase_casino.Casino().evento_especial()[0], clase_casino

                                elif apuesta > int(lista_de_juegos[int(opcion_opciones_de_juegos)-1][3]):
                                    print(
                                        "Lo sentimos, no puede apostar tanto dinero en un juego. Existe una apuestsa máxima específica.")
                                    print("Porfavor, intente nuevamente. ")

                    elif str(opcion_menu_principal) == "2":
                        finalizar_menu_comprar_bebestibles = False
                        while not finalizar_menu_comprar_bebestibles:
                            funciones_menus.menu_principal_comprar_bebestible()
                            opcion_menu_comprar_bebestible = input(
                                "Ingrese el índice del bebestible que desea consumir (Carta de Bebestibles): ")

                            if str(opcion_menu_comprar_bebestible) == "0":
                                finalizar_menu_comprar_bebestibles = True

                            elif opcion_menu_comprar_bebestible == "X":
                                finalizar_menu_comprar_bebestibles = True
                                finalizar_menu_principal = True
                                finalizar_opciones_de_jugador = True
                                finalizar_programa = True

                            else:  # Acá se instanciará el bebestible
                                lista_bebestibles = funciones2.abrir_archivo(
                                    "bebestibles.csv")
                                print(lista_bebestibles[int(
                                    opcion_menu_comprar_bebestible)-1])
                                if lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][1] == "Jugo":
                                    bebestible = clase_bebestible.Jugo(lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][0],
                                     lista_bebestibles[int(
                                        opcion_menu_comprar_bebestible)-1][1], 
                                        lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][2])

                                elif lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][1] == "Gaseosa":
                                    bebestible = clase_bebestible.Gaseosa(lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][0],
                                     lista_bebestibles[int(
                                        opcion_menu_comprar_bebestible)-1][1],
                                         lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][2])

                                elif lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][1] == "Brebaje mágico":
                                    bebestible = clase_bebestible.BrebajeMagico(lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][0],
                                     lista_bebestibles[int(
                                        opcion_menu_comprar_bebestible)-1][1],
                                         lista_bebestibles[int(opcion_menu_comprar_bebestible)-1][2])

                                jugador.comprar_bebestible(bebestible)
                                bebestible.consumir_bebestible(jugador)

                    elif str(opcion_menu_principal) == "3":
                        for listas in funciones_menus.funcion_diccionario_opciones_de_jugador()[1]:
                            if listas[0] == nombre_jugador:
                                nombre_jugador_lista = listas

                        finalizar_menu_principal_habilidades_del_jugador = False
                        while not finalizar_menu_principal_habilidades_del_jugador:
                            funciones_menus.menu_principal_habilidades_del_jugador(
                                jugador)
                            # Insertar variable de dinero faltante
                            print("[0] Volver")
                            print("[X] Salir\n")
                            opcion_menu_principal_habilidades_del_jugador = input(
                                "Ingrese el índice de la opción que desee realizar (Ver estado del jugador): ")
                            if str(opcion_menu_principal_habilidades_del_jugador) == "0":
                                finalizar_menu_principal_habilidades_del_jugador = True

                            elif opcion_menu_principal_habilidades_del_jugador == "X":
                                finalizar_menu_principal_habilidades_del_jugador = True
                                finalizar_menu_principal = True
                                finalizar_opciones_de_jugador = True
                                finalizar_programa = True

                    elif str(opcion_menu_principal) == "0":
                        finalizar_menu_principal = True

                    elif opcion_menu_principal == "X":
                        finalizar_menu_principal = True
                        finalizar_opciones_de_jugador = True
                        finalizar_programa = True

    elif ingresar_input == "X":
        finalizar_programa = True
