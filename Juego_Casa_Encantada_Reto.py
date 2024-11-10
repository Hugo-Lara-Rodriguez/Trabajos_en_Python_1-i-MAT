# Asignamos las variables con las que vamos a trabajar
import random 
preguntassi = ["¿En la tradición celta de Samhain, se usaban disfraces para protegerse de los espíritus?", "¿Se cree que la tradición de Halloween tiene sus raíces en el festival celta de Samhain?"]
preguntasno = ["¿El símbolo de la calabaza tallada, conocida como Jack o lantern, se originó en Estados Unidos?", "¿Los colores tradicionales de Halloween, el naranja, simboliza el miedo?"]
preguntas = [preguntassi, preguntasno]

puerta = "\U0001F6AA"  # 🚪
vacio = "\U00002B1C"  # ⬜️
fantasma = "\U0001F47B"  # 👻
chuche = "\U0001F36D"  # 🍭

p1 = ["","","",""]
p2 = ["","","",""]
p3 = ["","","",""]
p4 = ["","","",""]
casa = [p1, p2, p3, p4]

# Creamos la casa
for n in range(0,4):
    for m in range(0,4):
        casa[n][m] = vacio
        if random.randint(1,10) == 1:
            casa[n][m] = fantasma
casa[random.randint(1,3)][random.randint(0,3)] = chuche
casa[0][0] = puerta
print(casa)

# Creamos el sistema de movimiento
ganar = False
p = 0 #Piso
h = 0 #Habitación
while ganar == False:
    print(casa[p][h])
    h = (int(input(f"Estás en el piso {p}, ¿A dónde te quieres mover?: puerta 1/2/3/4", )) - 1)
    p += 1
    n_r1 = random.randint(0,1)
    n_r2 = random.randint(0,1)
    respuesta = input(f"{preguntas[n_r1][n_r2]}, S/N", )
    if n_r1 == 0:
        if respuesta != "S":
            print("Mal, vuelves a empezar")
            h = 0
            p = 0
    else:
        if respuesta != "N":
            print("Mal, vuelves a empezar")
            h = 0
            p = 0
    if casa[p][h] == fantasma:
        print(casa[p][h])
        respuesta = input("O no, un fantasma, responde la pregunta bien para seguir: Soy alto cuando soy joven y bajo cuando soy viejo ¿qué soy? a:calabaza, b:vela", )
        if respuesta != "b":
            print("Muy mal, te voy a deborar")
            ganar = True
    if casa[p][h] == chuche:
        print(casa[p][h])
        print("Felicidades, conseguiste salir de la casa")
        ganar = True
    if p == 3 and casa[p][h] != chuche and ganar != True: 
        print(casa[p][h])
        print("Llegaste al final, pero no hay salida, volvamos sobre nuestros pasos")
        h = 0
        p = 0
print("FIN")
