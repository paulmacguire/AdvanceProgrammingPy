def actualizar_encomiendas(parametro):
    if parametro[6] == "Emitida":
        parametro[6] = "Revisada por agencia"

    elif parametro[6] == "Revisada por agencia":
        parametro[6] = "En camino"
    
    elif parametro[6] == "En camino":
        parametro[6] == "Llegada al destino"

    elif parametro[6] == "Llegada al destino":
        print("Opción inválida. El producto ya ha llegado a destino.")
    
    return parametro

def contador_caracteres_especiales(parametro_cuenta):
    contador_caracteres_especiales = 0
    caracteres_especiales = "!#$%&/()=¿?¨*[]_;;,.-+|°<>-@¬"
    for caracteres in parametro_cuenta:
        if caracteres in caracteres_especiales:
            contador_caracteres_especiales += 1
    return contador_caracteres_especiales

def contador_caracteres_numericos(parametro_cuenta_2):
    caracteres_numericos = "0123456789"
    contador_caracteres_numericos = 0
    for caracteres in parametro_cuenta_2:
        if caracteres in caracteres_numericos:
            contador_caracteres_numericos += 1
    return contador_caracteres_numericos

def contador_de_caracteres_alfabeticos(parametro_cuenta_3):
    contador_de_caracteres_alfabeticos = 0
    for caracteres in parametro_cuenta_3:
        if caracteres.isalpha():
            contador_de_caracteres_alfabeticos += 1
    return contador_de_caracteres_alfabeticos

