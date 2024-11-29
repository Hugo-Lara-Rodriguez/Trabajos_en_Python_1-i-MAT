# AVISO: NO LEER EL RESTO DE COMENTARIOS, SON ANOTACIONES MÍAS PARA ESTUDIAR

# FUNCIONALIDAD: SE TRATA DE UNA CIUDAD (MATRIZ 5X5) EN LA QUE SE INTRODUCEN 2 UBERS CON 2 CLIENTES, 
# HACIENDO EL TRANSPORTE A LOS PUNTOS QUE SE ELIJAN Y COBRANDO UN PRECIO ACORDE A LA DISTANCIA RECORRIDA

# EXPLICACIÓN: MEDIANTE DOS FUNCIONES SE IMPRIME LA CIUDAD Y SE AÑADEN LAS UBICACIONES DE LOS 4 ELEMENTOS,
# SE PIDEN LOS DESTINOS Y SE VALIDAN, CONTEMPLANDO LOS POSIBLES ERRORES EN LA INTRODUCCIÓN DE DATOS. UNA VEZ 
# CON LOS DATOS: SE CREAN LOS UBERS COMO OBJETOS, QUE, CON UN MÉTODO DEL MISMO, SE DESPLAZA HACIA AL CLIENTE (DESTINO 
# DEL UBER) (MIENTRAS QUE CON OTRO SE VA LIMPIANDO LAS POSICIONES ANTERIORES DE LOS UBERS). DESPUÉS, CON EL ÚLTIMO
# MÉTODO DEL OBJETO, SE CAMBIA EL DESTINO A LA UBICACIÓN FINAL Y SE REPITE EL FUNCIONAMIENTO. Y, MIENTRAS SE EJECUTA 
# EL MOVIMIENTO, A SU VEZ SE VA CALCULANDO EL PRECIO DEL TRANSPORTE, QUE SE DÁ AL FINAL (5€ POR CASILLA).


from constantes import *
import funciones as f
import clases as c

if __name__ == "__main__":
    print(leyenda)

    print("\n## Creando ciudad...\n")
    f.time.sleep(1)
    f.pintar_matriz()

    for n in range(len(coordenadas_ubers)):
        print(f"\n## Añadiendo ubicación #{n+1}...\n")
        f.time.sleep(1)
        f.añadir_ubicaciones(coordenadas_ubers[n], coordenadas_clientes[n])

    validacion = False
    while validacion == False:
        try:
            for n in range(len(coordenadas_ubers)):
                f.time.sleep(1)
                print(f"\nCliente #{n+1}:\n")
                destinos[n] = f.validar_entrada()
            validacion = True
        except c.NoComaError as error:
            print(error, "\nLos valores introducidos no cuentan con una coma")
        except c.NoNumeroError as error:
            print(error, "\nLos valores introducidos no son numéricos")
        except c.FueraDeMatrizError as error:
            print(error, "\nLos valores introducidos están fuera del rango de la ciudad")

    f.pintar_matriz() 
    f.time.sleep(1)

    # ESTO ES PARA DOS UBERS (ES LA ÚNICA PARTE DE "HARDCODING", PERO ES INEVITABLE)
    uber1 = c.Uber(coordenadas_ubers[0], coordenadas_clientes[0], nombres_clientes[0], precio[0]) #SE PUEDE HACER PRIMERO LA CLASE Y LUEGO LLAMAR A SU MÉTODO
    uber2 = c.Uber(coordenadas_ubers[1], coordenadas_clientes[1], nombres_clientes[1], precio[1]) 
    ubers = [uber1, uber2]

    for n in range(len(ubers)): # CUIDADO!!!!: AUNQUE PONGA QUE NO LO RECONOCE, SI SE PUEDE.
        ubers[n].movimiento_uber()
        ubers[n].nuevo_destino(destinos[n]) 
    for n in range(len(ubers)):
        ubers[n].movimiento_uber()

    print("\n## Fin de la simulación\n")

# SE PODRÍA CALCULAR QUE UBER ESTÁ MÁS CERCA DE CADA CLIENTE
"""def asignar_ubers(): #  HARCODE 
    d1 = [0]*len(coordenadas_ubers) # UBER1 - P1, UBER1 - P2
    d2 = [0]*len(coordenadas_ubers)
    for i in range(len(coordenadas_ubers[1])):
        d1[i] = abs(coordenadas_ubers[0][0] - coordenadas_clientes[i][0]) + abs(coordenadas_ubers[0][1] - coordenadas_clientes[i][1])
        d2[i] = abs(coordenadas_ubers[1][0] - coordenadas_clientes[i][0]) + abs(coordenadas_ubers[1][1] - coordenadas_clientes[i][1])
    # TODAVÍA ME FALTAN RECURSOS, CONTINUARÁ...."""
# IMPORTANTE: SIEMPRE QUE VEAS NÚMEROS SIN CONTEXTO O BASADOS SOLO EN LOS DATOS ACTUALES, ESTÁN MAL, ES HARDCODING(TIENEN QUE SER ESCALABLES)
# SELF.ATRIBUTO = PARÁMETRO

# A PARTIR DE AHORA SI NECESITAS USAR UNA VARIABLE DEL MAIN MUCHO EN FUNCIONES, IMPORTALA POR FAVOR; SI SON POCAS: FUNCION.(VARIABLE)
# PRÓXIMA VEZ(YA MUY DIFÍCIL DE CAMBIAR): LA FUNCIÓN DEL UBER EN VEZ DE HACER BUCLE DENTRO DE LA FUNCIÓN (UN POCO DE "HARCODE"), 
# LLAMARLA DOS VECES (QUE ES EL USO REAL DE LAS FUNCIONES)
