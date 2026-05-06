# ============================================================
# ARCHIVO PRINCIPAL: main.py
# Este archivo ejecuta todo el sistema.
# Aquí se realizan pruebas válidas e inválidas
# para demostrar el manejo de excepciones.
# ============================================================


# Importación de clases.
from models.cliente import Cliente
from models.servicio import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)
from models.reserva import Reserva

# Importación del logger.
from utils.logger import registrar_log


# Lista para almacenar clientes.
clientes = []

# Lista para almacenar reservas.
reservas = []


# ============================================================
# PRIMERA OPERACIÓN
# ============================================================

try:

    # Crear cliente válido.
    cliente1 = Cliente("Carlos", "carlos@gmail.com")

    # Guardar cliente en la lista.
    clientes.append(cliente1)

    print(cliente1.mostrar_informacion())

except Exception as error:

    registrar_log(f"Error al crear cliente: {error}")


# ============================================================
# SEGUNDA OPERACIÓN
# ============================================================

try:

    # Cliente inválido.
    cliente2 = Cliente("Al", "correo_invalido")

    clientes.append(cliente2)

except Exception as error:

    registrar_log(f"Error cliente inválido: {error}")


# ============================================================
# TERCERA OPERACIÓN
# ============================================================

try:

    # Crear servicio.
    servicio1 = ReservaSala("Sala VIP", 100)

    # Crear reserva.
    reserva1 = Reserva(cliente1, servicio1, 3)

    # Confirmar reserva.
    reserva1.confirmar()

    # Mostrar total.
    print("Total reserva:", reserva1.calcular_total(0.19))

except Exception as error:

    registrar_log(f"Error en reserva: {error}")


# ============================================================
# CUARTA OPERACIÓN
# ============================================================

try:

    # Servicio de alquiler.
    servicio2 = AlquilerEquipo("Laptop Gamer", 80)

    # Reserva inválida.
    reserva2 = Reserva(cliente1, servicio2, -5)

    reserva2.confirmar()

except Exception as error:

    registrar_log(f"Error reserva inválida: {error}")


# ============================================================
# QUINTA OPERACIÓN
# ============================================================

try:

    # Servicio de asesoría.
    servicio3 = Asesoria("Asesoría en programación", 120)

    # Reserva correcta.
    reserva3 = Reserva(cliente1, servicio3, 2)

    reserva3.confirmar()

    print("Reserva confirmada.")

except Exception as error:

    registrar_log(f"Error asesoría: {error}")

finally:

    # Este bloque siempre se ejecuta.
    print("El sistema continúa funcionando correctamente.")