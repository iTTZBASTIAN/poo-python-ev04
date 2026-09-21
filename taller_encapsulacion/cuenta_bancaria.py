class CuentaBancaria:
    """Cuenta bancaria con atributos protegidos y acceso controlado.

    Atributos privados (por convención, con guion bajo):
        _titular: nombre del titular (solo lectura desde fuera).
        _saldo:   dinero disponible (nunca puede ser negativo).
    """

    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = 0.0
        self.saldo = saldo  # pasa por el setter, así se valida el saldo inicial

    # --- Propiedad titular: solo lectura ---
    @property
    def titular(self):
        return self._titular

    # --- Propiedad saldo: lectura y escritura controlada ---
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(valor)

    # --- Operaciones ---
    def depositar(self, cantidad):
        """Suma `cantidad` al saldo si es positiva. Devuelve True/False."""
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """Resta `cantidad` del saldo si es positiva y hay fondos suficientes.
        Devuelve True/False."""
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False
