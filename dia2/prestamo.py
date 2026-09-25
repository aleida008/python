ingreso_mensual = 4800000
historial_positivo = True 
deuda_actual = 1200000

if historial_positivo and ingreso_mensual >= deuda_actual *3:
    print("Prestamo aprovado")
elif historial_positivo:
    print("Monto aprovado reducido")
else:
    print("préstamo rechazado")    