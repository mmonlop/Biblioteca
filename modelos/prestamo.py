from datetime import date


class Prestamo:
    def __init__(self,usuario,libro,fecha_prestamo=None,fecha_devolucion=None):
        self.usuario = usuario
        self.libro = libro 
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion

    @property
    def activo(self):
        return self.fecha_devolucion is None

    def __str__(self):
        return f"USUARIO {self.usuario} - LIBRO {self.libro} - F_PRESTAMO {self.fecha_prestamo} - F_DEVOLUCION {self.fecha_devolucion}"