import os

# Paths

RUTA_UI_VENTANA_VER_RANKINGS = os.path.join(
    "frontend", "archivos_ui", "ventana_rankings.ui")

RUTA_UI_VENTANA_PRINCIPAL = os.path.join(
    "frontend", "archivos_ui", "ventana_principal.ui")

RUTA_UI_VENTANA_INICIO = os.path.join(
    "frontend", "archivos_ui", "ventana_de_inicio.ui")

RUTA_UI_VENTANA_JUEGO = os.path.join(
    "frontend", "archivos_ui", "ventana_de_juego.ui")

RUTA_UI_VENTANA_POST_JUEGO = os.path.join(
    "frontend", "archivos_ui", "ventana_post_juego.ui")


# Paths fondos de los escenarios

RUTA_ESCENARIO_TUTORIAL_LUNAR = os.path.join(
    "frontend", "assets", "Sprites", "Fondos", "Luna.png")

RUTA_ESCENARIO_ENTRENAMIENTO_JUPITER = os.path.join(
    "frontend", "assets", "Sprites", "Fondos", "Jupiter.png")

RUTA_ESCENARIO_INVASION_INTERGALACTICA = os.path.join(
    "frontend", "assets", "Sprites", "Fondos", "Galaxia.png")


# Paths de elementos de juego

RUTA_MIRA_NEGRA = os.path.join(
    "frontend", "assets", "Sprites", "Elementos juego", "Disparador_negro.png")

RUTA_MIRA_ROJA = os.path.join(
    "frontend", "assets", "Sprites", "Elementos juego", "Disparador_rojo.png")


# Tamaño de la ventana de juego

LADO_IZQUIERDO_VENTANA = -35
LADO_DERECHO_VENTANA = 705
LADO_ABAJO_VENTANA = 290
LADO_ARRIBA_VENTANA = 0


# Velocidad de la mira en el juego

VELOCIDAD_DE_LA_MIRA = 5

# Posición de la mira

ALTURA_DE_LA_MIRA = 131
ANCHO_DE_LA_MIRA = 191
POSICION_DE_LA_MIRA = (330, 160, ANCHO_DE_LA_MIRA, ALTURA_DE_LA_MIRA)

# Posición de los aliens

ALTURA_ALIEN_1 = 40
ANCHO_ALIEN_1 = 50
POSICION_ALIEN_1 = (300, 160, ANCHO_ALIEN_1, ALTURA_ALIEN_1)

ALTURA_ALIEN_2 = 40
ANCHO_ALIEN_2 = 50
POSICION_ALIEN_2 = (360, 160, ANCHO_ALIEN_2, ALTURA_ALIEN_2)


# Paths de las fotos de los aliens

RUTA_ALIEN_LUNAR_VIVO = os.path.join(
    "frontend", "assets", "Sprites", "Aliens", "Alien1.png")

RUTA_ALIEN_LUNAR_MUERTO = os.path.join(
    "frontend", "assets", "Sprites", "Aliens", "Alien1_dead.png")

RUTA_ALIEN_JUPITER_VIVO = os.path.join(
    "frontend", "assets", "Sprites", "Aliens", "Alien2.png")

RUTA_ALIEN_JUPITER_MUERTO = os.path.join(
    "frontend", "assets", "Sprites", "Aliens", "Alien2_dead.png")

RUTA_ALIEN_INTERGALACTICO_VIVO = os.path.join(
    "frontend", "assets", "Sprites", "Aliens", "Alien3.png")

RUTA_ALIEN_INTERGALACTICO_MUERTO = os.path.join(
    "frontend", "assets", "Sprites", "Aliens", "Alien3_dead.png")

# Paths explosiones aliens

RUTA_EXPLOSION_1 = os.path.join(
    "frontend", "assets", "Sprites", "Elementos juego", "Disparo_f1.png")

RUTA_EXPLOSION_2 = os.path.join(
    "frontend", "assets", "Sprites", "Elementos juego", "Disparo_f2.png")

RUTA_EXPLOSION_3 = os.path.join(
    "frontend", "assets", "Sprites", "Elementos juego", "Disparo_f3.png")

# Path sonido disparo bala

RUTA_DISPARO = os.path.join("frontend", "Sonidos", "disparo.wav")

# Path sonido risa perro

RUTA_RISA_PERRO = os.path.join("frontend", "Sonidos", "risa_robotica.wav")

# Ponderadores de los escenarios

PONDERADOR_TUTORIAL = 1

PONDERADOR_ENTRENAMIENTO = 0.85

PONDERADOR_INVASION = 0.71

# Velocidad aliens

VELOCIDAD_ALIENS = 5

# Ruta perro post nivel

RUTA_PERRO = os.path.join(
    "frontend", "assets", "Sprites", "Terminator-Dog", "Dog1.png")

RUTA_ALIEN_PERRO_1 = os.path.join(
    "frontend", "assets", "Sprites", "Terminator-Dog", "Perro_y_alien1.png")

RUTA_ALIEN_PERRO_2 = os.path.join(
    "frontend", "assets", "Sprites", "Terminator-Dog", "Perro_y_alien2.png")

RUTA_ALIEN_PERRO_3 = os.path.join(
    "frontend", "assets", "Sprites", "Terminator-Dog", "Perro_y_alien3.png")

# Ruta BONUS

RUTA_BOMBA_DE_HIELO = os.path.join(
    "frontend", "assets", "Sprites", "Bonus", "Bomba_hielo.png")

# Duracion de nivel escenarios

DURACION_ESCENARIO_LUNAR = 60

DURACION_ESCENARIO_JUPITER = 50

DURACION_ESCENARIO_INTERGALACTICO = 40

