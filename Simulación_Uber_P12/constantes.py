VACIO =  "_........_"     # Símbolo en la matriz para representar una celda vacía
UBER =  "_..oT=o.._"      # Símbolo en la matriz para representar un UBER
CLIENTE =  "_. =:-) ._"   # Símbolo en la matriz para representar un CLIENTE/PASAJERO

COLOR_VERDE = "\033[1;32m"
COLOR_ROJO = "\033[1;31m"
COLOR_AMARILLO = "\033[1;33m"
COLOR_AZUL = "\033[1;34m"
COLOR_DEFECTO = "\033[0m"

coordenadas_ubers = [[0, 2], [4, 4]]
coordenadas_clientes = [[3, 0], [4, 2]]
nombres_clientes = ["Luis", "Ana"]
destinos = [0,0]
precio = [0,0]

leyenda = f"""\n\n### Leyenda:\n
{COLOR_AMARILLO+CLIENTE+COLOR_DEFECTO}: Cliente de Uber
{COLOR_VERDE+UBER+COLOR_DEFECTO}: Uber libre, no tiene servicio
{COLOR_AZUL+UBER+COLOR_DEFECTO}: Uber buscando cliente
{COLOR_ROJO+UBER+COLOR_DEFECTO}: Uber llevando cliente"""

calle1, calle2, calle3, calle4, calle5 = [VACIO]*5, [VACIO]*5, [VACIO]*5, [VACIO]*5, [VACIO]*5 
matriz_calles = [calle1, calle2, calle3, calle4, calle5]
