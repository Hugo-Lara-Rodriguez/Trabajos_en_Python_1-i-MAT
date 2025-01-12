"""
En este módulo se encuentran las otras funciones que el programa no pregunta pero adivina que... SIGUEN SIENDO ESCALABLES. Se pueden 
cambiar todos los menús, introducciones, tamaños, símbolos dentro del juego e incluso añadir todas las habilidades que se te ocurran 
ya que estas habilidades las he creado en funciones separadas.
"""
# Diccionario de simbolos para representar
SIMBOLOS = {
    " ": "🌊",  
    "X": "💥",  
    "O": "💧",  
    "B": "🚢"   
}

# Habilidades especiales iniciales
HABILIDADES_INICIALES = {
    "bomba": 1,
    "torpedo": 1,
    "radar": 1
}

# Límites establecidos del tablero (para que no se vaya mucho por tema de visualización)
TAMANO_MIN = 5
TAMANO_MAX = 26

# Mensajes estáticos
MENSAJE_BIENVENIDA = """🎮═════════════════════════════════════════════════════🎮
        ¡BIENVENIDO A HUNDIR LA FLOTA ESCALABLE!       
🎮═════════════════════════════════════════════════════🎮

──────────────────────────────────────────────────────
        Diseñado por Hugo Lara Rodríguez - 1ºA         
        ¡Espero que os guste! 🎉                      
══════════════════════════════════════════════════════"""

MENU_PRINCIPAL = """══════════════════════════════════
        🎮 MENÚ PRINCIPAL 🎮
══════════════════════════════════
1️⃣  Nueva partida contra jugador
2️⃣  Nueva partida contra IA
3️⃣  Guardar partida
4️⃣  Cargar partida
5️⃣  Reanudar partida
6️⃣  Salir
══════════════════════════════════"""

MENU_CONFIGURACION = """══════════════════════════════════
    ⚙️ CONFIGURACIÓN DE JUEGO ⚙️
══════════════════════════════════"""

# Para la visualización del tablero
SEPARADOR_TABLERO = "═" * 60
BARRA_VERTICAL = "║"