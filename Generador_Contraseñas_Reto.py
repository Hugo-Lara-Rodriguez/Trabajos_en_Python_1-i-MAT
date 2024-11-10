import random

letras = "kxnqrgyhjiscdebpzufovmwtla"
numero = "7941620835"
caracteres = "(·%)/=&$"

def generar_passwd(num_letras, num_numero, num_caracteres):
    passwd = ""
    contador = 0
    while contador < num_letras or contador < num_numero or contador < num_caracteres:
        if contador < num_letras:
            posicion = random.randint(0, len(letras)-1) 
            passwd += letras[posicion]
        if contador < num_numero:
            posicion = random.randint(0, len(numero)-1)
            passwd += numero[posicion]
        if contador < num_caracteres:
            posicion = random.randint(0, len(caracteres)-1)
            passwd += caracteres[posicion]
        contador += 1
    return passwd

def aleatorizar_passwd(passwd):
    passwd_aleatoria = ""
    while len(passwd) > 0:
        posicion = random.randint(0, len(passwd)-1)
        passwd_aleatoria += passwd[posicion]
        passwd = passwd[:posicion] + passwd[posicion+1:]
    return passwd_aleatoria 


passwd = generar_passwd(int(input("Número de letras: ")), int(input("Número de números: ")), int(input("Número de caracteres: ")))
print("Passwword generada:", passwd)
passwd_aleatoria = aleatorizar_passwd(passwd)
print("Password aleatoria:", passwd_aleatoria)