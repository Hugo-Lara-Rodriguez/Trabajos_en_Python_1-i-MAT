import matplotlib.pyplot as plt
figuras = {}
menu = 0
# CREACIÓN DEL MENÚ CON SUS OPCIONES
while menu != 9:
    menu = int(input("""MENU    
      ==========
      1. Cargar figuras por defecto
      2. Crear una nueva figura desde cero
      3. Dibujar un polígono 
      4. Dibujar todos los polígonos 
      
      9. Salir""", ))
    # SE CARGAN UNAS FIGURAS PREDEFINIDAS
    if menu == 1:
        figuras["pentágono"] = [(1,1),(3,1),(4,2),(2,3),(0,2),(1,1)]
        figuras["triángulo"] = [(2,2),(2,4),(5,5),(2,2)]
    # SE CREA UNA NUEVA FIGURA: SE PIDE EL NOMBRE Y SE PIDEN PUNTOS EN FORMA DE STRING, QUE SE VAN INTRODUCIENDO EN
    # UNA LISTA EN FORMA DE TUPLAS (x,y) HASTA QUE EL USUARIO PARE, ENTONCES, LA FIGURA ES AGREGADA AL DICCIONARIO DE FIGURAS
    elif menu == 2:
        nombre = input("Introduzca un nombre de figura:", )
        puntos = []
        z = ""
        while z != "Z":
            z = input("Introduzca el primer punto x,y (Z para terminar)", )
            if z != "Z":
                x = int(z[:z.index(","):])
                y = int(z[z.index(",")+1::])
                punto = (x,y)
                puntos.append(punto)
        figuras[nombre] = puntos
    # MEDIANTE LA LIBRERÍA ANTES CARGADA, SE REPRESENTA UNA FIGURA QUE EL USUARIO ELEGIJA: RECORRIENDO LA LISTA DE TUPLAS
    # (QUE CONTIENE LOS PUNTOS) Y AGREGANDO CADA UNA DE SUS COORDENADAS A LAS LISTAS CORRESPONDIENTES
    elif menu == 3:
        lista_x = []
        lista_y = []
        pintar = input("Figura a pintar:", )
        for punto in figuras[pintar]:
            lista_x.append(punto[0])  
            lista_y.append(punto[1]) 
        plt.plot(lista_x,lista_y)
        plt.show()
    # REPRESENTAR TODAS LAS FIGURAS: SE REPITE EL PROCESO PERO PARA TODAS LAS FIGURAS EN EL DICCIONARIO
    elif menu == 4:
        for pintar in figuras:
            lista_x = []
            lista_y = []
            for punto in figuras[pintar]:
                lista_x.append(punto[0])  
                lista_y.append(punto[1]) 
            plt.plot(lista_x,lista_y)
        plt.show()