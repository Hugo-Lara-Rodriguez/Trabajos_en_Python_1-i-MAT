if __name__ == "__main__":
    # AQUÍ NO SIRVE DE MUCHO, PERO ES UNA BUENA PRÁCTICA 
    import Funciones_Calculadora_Hugo_Lara_P9 as fun
    menu = """
        ******** Calculadora iMAT ********
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Valor absoluto
        6. Redondeo de un número al alzar
        7. Valor ASCII de un carácter
        8. Carácter de un código ASCII
        9. Salir
        10. Historial de operaciones
        11. Repetir operación
        **********************************"""
    # HE REALIZADO COMO FUNCIONES LA VALIDACIÓN DEL NÚMERO (SE REPITE) Y EL HISTORIAL JUNTO A LA REPETICIÓN DE 
    # OPERACIONES (POR SER COMPLEJAS, MEJOR FUERA DEL CÓDIGO P.P.)

    # CÓDIGO PRINCIPAL: NO HE HECHO FUNCIONES LAS OPCIONES DE LA 1 A LA 9, YA QUE NO SON COMPLEJAS,
    # Y SACARLAS COMO FUNCIONES SERÍA COMPLICARLO TOD0
    opcion_numero = 0
    historial_operaciones = {}
    while opcion_numero != 9:
        print(menu)
        opcion_numero = int(input("Opción a escoger: "))
        if 1 <= opcion_numero <= 4:  # Para las primeras cuatro opciones que requieren dos números
            numero1 = fun.validacion_num()
            numero2 = fun.validacion_num()
            if opcion_numero == 1:  # Sumar
                resultado = numero1 + numero2
                historial_operaciones[len(historial_operaciones) + 1] = (numero1, "+", numero2, resultado)
            elif opcion_numero == 2:  # Restar
                resultado = numero1 - numero2
                historial_operaciones[len(historial_operaciones) + 1] = (numero1, "-", numero2, resultado)
            elif opcion_numero == 3:  # Multiplicar
                resultado = numero1 * numero2
                historial_operaciones[len(historial_operaciones) + 1] = (numero1, "*", numero2, resultado)
            elif opcion_numero == 4:  # Dividir
                resultado = numero1 / numero2
                historial_operaciones[len(historial_operaciones) + 1] = (numero1, "/", numero2, resultado)
            print(f"-------- Con tu número {numero1} y {numero2}, el resultado es {resultado} --------")
        elif opcion_numero == 5:  # Valor absoluto
            numero = fun.validacion_num()
            resultado = abs(numero)
            print(f"-------- El valor absoluto de {numero} es {resultado} --------")
            historial_operaciones[len(historial_operaciones) + 1] = (numero, "V.A", resultado)
        elif opcion_numero == 6:  # Redondeo al alza
            numero = fun.validacion_num()
            resultado = round(numero)
            print(f"-------- El redondeo de {numero} es {resultado} --------")
            historial_operaciones[len(historial_operaciones) + 1] = (numero, "ROUND", resultado)
        elif opcion_numero == 7:  # ASCII de un carácter
            char = input("Carácter: ")
            resultado = ord(char)
            print(f"-------- El valor ASCII de '{char}' es {resultado} --------")
            historial_operaciones[len(historial_operaciones) + 1] = (char, "ASCII", resultado)
        elif opcion_numero == 8:  # Carácter de un valor ASCII
            numero = int(input("Valor ASCII: "))
            resultado = chr(numero)
            print(f"-------- El carácter de {numero} es '{resultado}' --------")
            historial_operaciones[len(historial_operaciones) + 1] = (numero, "CHAR", resultado)
        elif opcion_numero == 9:  # Salir
            print("Bye!")
        elif opcion_numero == 10:  # Mostrar historial
            fun.mostrar_historial(historial_operaciones)
        elif opcion_numero == 11:  # Repetir operación
            fun.repetir_operacion(historial_operaciones)
        else:
            print("Opción no válida")