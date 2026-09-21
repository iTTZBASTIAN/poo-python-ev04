import os

from sistema import SistemaPrestamos


def limpiar_pantalla():
    # 'cls' funciona en Windows, 'clear' en Linux y macOS
    os.system('cls' if os.name == 'nt' else 'clear')


def cargar_datos_iniciales(sistema):
    sistema.agregar_equipo("Laptop Dell XPS")
    sistema.agregar_equipo("Proyector Epson")
    sistema.agregar_equipo("Micrófono Shure")
    sistema.registrar_usuario("1001", "Ana Gómez")
    sistema.registrar_prestamo("Proyector Epson", "1001", fecha="2026-08-01")


# ---------- Opciones del menú ----------
def ver_equipos(sistema):
    print("\n--- Estado Actual de Equipos ---")
    equipos = sistema.listar_equipos()
    if not equipos:
        print("No hay equipos registrados en el sistema.")
    for equipo in equipos:
        print(f"• {equipo}")


def registrar_prestamo(sistema):
    ver_equipos(sistema)
    nombre_equipo = input("\nIngrese el nombre exacto del equipo a prestar: ")
    equipo = sistema.buscar_equipo(nombre_equipo)
    if not equipo.esta_disponible():
        raise ValueError("El equipo no está disponible para préstamo.")

    documento = input("Ingrese el documento del usuario: ")
    if sistema.buscar_usuario(documento) is None:
        print("Usuario nuevo: vamos a registrarlo.")
        nombre = input("Ingrese el nombre del usuario: ")
        sistema.registrar_usuario(documento, nombre)

    prestamo = sistema.registrar_prestamo(nombre_equipo, documento)
    print(f"\nPréstamo de '{prestamo.equipo.nombre}' registrado a nombre de {prestamo.usuario.nombre}.")


def devolver_equipo(sistema):
    nombre_equipo = input("\nIngrese el nombre exacto del equipo a devolver: ")
    prestamo = sistema.devolver_equipo(nombre_equipo)
    print(f"\nEl equipo '{prestamo.equipo.nombre}' fue devuelto y está disponible nuevamente.")


def ver_historial(sistema):
    print("\n================ HISTORIAL DE PRÉSTAMOS ================")
    for equipo in sistema.listar_equipos():
        print(f"\nEquipo: {equipo.nombre}")
        prestamos = sistema.historial_de_equipo(equipo)
        if prestamos:
            for prestamo in prestamos:
                print(f"  - {prestamo}")
        else:
            print("  - Sin préstamos registrados")
    print("=======================================================")


def modificar_prestamo(sistema):
    activos = sistema.prestamos_activos()
    if not activos:
        print("\nNo hay préstamos activos para modificar.")
        return
    print("\n--- Préstamos activos ---")
    for prestamo in activos:
        print(f"  {prestamo}")
    try:
        id_prestamo = int(input("\nIngrese el número del préstamo a modificar: "))
    except ValueError:
        raise ValueError("El número del préstamo debe ser un entero.")
    documento = input("Ingrese el documento del nuevo responsable: ")
    prestamo = sistema.modificar_prestamo(id_prestamo, documento)
    print(f"\nPréstamo #{prestamo.id} actualizado. Nuevo responsable: {prestamo.usuario.nombre}.")


def agregar_equipo(sistema):
    nombre = input("\nIngrese el nombre del nuevo equipo: ")
    equipo = sistema.agregar_equipo(nombre)
    print(f"\nEl equipo '{equipo.nombre}' fue agregado correctamente al inventario.")


def ver_prestamos_usuario(sistema):
    documento = input("\nIngrese el documento del usuario: ")
    usuario = sistema.buscar_usuario(documento)
    if usuario is None:
        raise ValueError("El usuario no está registrado.")
    prestamos = sistema.prestamos_de_usuario(documento)
    print(f"\n--- Préstamos de {usuario} ---")
    if not prestamos:
        print("  Sin préstamos registrados")
    for prestamo in prestamos:
        print(f"  {prestamo}")


# ---------- Menú principal ----------
OPCIONES = {
    "1": ver_equipos,
    "2": registrar_prestamo,
    "3": devolver_equipo,
    "4": ver_historial,
    "5": modificar_prestamo,
    "6": agregar_equipo,
    "7": ver_prestamos_usuario,
}


def menu():
    sistema = SistemaPrestamos()
    cargar_datos_iniciales(sistema)

    while True:
        limpiar_pantalla()
        print("========================================")
        print("     SISTEMA DE PRÉSTAMO DE EQUIPOS")
        print("========================================")
        print("1. Ver equipos y su estado")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Modificar préstamo")
        print("6. Agregar nuevo equipo")
        print("7. Ver préstamos de un usuario")
        print("8. Salir del programa")
        print("========================================")

        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "8":
            limpiar_pantalla()
            print("¡Gracias por usar el sistema de préstamos! Hasta luego.")
            break

        accion = OPCIONES.get(opcion)
        if accion is None:
            input("\nOpción no válida. Presione Enter para reintentar...")
            continue

        limpiar_pantalla()
        try:
            accion(sistema)
        except ValueError as error:
            print(f"\nError: {error}")
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    menu()
