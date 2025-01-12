"""
La parte pp del programa se basa en una única clase, ya que así es más fácil compartir información entre funciones 
en forma de atributos; siendo estos los tableros (lista de listas), el tamaño, los barcos (una lista con la longitud de casa barcos), 
el turno actual, el estado de la partida, los simbolos para cada elemento y un diccionario con las habilidades y sus usos.

Básicamente la lógica del juego es la siguiente:
El programa comienza con iniciar_juego() el cual controla el flujo pp, que funciona como menú, permitiendo elegir todas las opciones. Se
puede elegir crear una nueva partida, entonces, se utiliza el método configurar_juego(); si se acpetan los valores pedidos 
(básicamente el tamaño del tablero y número/longitud de barcos) se entra en colocar_barcos_jugadores() donde cada jugador tiene la opción
de colocar sus barcos manual o aleatoriamente, buena funcionalidad para vagos jeje. Luego, si todo va bien, se entra en jugar_partida() que 
se encarga de gestionar los turnos alternando entre jugadores, donde se realizan las acciones como disparar o usar habilidades 
especiales (bomba, torpedo, radar, ...) mediante sus métodos. Todo ello se va imprimiendo y borrando de la pantalla, de manera limpia
con el método de imprimir_tableros(), mostrando la situación de los tableros ocultando los barcos del oponente. Para el modo contra IA, 
he creado una lógica específica, más aislada y compleja: se empieza con jugar_contra_ia() que implementa la colocación automática de barcos 
con colocar_barcos_ia() y disparo mediante disparo_ia(). Todo ello, la IA y no IA,es validado mediante los métodos es_posicion_valida() y 
pedir_coordenadas(), asegurando que los movimientos sean legales. La partida continúa hasta que quedan_barcos() ejecutado en cada ronda 
diga lo contrario, terminando la partida.Luego, está también la funcionalidad para guardar_partida() y cargar_partida(), permitiendo continuar partidas previas.
"""
import random 
import time
from constantes import *
from funciones import limpiar_consola, letra_a_numero, numero_a_letra, crear_tablero

