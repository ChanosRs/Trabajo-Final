import random

tickets = {}

def generar_numero_ticket():
    return random.randint(1000, 9999)

def alta_ticket():
    while True:
        nombre = input("Ingrese nombre: ")
        sector = input("Ingrese sector: ")
        asunto = input("Ingrese asunto: ")
        problema = input("Describa el problema: ")
        numero = generar_numero_ticket()

        ticket = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }
        tickets[numero] = ticket

        print("\nTicket generado exitosamente:")
        print(f"Número de ticket: {numero}")
        for clave, valor in ticket.items():
            print(f"{clave}: {valor}")
        print("Por favor, recuerde el número de su ticket.\n")

        otro = input("¿Desea crear otro ticket? (s/n): ").lower()
        if otro != 's':
            break

def leer_ticket():
    while True:
        try:
            numero = int(input("Ingrese el número del ticket: "))
            if numero in tickets:
                print("\nTicket encontrado:")
                for clave, valor in tickets[numero].items():
                    print(f"{clave}: {valor}")
                print()
            else:
                print("Ticket no encontrado.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.")

        otro = input("¿Desea leer otro ticket? (s/n): ").lower()
        if otro != 's':
            break

def menu_principal():
    while True:
        print("=== MENÚ DE TICKETS ===")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            confirmar = input("¿Está seguro que desea salir? (s/n): ").lower()
            if confirmar == 's':
                print("Programa finalizado.")
                break
        else:
            print("Opción inválida. Intente nuevamente.\n")

# Ejecutar el menú al correr el archivo
if __name__ == "__main__":
    menu_principal()
