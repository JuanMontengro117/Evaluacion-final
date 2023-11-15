def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Generar la representación en byte de un carácter")
    print("2. Generar la representación en byte de una palabra")

def obtener_representacion_byte_caracter(caracter):
    return ' '.join(format(ord(c), '08b') for c in caracter)

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción (1 o 2): ")

        if opcion == '1':
            caracter = input("Ingrese un carácter: ")
            print("El numero ASCII es", ord(caracter))
            print("Representación en binaria:", obtener_representacion_byte_caracter(caracter))
            
        elif opcion == '2':
            total = []
            palabra = input("Ingrese una palabra: ")
            for caracter in palabra:
                print("El numero ASCII de", caracter, "es", ord(caracter))
                representacion_byte = obtener_representacion_byte_caracter(caracter)
                print(f"Representación en binaria de '{caracter}': {representacion_byte}")
                total.append(representacion_byte)
            print("El total es", total)  
        else:
            print("Opción no válida. Intente de nuevo.")

        continuar = input("¿Desea continuar? (s/n): ")
        if continuar.lower() != 's':
            break

main()