# 1: Iniciar sesión como usuario.
with open("usuarios.csv", encoding="UTF-8") as us:
    lista_cuentas = []
    # Con este for lo que se hará es recorrer las lineas del archivo.csv y agregar cada fila filtrada a una lista_cuentas
    # la cual contendrá todos los usuarios y sus contraseñas.
    for linea in us:
        nombre_usuario = linea.strip("\n").split(",")
        lista_cuentas.append(nombre_usuario)

    # Con este diccionario, se podrá verificar si el usuario ya existe en el sistema. El diccionario tendrá la forma {"usuario": "contraseña"} para todas las cuentas.
    diccionario_de_cuentas = {}
    for cuenta in lista_cuentas:
        diccionario_de_cuentas[cuenta[0]] = cuenta[1]
    