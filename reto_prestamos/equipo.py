class Equipo:
    """Equipo que puede ser prestado.

    El estado es un atributo privado: desde fuera solo se puede leer
    (propiedad `estado`) y se modifica únicamente con los métodos
    `marcar_prestado()` y `marcar_disponible()`, que validan la transición.
    """

    DISPONIBLE = "disponible"
    PRESTADO = "prestado"

    def __init__(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del equipo no puede estar vacío.")
        self.__nombre = nombre
        self.__estado = Equipo.DISPONIBLE

    # --- Lectura (sin setters: son atributos protegidos) ---
    @property
    def nombre(self):
        return self.__nombre

    @property
    def estado(self):
        return self.__estado

    def esta_disponible(self):
        return self.__estado == Equipo.DISPONIBLE

    # --- Únicas formas de cambiar el estado ---
    def marcar_prestado(self):
        if not self.esta_disponible():
            raise ValueError(f"El equipo '{self.__nombre}' no está disponible para préstamo.")
        self.__estado = Equipo.PRESTADO

    def marcar_disponible(self):
        if self.esta_disponible():
            raise ValueError(f"El equipo '{self.__nombre}' no se encuentra prestado actualmente.")
        self.__estado = Equipo.DISPONIBLE

    def __str__(self):
        return f"{self.__nombre} -> Estado: {self.__estado}"