class HundirLaFlota:
    def __init__(self):
        self.tablero1 = None
        self.tablero2 = None
        self.tamaño = None
        self.barcos = None
        self.turno = 1
        self.partida_en_curso = False
        self.habilidades = HABILIDADES_INICIALES.copy()
        self.simbolos = SIMBOLOS

    def imprimir_tableros(self, ocultar_barcos: bool = False) -> None:
        """
        Se encarga de imprimir los tableros uno al lado del otro de manera horizontal
        Recibe un booleano para saber si tiene que mostrar o no los barcos, e imprime lo que se le pide
        """

        # Valores en los que se ve bien a culauier escala jeje
        ancho_tablero = self.tamaño * 4 + 4  
        ancho_total = ancho_tablero * 2 + 8  
        espacio_central = 8  
        
        print(f"\n{'-' * ancho_total}")
        print(f"{'JUGADOR 1':^{ancho_tablero}}{' ' * (espacio_central - 9)}{'JUGADOR 2':^{ancho_tablero}}")
        print('-' * ancho_total)

        print("     ", end="")  
        for i in range(self.tamaño):
            print(f"{i:2}", end=" ")
        print(" " * espacio_central, end="  ")
        for i in range(self.tamaño):
            print(f"{i:2}", end=" ")
        print()
        
        for i in range(self.tamaño):
            letra = numero_a_letra(i)
            tableros = [self.tablero1, self.tablero2]
            for tablero in tableros:
                print(f"  {letra} {BARRA_VERTICAL}", end=" ")
                for j in range(self.tamaño):
                    simbolo = tablero[i][j]
                    if ocultar_barcos and simbolo == 'B':
                        print(f"{SIMBOLOS[' ']}", end=" ")
                    else:
                        print(f"{SIMBOLOS[simbolo]}", end=" ")
                print(BARRA_VERTICAL, end="   ")
            print()
        
        print('-' * ancho_total)
 


    def es_posicion_valida(self, tablero, fila, columna, longitud=1, horizontal=True):
        """
        Valida si una posición está dentro del tablero y disponible
        Tiene dos partes: para disparos/habilidades usa longitud 1, y 
        para barcos con más longitud se tiene que dar, además de su orientación; devuelve un booleano
        """

        if fila < 0 or fila >= self.tamaño or columna < 0 or columna >= self.tamaño:
            return False

        if longitud == 1:
            return True
        
        if horizontal:
            if columna + longitud > self.tamaño:
                return False
            for i in range(longitud):
                if tablero[fila][columna + i] != " ":
                    return False
        else:
            if fila + longitud > self.tamaño:
                return False
            for i in range(longitud):
                if tablero[fila + i][columna] != " ":
                    return False

        return True


    def pedir_coordenadas(self, accion=""):
        """
        Pide coordenadas al usuario hasta que sean válidas
        Se le entrega un texto con la acción del usuario (realmente no hace falta) y devuelve una tupla con (letra de fila, número de columna)
        """    
        while True:
            try:
                letra = input(f"Fila (A-{numero_a_letra(self.tamaño-1)}): ").upper()
                columna = int(input(f"Columna (0-{self.tamaño-1}): "))
                fila = letra_a_numero(letra)

                if self.es_posicion_valida(None, fila, columna, 1, True):
                    return letra, columna
                else:
                    print(f"❌ Coordenadas fuera del tablero. {accion}. El tablero es de tamaño {self.tamaño}x{self.tamaño}")
            except ValueError:
                print(f"❌ Coordenadas inválidas. {accion}. Intenta de nuevo.")

    def colocar_barco(self, tablero, letra, columna, longitud, horizontal):
        """
        Coloca un barco en el tablero 
        Se le da toda la información para posicionari un barco, verifica que se cumple, lo coloca, y devulve la señal
        de que todo ha funcionado, un booleano
        """
        fila = letra_a_numero(letra)
        if not self.es_posicion_valida(tablero, fila, columna, longitud, horizontal):
            return False
        
        if horizontal:
            for i in range(longitud):
                tablero[fila][columna + i] = "B"
        else:
            for i in range(longitud):
                tablero[fila + i][columna] = "B"
        return True

    def quedan_barcos(self, tablero):
        """
        Controla la victoria, verifica en cada ronda si siguen habiendo barcos
        Se le entrega el tablero, lo itera, y devuelve una respuesta, un booleano
        """
        for fila in tablero:
            if "B" in fila:
                return True
        return False

    def disparar(self, tablero, letra, columna):
        """
        Dispara a una posición del tablero dada
        Se le entrega la posición a disparar, verifica que se pueda realizar, lo realiza y 
        devuelve si ha sido dado o no, un booleano
        """
        fila = letra_a_numero(letra)
        if not self.es_posicion_valida(tablero, fila, columna, 1, True):
            return False
        if tablero[fila][columna] == "B":
            tablero[fila][columna] = "X"
            return True
        elif tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
        return False

    def usar_bomba(self, tablero, letra, columna):
        """
        Lanza la habilidad a una posición del tablero dada
        Se le entrega la posición a disparar, verifica que se pueda realizar y lo realiza,
        devulve un booleano diciendo si ha
        """
        fila = letra_a_numero(letra)
        if not self.es_posicion_valida(tablero, fila, columna, 1, True):
            return False

        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_fila = fila + i
                nueva_columna = columna + j
                if self.es_posicion_valida(tablero, nueva_fila, nueva_columna, 1, True):
                    if tablero[nueva_fila][nueva_columna] == "B":
                        tablero[nueva_fila][nueva_columna] = "X"
                    elif tablero[nueva_fila][nueva_columna] == " ":
                        tablero[nueva_fila][nueva_columna] = "O"
        return True
    
    def usar_torpedo(self, tablero, tipo, indice):
        """
        x2:
        Lanza la habilidad a una posición del tablero dada
        Se le entrega la posición a disparar, verifica que se pueda realizar y lo realiza,
        devulve un booleano diciendo si ha funcionado
        """
        if tipo == "fila":
            for j in range(self.tamaño):
                if tablero[indice][j] == "B":
                    tablero[indice][j] = "X"
                elif tablero[indice][j] == " ":
                    tablero[indice][j] = "O"
        elif tipo == "columna":
            for i in range(self.tamaño):
                if tablero[i][indice] == "B":
                    tablero[i][indice] = "X"
                elif tablero[i][indice] == " ":
                    tablero[i][indice] = "O"

    def usar_radar(self, tablero, letra, columna):
        """
        x3
        Lanza la habilidad a una posición del tablero dada
        Se le entrega la posición a disparar, verifica que se pueda realizar y lo realiza,
        devulve un booleano diciendo si ha funcionado
        Pero, aquí se determina también si se ha detectado un barco o no, en vez de destruirlo.
        """
        fila = letra_a_numero(letra)
        if not self.es_posicion_valida(tablero, fila, columna, 1, True):
            return False

        barcos_encontrados = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_fila = fila + i
                nueva_columna = columna + j

                if self.es_posicion_valida(tablero, nueva_fila, nueva_columna, 1, True):
                    if tablero[nueva_fila][nueva_columna] == "B":
                        print(f"¡Detectado barco en {numero_a_letra(nueva_fila)}{nueva_columna}!")
                        barcos_encontrados = True
                    elif tablero[nueva_fila][nueva_columna] == " ":
                        tablero[nueva_fila][nueva_columna] = "O"

        if barcos_encontrados:
            print("💡 ¡Radar ha detectado barcos en el área!")
        else:
            print("🌊 No se detectaron barcos en el área")

        return True

    def configurar_juego(self) -> bool:
        """
        Configura el juego pidiendo tamaño y barcos.
        Devulve un booleano diciendo que todo ha ido bien, se pide el tamaño, los barcos y la longitud de cada uno
        Si falla, se piden de nuevo
        """
        limpiar_consola()
        print(MENU_CONFIGURACION)
        
        try:

            tamano_valido = False
            while not tamano_valido:
                self.tamaño = int(input(f"Introduce el tamaño del tablero ({TAMANO_MIN}-{TAMANO_MAX}): "))
                if TAMANO_MIN <= self.tamaño <= TAMANO_MAX:
                    tamano_valido = True
                else:
                    print(f"El tamaño debe estar entre {TAMANO_MIN} y {TAMANO_MAX}")

            max_barcos = (self.tamaño * self.tamaño) // 4
            num_barcos_valido = False
            while not num_barcos_valido:
                num_barcos = int(input("Introduce el número de barcos por jugador: "))
                if 1 <= num_barcos <= max_barcos:
                    num_barcos_valido = True
                else:
                    print(f"El número de barcos debe estar entre 1 y {max_barcos}")

            self.barcos = []
            for i in range(num_barcos):
                longitud_valida = False
                while not longitud_valida:
                    longitud = int(input(f"Introduce la longitud del barco {i+1}: "))
                    if 1 <= longitud <= self.tamaño:
                        self.barcos.append(longitud)
                        longitud_valida = True
                    else:
                        print(f"La longitud debe estar entre 1 y {self.tamaño}")

            
            self.tablero1 = crear_tablero(self.tamaño)
            self.tablero2 = crear_tablero(self.tamaño)
            return True
            
        except ValueError:
            print("Por favor, introduce números válidos")
            return False 

    def colocar_barcos_jugadores(self) -> None: 
        """
        Permite a los jugadores colocar sus barcos de forma manual o aleatoria en los tableros
        No recibe ningún parámetro, solo modifica las posiciones de juego dependiendo de que se elija. Cuenta con funciones internas 
        para el modo automático
        Además, he ehcho uso de estructuras un poco más complejas vinculadas con otras más simples cuando lo he visto conveniente
        """
        def colocar_aleatorio(tablero: list, longitud: int) -> None:

            posicion_valida = False
            while not posicion_valida:
                horizontal = random.choice([True, False])
                
                if horizontal:
                    max_fila = self.tamaño - 1
                    max_columna = self.tamaño - longitud
                else:
                    max_fila = self.tamaño - longitud
                    max_columna = self.tamaño - 1
                    
                fila = random.randint(0, max_fila)
                columna = random.randint(0, max_columna)
                
                if self.es_posicion_valida(tablero, fila, columna, longitud, horizontal):
                    for i in range(longitud):
                        if horizontal:
                            tablero[fila][columna + i] = "B"
                        else:
                            tablero[fila + i][columna] = "B"
                    posicion_valida = True
        
        for jugador in range(2):
            if jugador == 0:
                tablero = self.tablero1
            else:
                tablero = self.tablero2

            print(f"\nJugador {jugador + 1}, coloca tus {len(self.barcos)} barcos")

            def mostrar_tablero():
                if jugador == 0:
                    temp_tablero = self.tablero2
                    self.tablero2 = [[" "] * self.tamaño for _ in range(self.tamaño)]
                    self.imprimir_tableros()
                    self.tablero2 = temp_tablero
                else:
                    temp_tablero = self.tablero1
                    self.tablero1 = [[" "] * self.tamaño for _ in range(self.tamaño)]
                    self.imprimir_tableros()
                    self.tablero1 = temp_tablero
                        
            if input("¿Deseas colocar los barcos manualmente o aleatoriamente? (M/A): ").upper() == 'A':
                for i, longitud in enumerate(self.barcos):
                    colocar_aleatorio(tablero, longitud)
                    print(f"\nColocado barco {i+1} de longitud {longitud}")
                    mostrar_tablero()
                    input("Presiona Enter para continuar...")
            else:
                for longitud in self.barcos:
                    mostrar_tablero()
                    while True:
                        try:
                            fila = input(f"\nFila (A-{numero_a_letra(self.tamaño-1)}): ").upper()
                            col = int(input(f"Columna (0-{self.tamaño-1}): "))
                            horizontal = input("¿Horizontal? (s/n): ").lower() == 's'
                            
                            if self.colocar_barco(tablero, fila, col, longitud, horizontal):
                                break
                            print("Posición inválida. Reintenta.")
                        except ValueError:
                            print("Entrada inválida. Reintenta.")
            
            limpiar_consola()

    def guardar_partida(self, filename: str = "") -> None: 
        """
        Guarda el estado actual de la partida en cualquier momento en un archivo con el nombre que quieras
        Se le da un nombre del archivo y lo guarda
        Si falla por algún motivo, no da error, se devuelve al menú principal
        """
        if not filename:
            filename = input("Elija el nombre de la partida que quiere guardar (solo el nombre): ") + ".txt"
            
        try: # Aquí, aplica he creado una buena UX con el uso de iteraciones y el .join() para la lista, así no resulta complicado
            with open(filename, "w") as f:
                f.write("====== ESTADO DE LA PARTIDA ======\n")
                f.write(f"Tamaño del tablero: {self.tamaño}\n")
                f.write(f"Turno actual: {self.turno}\n")
                f.write(f"Barcos (longitudes): {','.join(map(str, self.barcos))}\n\n") 

                f.write("====== HABILIDADES DISPONIBLES ======\n")
                for hab, cant in self.habilidades.items():
                    f.write(f"{hab.capitalize()} - {cant}\n")
                f.write("\n")
                
                for num in range(1, 3):
                    if num == 1:
                        tablero = self.tablero1
                    else:
                        tablero = self.tablero2

                    f.write(f"====== TABLERO JUGADOR {num} ======\n")

                    for fila in tablero:
                        linea = ''
                        for cell in fila:
                            if cell == ' ':
                                linea += '.'
                            else:
                                linea += cell
                        f.write(linea + "\n")

                    if num == 1:
                        f.write("\n")

                        
        except Exception as e:
            print(f"❌ Error al guardar partida: {e}")

    def cargar_partida(self, filename: str = "") -> bool:
        """
        Carga una partida desde un archivo con el nombre que le des
        Se entrega el nombre del archivo, y se devulve un booleano diciendo si se cargó bien,
        empezando la partida
        Si falla por algún motivo, no da error, se devuelve al menú principal
        """
        if not filename:
            filename = input("Elija el nombre de la partida que quiere cargar (solo el nombre): ") + ".txt"
            
        try:
            with open(filename, "r") as f:
                lineas = f.readlines()
                
            self.tamaño = int(lineas[1].split(": ")[1])
            self.turno = int(lineas[2].split(": ")[1])
            self.barcos = list(map(int, lineas[3].split(": ")[1].split(",")))
            
            idx_hab = lineas.index("====== HABILIDADES DISPONIBLES ======\n") + 1
            for linea in lineas[idx_hab:idx_hab + 3]:
                hab, cant = linea.strip().split(" - ")
                self.habilidades[hab.lower()] = int(cant)
            
            for tablero_num, idx in enumerate([
                lineas.index("====== TABLERO JUGADOR 1 ======\n"),
                lineas.index("====== TABLERO JUGADOR 2 ======\n")
            ], 1):
                tablero = []
                for linea in lineas[idx + 1:idx + 1 + self.tamaño]:
                    fila = []
                    for cell in linea.strip():
                        if cell == '.':
                            fila.append(' ')
                        else:
                            fila.append(cell)
                    tablero.append(fila)
                if tablero_num == 1:
                    self.tablero1 = tablero
                else:
                    self.tablero2 = tablero
                    
            return True
            
        except Exception as e:
            print(f"❌ Error al cargar partida: {e}")
            return False

    def mostrar_menu(self) -> str:
        """
        Muestra el menú principal del juego
        Devuelve el input con la elección del menú
        """
        limpiar_consola()
        print(MENU_PRINCIPAL)
        return input("Selecciona una opción (1-6): ")

    def turno_jugador(self, jugador):
        """
        Controla el curso del juego en cuanto a las acciones durante la partida
        Se le da una opción, y este entra dentro del método pedido; además controla los errores 
        y el final de la partida. Si todo va bien devulve un booleano para continuar la partida
        """
        while True: 
            print(f"\nTurno del Jugador {jugador}")
            print("Habilidades 💣/🚀/📡 -- ¡Se las queda el más rápido!")
            for habilidad, numero in self.habilidades.items():
                print(f" {habilidad} - Disponible: {numero}")
            print("Menú 📋 - m /// Guardar 💾 - g")
            
            if jugador == 1:
                tablero = self.tablero2
            else:
                tablero = self.tablero1
            accion = input("¿Qué quieres hacer? (disparar/bomba/torpedo/radar): ").lower()

            if accion == "m":
                return False
            
            if accion == "g":
                self.guardar_partida()
                print("Partida guardada correctamente")
                continue

            try: # AQUÍ ES MÁS SENCILLO USANDO BREAKS, Y EN LAS OTRAS ALGUNOS CASOS
                if accion == "disparar":
                    while True:
                        letra, col = self.pedir_coordenadas()
                        if self.disparar(tablero, letra, col):
                            print("💥 ¡IMPACTO!")
                        else:
                            print("💧 ¡Agua!")
                        break

                elif accion == "bomba" and self.habilidades["bomba"] > 0:
                    while True:
                        letra, col = self.pedir_coordenadas("bomba")
                        if self.usar_bomba(tablero, letra, col):
                            self.habilidades["bomba"] -= 1
                            print("💣 ¡Bomba utilizada!")
                            break
                        
                elif accion == "torpedo" and self.habilidades["torpedo"] > 0:
                    tipo = input("¿Fila o columna? (fila/columna): ").lower()
                    if tipo not in ["fila", "columna"]:
                        print("❌ Tipo inválido. Debe ser 'fila' o 'columna'.")
                        continue
                    while True:
                        try:
                            indice = int(input(f"Índice (0-{self.tamaño-1}): "))
                            if self.es_posicion_valida(tablero, indice, 0, 1, True): 
                                self.usar_torpedo(tablero, tipo, indice)
                                self.habilidades["torpedo"] -= 1
                                print("🚀 ¡Torpedo utilizado!")
                                break
                            else:
                                print(f"❌ Índice fuera del tablero. Debe estar entre 0 y {self.tamaño-1}")
                        except ValueError:
                            print("❌ Índice inválido. Debe ser un número.")
                            
                elif accion == "radar" and self.habilidades["radar"] > 0:
                    while True:
                        letra, col = self.pedir_coordenadas("radar")
                        if self.usar_radar(tablero, letra, col):
                            self.habilidades["radar"] -= 1
                            print("📡 ¡Radar utilizado!")
                            break

                else:
                    print("❌ Acción no válida o habilidad agotada. Intenta de nuevo.")
                    continue
                break 
                    
            except ValueError:
                print("❌ Coordenadas inválidas. Intenta de nuevo.")
                continue
            
        if not self.quedan_barcos(tablero):
            print(f"🎉 ¡Jugador {jugador} gana!")
            self.imprimir_tableros()
            input("Enter para continuar...")
            return False
            
        return True  

    def jugar_partida(self) -> None:
        """
        Controla el flujo principal de una partida
        No recibe nada, pero controla que se ejecute el juego y el turno del jugador
        """
        while True:
            limpiar_consola()
            self.imprimir_tableros(True)
            jugador = (self.turno % 2) + 1
            
            if not self.turno_jugador(jugador):
                break
                
            self.turno += 1
            input("Enter para continuar...")
            
        self.partida_en_curso = False

    def mostrar_bienvenida(self):
        """
        Imprime el mensaje de bienvenida
        """
        print(MENSAJE_BIENVENIDA)
        time.sleep(2)

    def iniciar_juego(self):
        """
        El menú del juego, también forma parte del control sobre el flujo de la partida
        """
        self.mostrar_bienvenida()
        
        while True:
            if not self.partida_en_curso:
                opcion = self.mostrar_menu()
                
                if opcion == "1":
                    if self.configurar_juego():
                        self.colocar_barcos_jugadores()
                        self.partida_en_curso = True
                        self.jugar_partida()
                elif opcion == "2":
                    self.jugar_contra_ia()
                elif opcion == "3":
                    print("Entre dentro de la partida y presione g")
                    time.sleep(2)
                    if self.partida_en_curso:
                        self.jugar_partida()
                elif opcion == "4":
                    self.cargar_partida()
                    self.partida_en_curso = True
                    self.jugar_partida()
                elif opcion == "5":
                    if self.tablero1 and self.tablero2:
                        self.partida_en_curso = True
                        self.jugar_partida()
                    else:
                        print("No existe partida para reanudar")
                        time.sleep(1)
                elif opcion == "6":
                    break
            else:
                limpiar_consola()
                self.jugar_partida()

