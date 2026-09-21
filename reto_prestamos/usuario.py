class Usuario:
    """Persona que puede solicitar préstamos de equipos."""

    def __init__(self, documento, nombre):
        documento = documento.strip()
        if not documento:
            raise ValueError("El documento del usuario no puede estar vacío.")
        self.__documento = documento
        self.__nombre = ""
        self.nombre = nombre  # pasa por el setter para validar

    @property
    def documento(self):
        return self.__documento

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre:
            raise ValueError("El nombre del usuario no puede estar vacío.")
        self.__nombre = nuevo_nombre

    def __str__(self):
        return f"{self.__nombre} (doc. {self.__documento})"
