"""
Este módulo sirve para verificar las tres funciones de la clase más clave, configurar juego para la creación
de la partida, la parte de posicionar los barcos, y la función de disparar (que viene siendo lo mismo que el resto
de habilidades). Además, para añadir tensión, hay dos segundos de espera antes de dar los resultados de las pruebas jeje.
"""
from clases import HundirLaFlota
from funciones import crear_tablero
import time 

# Colores copiados del trbajo de Wordlet jeje
COLOR_VERDE = "\033[1;32m"
COLOR_ROJO = "\033[1;31m"
COLOR_DEFECTO = "\033[0m"
OK = COLOR_VERDE + "OK" + COLOR_DEFECTO
ERROR = COLOR_ROJO + "ERROR" + COLOR_DEFECTO

print("Iniciando pruebas...\n")

juego = HundirLaFlota()
juego.size = 5
juego.tablero1 = crear_tablero(5)
juego.tablero2 = crear_tablero(5)

# Caso 1: el bueno, con un barco en el A,0
tablero_con_barco = crear_tablero(5)
tablero_con_barco[0][0] = "B"

# Caso 2: el malo, todo fallos 
tablero_malo = crear_tablero(5)
for i in range(5):
    for j in range(5):
        tablero_malo[i][j] = "O"

try:
    print("- Método es_posicion_valida(): ", end="")
    caso_bueno = juego.es_posicion_valida(juego.tablero1, 0, 0, 2, True)
    caso_malo = juego.es_posicion_valida(juego.tablero1, -1, 0, 2, True)
    
    time.sleep(2) # Para crear algo de tensión

    if caso_bueno and not caso_malo:
        print(OK)
    else:
        print(ERROR)
except Exception as e:
    print(f"{ERROR} - {e}")

try:
    print("- Método colocar_barco(): ", end="")
    caso_bueno = juego.colocar_barco(juego.tablero1, "A", 0, 2, True)
    caso_malo = juego.colocar_barco(juego.tablero1, "A", 4, 2, True)

    time.sleep(2)
    
    if caso_bueno and not caso_malo:
        print(OK)
    else:
        print(ERROR)
except Exception as e:
    print(f"{ERROR} - {e}")

try:
    print("- Método disparar(): ", end="")
    juego.tablero2[0][0] = "B"
    caso_bueno = juego.disparar(juego.tablero2, "A", 0)
    caso_malo = juego.disparar(tablero_malo, "A", 0)

    time.sleep(2)
    
    if caso_bueno and not caso_malo:
        print(OK)
    else:
        print(ERROR)
except Exception as e:
    print(f"{ERROR} - {e}")

try:
    print("- Método quedan_barcos(): ", end="")
    caso_bueno = juego.quedan_barcos(tablero_con_barco)
    caso_malo = juego.quedan_barcos(tablero_malo)
    
    time.sleep(2)

    if caso_bueno and not caso_malo:
        print(OK)
    else:
        print(ERROR)
except Exception as e:
    print(f"{ERROR} - {e}")

print("\nFin de las pruebas")