########################################################################################## 
# Funcionalidad de la IA (limitada): Aquí, he intentado reducir, y hacer estructuras más complejas de código

    def colocar_barcos_ia(self):
        """
        Coloca los barcos de la IA aleatoriamente (imposible que falle, usa el tamaño del tablero)
        """
        for longitud in self.barcos:
            while True:
                horizontal = random.choice([True, False])
                if horizontal:
                    fila = random.randint(0, self.tamaño - 1)
                    columna = random.randint(0, self.tamaño - longitud)
                else:
                    fila = random.randint(0, self.tamaño - longitud)
                    columna = random.randint(0, self.tamaño - 1)
                
                if self.es_posicion_valida(self.tablero2, fila, columna, longitud, horizontal):
                    if horizontal:
                        for i in range(longitud):
                            self.tablero2[fila][columna + i] = "B"
                    else:
                        for i in range(longitud):
                            self.tablero2[fila + i][columna] = "B"
                    break

    def disparo_ia(self): 
        """
        Genera coordenadas válidas para el disparo de la IA usando estructuras más complejas y estrechas de código jeje
        Se ejecuta, busca unas coordenadas válidas y devuleve el lugar del disparo en una tupla: (letra, columna)
        """
        # Valores para no tener un bucle infinito por la IA
        intentos = 0
        max_intentos = self.tamaño * self.tamaño 
        
        while intentos < max_intentos:
            fila = random.randint(0, self.tamaño - 1)
            columna = random.randint(0, self.tamaño - 1)
            
            if (self.es_posicion_valida(self.tablero1, fila, columna, 1, True) and self.tablero1[fila][columna] in [" ", "B"]):
                return numero_a_letra(fila), columna
            intentos += 1
        
        # Por si aca no se encuentra lugar de disparo, se busca a la fuerza
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if self.tablero1[i][j] in [" ", "B"]:
                    return numero_a_letra(i), j
                    
        return numero_a_letra(0), 0  
    
    def jugar_contra_ia(self):
        """
        Gestiona lo que viene siendo la partida contra la IA
        Pide posiciones para los barcos, coloca los barcos de la IA, pide disparo, ...; basicamente se corre
        la partida contra la IA
        """
        if not self.configurar_juego():
            return
            
        print("\nColoca tus barcos:")
        for longitud in self.barcos:
            self.imprimir_tableros()
            while True:
                try:
                    letra, col = self.pedir_coordenadas()
                    horizontal = input("¿Horizontal? (s/n): ").lower() == 's'
                    if self.colocar_barco(self.tablero1, letra, col, longitud, horizontal):
                        break
                    print("Posición inválida. Reintenta.")
                except ValueError:
                    print("Entrada inválida. Reintenta.")
        
        self.colocar_barcos_ia()
        
        while True:
            limpiar_consola()
            self.imprimir_tableros(True)
            
            print("\n👤 Tu turno:")
            while True:
                try:
                    letra, col = self.pedir_coordenadas()
                    if self.disparar(self.tablero2, letra, col):
                        print("💥 ¡IMPACTO!")
                    else:
                        print("💧 ¡Agua!")
                    break
                except ValueError:
                    print("❌ Coordenadas inválidas")
            
            if not self.quedan_barcos(self.tablero2):
                print("🎉 ¡Has ganado!")
                break
            
            input("\nPresiona Enter para el turno de la IA...")
            fila, col = self.disparo_ia()
            print(f"\n🤖 La IA dispara a {fila}{col}")
            if self.disparar(self.tablero1, fila, col):
                print("💥 ¡La IA te ha dado!")
            else:
                print("💧 La IA ha fallado")
                
            if not self.quedan_barcos(self.tablero1):
                print("🤖 ¡La IA ha ganado!")
                break
            
            input("\nPresiona Enter para continuar...")

        ##########################################################################################
