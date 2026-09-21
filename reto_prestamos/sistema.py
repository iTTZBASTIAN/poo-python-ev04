from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo


class SistemaPrestamos:
    """Gestiona las colecciones del proyecto:

    - equipos:   diccionario  {nombre en minúsculas: Equipo}
    - usuarios:  diccionario  {documento: Usuario}
    - prestamos: lista de objetos Prestamo (historial completo)
    """

    def __init__(self):
        self.__equipos = {}
        self.__usuarios = {}
        self.__prestamos = []

    # ---------- Equipos ----------
    def agregar_equipo(self, nombre):
        equipo = Equipo(nombre)  # valida que no venga vacío
        clave = equipo.nombre.lower()
        if clave in self.__equipos:
            raise ValueError(f"El equipo '{equipo.nombre}' ya está registrado en el sistema.")
        self.__equipos[clave] = equipo
        return equipo

    def buscar_equipo(self, nombre):
        equipo = self.__equipos.get(nombre.strip().lower())
        if equipo is None:
            raise ValueError("El equipo ingresado no existe en el sistema.")
        return equipo

    def listar_equipos(self):
        return list(self.__equipos.values())

    # ---------- Usuarios ----------
    def registrar_usuario(self, documento, nombre):
        usuario = Usuario(documento, nombre)
        if usuario.documento in self.__usuarios:
            raise ValueError(f"Ya existe un usuario con el documento {usuario.documento}.")
        self.__usuarios[usuario.documento] = usuario
        return usuario

    def buscar_usuario(self, documento):
        """Devuelve el Usuario o None si no está registrado."""
        return self.__usuarios.get(documento.strip())

    # ---------- Préstamos ----------
    def registrar_prestamo(self, nombre_equipo, documento, fecha=None):
        equipo = self.buscar_equipo(nombre_equipo)
        usuario = self.buscar_usuario(documento)
        if usuario is None:
            raise ValueError("El usuario no está registrado.")
        prestamo = Prestamo(len(self.__prestamos) + 1, equipo, usuario, fecha)
        self.__prestamos.append(prestamo)
        return prestamo

    def devolver_equipo(self, nombre_equipo):
        equipo = self.buscar_equipo(nombre_equipo)
        for prestamo in reversed(self.__prestamos):
            if prestamo.equipo is equipo and prestamo.esta_activo():
                prestamo.devolver()
                return prestamo
        raise ValueError("El equipo no se encuentra prestado actualmente.")

    def buscar_prestamo(self, id_prestamo):
        for prestamo in self.__prestamos:
            if prestamo.id == id_prestamo:
                return prestamo
        raise ValueError(f"No existe el préstamo #{id_prestamo}.")

    def modificar_prestamo(self, id_prestamo, documento_nuevo):
        prestamo = self.buscar_prestamo(id_prestamo)
        nuevo_usuario = self.buscar_usuario(documento_nuevo)
        if nuevo_usuario is None:
            raise ValueError("El usuario no está registrado.")
        prestamo.cambiar_usuario(nuevo_usuario)
        return prestamo

    # ---------- Consultas ----------
    def listar_prestamos(self):
        return list(self.__prestamos)

    def prestamos_activos(self):
        return [p for p in self.__prestamos if p.esta_activo()]

    def prestamos_de_usuario(self, documento):
        return [p for p in self.__prestamos if p.usuario.documento == documento.strip()]

    def historial_de_equipo(self, equipo):
        return [p for p in self.__prestamos if p.equipo is equipo]
