# AVISO: EL RESTO DE COMENTARIOS EN EL PROGRAMA SON ANOTACIONES MÍAS QUE ME AYUDAN A LA HORA DE ESTUDIAR, NO MOLESTARSE EN LEER.
# FUNCIONALIDAD (CADA FUNCIÓN ES UNO DE LOS SIGUIENTES PASOS): UNA VEZ CREADO EL FICHERO CON LAS PALABRAS BUENAS:
# SE SELECCIONA LA PALABRA CLAVE DEL FICHERO, SE VALIDA LAS PALABRAS INTRODUCIDAS POR EL USUARIO GRACIAS A LA LISTA DE PALABRAS 
# DEL MÓDULO, SE INTRODUCE EL INTENTO DEL USUARIO EN UNA MATRIZ QUE SE IRÁ IMPRIMIENDO, Y UNA VEZ GANE, SE ANOTA 
# EN QUÉ INTENTO HA GANADO EN EL FICHERO "historial_partidas.txt".
import random
import os.path
import sys
from Crear_Fichero_5Letras import lista_palabras_buenas

GRIS = "\033[1;47m"
VERDE = "\033[1;42m"
AMARILLO = "\033[1;43m"
DEFECTO = "\033[0m"
matriz_intentos= []

def seleccionar_palabra():
    with open("palabras_wordlet.txt", "r") as palabras:
        palabras_con_espacios = palabras.readlines()
        palabras_buenas = []
        for palabras in palabras_con_espacios:
            palabras_buenas.append(palabras.rstrip())
        palabra_clave = (random.choice(palabras_buenas)).lower()
        print(f"Palabra de {len(palabra_clave)} letras")
    return palabra_clave

def validar_palabra_prueba():
    palabra_prueba = input("Palabra aquí: ").lower()
    with open("palabras_wordlet.txt", "r"):
        while not palabra_prueba in lista_palabras_buenas or len(palabra_clave) != len(palabra_prueba): #ERROR: .UPPER() (NUNCA SERÁ IGUAL)
            palabra_prueba = input("Palabra aquí: ").lower()
    return palabra_prueba

def intentos():
    intento = ""
    for num_letra in range(0, len(palabra_prueba)):
        if palabra_prueba[num_letra] == palabra_clave[num_letra]:
            intento += VERDE + palabra_prueba[num_letra] + DEFECTO
        elif palabra_prueba[num_letra] in palabra_clave:
            intento += AMARILLO + palabra_prueba[num_letra] + DEFECTO
        else:
            intento += DEFECTO + palabra_prueba[num_letra]
    matriz_intentos.append(intento)

def historial(): # CUIDADO !!!! BUEN EJEMPLO
    with open("historial_partidas.txt", "r") as historial_fichero: # Linea 3 - 12 están las partidas intercaladas
        historial = historial_fichero.readlines()
    historial[historial.index(str(num_victoria)+":"+"\n")] += "#" # ERROR: USAR LA VARIABLE i DOS VECES
    with open("historial_partidas.txt", "w") as historial_fichero:
        historial_fichero.writelines(historial) #MUY BUENO /// LO HICHE QUITANDO TODOS LOS \n PERO ES MÁS DIFÍCIL

# PQ NO ME FUNCIONA CON EL MAIN ?? PQ NO HABÍAS PUESTO BIEN __NAME__, HAS PUESTO "__NAME__", Y ESO NUNCA SERÁ IGUAL
if __name__ == "__main__":
    if os.path.isfile("palabras_wordlet.txt"): # CUIDADO
        palabra_clave = seleccionar_palabra()
    else:
        palabra_clave = "rosal"
        print(f"Palabra de {len(palabra_clave)} letras") 

    argumentos = sys.argv # CUIDADO

    if len(argumentos) > 1 and argumentos[1] == "1":
        print(f"La palabra clave es {palabra_clave}")

    num_intentos = 5
    for i in range(num_intentos):
        palabra_prueba = validar_palabra_prueba()
        intentos()
        if palabra_prueba == palabra_clave:
            print (DEFECTO + " Has ganado !!")
            num_victoria = i+1 # ERROR: EMPIEZA EN EL 0
            break # ??
        else: 
            for intento in matriz_intentos:
                print(intento)        
    if palabra_prueba != palabra_clave: 
        print(DEFECTO + " Se acabaron los intentos, la palabra era:", palabra_clave)
    else:
        historial()