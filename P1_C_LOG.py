# P1 C, LOG. 2024 J.N.

def mostrar_menu():
    print("\n=== Menú  ===")
    print("1. Mostrar sistemas numéricos")
    print("2. Convertir número decimal")
    print("3. Resta binaria A2")
    print("4. Código Gray")
    print("5. Redundancia cíclica")
    print("0. Salir")


def mostrar_sistemas_numericos():
    info_teoria = """
    Sistemas Numéricos:
    - Sistema Decimal: Utiliza los símbolos 0 al 9.
    - Sistema Binario: Utiliza los símbolos 0 y 1.
    - Sistema Octal: Utiliza los símbolos 0 al 7.
    - Sistema Hexadecimal: Utiliza los símbolos 0 al 9 y las letras A a F.
    """
    print(info_teoria)


def convertir_decimal_a_binario(numero_decimal):
    # Verificar si el número está dentro del rango de 8 bits
    if numero_decimal < -128 or numero_decimal > 127:
        print("El número decimal debe estar en el rango de -128 a 127 para ajustarse a 8 bits.")
        return "", []

    # Convertir el número decimal a binario utilizando operaciones de bits
    binario = bin(numero_decimal & 0xFF)[2:].zfill(8)

    # Pasos a paso para la conversión
    pasos = [f"Decimal: {numero_decimal}"]
    pasos.append("Convertir a binario:")

    # Realizar la conversión dividiendo por 2 y registrando los restos
    cociente = numero_decimal
    for i in range(7, -1, -1):
        residuo = cociente % 2
        cociente //= 2
        pasos.append(f"   Dividir {cociente * 2} entre 2:")
        pasos.append(f"      Cociente: {cociente}")
        pasos.append(f"      Resto (Bit {i}): {residuo}")

    pasos.append(f"   Binario: {binario}")
    pasos.append(f"   ...")

    return binario, pasos


def convertir_decimal_a_octal(numero_decimal):
    # Verificar si el número está dentro del rango de 8 bits
    if numero_decimal < -128 or numero_decimal > 127:
        print("El número decimal debe estar en el rango de -128 a 127 para ajustarse a 8 bits.")
        return "", []

    # Convertir el número decimal a octal utilizando operaciones de bits
    octal = oct(numero_decimal & 0xFF)[2:].zfill(3)

    # Pasos a paso para la conversión
    pasos = [f"Decimal: {numero_decimal}"]
    pasos.append("Convertir a octal:")

    # Realizar la conversión dividiendo por 8 y registrando los restos
    cociente = numero_decimal
    for i in range(2, -1, -1):
        residuo = cociente % 8
        cociente //= 8
        pasos.append(f"   Dividir {cociente * 8} entre 8:")
        pasos.append(f"      Cociente: {cociente}")
        pasos.append(f"      Resto (Dígito {i}): {residuo}")

    pasos.append(f"   Octal: {octal}")
    pasos.append(f"   ...")

    return octal, pasos


def convertir_decimal_a_hexadecimal(numero_decimal):
    # Verificar si el número está dentro del rango de 8 bits
    if numero_decimal < -128 or numero_decimal > 127:
        print("El número decimal debe estar en el rango de -128 a 127 para ajustarse a 8 bits.")
        return "", []

    # Convertir el número decimal a hexadecimal utilizando operaciones de bits
    hexadecimal = hex(numero_decimal & 0xFF)[2:].upper()

    # Pasos a paso para la conversión
    pasos = [f"Decimal: {numero_decimal}"]
    pasos.append("Convertir a hexadecimal:")

    # Realizar la conversión dividiendo por 16 y registrando los restos
    cociente = numero_decimal
    for i in range(1, -1, -1):
        residuo = cociente % 16
        cociente //= 16
        pasos.append(f"   Dividir {cociente * 16} entre 16:")
        pasos.append(f"      Cociente: {cociente}")
        pasos.append(f"      Resto (Dígito {i}): {residuo}")

    pasos.append(f"   Hexadecimal: {hexadecimal}")
    pasos.append(f"   ...")

    return hexadecimal, pasos


def convertir_binario_a_gray(numero_binario):
    # Convertir binario a código Gray utilizando el método de XOR
    gray = ''
    pasos = [f"Binario: {numero_binario}", "Convertir a código Gray:"]

    gray += numero_binario[0]
    pasos.append(f"   Bit 0 del código Gray: {numero_binario[0]}")

    for i in range(1, len(numero_binario)):
        if numero_binario[i - 1] == numero_binario[i]:
            gray += '0'
            pasos.append(f"   Bit {i} del código Gray: 0 (Bit {i - 1} = Bit {i})")
        else:
            gray += '1'
            pasos.append(f"   Bit {i} del código Gray: 1 (Bit {i - 1} ≠ Bit {i})")

    pasos.append(f"   Código Gray: {gray}")
    pasos.append(f"   ...")

    return gray, pasos


def convertir_binario_a_decimal(numero_binario):
    # Convertir binario a decimal
    decimal = int(numero_binario, 2)
    return decimal


