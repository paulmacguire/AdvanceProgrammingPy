
def abrir_archivo(archivo):
    
    lista_de_elementos = []
    with open(archivo, encoding="UTF-8") as archivo_abierto:
        for lineas in archivo_abierto:
            juego = lineas.strip("\n").split(",")
            lista_de_elementos.append(juego)
        lista_de_elementos.pop(0)

    return lista_de_elementos