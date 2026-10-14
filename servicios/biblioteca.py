class Biblioteca:

    def __init__(self):
        self.libros = []
        usuarios = []
        prestamos = []


    def registrar_libro(self,libro):
        #buscar si hay otro libro con ese isbn
        if self.buscar_libro(libro):
            print("El libro ya existe")
            return 

        self.libros.append(libro)

    def buscar_libro(self,libro_nuevo):
        for libro in self.libros:
            if libro.isbn == libro_nuevo.isbn:
                return libro
        return None