def convertir_gray_a_binario(numero_gray):
    # Convertir código Gray a binario utilizando el método de XOR
    binario = ''
    pasos = [f"Código Gray: {numero_gray}", "Convertir a binario:"]

    binario += numero_gray[0]
    pasos.append(f"   Bit 0 del binario: {numero_gray[0]}")

    for i in range(1, len(numero_gray)):
        if numero_gray[i] == '0':
            binario += binario[i - 1]
            pasos.append(f"   Bit {i} del binario: {binario[i - 1]} (Bit {i} = Bit {i - 1})")
        else:
            if binario[i - 1] == '0':
                binario += '1'
            else:
                binario += '0'
            pasos.append(f"   Bit {i} del binario: {binario[i]} (Bit {i} ≠ Bit {i - 1})")

    pasos.append(f"   Binario: {binario}")
    pasos.append(f"   ...")

    return binario, pasos


def suma_binaria(a, b):
    # Convertir a enteros
    a_decimal = int(a, 2)
    b_decimal = int(b, 2)

    # Sumar los enteros
    suma_decimal = a_decimal + b_decimal

    # Convertir de nuevo a binario
    suma_binario = bin(suma_decimal)[2:]

    return suma_binario


def resta_binaria_a2(minuendo, sustraendo):
    # Complemento a 2 del sustraendo
    sustraendo_complemento_a2 = bin(-int(sustraendo, 2) & 0xFF)[2:].zfill(8)

    # Sumar el minuendo y el complemento a 2 del sustraendo
    resultado = suma_binaria(minuendo, sustraendo_complemento_a2)

    # Si el resultado tiene más de 8 bits, descartar los bits adicionales
    if len(resultado) > 8:
        resultado = resultado[-8:]

    # Si el resultado es cero, ajustar a cero binario
    if resultado == '00000000':
        resultado = '0' * 8

    return resultado, sustraendo_complemento_a2


def calcular_crc(informacion, polinomio_generador):
    informacion_decimal = int(informacion, 2)
    generador_decimal = int(polinomio_generador, 2)
    residuo = informacion_decimal % generador_decimal

    return residuo == 0


def mostrar_paso_a_paso(pasos):
    print("Paso a paso:")
    print("+" + "-" * 80 + "+")
    print("| {:^78} |".format("Paso"))
    print("+" + "-" * 80 + "+")
    for i, paso in enumerate(pasos):
        print("| {:<78} |".format(f"Paso {i + 1}: {paso}"))
        print("+" + "-" * 80 + "+")


def mostrar_paso_a_paso_en_tabla(pasos):
    print("Paso a paso:")
    print("+" + "-" * 80 + "+")
    print("| {:^78} |".format("Paso"))
    print("+" + "-" * 80 + "+")
    for paso in pasos:
        print("| {:<78} |".format(paso))
        print("+" + "-" * 80 + "+")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción: ")
        if opcion == '0':
            print("Saliendo del programa...")
            break
        elif opcion == '1':
            print("\n--- Mostrar sistemas numéricos ---")
            mostrar_sistemas_numericos()
        elif opcion == '2':
            print("\n--- Convertir número decimal ---")
            numero_decimal = int(input("Ingrese un número decimal: "))
            binario, pasos_binario = convertir_decimal_a_binario(numero_decimal)
            octal, pasos_octal = convertir_decimal_a_octal(numero_decimal)
            hexadecimal, pasos_hexadecimal = convertir_decimal_a_hexadecimal(numero_decimal)

            print("Resultado de la Conversión:")
            print("Binario:", binario)
            print("Octal:", octal)
            print("Hexadecimal:", hexadecimal)

            print("\nPasos a paso a binario:")
            mostrar_paso_a_paso_en_tabla(pasos_binario)
            print("\nPasos a paso a octal:")
            mostrar_paso_a_paso_en_tabla(pasos_octal)
            print("\nPasos a paso a hexadecimal:")
            mostrar_paso_a_paso_en_tabla(pasos_hexadecimal)
        elif opcion == '3':
            print("\n--- Resta binaria A2 ---")
            minuendo = input("Ingrese el minuendo (decimal): ")
            sustraendo = input("Ingrese el sustraendo (decimal): ")
            minuendo_binario, _ = convertir_decimal_a_binario(int(minuendo))
            sustraendo_binario, _ = convertir_decimal_a_binario(int(sustraendo))
            resultado, complemento_a2 = resta_binaria_a2(minuendo_binario, sustraendo_binario)
            resultado_decimal = convertir_binario_a_decimal(resultado)

            print("Resultado de la Resta:")
            print("Resultado (binario):", resultado)
            print("Resultado (decimal):", resultado_decimal)

            print("\nPaso a paso:")
            mostrar_paso_a_paso_en_tabla([
                "Complemento A2 del sustraendo",
                complemento_a2
            ])
        elif opcion == '4':
            print("\n--- Código Gray ---")
            numero_binario = input("Ingrese un número binario: ")
            codigo_gray, pasos_gray = convertir_binario_a_gray(numero_binario)
            print("Código Gray:", codigo_gray)
            print("\nPasos a paso a código Gray:")
            mostrar_paso_a_paso_en_tabla(pasos_gray)
        elif opcion == '5':
            print("\n--- Redundancia cíclica ---")
            informacion = input("Ingrese el número binario que representa la información: ")
            polinomio_generador = input("Ingrese el polinomio generador (binario): ")
            if calcular_crc(informacion, polinomio_generador):
                print("Sin error detectado.")
            else:
                print("Error detectado.")
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()
