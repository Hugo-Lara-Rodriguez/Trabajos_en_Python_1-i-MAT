# LAS FUNCIONES DE ESTE MÓDULO ESTÁN EXPLICADAS EN EL PRINCIPAL

from constantes import * 
from main import matriz_calles
import clases as c
import time 

def pintar_matriz():
    print(" ",end = "")
    for i in range(len(matriz_calles)):
        print(f"     {i}    ", end="")
    print(" ") 
    for num_calle in range(len(matriz_calles)):
        print(num_calle, end= " ") # SE PUEDE: FOR I, CALLE IN ENUMERATE(MATRIZ_CALLES, START = 1): I = NUM CALLE Y CALLE = CALLE
        for hueco in matriz_calles[num_calle]: # CUIDADO: SI EL EJE DE LAS YS ESTUBIERA AL REVÉS ---> JUGAR CON INVERSAS 
            print(hueco, end= "")
        print()

def añadir_ubicaciones(coordenadas_ubers, coordenadas_clientes):
    matriz_calles[coordenadas_ubers[0]][coordenadas_ubers[1]] = COLOR_VERDE+UBER+COLOR_DEFECTO
    matriz_calles[coordenadas_clientes[0]][coordenadas_clientes[1]] = COLOR_AMARILLO+CLIENTE+COLOR_DEFECTO
    pintar_matriz()

def limpiar_ubicacion(ubicacion):
    matriz_calles[ubicacion[0]][ubicacion[1]] = VACIO

def validar_entrada():



    destino = input("Destino deseado aquí:", ).strip()
    if destino.find(",") != 1: # TODO_ ESTO PENSANDO EN LA FORMA QUE TIENE
        raise c.NoComaError
    else:
        try:
            destino = [int(destino[0]),int(destino[2])] # ESTE PQ ES SOLO DE 5, SI FUERA DE MÁS HABRÍA QUE HACER SLICING HASTA LA COMA
        except ValueError:
            raise c.NoNumeroError
        n = 0
        while n < 2: # UN BUCLE QUE SALTA DE DOS EN DOS PARA SUS DOS COORDENADAS
            if  0 > destino[n] or destino[n] >= len(matriz_calles):
                raise c.FueraDeMatrizError
            n += 2
    return destino
