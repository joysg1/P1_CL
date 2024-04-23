
import crcmod

def crc_algorithm(message, generator):
    crc_func = crcmod.mkCrcFun(int(generator, 2), rev=False)
    crc = crc_func(message.encode())
    return crc == 0

# Solicitar al usuario que ingrese el mensaje y el polinomio generador
message = input("Ingrese el mensaje en forma de cadena binaria: ")
generator = input("Ingrese el polinomio generador en forma de cadena binaria: ")

# Aplicar el algoritmo CRC
if crc_algorithm(message, generator):
    print("El mensaje ha llegado sin errores.")
else:
    print("El mensaje ha llegado con errores.")