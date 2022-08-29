from prettytable import PrettyTable


def menu_de_inicio():
    print(f"\n"+"*"*3 + " Menú de Inicio " + "*"*3)
    print(f"-"*22)
    print(f"[1] Iniciar partida")
    print(f"[X] Salir")
    pass


def opciones_de_jugador():
    print(f"\n"+"*"*3 + " Opciones de Jugador " + "*"*3)
    print(f"-"*40)

    lista_de_jugadores = []
    diccionario_de_jugadores = {}
    with open("jugadores.csv", encoding="UTF-8") as archivo_jugadores:
        for lineas in archivo_jugadores:
            jugador = lineas.strip("\n").split(",")
            lista_de_jugadores.append(jugador)
        lista_de_jugadores.pop(0)

    indice = 1
    for lista_jugador in lista_de_jugadores:
        print(f"[{indice}] {lista_jugador[0]}: {lista_jugador[1]}")
        diccionario_de_jugadores[indice] = lista_jugador[0]
        indice += 1
    print("[0] Volver")
    print("[X] Salir")


def funcion_diccionario_opciones_de_jugador():
    lista_de_jugadores = []
    diccionario_de_jugadores = {}
    with open("jugadores.csv", encoding="UTF-8") as archivo_jugadores:
        for lineas in archivo_jugadores:
            jugador = lineas.strip("\n").split(",")
            lista_de_jugadores.append(jugador)
        lista_de_jugadores.pop(0)

    indice = 1
    for lista_jugador in lista_de_jugadores:
        diccionario_de_jugadores[indice] = lista_jugador[0]
        indice += 1
    return diccionario_de_jugadores, lista_de_jugadores


def menu_principal():
    print(f"\n"+"*"*3 + " Menú Principal " + "*"*3)
    print(f"-"*28)
    print("[1] Opciones de juegos")
    print("[2] Comprar bebestible")
    print("[3] Habilidades jugador")
    print("[0] Volver")
    print("[X] Salir")


def menu_principal_comprar_bebestible():
    with open("bebestibles.csv", encoding="UTF-8") as bebestibles:
        tabla = PrettyTable(
            [" N° ", "   Nombre del bebestible   ", "   Tipo   ", "   Precio ($)   "])
        lista_bebestibles = []
        # Con este for lo que se hará es recorrer las lineas del bebestibles.csv
        # y agregar cada fila filtrada a una lista_bebestibles
        # la cual contendrá todas las bebestibles.
        indice = 0
        for linea in bebestibles:
            linea = linea.strip("\n").split(",")
            indice_con_corchetes = [indice]
            linea.insert(0, indice_con_corchetes)
            lista_bebestibles.append(linea)
            indice += 1

        # Con este pop se saca nombre_articulo,receptor,peso,destino,fecha,estado
        lista_bebestibles.pop(0)
        for bebestibles_en_particular in lista_bebestibles:
            tabla.add_row(bebestibles_en_particular)
        print(tabla)
        print("[0] Volver")
        print("[X] Salir")


def menu_principal_habilidades_del_jugador(jugador):
    print(f"\n"+"*"*3 + " Ver estado del jugador " + "*"*3)
    print(f"-"*45)
    print(f"Nombre: {jugador.nombre}")
    print(f"Pesonalidad: {jugador.personalidad}")
    print(f"Energía: {jugador.energia}")
    print(f"Suerte: {jugador.suerte}")
    print(f"Dinero: {jugador.dinero}")
    print(f"Frustración: {jugador.frustracion}")
    print(f"Ego: {jugador.ego}")
    print(f"Carisma: {jugador.carisma}")
    print(f"Confianza: {jugador.confianza}")
    print(f"Juego favorito: {jugador.juego_favorito}")
    juegos_jugados_string = ",".join(jugador.juegos_jugados)
    print(f"Juegos jugados: {juegos_jugados_string}")



def opciones_de_juegos():

    print(f"\n"+"*"*3 + " Opciones de Juegos " + "*"*3)
    print("-"*32)
    tabla = PrettyTable([" N° ", "   Nombre del Juego   ",
                        "   Apuesta Mínima($)   ", "   Apuesta Máxima ($)   "])
    lista_de_juegos = []
    with open("juegos.csv", encoding="UTF-8") as archivo_juegos:
        # for lineas in archivo_juegos:
        #     juego = lineas.strip("\n").split(",")
        #     lista_de_juegos.append(juego)
        # lista_de_juegos.pop(0)
        indice = 0
        for linea in archivo_juegos:
            linea = linea.strip("\n").split(",")
            indice_con_corchetes = [indice]
            linea.insert(0, indice_con_corchetes)
            linea.pop(2)
            lista_de_juegos.append(linea)
            indice += 1

        # Con este pop se saca nombre_articulo,receptor,peso,destino,fecha,estado
        lista_de_juegos.pop(0)
        for juego_en_particular in lista_de_juegos:
            tabla.add_row(juego_en_particular)
        print(tabla)

    # for lista_juego in lista_de_juegos:
    #     print(f"[{indice}] {lista_juego[0]}: {lista_juego[1]}")
    #     indice += 1
    print("[0] Volver")
    print("[X] Salir")
