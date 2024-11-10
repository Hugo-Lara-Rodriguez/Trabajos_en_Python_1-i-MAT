# HE HECHO LAS 2 VERSIONES, LA 1ª CON MI CÓDIGO, Y LA 2ª CON LO PEDIDO

# VERSIÓN 1 CON CÓDIGO PROPIO
import random

contador_victorias = 0
contador_derrotas = 0
contador_empates = 0

nombre = input("Nombre:")
partidas = int(input("¿Cuántas partidas quieres jugar? [1, 5]:"))
while not (1 <= partidas <= 5): 
    partidas = int(input("¿Cuántas partidas quieres jugar? [1, 5]:"))

while partidas > 0:
    random_num = random.randint(1,3)
    if random_num == 1: 
        valor2 = "P"
    elif random_num == 2:
        valor2 = "p"
    elif random_num == 3:
        valor2 = "t"
    partidas -= 1
    valor1 = input("¿[P]iedra, [p]apel o [t]ijera?")
    if ((valor1 == "P" and valor2 == "t") or (valor1 == "p" and valor2 == "P") or (valor1 == "t" and valor2 == "p")):
        contador_victorias += 1
        print(nombre + " : " + valor1 +  " MÁQUINA : " + valor2 + " >>> GANAS ")
    elif valor1 == valor2:
        contador_empates += 1
        print(nombre + " : " + valor1 +  " MÁQUINA : " + valor2 + " >>> EMPATAS ")
    else: 
        contador_derrotas += 1
        print(nombre + " : " + valor1 +  " MÁQUINA : " + valor2 + " >>> PIERDES ")

print("Resultado Final ///// " + nombre + " - " + str(contador_victorias) + " // MÁQUINA " + " - " + str(contador_derrotas) 
      +" // Empates - " + str(contador_empates))

clear(all) 

# VERSIÓN 2 DEL JUEGO COMPLETA
import random

resultados = 0

print("""Valores de juego: 
"P" = PIEDRA 
"p" = PAPEL 
"T" = TIJERA """)

ELEMENTOS = ["P", "p", "t"]
LOGICA_JUEGO = "P" + "t" + "t" + "p" + "p" + "P"

nombre = input("Nombre:")
partidas = int(input("¿Cuántas partidas quieres jugar? [1, 5]:"))
while not (1 <= partidas <= 5): 
    partidas = int(input("¿Cuántas partidas quieres jugar? [1, 5]:"))

while partidas > 0:
    partidas -= 1
    victoria = False
    i = 0
    u = 2
    valor1 = input("¿[P]iedra, [p]apel o [t]ijera?")
    valor2 = random.choice(ELEMENTOS)
    partida = (valor1 + valor2)
    while i < 7:
        if partida == LOGICA_JUEGO[i:u]:
            resultados += 64
            victoria = True
            print(nombre + " : " + valor1 +  " MÁQUINA : " + valor2 + " >>> GANAS ")
        i += 2
        u += 2
    if valor1 == valor2:
        resultados += 8
        print(nombre + " : " + valor1 +  " MÁQUINA : " + valor2 + " >>> EMPATAS ")
    elif victoria == False:
        resultados += 1
        print(nombre + " : " + valor1 +  " MÁQUINA : " + valor2 + " >>> PIERDES ")

print("Cadena de vistorias/empates/derrotas: ", (9-len(bin(resultados)[2:]))*str(0) + bin(resultados)[2:])
