from cuenta_bancaria import CuentaBancaria


def mostrar(cuenta):
    print(f"   Titular: {cuenta.titular} | Saldo: ${cuenta.saldo:,.2f}")


print("=== 1. Crear cuentas ===")
cuenta = CuentaBancaria("Ana Gómez", 100000)
mostrar(cuenta)
cuenta_vacia = CuentaBancaria("Luis Pérez")  # saldo por defecto = 0
mostrar(cuenta_vacia)

print("\n=== 2. Propiedad titular (solo lectura) ===")
print(f"   Titular leído: {cuenta.titular}")
try:
    cuenta.titular = "Otra persona"
except AttributeError as error:
    print(f"   No se puede modificar el titular -> AttributeError: {error}")

print("\n=== 3. Propiedad saldo (validación) ===")
cuenta.saldo = 250000
print("   Saldo cambiado a 250000:")
mostrar(cuenta)
try:
    cuenta.saldo = -500
except ValueError as error:
    print(f"   Intento de saldo negativo -> ValueError: {error}")
try:
    CuentaBancaria("Carla Ruiz", -10)
except ValueError as error:
    print(f"   Saldo inicial negativo -> ValueError: {error}")
mostrar(cuenta)

print("\n=== 4. Método depositar() ===")
print(f"   depositar(50000)  -> {cuenta.depositar(50000)}")
print(f"   depositar(0)      -> {cuenta.depositar(0)}")
print(f"   depositar(-100)   -> {cuenta.depositar(-100)}")
mostrar(cuenta)

print("\n=== 5. Método retirar() ===")
print(f"   retirar(100000)   -> {cuenta.retirar(100000)}")
print(f"   retirar(999999)   -> {cuenta.retirar(999999)}  (fondos insuficientes)")
print(f"   retirar(-50)      -> {cuenta.retirar(-50)}  (cantidad inválida)")
mostrar(cuenta)