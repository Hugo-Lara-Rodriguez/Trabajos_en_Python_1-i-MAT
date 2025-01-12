"""
En este módulo se encuentra para separar aquellas funciones TOTALMENTE separadas de la clase, 
de modo que se extraen en otro módulo para no confundirlas.
"""
import os 

def limpiar_consola() -> None: 
    """
    Comando de os para limpiar la pantalla y mejorar el UX
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def letra_a_numero(letra: str) -> int:
    """
    Cambio sencillo pero vital para vincular las filas con letras
    Recibe una letra, devuleve un número
    """
    return ord(letra.upper()) - ord('A')

def numero_a_letra(numero: int) -> str:
    """
    Otro cambio sencillo pero vital para vincular las filas con letras
    Recibe una número, devuleve una letra
    """
    return chr(ord('A') + numero)

def crear_tablero(size: int) -> list:
    """
    Se encarga de la creación inicial del tablero, únicamente con una longitud dada
    Recibe una longitud, devuleve una matriz, o lista de listas
    """
    tablero = []
    for _ in range(size):
        fila = []
        for _ in range(size):
            fila.append(" ")
            
        tablero.append(fila)
    
    return tablero