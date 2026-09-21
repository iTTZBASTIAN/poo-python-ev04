from datetime import datetime

FORMATO_FECHA = "%Y-%m-%d"


def fecha_hoy():
    return datetime.now().strftime(FORMATO_FECHA)


class Prestamo:
    """Préstamo de un Equipo a un Usuario.

    Al crearse marca el equipo como prestado; al devolverse lo libera.
    Así la regla "un equipo prestado no puede prestarse otra vez"
    se cumple siempre, sin depender de quien use la clase.
    """

    def __init__(self, id_prestamo, equipo, usuario, fecha_prestamo=None):
        equipo.marcar_prestado()  # lanza ValueError si no está disponible
        self.__id = id_prestamo
        self.__equipo = equipo
        self.__usuario = usuario
        self.__fecha_prestamo = fecha_prestamo or fecha_hoy()
        self.__fecha_devolucion = None

    # --- Lectura ---
    @property
    def id(self):
        return self.__id

    @property
    def equipo(self):
        return self.__equipo

    @property
    def usuario(self):
        return self.__usuario

    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion

    def esta_activo(self):
        return self.__fecha_devolucion is None

    # --- Operaciones ---
    def devolver(self, fecha_devolucion=None):
        if not self.esta_activo():
            raise ValueError(f"El préstamo #{self.__id} ya fue devuelto.")
        self.__equipo.marcar_disponible()
        self.__fecha_devolucion = fecha_devolucion or fecha_hoy()

    def cambiar_usuario(self, nuevo_usuario):
        """Modifica el responsable de un préstamo que sigue activo."""
        if not self.esta_activo():
            raise ValueError("No se puede modificar un préstamo ya devuelto.")
        self.__usuario = nuevo_usuario

    def __str__(self):
        devolucion = self.__fecha_devolucion or "pendiente"
        return (f"#{self.__id} | {self.__equipo.nombre} | {self.__usuario.nombre} | "
                f"Préstamo: {self.__fecha_prestamo} | Devolución: {devolucion}")
