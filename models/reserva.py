# ============================================================
# ARCHIVO: reserva.py
# Este archivo contiene la clase Reserva.
# La reserva relaciona clientes y servicios.
# ============================================================


# Importación de excepciones.
from utils.excepciones import ReservaError


# Clase Reserva.
class Reserva:

    # Constructor.
    def __init__(self, cliente, servicio, horas):

        # Cliente asociado.
        self.cliente = cliente

        # Servicio asociado.
        self.servicio = servicio

        # Cantidad de horas.
        self.horas = horas

        # Estado inicial.
        self.estado = "PENDIENTE"

    # Método para confirmar reserva.
    def confirmar(self):

        # Validación de horas.
        if self.horas <= 0:
            raise ReservaError(
                "La cantidad de horas debe ser mayor a cero."
            )

        # Cambio de estado.
        self.estado = "CONFIRMADA"

    # Método para cancelar reserva.
    def cancelar(self):

        self.estado = "CANCELADA"

    # Método para calcular el total.
    # Se usan parámetros opcionales para simular sobrecarga.
    def calcular_total(self, impuesto=0, descuento=0):

        # Cálculo inicial.
        total = self.servicio.calcular_costo(self.horas)

        # Aplicación de impuesto.
        total += total * impuesto

        # Aplicación de descuento.
        total -= descuento

        return total