import random
import string
import os

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔═══════════«WELCOME»═══════════╗")
    print("║      Generador de Contraseñas V0.1      ║")
    print("╚═════════(••)══════════════════╝\n")
    print("Seleccione una de las siguientes opciones:\n")
    print("» 1. Generar contraseña solo de Letras.")
    print("» 2. Generar contraseña solo de Números.")
    print("» 3. Generar contraseña Letras y Números.")
    print("» 4. Generar contraseña Letras, Números y Caracteres.")
    print("» 0. Salir.\n")

def generar_contraseña(opcion, longitud=12):
    if opcion == 1:
        caracteres = string.ascii_letters
    elif opcion == 2:
        caracteres = string.digits
    elif opcion == 3:
        caracteres = string.ascii_letters + string.digits
    elif opcion == 4:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Escriba la opción seleccionada: "))
            if opcion == 0:
                print("¡Gracias por usar el generador de contraseñas!")
                break
            elif 1 <= opcion <= 4:
                longitud = int(input("Ingrese la longitud de la contraseña: "))
                contraseña = generar_contraseña(opcion, longitud)
                print(f"\n Contraseña generada: {contraseña}\n")
                input("Presione Enter para continuar...")
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
