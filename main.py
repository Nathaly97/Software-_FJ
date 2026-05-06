# ============================================================
# ARCHIVO PRINCIPAL: main.py
# Este archivo es el encargado de ejecutar todo el sistema.
# ============================================================


# ============================================================
# IMPORTACIÓN DE CLASES
# ============================================================

# Se importan las clases necesarias para el funcionamiento.
from models.cliente import Cliente

from models.servicio import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)

from models.reserva import Reserva

# Se importa la función encargada de registrar logs.
from utils.logger import registrar_log


# ============================================================
# LISTAS DEL SISTEMA
# ============================================================

# Lista donde se almacenarán los clientes.
clientes = []

# Lista donde se almacenarán las reservas.
reservas = []


# ============================================================
# MENSAJE DE INICIO DEL SISTEMA
# ============================================================

print("===================================")
print("      SISTEMA SOFTWARE FJ")
print("===================================")
print("Iniciando sistema...\n")


# ============================================================
# PRIMERA OPERACIÓN
# CREAR CLIENTE VÁLIDO
# ============================================================

try:

    # Se crea un cliente válido.
    cliente1 = Cliente("Carlos", "carlos@gmail.com")

    # Se almacena en la lista.
    clientes.append(cliente1)

    # Mostrar información.
    print(cliente1.mostrar_informacion())

except Exception as error:

    # Registrar error en logs.
    registrar_log(f"Error al crear cliente 1: {error}")


# ============================================================
# SEGUNDA OPERACIÓN
# CREAR CLIENTE INVÁLIDO
# ============================================================

try:

    # Cliente con nombre muy corto y correo inválido.
    cliente2 = Cliente("Al", "correo_invalido")

    clientes.append(cliente2)

except Exception as error:

    registrar_log(f"Error cliente inválido: {error}")


# ============================================================
# TERCERA OPERACIÓN
# RESERVA VÁLIDA DE SALA
# ============================================================

try:

    # Crear servicio.
    servicio1 = ReservaSala("Sala VIP", 100)

    # Crear reserva.
    reserva1 = Reserva(cliente1, servicio1, 3)

    # Confirmar reserva.
    reserva1.confirmar()

    # Guardar reserva.
    reservas.append(reserva1)

    # Mostrar costo total.
    print(f"Total reserva sala: {reserva1.calcular_total(0.19)}")

except Exception as error:

    registrar_log(f"Error en reserva sala: {error}")


# ============================================================
# CUARTA OPERACIÓN
# RESERVA INVÁLIDA
# ============================================================

try:

    # Crear servicio.
    servicio2 = AlquilerEquipo("Laptop Gamer", 80)

    # Reserva con horas negativas.
    reserva2 = Reserva(cliente1, servicio2, -5)

    # Intentar confirmar.
    reserva2.confirmar()

    reservas.append(reserva2)

except Exception as error:

    registrar_log(f"Error reserva inválida: {error}")


# ============================================================
# QUINTA OPERACIÓN
# RESERVA DE ASESORÍA
# ============================================================

try:

    # Crear servicio de asesoría.
    servicio3 = Asesoria("Asesoría en programación", 120)

    # Crear reserva.
    reserva3 = Reserva(cliente1, servicio3, 2)

    # Confirmar reserva.
    reserva3.confirmar()

    # Guardar reserva.
    reservas.append(reserva3)

    print("Reserva de asesoría confirmada.")

except Exception as error:

    registrar_log(f"Error asesoría: {error}")


# ============================================================
# SEXTA OPERACIÓN
# CREAR OTRO CLIENTE VÁLIDO
# ============================================================

try:

    # Crear cliente válido.
    cliente3 = Cliente("Maria", "maria@gmail.com")

    # Guardar cliente.
    clientes.append(cliente3)

    # Mostrar información.
    print(cliente3.mostrar_informacion())

except Exception as error:

    registrar_log(f"Error cliente 3: {error}")


# ============================================================
# SÉPTIMA OPERACIÓN
# CLIENTE SIN NOMBRE
# ============================================================

try:

    # Cliente inválido.
    cliente4 = Cliente("", "sin_nombre@gmail.com")

    clientes.append(cliente4)

except Exception as error:

    registrar_log(f"Error cliente vacío: {error}")


# ============================================================
# OCTAVA OPERACIÓN
# RESERVA EMPRESARIAL
# ============================================================

try:

    # Crear servicio.
    servicio4 = ReservaSala("Sala Empresarial", 200)

    # Crear reserva.
    reserva4 = Reserva(cliente3, servicio4, 5)

    # Confirmar reserva.
    reserva4.confirmar()

    # Guardar reserva.
    reservas.append(reserva4)

    print("Reserva empresarial confirmada.")

except Exception as error:

    registrar_log(f"Error reserva empresarial: {error}")


# ============================================================
# NOVENA OPERACIÓN
# RESERVA CON HORAS EN CERO
# ============================================================

try:

    # Crear servicio.
    servicio5 = AlquilerEquipo("Proyector", 50)

    # Reserva inválida.
    reserva5 = Reserva(cliente3, servicio5, 0)

    # Confirmar reserva.
    reserva5.confirmar()

    reservas.append(reserva5)

except Exception as error:

    registrar_log(f"Error horas inválidas: {error}")


# ============================================================
# DÉCIMA OPERACIÓN
# RESERVA DE CIBERSEGURIDAD
# ============================================================

try:

    # Crear servicio.
    servicio6 = Asesoria("Ciberseguridad", 300)

    # Crear reserva.
    reserva6 = Reserva(cliente1, servicio6, 4)

    # Confirmar reserva.
    reserva6.confirmar()

    # Guardar reserva.
    reservas.append(reserva6)

    print("Reserva de ciberseguridad confirmada.")

except Exception as error:

    registrar_log(f"Error asesoría ciberseguridad: {error}")


# ============================================================
# BLOQUE FINALLY
# ------------------------------------------------------------
# Este bloque siempre se ejecuta aunque existan errores.
# ============================================================

finally:

    print("\n===================================")
    print("El sistema continúa funcionando.")
    print("Proceso finalizado correctamente.")
    print("===================================")


# ============================================================
# MOSTRAR RESUMEN FINAL
# ============================================================

print(f"\nCantidad total de clientes válidos: {len(clientes)}")

print(f"Cantidad total de reservas válidas: {len(reservas)}")