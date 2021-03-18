#Crear una lista diccionario con el contenido de esta tabla:
# Videojuegos de:
# ACCION   AVENTURA     DEPORTES
# GTA      TUMB         FIFA
# COD      CRASH        PRO21
# PUGB     POP          MOTO GP21


tabla = dict()

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "AVENTURAS",
        "juegos": ["TUMB", "CRASH", "POP"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PES 21", "MOTO GP21"]
    }
]

for elemento in tabla:
    print(f"---------{elemento['categoria']}-----------")
    for juego in elemento['juegos']:
        print(juego)


print("----------------------------------------------------------")
print("Devuelve el numero de elementos que tiene el diccionario")
print(len(tabla))

