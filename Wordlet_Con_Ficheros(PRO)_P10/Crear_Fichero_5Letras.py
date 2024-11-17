# ESTE MÓDULO SIRVE PARA LIMPIAR EL FICHERO "palabras.txt" QUITANDO LAS PALABRAS MÁS LARGAS QUE 5 Y 
# LAS TÍLDES. CREANDO EL FICHERO DE PALABRAS BUENAS "palabras_wordlet.txt" Y UNA LISTA CON LAS PALABRAS 
# QUE SE USARÁ EN EL PROGRAMA PRINCIPAL PARA VALIDAR LAS PALABRAS.
def convertir_palabras():
    with open("palabras.txt", "r", encoding="utf-8") as lista:
        palabras = lista.readlines()
        for i in range(len(palabras)):
            palabras[i] = palabras[i].rstrip()
    return palabras

def limpiar_palabras():
    palabras_buenas = []
    diccionario_correccion = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    for palabra in palabras:
        longitud_palabras = 6
        if len(palabra) < longitud_palabras: # CUIDADO
            for letra in range(0,len(palabra)):
                if palabra[letra] in diccionario_correccion:
                    palabra = palabra[:letra:] + diccionario_correccion[palabra[letra]] + palabra[letra+1::]
            palabras_buenas.append(palabra)
    return palabras_buenas

def nueva_lista():
    with open("palabras_wordlet.txt", "w") as lista:
        for palabra in lista_palabras_buenas:
            lista.write(palabra)


palabras = convertir_palabras()
lista_palabras_buenas = limpiar_palabras()
if "__name__" == "main":
    nueva_lista()