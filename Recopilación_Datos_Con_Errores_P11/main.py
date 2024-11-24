# AVISO: NO PERDER EL TIEMPO EN LEER EL RESTO DE COMENTARIOS, SON ANOTACIONES PROPIAS USADAS PARA ESTUDIAR
# SE PIDE RECOPILAR Y TRABAJAR CON LOS DATOS DE UN GRUPO DE PERSONAS DIVIDIDAS POR CIUDADES, ENFOCADO A LA RECOPILACIÓN
# DE ERRORES (AUNQUE ALGO LIMITADOS):

# SE TRABAJA SOBRE UN MENÚ: SE PIDE LA OPCIÓN Y SE VERIFICA QUE SEA VÁLIDA: LA 1ª OPCIÓN: PERMITE AÑADIR UNA PERSONA
# CON SU NOMBRE Y DNI LOS CUALES SE VALIDAN (SIGUIENDO UNAS REGLAS); LA 2ª: SE AÑADEN UNAS PERSONAS PREDEFINIDAS; 
# LA 3ª: SE MUESTRAN TODAS LAS PERSONAS GUARDADAS; LA 4ª: SE MUESTRAN LAS PERSONAS POR CIUDADES VALIDANDO QUE EXISTA 
# LA CIUDAD INTRODUCIDA; LA 5ª: SE HACE UN DIAGRAMA DE BARRAS O HISTOGRAMA DEL NÚMERO DE PERSONAS EN CADA CIUDAD; 
# Y CON LA 6ª FINALIZA EL PROGRAMA.

import operaciones as op
import excepciones as excep

menu = """
1.- Crear persona
2.- Cargar personas por defecto
3.- Mostrar todas las personas
4.- Mostrar personas de una ciudad
5.- Dibujar histograma por ciudades
6.- Salir
"""
ciudades = {}

if __name__ == "__main__":
    opcion = 0
    while opcion != 6:
        print(menu)
        opcion_valida = False
        while not opcion_valida:
            try: # CUIDADO: ES LA ESTRUCTURA DE LAS EXCEPCIONES
                opcion = op.validar_opcion(ciudades) # EN VEZ DE HACER UN IMPORT EN OPERACIONES DE CIUDADES, SE PUEDE METER ESA VARIBLE COMO PARÁMETRO DE LA FUNCIÓN 
                                             # ES LA MANERA CORRECTA 
                opcion_valida = True
            except excep.OpcionNoValidaError as error:
                print(error)
        
        if opcion == 1:
            try:
                op.crear_personas(ciudades)
            except excep.NombreError as error:
                print("··E001··", error)
            except excep.DNIError as error:
                print("··E002··", error)
        elif opcion == 2:
            op.cargar_personas_por_defecto(ciudades)
        elif opcion == 3:
            op.mostrar_todas_personas(ciudades)
        elif opcion == 4:
            try:
                op.mostrar_personas_ciudad(ciudades)
            except excep.CiudadNoEncontrada as error: # ES UN ERROR "PREPARADO", HARÍA FALTA PONER MÁS EXCEPTS PARA ACOGER A MÁS MÁS NORMALES 
                print(error, "Introduzca otra ciudad") # ARRIBA: NO, CON PONER TRY: Y EXPECT: (SIN ESPECIFICAR EL EXCEPT) CAPTA TODOSSSS LOS ERRORES
        elif opcion == 5:                              # ARRIBA: CHETADO
            op.dibujar_histograma(ciudades)                    # LO MEJOR: DEFINIR LOS ERRORES PROPIOS CON MENSAJE PROPIO, LOS ERRORES COMUNES CON MENSAJE PROPIO, Y EL RESTO CON EXCEPT.
