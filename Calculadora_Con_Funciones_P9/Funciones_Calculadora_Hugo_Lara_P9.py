def validacion_num():
    # HE ELIMINADO LA PRIMERA ITERACIÓN PORQUE SE REALIZA EN LA SEGUNDA
    error_entrada_tipo = True
    while error_entrada_tipo == True:
        numero_str = input("Número: ")
        if numero_str.isdecimal():
            numero = int(numero_str)
            error_entrada_tipo = False
        else:
            error_entrada_tipo = True
            if numero_str.count(".") == 1:
                numero = float(numero_str)
                error_entrada_tipo = False
            else:
                error_entrada_tipo = True
                if numero_str.count("+") == 1 and numero_str.count("j") == 1:
                    numero = complex(numero_str)
                    error_entrada_tipo = False
                else:
                    error_entrada_tipo = True
                    print("Prueba con otro")
    return numero 

def mostrar_historial(historial_operaciones):
    """Función para mostrar el historial de operaciones."""
    print(f"{'Historial':^20}")
    print("=" * 20)
    for clave, operacion in historial_operaciones.items():
        print(f"· {clave}: INPUT: {operacion[:-1]} -> OUTPUT: {operacion[-1:][0]}")

def repetir_operacion(historial_operaciones):
    """Función para repetir una operación a partir del historial."""
    clave = int(input("Número de la operación: "))
    if clave in historial_operaciones:
        operacion = historial_operaciones[clave]
        salida = " ".join(map(str, operacion[:-1])) + " = " + str(operacion[-1])
        print(f"Operación {clave}: {salida}")
    else:
        print("Clave no válida.")