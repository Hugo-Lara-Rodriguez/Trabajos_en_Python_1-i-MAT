"""
Hola, bienvenido al juego Hundir la Flota mejorado. Como proyecto me falta algo de originalidad por coger el predeterminado, 
así que espero que se supla con las funcionalidades avanzadas que he implementado, dejo por aquí una lista con todo lo que cuenta:
(los requisítos básicos del proyectos están cumplidos, estos que menciono son extras o estos requisitos bastante mejorados)

Generales:
- Tablero totalmente modificable: en vez de una anchura rígida, el juego siempre te pregunta por la anchura del tablero
con el que quieres jugar (de 5x5 a 24x24 por temas de la visualización). Además, los emojis que representan cada situación son escalables
- Sistema de guardado y carga de partidas con nombre propio del jugador para la partida y guardado que cuida la UX, para poder
ver el estado de la partida fuera de la misma(ej.: en partida_guardada.txt)
- Menú principal completo con opciones añadidas
- Diferentes niveles de dificultad según la configuración

Funcionalidades del Juego:
- Habilidades Especiales: Disparo (habitual), bomba (ataque en área 3x3), torpedo (ataque en línea (fila o columna)), radar (detecta barcos en área 3x3), ... 
(son totalmente escalables y se pueden añadir más, ya que SON FUNCIONES INDEPENDIENTES)
- El número de barcos es totalmente libre y modificable, así como sus longitudes, se pregunta todo al iniciar partida, y luego se guarda también
- Posibilidad de colocación manual de los barcos o aleatoria (por si estás vago, mejor que una colocación predeterminada)

UX:
- Visualización clara de dos tableros simultáneamente de manera horizontal
- Interfaz en consola con símbolos Unicode para mejor visualización con emojis (💣, 🚀, 📡,...)

Errores:
- Validación de todas las entradas por el jugador Y manejo de errores en todas las operaciones (están todos capados)

Cambios respecto a la funcionalidad del hundir la flota clásico:
- Sistema de armas siendo el que llegue primero a por ellas quien se las queda, un turno por jugador aunque se de al 
objetivo (en tableros pequeños es más justo con las habilidades)

"""

from clases import HundirLaFlota

if __name__ == "__main__": # Estrucuta básica de inicio de programa
    juego = HundirLaFlota()
    juego.iniciar_juego()