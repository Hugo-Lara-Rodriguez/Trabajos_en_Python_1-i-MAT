# AVISO: NO PERDER EL TIEMPO EN LEER EL RESTO DE COMENTARIOS, SON ANOTACIONES PROPIAS USADAS PARA ESTUDIAR
# CONTENIDO DE ESTE MÓDULO EXPLICADO EN EL MÓDULO PRINCIPAL (AUNQUE LAS FUNCIONES TENGAN NOMBRES BASTANTE DEFINIDOS)

import excepciones as excep
import matplotlib.pyplot as plt

def validar_opcion(ciudades):
    opcion = input("Introduce una de las opciones:", )
    try:
        opcion = int(opcion)
    except ValueError:
        print("Introduce un número")
        raise excep.OpcionNoValidaError
    if not (1<=opcion<=6):
        print("La opción debe estar entre 1 y 6")
    else:
        return opcion 

def crear_personas(ciudades):
    nombre = input("Nombre:", ) # CONFORME A LAS REGLAS DE LA PRÁCTICA 
    if nombre[0].upper() != nombre[0] or nombre[1::].lower() != nombre[1::]:
        raise excep.NombreError
    else:
        dni = input("DNI:", ) # CONFORME A LAS REGLAS DE LA PRÁCTICA (SUPONEMOS QUE METEN EL FORMATO PEDIDO)
        if not (65 + int(dni[0]) + int(dni[1]) == ord(dni[2])): # RECUERDA: ORD() CONVIERTE A ASCII/UNICODE Y CHR() DEVUELVE EL NUM DE ASCII/UNICODE A CARÁCTER NORMAL
            raise excep.DNIError # ARRIBA: SE PUEDE HACER: SI TE DAN palabra = DNI-1-1234: SE PUEDE HACER: dni, num1, num2 = palabra.split("-")
        else: 
            ciudad = input("Ciudad:",)
            ciudades.setdefault(ciudad, []).append((nombre,dni))

def cargar_personas_por_defecto(ciudades): # ESTE MÉTODO SOLO SIRVE PARA DICC, PARA LISTAS: IF LISTA IS NONE: ... ELSE: ...
    ciudades.setdefault("Madrid", []).extend([("Luis", "11C"),("Ana", "22E"),("María", "33G")])
    ciudades.setdefault("Barcelona", []).extend([("Javier", "22I"), ("Julián", "66M")])
    ciudades.setdefault("Bilbao", []).extend([("Raquel", "77O")])

def mostrar_todas_personas(ciudades):
    for ciudad, personas in ciudades.items(): # PARA ITERAR EN UN DICCIONARIO CON CLAVES Y VALORES SE NECESITA EL .ITEMS(), CLAVES CON .KEYS(), VALORES CON .VALUES()
        print(f"En {ciudad} viven {personas}")

def mostrar_personas_ciudad(ciudades):
    ciudad = input("Nombre de la ciudad:", )
    if ciudad not in ciudades: # ESTO SE PUEDE HACER CON WHILE
        raise excep.CiudadNoEncontrada 
    else:
        print(f"En {ciudad} vive {ciudades[ciudad]}")

def dibujar_histograma(ciudades):
    lista_ciudades = []
    num_personas = []
    for ciudades, personas in ciudades.items(): # PARA ITERAR EN UN DICCIONARIO CON CLAVES Y VALORES SE NECESITA EL .ITEMS(), CLAVES CON .KEYS(), VALORES CON .VALUES()
        lista_ciudades.append(ciudades)
        num_personas.append(len(personas))
    
    plt.bar(lista_ciudades, num_personas)
    plt.title('Número de personas viviendo en ciudades')
    plt.show()