# LAS CLASES DE ESTE MÓDULO ESTÁN EXPLICADAS EN EL PRINCIPAL

from constantes import *
import funciones as f

class Uber():
    def __init__(self, coordenadas_uber, destino, nombres_clientes, precio):
        self.coordenadas_uber = coordenadas_uber
        self.destino = destino
        self.matriz_calles = matriz_calles
        self.nombre_clientes = nombres_clientes
        self.precio = precio

    def movimiento_uber(self):
        uber_con_cliente = False
        while self.coordenadas_uber != self.destino: 
            f.limpiar_ubicacion(self.coordenadas_uber)
            for i in range(len(self.coordenadas_uber)):
                if self.coordenadas_uber[i] < self.destino[i]:
                    self.coordenadas_uber[i] += 1
                    self.precio += 5
                elif self.coordenadas_uber[i] > self.destino[i]:
                    self.coordenadas_uber[i] -= 1
                    self.precio += 5
    
            if self.coordenadas_uber == self.destino:
                uber_con_cliente = True
            if uber_con_cliente:
                f.matriz_calles[self.coordenadas_uber[0]][self.coordenadas_uber[1]] = COLOR_ROJO+UBER+COLOR_DEFECTO
            else: 
                matriz_calles[self.coordenadas_uber[0]][self.coordenadas_uber[1]] = COLOR_AZUL+UBER+COLOR_DEFECTO
            
            f.pintar_matriz()
            f.time.sleep(1)
        print(f"\nEl Uber {self.coordenadas_uber} con el cliente {self.nombre_clientes} ha llegado a {self.destino} - Coste: {self.precio}€\n")
        f.pintar_matriz()
        f.time.sleep(1)
        return self.coordenadas_uber
    def nuevo_destino(self, nuevo_destino):
        self.destino = nuevo_destino

class NoComaError(Exception):
    pass
class NoNumeroError(Exception):
    pass
class FueraDeMatrizError(Exception):
    pass