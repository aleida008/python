saldo_disponible = 12500000
monto_transferencia = int(input("Ingrese monto a tranferir: "))

if monto_transferencia > saldo_disponible:
    print("saldo insuficiente")
else:
    saldo_disponible = saldo_disponible - monto_transferencia
    print("Trnsferencia realizada con exito")
    print("Su saldo actual es: " + str(saldo_disponible))    